# Data transcribed from: Purba Medinipur (Tamluk) Courts — Monthly Descriptive Analysis
# Window: Jan 2010 - Jun 2026 (198 months). Extracted 20 Jul 2026.

META = {
    "district": "Purba Medinipur (Tamluk)",
    "window_start": "Jan 2010",
    "window_end": "Jun 2026",
    "months": 198,
    "extracted_on": "20 Jul 2026",
    "courts": ["CJM", "DJ", "CJ (Sr.)", "CJ (Jr.)"],
}

COURTS = {
    "CJM": {
        "full_name": "Chief Judicial Magistrate",
        "listing_cutoff": "2017-01-01",
        "working_days": {"mean": 23.4, "min": 19, "max": 25},
        "arrivals": [
            {"case_type": "Gr Case", "side": "Criminal", "filings": 31136, "mean": 157.3, "median": 133.5, "max": 565, "daily_rate": 6.643},
            {"case_type": "M . P Case", "side": "Criminal", "filings": 7855, "mean": 39.7, "median": 35.5, "max": 140, "daily_rate": 1.683},
            {"case_type": "Misc", "side": "Criminal", "filings": 6859, "mean": 34.6, "median": 38.0, "max": 98, "daily_rate": 1.462},
            {"case_type": "Misc. Execution Case", "side": "Criminal", "filings": 6546, "mean": 33.1, "median": 32.0, "max": 86, "daily_rate": 1.395},
            {"case_type": "Cr Case", "side": "Criminal", "filings": 5661, "mean": 28.6, "median": 28.0, "max": 90, "daily_rate": 1.203},
            {"case_type": "Excise Case", "side": "Criminal", "filings": 1569, "mean": 7.9, "median": 6.0, "max": 28, "daily_rate": 0.335},
            {"case_type": "NGR Case", "side": "Criminal", "filings": 787, "mean": 4.0, "median": 3.0, "max": 27, "daily_rate": 0.168},
            {"case_type": "Complaint Case", "side": "Criminal", "filings": 610, "mean": 3.1, "median": 0.0, "max": 43, "daily_rate": 0.132},
        ],
        "gap": [
            {"case_type": "Gr Case", "n": 22047, "mean": 75.8, "median": 45, "p75": 83, "p90": 179, "p95": 256},
            {"case_type": "Misc. Execution Case", "n": 4408, "mean": 37.5, "median": 14, "p75": 69, "p90": 94, "p95": 113},
            {"case_type": "NGR Case", "n": 440, "mean": 24.2, "median": 8, "p75": 18, "p90": 39, "p95": 156},
            {"case_type": "Misc. P", "n": 85, "mean": 42.1, "median": 49, "p75": 67, "p90": 92, "p95": 121},
        ],
        "hearings_per_case": [
            {"case_type": "Gr Case", "n": 8901, "mean": 2.9, "median": 1, "p75": 5, "p90": 8, "p95": 10},
            {"case_type": "Cr Case", "n": 2061, "mean": 8.6, "median": 7, "p75": 12, "p90": 18, "p95": 22},
            {"case_type": "Misc", "n": 3967, "mean": 7.9, "median": 6, "p75": 11, "p90": 16, "p95": 21},
            {"case_type": "Misc. Execution Case", "n": 3359, "mean": 7.6, "median": 6, "p75": 10, "p90": 17, "p95": 21},
            {"case_type": "Excise Case", "n": 356, "mean": 10.5, "median": 11, "p75": 12, "p90": 13, "p95": 14},
        ],
        "hearing_rate_monthly": [
            {"case_type": "Gr Case", "mean": 48.848, "median": 52.146, "p75": 82.513, "p90": 93.362, "p95": 96.484},
            {"case_type": "Cr Case", "mean": 13.008, "median": 15.597, "p75": 22.750, "p90": 24.981, "p95": 25.895},
            {"case_type": "Misc", "mean": 12.858, "median": 14.102, "p75": 21.948, "p90": 25.968, "p95": 28.904},
            {"case_type": "Misc. Execution Case", "mean": 12.391, "median": 16.142, "p75": 20.125, "p90": 22.328, "p95": 23.235},
        ],
        "disposal": [
            {"case_type": "Gr Case", "n": 14871, "mean": 973, "median": 643, "p75": 1641, "p90": 2503, "p95": 2986},
            {"case_type": "M . P Case", "n": 7720, "mean": 18, "median": 0, "p75": 0, "p90": 30, "p95": 48},
            {"case_type": "Misc", "n": 5740, "mean": 670, "median": 541, "p75": 948, "p90": 1428, "p95": 1763},
            {"case_type": "Misc. Execution Case", "n": 5413, "mean": 671, "median": 460, "p75": 972, "p90": 1542, "p95": 1958},
            {"case_type": "Cr Case", "n": 3560, "mean": 1009, "median": 761, "p75": 1526, "p90": 2246, "p95": 2731},
            {"case_type": "Excise Case", "n": 629, "mean": 2085, "median": 2027, "p75": 2527, "p90": 3071, "p95": 3399},
        ],
    },
    "DJ": {
        "full_name": "District Judge",
        "listing_cutoff": "2015-01-01",
        "working_days": {"mean": 20.9, "min": 3, "max": 25},
        "arrivals": [
            {"case_type": "Criminal Misc.", "side": "Criminal", "filings": 20372, "mean": 102.9, "median": 98.5, "max": 346, "daily_rate": 4.593},
            {"case_type": "Electricity Act", "side": "Criminal", "filings": 13329, "mean": 67.3, "median": 57.5, "max": 297, "daily_rate": 3.050},
            {"case_type": "M A C C", "side": "Civil", "filings": 9953, "mean": 50.3, "median": 49.5, "max": 145, "daily_rate": 2.258},
            {"case_type": "Matrimonial Suit", "side": "Civil", "filings": 9148, "mean": 46.2, "median": 45.0, "max": 142, "daily_rate": 2.034},
            {"case_type": "Sessions Case", "side": "Criminal", "filings": 2346, "mean": 11.8, "median": 8.5, "max": 58, "daily_rate": 0.528},
            {"case_type": "Sessions Trial", "side": "Criminal", "filings": 2084, "mean": 10.5, "median": 9.0, "max": 46, "daily_rate": 0.465},
            {"case_type": "Misc", "side": "Criminal", "filings": 1905, "mean": 9.6, "median": 0.0, "max": 231, "daily_rate": 0.411},
            {"case_type": "Criminal Revision", "side": "Criminal", "filings": 1419, "mean": 7.2, "median": 5.0, "max": 67, "daily_rate": 0.316},
        ],
        "gap": [
            {"case_type": "Electricity Act", "n": 11325, "mean": 42.6, "median": 0, "p75": 0, "p90": 225, "p95": 267},
            {"case_type": "Matrimonial Suit", "n": 8256, "mean": 9.9, "median": 0, "p75": 0, "p90": 26, "p95": 123},
            {"case_type": "M A C C", "n": 8047, "mean": 6.2, "median": 0, "p75": 0, "p90": 27, "p95": 36},
            {"case_type": "Sessions Trial", "n": 1694, "mean": 27.2, "median": 6, "p75": 30, "p90": 69, "p95": 124},
        ],
        "hearings_per_case": [
            {"case_type": "Criminal Misc.", "n": 20361, "mean": 1.4, "median": 1, "p75": 2, "p90": 2, "p95": 3},
            {"case_type": "Electricity Act", "n": 8115, "mean": 3.9, "median": 3, "p75": 5, "p90": 9, "p95": 11},
            {"case_type": "Matrimonial Suit", "n": 6609, "mean": 5.3, "median": 4, "p75": 7, "p90": 12, "p95": 15},
            {"case_type": "M A C C", "n": 5166, "mean": 10.4, "median": 7, "p75": 14, "p90": 24, "p95": 31},
            {"case_type": "Sessions Trial", "n": 789, "mean": 20.6, "median": 17, "p75": 28, "p90": 39, "p95": 47},
        ],
        "hearing_rate_monthly": [
            {"case_type": "M A C C", "mean": 25.520, "median": 31.217, "p75": 41.889, "p90": 46.183, "p95": 47.925},
            {"case_type": "Electricity Act", "mean": 14.939, "median": 16.376, "p75": 23.604, "p90": 30.613, "p95": 33.476},
            {"case_type": "Matrimonial Suit", "mean": 9.971, "median": 9.915, "p75": 15.594, "p90": 20.476, "p95": 22.582},
            {"case_type": "Criminal Misc.", "mean": 6.371, "median": 5.837, "p75": 11.311, "p90": 14.688, "p95": 15.892},
        ],
        "disposal": [
            {"case_type": "Criminal Misc.", "n": 20363, "mean": 14, "median": 11, "p75": 17, "p90": 22, "p95": 24},
            {"case_type": "Electricity Act", "n": 10014, "mean": 820, "median": 516, "p75": 1196, "p90": 1989, "p95": 2532},
            {"case_type": "Matrimonial Suit", "n": 7564, "mean": 336, "median": 243, "p75": 423, "p90": 682, "p95": 870},
            {"case_type": "M A C C", "n": 7067, "mean": 684, "median": 498, "p75": 944, "p90": 1527, "p95": 1928},
            {"case_type": "Sessions Case", "n": 1477, "mean": 453, "median": 243, "p75": 660, "p90": 1222, "p95": 1580},
            {"case_type": "Title Appeal", "n": 517, "mean": 1177, "median": 990, "p75": 1589, "p90": 2252, "p95": 2905},
        ],
    },
    "CJ (Sr.)": {
        "full_name": "Civil Judge (Sr. Div.)",
        "listing_cutoff": "2015-01-01",
        "working_days": {"mean": 18.3, "min": 0, "max": 25},
        "arrivals": [
            {"case_type": "Title Suit", "side": "Civil", "filings": 3604, "mean": 18.2, "median": 18.0, "max": 43, "daily_rate": 0.951},
            {"case_type": "Other Suit", "side": "Civil", "filings": 1058, "mean": 5.3, "median": 2.0, "max": 51, "daily_rate": 0.290},
            {"case_type": "J.misc", "side": "Civil", "filings": 535, "mean": 2.7, "median": 2.0, "max": 11, "daily_rate": 0.139},
            {"case_type": "Money Suit", "side": "Civil", "filings": 275, "mean": 1.4, "median": 1.0, "max": 15, "daily_rate": None},
            {"case_type": "Succession Case", "side": "Civil", "filings": 241, "mean": 1.2, "median": 1.0, "max": 9, "daily_rate": None},
            {"case_type": "Probate Suit", "side": "Civil", "filings": 170, "mean": 0.9, "median": 1.0, "max": 5, "daily_rate": None},
        ],
        "gap": [
            {"case_type": "Title Suit", "n": 2790, "mean": 2.9, "median": 0, "p75": 0, "p90": 0, "p95": 15},
            {"case_type": "J.misc", "n": 474, "mean": 30.0, "median": 0, "p75": 0, "p90": 37, "p95": 191},
            {"case_type": "Sessions Trial", "n": 148, "mean": 79.2, "median": 29, "p75": 72, "p90": 139, "p95": 283},
            {"case_type": "Title Appeal", "n": 51, "mean": 127.2, "median": 44, "p75": 140, "p90": 299, "p95": 306},
        ],
        "hearings_per_case": [
            {"case_type": "Title Suit", "n": 1097, "mean": 19.4, "median": 16, "p75": 28, "p90": 40, "p95": 48},
            {"case_type": "Other Suit", "n": 553, "mean": 17.8, "median": 15, "p75": 25, "p90": 34, "p95": 37},
            {"case_type": "J.misc", "n": 213, "mean": 19.1, "median": 18, "p75": 27, "p90": 35, "p95": 39},
            {"case_type": "Succession Case", "n": 178, "mean": 14.9, "median": 13, "p75": 19, "p90": 24, "p95": 30},
        ],
        "hearing_rate_monthly": [
            {"case_type": "Title Suit", "mean": 22.643, "median": 29.389, "p75": 36.958, "p90": 40.252, "p95": 42.113},
            {"case_type": "Other Suit", "mean": 3.691, "median": 2.909, "p75": 6.500, "p90": 8.452, "p95": 9.585},
            {"case_type": "J.misc", "mean": 2.273, "median": 1.947, "p75": 3.960, "p90": 4.833, "p95": 5.098},
        ],
        "disposal": [
            {"case_type": "Title Suit", "n": 1782, "mean": 946, "median": 776, "p75": 1371, "p90": 2068, "p95": 2540},
            {"case_type": "Other Suit", "n": 926, "mean": 996, "median": 824, "p75": 1443, "p90": 2047, "p95": 2468},
            {"case_type": "J.misc", "n": 273, "mean": 902, "median": 789, "p75": 1346, "p90": 1758, "p95": 1980},
            {"case_type": "Money Suit", "n": 201, "mean": 920, "median": 798, "p75": 1271, "p90": 2006, "p95": 2406},
        ],
    },
    "CJ (Jr.)": {
        "full_name": "Civil Judge (Jr. Div.)",
        "listing_cutoff": "2015-01-01",
        "working_days": {"mean": 19.1, "min": 7, "max": 24},
        "arrivals": [
            {"case_type": "Title Suit", "side": "Civil", "filings": 4247, "mean": 21.4, "median": 22.0, "max": 47, "daily_rate": 1.161},
            {"case_type": "J.misc", "side": "Civil", "filings": 819, "mean": 4.1, "median": 4.0, "max": 15, "daily_rate": 0.209},
            {"case_type": "Other Suit", "side": "Civil", "filings": 777, "mean": 3.9, "median": 3.0, "max": 22, "daily_rate": 0.200},
            {"case_type": "Misc Case (pre-emption)", "side": "Civil", "filings": 764, "mean": 3.9, "median": 2.0, "max": 22, "daily_rate": 0.191},
            {"case_type": "Title Execution", "side": "Civil", "filings": 166, "mean": 0.8, "median": 0.5, "max": 8, "daily_rate": None},
        ],
        "gap": [
            {"case_type": "Title Suit", "n": 3001, "mean": 3.8, "median": 0, "p75": 0, "p90": 20, "p95": 24},
            {"case_type": "J.misc", "n": 678, "mean": 21.6, "median": 0, "p75": 0, "p90": 24, "p95": 44},
            {"case_type": "Misc Case (pre-emption)", "n": 749, "mean": 0.2, "median": 0, "p75": 0, "p90": 0, "p95": 0},
        ],
        "hearings_per_case": [
            {"case_type": "Title Suit", "n": 1733, "mean": 24.8, "median": 19, "p75": 35, "p90": 56, "p95": 65},
            {"case_type": "Other Suit", "n": 548, "mean": 13.9, "median": 9, "p75": 17, "p90": 32, "p95": 45},
            {"case_type": "Misc Case (pre-emption)", "n": 486, "mean": 15.9, "median": 13, "p75": 25, "p90": 35, "p95": 43},
            {"case_type": "J.misc", "n": 443, "mean": 22.8, "median": 18, "p75": 31, "p90": 46, "p95": 60},
        ],
        "hearing_rate_monthly": [
            {"case_type": "Title Suit", "mean": 38.799, "median": 47.958, "p75": 61.250, "p90": 71.574, "p95": 74.953},
            {"case_type": "J.misc", "mean": 5.287, "median": 6.550, "p75": 8.458, "p90": 10.242, "p95": 10.844},
            {"case_type": "Misc Case (pre-emption)", "mean": 3.012, "median": 1.458, "p75": 6.250, "p90": 7.589, "p95": 8.155},
        ],
        "disposal": [
            {"case_type": "Title Suit", "n": 2805, "mean": 934, "median": 740, "p75": 1321, "p90": 2054, "p95": 2479},
            {"case_type": "Other Suit", "n": 689, "mean": 434, "median": 296, "p75": 532, "p90": 994, "p95": 1438},
            {"case_type": "J.misc", "n": 575, "mean": 788, "median": 613, "p75": 1065, "p90": 1778, "p95": 2229},
            {"case_type": "Misc Case (pre-emption)", "n": 505, "mean": 451, "median": 339, "p75": 683, "p90": 1020, "p95": 1229},
        ],
    },
}

# Illustrative monthly-shape series for trend sparkline (derived from report's described
# growth patterns per court; for POC visualization only — not the underlying raw series).
TREND_NOTE = (
    "Trend shapes below approximate the report's described 12-month moving-average "
    "patterns (rise post-2016 digitisation, dip ~2020-21, recent moderation). "
    "They illustrate direction only — the source PDF provides summary statistics, "
    "not the raw month-by-month series."
)
