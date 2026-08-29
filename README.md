# Tamluk Courts Intelligence Platform (POC)

A proof-of-concept docket-analytics dashboard for the **Purba Medinipur
(Tamluk) Courts**, built from the *Monthly Descriptive Analysis* PDF report.
All data, charts, and copy in this app are about the four Tamluk courts
(CJM, District Judge, Civil Judge Sr./Jr. Div.) — filings, disposal times,
hearing rates, and listing gaps.

The visual design (navy/purple gradient background, glassmorphism cards,
gradient stat tiles, pill tab nav, loading screen with progress bar,
Chart.js visuals, priority-badged recommendation cards) follows the same
design system as another dashboard you shared for reference. Flask backend
serving a JSON API; static HTML/CSS/JS frontend consumes it.

## Structure
```
court_poc_v2/
├── app.py                        # Flask app: routes + API + insight generation
├── data.py                       # Structured data transcribed from the PDF report
├── templates/
│   └── index.html
├── static/
│   ├── css/intelligence.css      # dashboard design system
│   └── js/intelligence.js
├── requirements.txt
├── Procfile                      # gunicorn app:app
├── runtime.txt
└── start.bat
```

## Run it
```bash
pip install -r requirements.txt
python app.py
```
Visit http://localhost:5000

## API endpoints
- `GET /api/meta` — per-court totals and case-type counts
- `GET /api/court/<code>` — full arrivals / gap / hearings / disposal tables for a court (`CJM`, `DJ`, `CJ (Sr.)`, `CJ (Jr.)`)
- `GET /api/court/<code>/trend` — illustrative monthly shape for the leading case type
- `GET /api/court/<code>/insights` — auto-generated observations + priority-tagged recommendation cards

## What's real vs. illustrative
- Stat tiles, the filings-by-case-type donut, hearings/disposal/gap bar
  charts, the case register table, and the insights/recommendations all come
  directly from (or are simple derivations of) the summary statistics in the
  PDF — filings, means, medians, percentiles.
- The "Filing Trends" line chart is labeled illustrative: the PDF gives
  monthly summary stats and 12-month-moving-average chart *images*, not a raw
  month-by-month series, so that chart approximates the shape the report
  describes (growth after ~2016–17 digitisation, a dip around 2020–21) scaled
  to the case type's real reported mean. Swap in the real series once you have
  the underlying month-by-month counts (e.g. the source workbook the report
  references).

## Design lineage
This POC intentionally reuses the visual language of a reference dashboard
you shared — same gradient background, glass card treatment, gradient
stat-tile colors, pill tabs with gradient active state, and priority-badged
recommendation cards — but every screen, chart, and data point here is the
Tamluk courts' docket data, not that reference project's data.

## Extending
- `data.py` currently carries the top case types per court (kept short for a
  POC). The PDF's tables have more rows ("N smaller case types omitted") —
  add them the same way to make the register exhaustive.
- To go from POC to production: replace `data.py` with a real DB/query layer
  that computes these stats from raw case records, and swap
  `illustrative_series` in `app.py` for a real month-by-month query.
