import math
import random
from flask import Flask, jsonify, render_template

from data import META, COURTS, TREND_NOTE

app = Flask(__name__)


def month_labels(n=198):
    labels = []
    y, m = 2010, 1
    for _ in range(n):
        labels.append(f"{y}-{m:02d}")
        m += 1
        if m > 12:
            m = 1
            y += 1
        if y > 2026 or (y == 2026 and m > 6):
            break
    return labels


def illustrative_series(mean_level, n=198, seed=0):
    """
    Bounded, clearly-labeled illustrative monthly shape mirroring the report's
    qualitative description (growth after ~2016-17 digitisation, a dip around
    2020-21, recent moderation), scaled to the case type's real reported mean.
    NOT the underlying raw series -- the PDF supplies summary stats + chart
    images, not month-by-month counts.
    """
    rnd = random.Random(seed)
    out = []
    for i in range(n):
        t = i / max(n - 1, 1)
        base = 0.35 + 0.65 * (1 / (1 + math.exp(-10 * (t - 0.35))))
        dip = 0.35 * math.exp(-((t - 0.62) ** 2) / (2 * 0.06 ** 2))
        noise = rnd.uniform(-0.08, 0.08)
        out.append(round(max(mean_level * (base - dip + noise), 0), 1))
    return out


def build_insights(code, c):
    """Derive simple, explainable insights + recommendation cards from the
    reported summary statistics for one court."""
    arrivals = c["arrivals"]
    disposal = {d["case_type"]: d for d in c["disposal"]}
    gaps = {g["case_type"]: g for g in c["gap"]}

    total_filings = sum(a["filings"] for a in arrivals)
    busiest = max(arrivals, key=lambda a: a["filings"])

    disposal_rows = list(disposal.values())
    slowest = max(disposal_rows, key=lambda d: d["median"]) if disposal_rows else None
    fastest = min(disposal_rows, key=lambda d: d["median"]) if disposal_rows else None

    gap_rows = list(gaps.values())
    worst_gap = max(gap_rows, key=lambda g: g["p90"]) if gap_rows else None

    insights = [
        f"{busiest['case_type']} dominates the docket at {c['full_name']}, "
        f"accounting for {busiest['filings']:,} of {total_filings:,} tracked filings "
        f"({busiest['filings'] / total_filings * 100:.0f}%).",
    ]
    if slowest:
        insights.append(
            f"{slowest['case_type']} carries the longest typical resolution time: "
            f"a median of {slowest['median']:,} working days, stretching to "
            f"{slowest['p90']:,} at the 90th percentile."
        )
    if fastest:
        insights.append(
            f"{fastest['case_type']} clears fastest, with a median disposal of "
            f"{fastest['median']:,} working days."
        )
    if worst_gap:
        insights.append(
            f"{worst_gap['case_type']} shows the widest filing-to-first-listing spread: "
            f"90th percentile of {worst_gap['p90']} working days versus a median of "
            f"{worst_gap['median']}."
        )
    insights.append(
        f"Gap and hearing-count measures are only reliable from {c['listing_cutoff']} "
        f"onward for this court; arrivals and disposal use the full "
        f"{META['window_start']}\u2013{META['window_end']} window."
    )

    recommendations = []
    if slowest and slowest["median"] > 500:
        recommendations.append({
            "priority": "high",
            "title": f"Backlog risk: {slowest['case_type']}",
            "description": (
                f"Median time to disposal is {slowest['median']:,} working days "
                f"(90th pct {slowest['p90']:,}), the slowest tracked case type at this court."
            ),
            "action": "Prioritise case-management review and additional listing slots for this case type.",
            "impact": "Reduced pendency and faster clearance for the largest-backlog category.",
        })
    if worst_gap and worst_gap["p90"] > 100:
        recommendations.append({
            "priority": "medium",
            "title": f"Listing delay: {worst_gap['case_type']}",
            "description": (
                f"90th percentile filing-to-first-listing gap is {worst_gap['p90']} working days "
                f"versus a median of {worst_gap['median']}, indicating a long tail of delayed first hearings."
            ),
            "action": "Audit the scheduling queue for outlier cases awaiting first listing.",
            "impact": "Shorter, more predictable time-to-first-hearing.",
        })
    busiest_rate = busiest.get("daily_rate")
    if busiest_rate and busiest_rate > 1.0:
        recommendations.append({
            "priority": "low",
            "title": f"Sustained high-volume intake: {busiest['case_type']}",
            "description": (
                f"Averaging {busiest_rate} filings per working day "
                f"({busiest['mean']}/month), this case type anchors the court's total workload."
            ),
            "action": "Maintain dedicated bench time and clerical capacity for this category.",
            "impact": "Keeps the court's single largest filing stream from crowding out others.",
        })

    return {"insights": insights, "recommendations": recommendations}


@app.route("/")
def index():
    return render_template("index.html", meta=META, courts=list(COURTS.keys()))


@app.route("/api/meta")
def api_meta():
    totals = {}
    for code, c in COURTS.items():
        totals[code] = {
            "full_name": c["full_name"],
            "listing_cutoff": c["listing_cutoff"],
            "total_filings": sum(a["filings"] for a in c["arrivals"]),
            "case_types_tracked": len(c["arrivals"]),
        }
    grand_total = sum(v["total_filings"] for v in totals.values())
    return jsonify({"meta": META, "court_totals": totals, "grand_total_filings": grand_total})


@app.route("/api/court/<code>")
def api_court(code):
    if code not in COURTS:
        return jsonify({"error": "unknown court code"}), 404
    return jsonify(COURTS[code])


@app.route("/api/court/<code>/trend")
def api_court_trend(code):
    if code not in COURTS:
        return jsonify({"error": "unknown court code"}), 404
    c = COURTS[code]
    top = c["arrivals"][0]
    labels = month_labels()
    series = illustrative_series(top["mean"], n=len(labels), seed=hash(code) % 1000)
    return jsonify({"case_type": top["case_type"], "labels": labels, "values": series, "note": TREND_NOTE})


@app.route("/api/court/<code>/insights")
def api_court_insights(code):
    if code not in COURTS:
        return jsonify({"error": "unknown court code"}), 404
    return jsonify(build_insights(code, COURTS[code]))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
