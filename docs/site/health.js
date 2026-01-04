const generatedEl = document.getElementById("healthGenerated");
const languagesEl = document.getElementById("healthLanguages");
const staleEl = document.getElementById("healthStale");
const tableBody = document.getElementById("healthTableBody");

function formatDate(value) {
  if (!value) return "—";
  const date = new Date(value);
  return date.toLocaleString();
}

function statusClass(language) {
  if (!language.fetchedAt) return "status-missing";
  const freshness = language.freshnessDays ?? Infinity;
  if (freshness <= 7) return "status-good";
  if (freshness <= 30) return "status-warning";
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
      } catch {
        return url;
      }
    })
    .join(", ");
}

function renderRow(language) {
  const tr = document.createElement("tr");
  tr.className = statusClass(language);
  const specCounts = `${language.spec.count} / ${language.stdlib.count}`;
  const linterCount = language.linters.reduce((sum, entry) => sum + entry.count, 0);
  const formatterCount = language.formatters.reduce((sum, entry) => sum + entry.count, 0);
  tr.innerHTML = `
    <td>
      <strong>${language.language}</strong>
      ${language.notes.length ? `<div class="health-notes">${language.notes.join(" • ")}</div>` : ""}
    </td>
    <td>${formatDate(language.fetchedAt)}</td>
    <td>${language.freshnessDays ?? "N/A"} days</td>
    <td>
      <div class="health-counts">
        Spec ${language.spec.count} • Stdlib ${language.stdlib.count} • Linters ${linterCount} • Formatters ${formatterCount}
      </div>
    </td>
    <td>${language.toolsVersion ?? "untracked"}</td>
    <td>${joinSources(language.toolSources)}</td>
  `;
  tableBody.appendChild(tr);
}

async function init() {
  const response = await fetch("./health.json");
  const data = await response.json();
  generatedEl.textContent = formatDate(data.generatedAt);
  languagesEl.textContent = data.languages.length;
  const staleCount = data.languages.filter((lang) => !lang.fetchedAt || (lang.freshnessDays ?? Infinity) > 30).length;
  staleEl.textContent = staleCount;
  data.languages.forEach(renderRow);
}

init().catch((err) => {
  tableBody.innerHTML = `<tr><td colspan="6">Failed to load health data: ${err.message}</td></tr>`;
});
