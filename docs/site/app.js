const languageList = document.getElementById("languageList");
const fileList = document.getElementById("fileList");
const preview = document.getElementById("preview");
const activeLanguage = document.getElementById("activeLanguage");
const fetchedAt = document.getElementById("fetchedAt");
const generatedAt = document.getElementById("generatedAt");
const languageCount = document.getElementById("languageCount");
const searchInput = document.getElementById("search");
const contentSearchToggle = document.getElementById("contentSearch");
const pills = Array.from(document.querySelectorAll(".pill"));

let indexData = null;
let selectedLanguage = null;
let selectedFilter = "all";
const languageCache = new Map();
const languageSearchCache = new Map();

function setActivePill(value) {
  selectedFilter = value;
  pills.forEach((pill) => pill.classList.toggle("active", pill.dataset.filter === value));
  renderFiles();
}

pills.forEach((pill) => {
  pill.addEventListener("click", () => setActivePill(pill.dataset.filter));
});

searchInput.addEventListener("input", () => renderFiles());
contentSearchToggle.addEventListener("change", () => renderFiles());

function matchesFilter(item) {
  if (selectedFilter === "all") return true;
  return item.category === selectedFilter;
}

function matchesSearch(item, query) {
  if (!query) return true;
  const haystack = `${item.category} ${item.path} ${item.name}`.toLowerCase();
  return haystack.includes(query);
}

function findSnippet(content, query) {
  const lines = content.split("\n");
  const needle = query.toLowerCase();
  for (let i = 0; i < lines.length; i += 1) {
    if (lines[i]?.toLowerCase().includes(needle)) {
      const start = Math.max(0, i - 1);
      const end = Math.min(lines.length, i + 2);
      return lines.slice(start, end).join("\n");
    }
  }
  return "";
}

async function loadSearchIndex(language) {
  if (!languageSearchCache.has(language)) {
    const response = await fetch(`./specs/${language}/search.json`);
    const data = await response.json();
    data.entries.forEach((entry) => {
      entry.contentLower = entry.content.toLowerCase();
    });
    languageSearchCache.set(language, data);
  }
  return languageSearchCache.get(language);
}

function renderFiles() {
  if (!selectedLanguage) return;
  const data = languageCache.get(selectedLanguage);
  if (!data) return;

  const query = searchInput.value.trim().toLowerCase();
  if (contentSearchToggle.checked && query) {
    loadSearchIndex(selectedLanguage).then((searchData) => {
      const matches = searchData.entries.filter(
        (entry) =>
          matchesFilter(entry) &&
          (entry.contentLower?.includes(query) || matchesSearch(entry, query)),
      );
      renderFileCards(matches, query, data.language);
    });
    return;
  }

  const items = data.items.filter((item) => matchesFilter(item) && matchesSearch(item, query));
  renderFileCards(items, query, data.language);
}

function renderFileCards(items, query, language) {
  fileList.innerHTML = "";
  if (items.length === 0) {
    fileList.innerHTML = "<p>No matches found.</p>";
    return;
  }

  const fragment = document.createDocumentFragment();
  items.slice(0, 200).forEach((item) => {
    const snippet = query && item.content ? findSnippet(item.content, query) : "";
    const card = document.createElement("button");
    card.type = "button";
    card.className = "file-card";
    card.innerHTML = `
      <div class="file-name">${item.name}</div>
      <div class="file-meta">${item.category} • ${item.path}</div>
      ${snippet ? `<pre class="snippet">${snippet}</pre>` : ""}
    `;
    card.addEventListener("click", () => loadPreview(language, item.path));
    fragment.appendChild(card);
  });
  fileList.appendChild(fragment);
}

function renderLanguages() {
  if (!indexData) return;
  languageCount.textContent = indexData.languages.length;
  generatedAt.textContent = new Date(indexData.generatedAt).toISOString();
  languageList.innerHTML = "";

  const fragment = document.createDocumentFragment();
  indexData.languages.forEach((lang) => {
    const card = document.createElement("button");
    card.type = "button";
    card.className = "lang-card";
    card.innerHTML = `
      <div class="lang-name">${lang.language}</div>
      <div class="lang-meta">spec ${lang.counts.spec} • stdlib ${lang.counts.stdlib}</div>
    `;
    card.addEventListener("click", () => selectLanguage(lang.language, card));
    fragment.appendChild(card);
  });
  languageList.appendChild(fragment);
}

async function selectLanguage(language, card) {
  selectedLanguage = language;
  document.querySelectorAll(".lang-card").forEach((btn) => btn.classList.remove("active"));
  card.classList.add("active");
  await loadLanguage(language);
  setActivePill("all");
}

async function loadLanguage(language) {
  if (!languageCache.has(language)) {
    const response = await fetch(`./specs/${language}/index.json`);
    const data = await response.json();
    languageCache.set(language, data);
  }
  const data = languageCache.get(language);
  activeLanguage.textContent = `${language} specs`;
  fetchedAt.textContent = `Fetched: ${data.fetchedAt}`;
  renderFiles();
}

async function loadPreview(language, path) {
  preview.textContent = "Loading preview...";
  const response = await fetch(`./specs/${language}/${path}`);
  const text = await response.text();
  preview.textContent = text;
}

async function init() {
  const response = await fetch("./specs/index.json");
  indexData = await response.json();
  renderLanguages();
}

init();
