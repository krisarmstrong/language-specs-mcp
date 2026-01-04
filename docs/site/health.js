"use strict";
const generatedEl = document.getElementById("healthGenerated");
const languagesEl = document.getElementById("healthLanguages");
const staleEl = document.getElementById("healthStale");
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
    var _a, _b;
    if (!tableBody)
        return;
    const tr = document.createElement("tr");
    tr.className = statusClass(language);
    const linterCount = language.linters.reduce((sum, entry) => sum + entry.count, 0);
    const formatterCount = language.formatters.reduce((sum, entry) => sum + entry.count, 0);
    tr.innerHTML = `
    <td>
      <strong>${language.language}</strong>
      ${language.notes.length
        ? `<div class="health-notes">${language.notes.join(" • ")}</div>`
        : ""}
    </td>
    <td>${formatDate(language.fetchedAt)}</td>
    <td>${(_a = language.freshnessDays) !== null && _a !== void 0 ? _a : "N/A"} days</td>
    <td>
      <div class="health-counts">
        Spec ${language.spec.count} • Stdlib ${language.stdlib.count} • Linters ${linterCount} • Formatters ${formatterCount}
      </div>
    </td>
    <td>${(_b = language.toolsVersion) !== null && _b !== void 0 ? _b : "untracked"}</td>
    <td>${joinSources(language.toolSources)}</td>
  `;
    tableBody.appendChild(tr);
}
async function init() {
    if (!tableBody || !generatedEl || !languagesEl || !staleEl) {
        return;
    }
    const response = await fetch("./health.json");
    const data = await response.json();
    generatedEl.textContent = formatDate(data.generatedAt);
    languagesEl.textContent = String(data.languages.length);
    const staleCount = data.languages.filter((lang) => { var _a; return !lang.fetchedAt || ((_a = lang.freshnessDays) !== null && _a !== void 0 ? _a : Number.MAX_SAFE_INTEGER) > 30; }).length;
    staleEl.textContent = String(staleCount);
    data.languages.forEach(renderRow);
}
init().catch((err) => {
    if (tableBody) {
        tableBody.innerHTML = `<tr><td colspan="6">Failed to load health data: ${err.message}</td></tr>`;
    }
});
