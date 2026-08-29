// Tamluk Courts Docket Intelligence — frontend logic
const API_BASE = '/api';

let metaCache = null;
let currentCourt = null;
let currentCourtData = null;
let charts = {};

const PALETTE = ['#60a5fa', '#a78bfa', '#f472b6', '#fbbf24', '#4ade80', '#f87171', '#38bdf8', '#c084fc'];

Chart.defaults.color = '#c4b5fd';
Chart.defaults.font.family = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif";

document.addEventListener('DOMContentLoaded', async () => {
    await loadAllData();
    setupEventListeners();
});

async function loadAllData() {
    try {
        updateProgress(15, 'Loading court metadata...');
        const metaRes = await fetch(`${API_BASE}/meta`);
        metaCache = await metaRes.json();

        updateProgress(45, 'Fetching case registers...');
        const firstCourt = document.getElementById('courtFilter').value;

        updateProgress(70, 'Computing working-day rates...');
        await selectCourt(firstCourt);

        updateProgress(100, 'Complete!');

        setTimeout(() => {
            document.getElementById('loadingScreen').style.display = 'none';
            document.getElementById('mainDashboard').style.display = 'block';
        }, 400);

    } catch (error) {
        console.error('Error loading data:', error);
        updateProgress(100, 'Error loading data');
        setTimeout(() => {
            document.getElementById('loadingScreen').style.display = 'none';
            document.getElementById('mainDashboard').style.display = 'block';
        }, 800);
    }
}

function updateProgress(percent, text) {
    document.getElementById('progressFill').style.width = `${percent}%`;
    document.getElementById('progressText').textContent = text ? `${text}` : `${percent}%`;
}

function setupEventListeners() {
    document.getElementById('courtFilter').addEventListener('change', (e) => {
        selectCourt(e.target.value);
    });

    document.getElementById('caseTypeFilter').addEventListener('change', () => {
        renderRegisterTable();
    });

    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
            btn.classList.add('active');
            document.getElementById(btn.dataset.tab).classList.add('active');
        });
    });

    document.getElementById('exportBtn').addEventListener('click', exportCurrentCourt);
}

function fmt(n) {
    if (n === null || n === undefined) return '—';
    return Number(n).toLocaleString('en-IN');
}

async function selectCourt(code) {
    currentCourt = code;
    const [courtRes, trendRes, insightsRes] = await Promise.all([
        fetch(`${API_BASE}/court/${code}`),
        fetch(`${API_BASE}/court/${code}/trend`),
        fetch(`${API_BASE}/court/${code}/insights`),
    ]);
    currentCourtData = await courtRes.json();
    const trendData = await trendRes.json();
    const insightsData = await insightsRes.json();

    populateCaseTypeFilter(currentCourtData);
    renderStatCards(code, currentCourtData);
    renderDistributionChart(currentCourtData);
    renderHearingsChart(currentCourtData);
    renderTopPerformers(currentCourtData);
    renderTrendChart(trendData);
    renderMeanFilingsChart(currentCourtData);
    renderDisposalChart(currentCourtData);
    renderGapChart(currentCourtData);
    renderOutliers(currentCourtData);
    renderRegisterTable();
    renderInsights(insightsData);

    document.getElementById('footnoteText').textContent =
        `Gap and hearing-count measures use this court's listing-reliable cut-off (${currentCourtData.listing_cutoff}); ` +
        `arrivals and disposal use the full ${metaCache.meta.window_start}\u2013${metaCache.meta.window_end} window. ` +
        trendData.note;
}

function populateCaseTypeFilter(courtData) {
    const sel = document.getElementById('caseTypeFilter');
    sel.innerHTML = '<option value="all">All Case Types</option>' +
        courtData.arrivals.map(a => `<option value="${a.case_type}">${a.case_type}</option>`).join('');
}

function renderStatCards(code, courtData) {
    const totals = metaCache.court_totals[code];
    const top = courtData.arrivals[0];
    const disposalByType = {};
    courtData.disposal.forEach(d => disposalByType[d.case_type] = d);
    const topDisposal = disposalByType[top.case_type];

    document.getElementById('totalFilings').textContent = fmt(totals.total_filings);
    document.getElementById('totalFilingsSub').textContent = `${totals.case_types_tracked} case types tracked`;

    document.getElementById('avgMonthly').textContent = top.mean;
    document.getElementById('avgMonthlySub').textContent = `${top.case_type} (mean/mo)`;

    document.getElementById('peakFilings').textContent = fmt(top.max);
    document.getElementById('peakCaseType').textContent = `${top.case_type}, single busiest month`;

    document.getElementById('medianDisposal').textContent = topDisposal ? fmt(topDisposal.median) : '—';
    document.getElementById('medianDisposalSub').textContent = topDisposal
        ? `working days \u2014 ${top.case_type}` : 'working days';
}

function destroy(key) {
    if (charts[key]) { charts[key].destroy(); delete charts[key]; }
}

function renderDistributionChart(courtData) {
    const rows = courtData.arrivals.slice(0, 7);
    destroy('dist');
    charts.dist = new Chart(document.getElementById('distributionChart'), {
        type: 'doughnut',
        data: {
            labels: rows.map(r => r.case_type),
            datasets: [{
                data: rows.map(r => r.filings),
                backgroundColor: PALETTE,
                borderColor: '#1e293b',
                borderWidth: 2,
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { position: 'bottom', labels: { color: '#c4b5fd', boxWidth: 12 } } },
            cutout: '55%',
        }
    });
}

function renderHearingsChart(courtData) {
    const rows = courtData.hearings_per_case.slice(0, 6);
    destroy('hearings');
    charts.hearings = new Chart(document.getElementById('hearingsChart'), {
        type: 'bar',
        data: {
            labels: rows.map(r => r.case_type),
            datasets: [{
                label: 'Median hearings',
                data: rows.map(r => r.median),
                backgroundColor: 'rgba(96,165,250,0.7)',
                borderRadius: 4,
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            plugins: { legend: { display: false } },
            scales: {
                x: { ticks: { color: '#c4b5fd' }, grid: { color: 'rgba(148,163,184,0.1)' } },
                y: { ticks: { color: '#e2e8f0' }, grid: { display: false } }
            }
        }
    });
}

function renderTopPerformers(courtData) {
    const rows = courtData.arrivals.slice(0, 5);
    const el = document.getElementById('topPerformers');
    el.innerHTML = rows.map((r, i) => `
        <div class="performer-item">
            <div class="performer-info">
                <div class="performer-rank">${i + 1}</div>
                <div>
                    <div class="performer-name">${r.case_type}</div>
                    <div class="performer-sub">${r.side}</div>
                </div>
            </div>
            <div class="performer-value">${fmt(r.filings)}</div>
        </div>
    `).join('');
}

function renderTrendChart(trendData) {
    document.getElementById('trendCaption').textContent =
        `${trendData.case_type} \u2014 illustrative monthly shape (see footnote)`;
    destroy('trend');
    charts.trend = new Chart(document.getElementById('trendChart'), {
        type: 'line',
        data: {
            labels: trendData.labels,
            datasets: [{
                data: trendData.values,
                borderColor: '#a78bfa',
                backgroundColor: 'rgba(139,92,246,0.15)',
                fill: true,
                tension: 0.35,
                pointRadius: 0,
                borderWidth: 2,
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { display: false } },
            scales: {
                x: { ticks: { color: '#94a3b8', maxTicksLimit: 8 }, grid: { color: 'rgba(148,163,184,0.08)' } },
                y: { ticks: { color: '#94a3b8' }, grid: { color: 'rgba(148,163,184,0.08)' } }
            }
        }
    });
}

function renderMeanFilingsChart(courtData) {
    const rows = courtData.arrivals.slice(0, 8);
    destroy('meanFilings');
    charts.meanFilings = new Chart(document.getElementById('meanFilingsChart'), {
        type: 'bar',
        data: {
            labels: rows.map(r => r.case_type),
            datasets: [{
                label: 'Mean filings / month',
                data: rows.map(r => r.mean),
                backgroundColor: 'rgba(167,139,250,0.7)',
                borderRadius: 4,
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { display: false } },
            scales: {
                x: { ticks: { color: '#c4b5fd', maxRotation: 30, minRotation: 30 }, grid: { display: false } },
                y: { ticks: { color: '#94a3b8' }, grid: { color: 'rgba(148,163,184,0.08)' } }
            }
        }
    });
}

function renderDisposalChart(courtData) {
    const rows = courtData.disposal.slice(0, 6);
    destroy('disposal');
    charts.disposal = new Chart(document.getElementById('disposalChart'), {
        type: 'bar',
        data: {
            labels: rows.map(r => r.case_type),
            datasets: [
                { label: 'Median', data: rows.map(r => r.median), backgroundColor: 'rgba(96,165,250,0.75)', borderRadius: 4 },
                { label: '90th percentile', data: rows.map(r => r.p90), backgroundColor: 'rgba(244,114,182,0.6)', borderRadius: 4 },
            ]
        },
        options: {
            responsive: true,
            plugins: { legend: { position: 'bottom', labels: { color: '#c4b5fd' } } },
            scales: {
                x: { ticks: { color: '#c4b5fd', maxRotation: 30, minRotation: 30 }, grid: { display: false } },
                y: { ticks: { color: '#94a3b8' }, grid: { color: 'rgba(148,163,184,0.08)' }, title: { display: true, text: 'working days', color: '#94a3b8' } }
            }
        }
    });
}

function renderGapChart(courtData) {
    const rows = courtData.gap.slice(0, 6);
    destroy('gap');
    charts.gap = new Chart(document.getElementById('gapChart'), {
        type: 'bar',
        data: {
            labels: rows.map(r => r.case_type),
            datasets: [
                { label: 'Median', data: rows.map(r => r.median), backgroundColor: 'rgba(74,222,128,0.7)', borderRadius: 4 },
                { label: '90th percentile', data: rows.map(r => r.p90), backgroundColor: 'rgba(251,191,36,0.7)', borderRadius: 4 },
            ]
        },
        options: {
            responsive: true,
            plugins: { legend: { position: 'bottom', labels: { color: '#c4b5fd' } } },
            scales: {
                x: { ticks: { color: '#c4b5fd', maxRotation: 30, minRotation: 30 }, grid: { display: false } },
                y: { ticks: { color: '#94a3b8' }, grid: { color: 'rgba(148,163,184,0.08)' }, title: { display: true, text: 'working days', color: '#94a3b8' } }
            }
        }
    });
}

function renderOutliers(courtData) {
    const flagged = courtData.gap.filter(g => g.p90 > 100);
    document.getElementById('outlierCount').textContent = `${flagged.length} case type(s) flagged \u2014 90th-pct listing gap over 100 working days`;
    const el = document.getElementById('outliersList');
    el.innerHTML = flagged.map(g => `
        <div class="anomaly-card">
            <div class="anomaly-date">${g.case_type}</div>
            <div class="anomaly-value">${g.p90} wd</div>
            <div class="anomaly-score">90th pct \u2014 median ${g.median} wd</div>
        </div>
    `).join('') || '<p style="color:#94a3b8;">No case types exceed the 100-working-day threshold at this court.</p>';
}

function renderRegisterTable() {
    if (!currentCourtData) return;
    document.getElementById('registerCourtName').textContent =
        metaCache.court_totals[currentCourt].full_name;

    const filterVal = document.getElementById('caseTypeFilter').value;
    const dispByType = {};
    currentCourtData.disposal.forEach(d => dispByType[d.case_type] = d);

    const rows = currentCourtData.arrivals.filter(a => filterVal === 'all' || a.case_type === filterVal);

    document.getElementById('registerBody').innerHTML = rows.map(a => {
        const d = dispByType[a.case_type];
        const sideClass = a.side.toLowerCase();
        return `
            <tr>
                <td>${a.case_type}</td>
                <td><span class="side-pill ${sideClass}">${a.side}</span></td>
                <td>${fmt(a.filings)}</td>
                <td>${a.mean}</td>
                <td>${a.median}</td>
                <td>${d ? fmt(d.median) : '—'}</td>
                <td>${d ? fmt(d.p90) : '—'}</td>
            </tr>
        `;
    }).join('');
}

function renderInsights(insightsData) {
    document.getElementById('insightsList').innerHTML =
        insightsData.insights.map(i => `<li>${i}</li>`).join('');

    const iconAlert = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" stroke-width="2"/><line x1="12" y1="9" x2="12" y2="13" stroke-width="2"/><line x1="12" y1="17" x2="12.01" y2="17" stroke-width="2"/></svg>`;

    document.getElementById('recommendationsList').innerHTML = insightsData.recommendations.map(r => {
        const cls = r.priority === 'high' ? 'rec-alert' : r.priority === 'medium' ? 'rec-warning' : 'rec-info';
        const badgeCls = `priority-${r.priority}`;
        return `
            <div class="recommendation-card ${cls}">
                <div class="rec-header">
                    <div class="rec-title-group">
                        ${iconAlert}
                        <div class="rec-title">${r.title}</div>
                    </div>
                    <span class="priority-badge ${badgeCls}">${r.priority.toUpperCase()}</span>
                </div>
                <p class="rec-description">${r.description}</p>
                <div class="rec-action-box">
                    <div class="rec-label">Recommended Action</div>
                    <div class="rec-action">${r.action}</div>
                </div>
                <div class="rec-impact-box">
                    <div class="rec-label">Expected Impact</div>
                    <div class="rec-impact">${r.impact}</div>
                </div>
            </div>
        `;
    }).join('') || '<p style="color:#94a3b8;">No flagged items for this court under current thresholds.</p>';
}

function exportCurrentCourt() {
    if (!currentCourtData) return;
    const blob = new Blob([JSON.stringify(currentCourtData, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${currentCourt.replace(/[^a-z0-9]/gi, '_')}_docket_data.json`;
    a.click();
    URL.revokeObjectURL(url);
}
