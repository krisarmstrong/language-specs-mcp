type UrlStatus = {
  errors: number;
  redirects: number;
  status: "ok" | "degraded" | "critical";
};

type UrlError = {
  url: string;
  status: string;
  error?: string;
  httpCode?: number;
};

type HealthRecord = {
  language: string;
  fetchedAt: string | null;
  freshnessDays: number | null;
  spec: { count: number };
  stdlib: { count: number };
  linters: Array<{ count: number }>;
  formatters: Array<{ count: number }>;
  toolsVersion: string | null;
  toolCheckedAt: string | null;
  toolSources: string[];
  stubCount: number;
  searchIndexCount?: number;
  searchIndexGeneratedAt?: string | null;
  urlStatus?: UrlStatus;
  urlErrors?: UrlError[];
  urlRedirects?: UrlError[];
  notes: string[];
};

type UrlSummary = {
  total: number;
  ok: number;
  redirects: number;
  errors: number;
  timeouts: number;
};

type HealthPayload = {
  generatedAt: string;
  searchIndexGeneratedAt?: string | null;
  urlValidatedAt?: string | null;
  urlSummary?: UrlSummary;
  languages: HealthRecord[];
};

const generatedEl = document.getElementById("healthGenerated");
const searchGeneratedEl = document.getElementById("healthSearchGenerated");
const urlValidatedEl = document.getElementById("healthUrlValidated");
const languagesEl = document.getElementById("healthLanguages");
const staleEl = document.getElementById("healthStale");
const urlErrorsEl = document.getElementById("healthUrlErrors");
const urlRedirectsEl = document.getElementById("healthUrlRedirects");
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

function urlStatusBadge(urlStatus?: UrlStatus): string {
  if (!urlStatus) return '<span class="url-status url-status-unknown">Not checked</span>';
  const { status, errors, redirects } = urlStatus;
  let badgeClass = "url-status-ok";
  let label = "OK";
  if (status === "critical") {
    badgeClass = "url-status-critical";
    label = `${errors} errors`;
  } else if (status === "degraded") {
    badgeClass = "url-status-degraded";
    label = `${errors} errors`;
  } else if (redirects > 0) {
    badgeClass = "url-status-redirects";
    label = `${redirects} redirects`;
  }
  return `<span class="url-status ${badgeClass}">${label}</span>`;
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
  const searchCount = language.searchIndexCount ?? 0;
  tr.innerHTML = `
    <td>
      <strong>${language.language}</strong>
      ${
        language.notes.length ? `<div class="health-notes">${language.notes.join(" • ")}</div>` : ""
      }
    </td>
    <td>${formatDate(language.fetchedAt)}</td>
    <td>${language.freshnessDays ?? "N/A"} days</td>
    <td>
      <div class="health-counts">
        Spec ${language.spec.count} • Stdlib ${language.stdlib.count} • Linters ${linterCount} • Formatters ${formatterCount}
      </div>
    </td>
    <td>${language.stubCount ?? 0}</td>
    <td>${searchCount}</td>
    <td>${urlStatusBadge(language.urlStatus)}</td>
    <td>${language.toolsVersion ?? "untracked"}</td>
    <td>${joinSources(language.toolSources)}</td>
  `;
  tableBody.appendChild(tr);
}

async function init(): Promise<void> {
  if (!tableBody || !generatedEl || !languagesEl || !staleEl || !searchGeneratedEl) {
    return;
  }
  const response = await fetch("./health.json");
  const data: HealthPayload = await response.json();
  generatedEl.textContent = formatDate(data.generatedAt);
  searchGeneratedEl.textContent = formatDate(data.searchIndexGeneratedAt ?? null);
  if (urlValidatedEl) {
    urlValidatedEl.textContent = formatDate(data.urlValidatedAt ?? null);
  }
  languagesEl.textContent = String(data.languages.length);
  const staleCount = data.languages.filter(
    (lang) => !lang.fetchedAt || (lang.freshnessDays ?? Number.MAX_SAFE_INTEGER) > 30,
  ).length;
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
