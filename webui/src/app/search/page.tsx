'use client'

import { useState } from 'react'
import { Search, FileText, Loader2 } from 'lucide-react'

interface SearchResult {
  language: string
  category: string
  name: string
  matches: string[]
}

export default function SearchPage() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<SearchResult[]>([])
  const [loading, setLoading] = useState(false)
  const [searched, setSearched] = useState(false)

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!query.trim()) return

    setLoading(true)
    setSearched(true)
    try {
      const res = await fetch('/api/search?q=' + encodeURIComponent(query))
      const data = await res.json()
      setResults(data.results || [])
    } catch (err) {
      console.error('Search failed:', err)
      setResults([])
    }
    setLoading(false)
  }

  return (
    <div className="min-h-screen p-8">
      <div className="max-w-4xl mx-auto">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-slate-900 dark:text-white mb-2">
            Search Specs
          </h1>
          <p className="text-slate-600 dark:text-slate-300">
            Search across all language specifications and patterns
          </p>
        </header>

        <form onSubmit={handleSearch} className="mb-8">
          <div className="flex gap-4">
            <div className="flex-1 relative">
              <Search className="absolute left-4 top-1/2 transform -translate-y-1/2 w-5 h-5 text-slate-400" />
              <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Search for error handling, async patterns, security..."
                className="w-full pl-12 pr-4 py-3 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <button
              type="submit"
              disabled={loading || !query.trim()}
              className="px-6 py-3 bg-blue-500 hover:bg-blue-600 disabled:bg-slate-300 dark:disabled:bg-slate-600 text-white rounded-xl font-medium transition-colors flex items-center gap-2"
            >
              {loading ? <Loader2 className="w-5 h-5 animate-spin" /> : <Search className="w-5 h-5" />}
              Search
            </button>
          </div>
        </form>

        {loading ? (
          <div className="flex items-center justify-center py-12">
            <Loader2 className="w-8 h-8 animate-spin text-blue-500" />
          </div>
        ) : results.length > 0 ? (
          <div className="space-y-4">
            <p className="text-sm text-slate-500 dark:text-slate-400">
              Found {results.length} results
            </p>
            {results.map((result, index) => (
              <div
                key={index}
                className="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-6"
              >
                <div className="flex items-center gap-2 mb-3">
                  <FileText className="w-5 h-5 text-blue-500" />
                  <span className="font-medium text-slate-900 dark:text-white">
                    {result.language}/{result.category}/{result.name}
                  </span>
                </div>
                {result.matches.map((match, matchIndex) => (
                  <pre
                    key={matchIndex}
                    className="bg-slate-50 dark:bg-slate-900 rounded-lg p-4 text-sm text-slate-700 dark:text-slate-300 overflow-x-auto whitespace-pre-wrap mt-2"
                  >
                    {match}
                  </pre>
                ))}
              </div>
            ))}
          </div>
        ) : searched ? (
          <div className="text-center py-12">
            <Search className="w-12 h-12 mx-auto text-slate-400 mb-4" />
            <p className="text-slate-500 dark:text-slate-400">
              No results found for "{query}"
            </p>
          </div>
        ) : (
          <div className="text-center py-12">
            <Search className="w-12 h-12 mx-auto text-slate-400 mb-4" />
            <p className="text-slate-500 dark:text-slate-400">
              Enter a search term to find relevant documentation
            </p>
            <div className="mt-6 flex flex-wrap gap-2 justify-center">
              {['error handling', 'async await', 'null safety', 'type guards', 'dependency injection'].map((term) => (
                <button
                  key={term}
                  onClick={() => setQuery(term)}
                  className="px-3 py-1 bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 rounded-full text-sm hover:bg-slate-200 dark:hover:bg-slate-600 transition-colors"
                >
                  {term}
                </button>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
