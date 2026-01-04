type HealthRecord = {
  language: string;
  fetchedAt: string | null;
  freshnessDays: number | null;
  spec: { count: number };
  stdlib: { count: number };
  linters: Array<{ count: number }>;
  formatters: Array<{ count: number }>;
  toolsVersion: string | null;
  toolSources: string[];
  notes: string[];
};

type HealthPayload = {
  generatedAt: string;
  languages: HealthRecord[];
};

const generatedEl = document.getElementById("healthGenerated");
const languagesEl = document.getElementById("healthLanguages");
const staleEl = document.getElementById("healthStale");
const tableBody = document.getElementById("healthTableBody");

function formatDate(value: string | null): string {
  if (!value) return "—";
  return new Date(value).toLocaleString();
}

function statusClass(language: HealthRecord): string {
  if (!language.fetchedAt) return "status-missing";
  const freshness = language.freshnessDays ?? Number.MAX_SAFE_INTEGER;
  if (freshness <= 7) return "status-good";
  if (freshness <= 30) return "status-warning";
  return "status-stale";
}

function joinSources(sources: string[]): string {
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

function renderRow(language: HealthRecord): void {
  if (!tableBody) return;
  const tr = document.createElement("tr");
  tr.className = statusClass(language);
  const linterCount = language.linters.reduce((sum, entry) => sum + entry.count, 0);
  const formatterCount = language.formatters.reduce((sum, entry) => sum + entry.count, 0);
  tr.innerHTML = `
    <td>
      <strong>${language.language}</strong>
      ${
        language.notes.length
          ? `<div class="health-notes">${language.notes.join(" • ")}</div>`
          : ""
      }
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

async function init(): Promise<void> {
  if (!tableBody || !generatedEl || !languagesEl || !staleEl) {
    return;
  }
  const response = await fetch("./health.json");
  const data: HealthPayload = await response.json();
  generatedEl.textContent = formatDate(data.generatedAt);
  languagesEl.textContent = String(data.languages.length);
  const staleCount = data.languages.filter(
    (lang) => !lang.fetchedAt || (lang.freshnessDays ?? Number.MAX_SAFE_INTEGER) > 30,
  ).length;
  staleEl.textContent = String(staleCount);
  data.languages.forEach(renderRow);
}

init().catch((err) => {
  if (tableBody) {
    tableBody.innerHTML = `<tr><td colspan="6">Failed to load health data: ${err.message}</td></tr>`;
  }
});
