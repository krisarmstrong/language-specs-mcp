"use strict";
const generatedEl = document.getElementById("healthGenerated");
const searchGeneratedEl = document.getElementById("healthSearchGenerated");
const urlValidatedEl = document.getElementById("healthUrlValidated");
const languagesEl = document.getElementById("healthLanguages");
const staleEl = document.getElementById("healthStale");
const urlErrorsEl = document.getElementById("healthUrlErrors");
const urlRedirectsEl = document.getElementById("healthUrlRedirects");
const tableBody = document.getElementById("healthTableBody");
function formatDate(value) {
    if (!value)
        return "—";
    return new Date(value).toLocaleString();
}
function statusClass(language) {
    var _a;
    if (!language.fetchedAt)
        return "status-missing";
    const freshness = (_a = language.freshnessDays) !== null && _a !== void 0 ? _a : Number.MAX_SAFE_INTEGER;
    if (freshness <= 7)
        return "status-good";
    if (freshness <= 30)
        return "status-warning";
    return "status-stale";
}
function urlStatusBadge(urlStatus) {
    if (!urlStatus)
        return '<span class="url-status url-status-unknown">Not checked</span>';
    const { status, errors, redirects } = urlStatus;
    let badgeClass = "url-status-ok";
    let label = "OK";
    if (status === "critical") {
        badgeClass = "url-status-critical";
        label = `${errors} errors`;
    }
    else if (status === "degraded") {
        badgeClass = "url-status-degraded";
        label = `${errors} errors`;
    }
    else if (redirects > 0) {
        badgeClass = "url-status-redirects";
        label = `${redirects} redirects`;
    }
    return `<span class="url-status ${badgeClass}">${label}</span>`;
}
function joinSources(sources) {
    if (!Array.isArray(sources) || sources.length === 0) {
        return "Unknown";
    }
    return sources
        .slice(0, 3)
        .map((url) => {
        try {
            return `<a href="${url}" target="_blank">${new URL(url).hostname}</a>`;
        }
        catch {
            return url;
        }
    })
        .join(", ");
}
function renderRow(language) {
    var _a, _b, _c, _d;
    if (!tableBody)
        return;
    const tr = document.createElement("tr");
    tr.className = statusClass(language);
    const linterCount = language.linters.reduce((sum, entry) => sum + entry.count, 0);
    const formatterCount = language.formatters.reduce((sum, entry) => sum + entry.count, 0);
    const searchCount = (_a = language.searchIndexCount) !== null && _a !== void 0 ? _a : 0;
    tr.innerHTML = `
    <td>
      <strong>${language.language}</strong>
      ${language.notes.length ? `<div class="health-notes">${language.notes.join(" • ")}</div>` : ""}
    </td>
    <td>${formatDate(language.fetchedAt)}</td>
    <td>${(_b = language.freshnessDays) !== null && _b !== void 0 ? _b : "N/A"} days</td>
    <td>
      <div class="health-counts">
        Spec ${language.spec.count} • Stdlib ${language.stdlib.count} • Linters ${linterCount} • Formatters ${formatterCount}
      </div>
    </td>
    <td>${(_c = language.stubCount) !== null && _c !== void 0 ? _c : 0}</td>
    <td>${searchCount}</td>
    <td>${urlStatusBadge(language.urlStatus)}</td>
    <td>${(_d = language.toolsVersion) !== null && _d !== void 0 ? _d : "untracked"}</td>
    <td>${joinSources(language.toolSources)}</td>
  `;
    tableBody.appendChild(tr);
}
async function init() {
    var _a, _b;
    if (!tableBody || !generatedEl || !languagesEl || !staleEl || !searchGeneratedEl) {
        return;
    }
    const response = await fetch("./health.json");
    const data = await response.json();
    generatedEl.textContent = formatDate(data.generatedAt);
    searchGeneratedEl.textContent = formatDate((_a = data.searchIndexGeneratedAt) !== null && _a !== void 0 ? _a : null);
    if (urlValidatedEl) {
        urlValidatedEl.textContent = formatDate((_b = data.urlValidatedAt) !== null && _b !== void 0 ? _b : null);
    }
    languagesEl.textContent = String(data.languages.length);
    const staleCount = data.languages.filter((lang) => { var _a; return !lang.fetchedAt || ((_a = lang.freshnessDays) !== null && _a !== void 0 ? _a : Number.MAX_SAFE_INTEGER) > 30; }).length;
    staleEl.textContent = String(staleCount);
    if (urlErrorsEl && data.urlSummary) {
        urlErrorsEl.textContent = String(data.urlSummary.errors + data.urlSummary.timeouts);
    }
    if (urlRedirectsEl && data.urlSummary) {
        urlRedirectsEl.textContent = String(data.urlSummary.redirects);
    }
    data.languages.forEach(renderRow);
}
init().catch((err) => {
    if (tableBody) {
        tableBody.textContent = `Failed to load health data: ${err.message}`;
    }
});
