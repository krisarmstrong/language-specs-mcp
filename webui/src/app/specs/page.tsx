'use client'

import { useState, useEffect } from 'react'
import { Book, FileCode, Folder } from 'lucide-react'

const LANGUAGES = [
  'assembly', 'basic', 'bash', 'batch', 'c', 'cpp', 'csharp', 'css',
  'dart', 'dockerfile', 'elixir', 'clojure', 'go', 'git', 'haskell',
  'html', 'java', 'javascript', 'julia', 'kotlin', 'lua', 'markdown',
  'ocaml', 'php', 'powershell', 'python', 'r', 'ruby', 'rust',
  'scala', 'sql', 'swift', 'typescript', 'yaml', 'zig'
]

const CATEGORIES = ['spec', 'stdlib', 'linters', 'patterns', 'formatters']

export default function SpecsPage() {
  const [selectedLanguage, setSelectedLanguage] = useState<string | null>(null)
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null)
  const [specs, setSpecs] = useState<string[]>([])
  const [specContent, setSpecContent] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)

  const fetchSpecs = async (language: string, category: string) => {
    setLoading(true)
    try {
      const res = await fetch('/api/specs?language=' + language + '&category=' + category)
      const data = await res.json()
      setSpecs(data.specs || [])
    } catch (err) {
      console.error('Failed to fetch specs:', err)
      setSpecs([])
    }
    setLoading(false)
  }

  const fetchSpecContent = async (language: string, category: string, topic: string) => {
    setLoading(true)
    try {
      const res = await fetch('/api/specs?language=' + language + '&category=' + category + '&topic=' + topic)
      const data = await res.json()
      setSpecContent(data.content || 'No content available')
    } catch (err) {
      console.error('Failed to fetch spec content:', err)
      setSpecContent('Failed to load content')
    }
    setLoading(false)
  }

  useEffect(() => {
    if (selectedLanguage && selectedCategory) {
      fetchSpecs(selectedLanguage, selectedCategory)
    }
  }, [selectedLanguage, selectedCategory])

  const selectLanguage = (lang: string) => {
    setSelectedLanguage(lang)
    setSelectedCategory(null)
    setSpecs([])
    setSpecContent(null)
  }

  const selectCategory = (cat: string) => {
    setSelectedCategory(cat)
    setSpecContent(null)
  }

  return (
    <div className="min-h-screen p-8">
      <div className="max-w-7xl mx-auto">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-slate-900 dark:text-white mb-2">
            Spec Browser
          </h1>
          <p className="text-slate-600 dark:text-slate-300">
            Browse language specifications, linter rules, and coding patterns
          </p>
        </header>

        <div className="flex gap-6">
          <div className="w-48 shrink-0">
            <h2 className="text-sm font-semibold text-slate-500 dark:text-slate-400 uppercase mb-3">
              Languages
            </h2>
            <div className="space-y-1 max-h-96 overflow-y-auto">
              {LANGUAGES.map((lang) => (
                <button
                  key={lang}
                  onClick={() => selectLanguage(lang)}
                  className={[
                    'w-full text-left px-3 py-2 rounded-lg text-sm transition-colors',
                    selectedLanguage === lang
                      ? 'bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300'
                      : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'
                  ].join(' ')}
                >
                  {lang}
                </button>
              ))}
            </div>
          </div>

          {selectedLanguage && (
            <div className="w-48 shrink-0">
              <h2 className="text-sm font-semibold text-slate-500 dark:text-slate-400 uppercase mb-3">
                Categories
              </h2>
              <div className="space-y-1">
                {CATEGORIES.map((cat) => (
                  <button
                    key={cat}
                    onClick={() => selectCategory(cat)}
                    className={[
                      'w-full text-left px-3 py-2 rounded-lg text-sm transition-colors flex items-center gap-2',
                      selectedCategory === cat
                        ? 'bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300'
                        : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'
                    ].join(' ')}
                  >
                    <Folder className="w-4 h-4" />
                    {cat}
                  </button>
                ))}
              </div>
            </div>
          )}

          {selectedCategory && (
            <div className="w-64 shrink-0">
              <h2 className="text-sm font-semibold text-slate-500 dark:text-slate-400 uppercase mb-3">
                Available Specs
              </h2>
              {loading && !specContent ? (
                <p className="text-slate-500">Loading...</p>
              ) : specs.length > 0 ? (
                <div className="space-y-1 max-h-96 overflow-y-auto">
                  {specs.map((spec) => (
                    <button
                      key={spec}
                      onClick={() => fetchSpecContent(selectedLanguage!, selectedCategory!, spec)}
                      className="w-full text-left px-3 py-2 rounded-lg text-sm text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 transition-colors flex items-center gap-2"
                    >
                      <FileCode className="w-4 h-4" />
                      {spec}
                    </button>
                  ))}
                </div>
              ) : (
                <p className="text-slate-500 text-sm">No specs available</p>
              )}
            </div>
          )}

          <div className="flex-1 min-w-0">
            {specContent ? (
              <div className="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-6 overflow-auto max-h-[600px]">
                <div className="prose dark:prose-invert max-w-none">
                  <pre className="whitespace-pre-wrap text-sm">{specContent}</pre>
                </div>
              </div>
            ) : (
              <div className="bg-slate-100 dark:bg-slate-800/50 rounded-xl border-2 border-dashed border-slate-300 dark:border-slate-600 p-12 text-center">
                <Book className="w-12 h-12 mx-auto text-slate-400 mb-4" />
                <p className="text-slate-500 dark:text-slate-400">
                  Select a language, category, and spec to view documentation
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}
