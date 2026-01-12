'use client'

import { useState, useEffect } from 'react'
import { Settings, Save, RefreshCw, Check, AlertCircle } from 'lucide-react'

interface Config {
  specsDir: string
  cacheEnabled: boolean
  cacheTTL: number
  searchFallback: boolean
  resourcePageSize: number
  theme: 'light' | 'dark' | 'system'
}

export default function ConfigPage() {
  const [config, setConfig] = useState<Config>({
    specsDir: '',
    cacheEnabled: true,
    cacheTTL: 60000,
    searchFallback: true,
    resourcePageSize: 250,
    theme: 'system'
  })
  const [saved, setSaved] = useState(false)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchConfig()
  }, [])

  const fetchConfig = async () => {
    try {
      const res = await fetch('/api/config')
      const data = await res.json()
      setConfig(data.config || config)
    } catch (err) {
      console.error('Failed to fetch config:', err)
    }
    setLoading(false)
  }

  const saveConfig = async () => {
    try {
      const res = await fetch('/api/config', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(config)
      })
      if (res.ok) {
        setSaved(true)
        setTimeout(() => setSaved(false), 2000)
      }
    } catch (err) {
      console.error('Failed to save config:', err)
    }
  }

  if (loading) {
    return (
      <div className="min-h-screen p-8 flex items-center justify-center">
        <RefreshCw className="w-8 h-8 animate-spin text-blue-500" />
      </div>
    )
  }

  return (
    <div className="min-h-screen p-8">
      <div className="max-w-3xl mx-auto">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-slate-900 dark:text-white mb-2">
            Configuration
          </h1>
          <p className="text-slate-600 dark:text-slate-300">
            Configure SpecForge plugin settings
          </p>
        </header>

        <div className="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 divide-y divide-slate-200 dark:divide-slate-700">
          <div className="p-6">
            <h2 className="text-lg font-semibold text-slate-900 dark:text-white mb-4">
              General Settings
            </h2>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">
                  Specs Directory
                </label>
                <input
                  type="text"
                  value={config.specsDir}
                  onChange={(e) => setConfig({ ...config, specsDir: e.target.value })}
                  className="w-full px-4 py-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white"
                  placeholder="/path/to/specs"
                />
                <p className="text-xs text-slate-500 mt-1">
                  Directory containing language specifications
                </p>
              </div>

              <div>
                <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">
                  Theme
                </label>
                <select
                  value={config.theme}
                  onChange={(e) => setConfig({ ...config, theme: e.target.value as Config['theme'] })}
                  className="w-full px-4 py-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white"
                >
                  <option value="system">System</option>
                  <option value="light">Light</option>
                  <option value="dark">Dark</option>
                </select>
              </div>
            </div>
          </div>

          <div className="p-6">
            <h2 className="text-lg font-semibold text-slate-900 dark:text-white mb-4">
              Performance
            </h2>
            
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <label className="text-sm font-medium text-slate-700 dark:text-slate-300">
                    Enable Caching
                  </label>
                  <p className="text-xs text-slate-500">
                    Cache spec files and search indexes
                  </p>
                </div>
                <button
                  onClick={() => setConfig({ ...config, cacheEnabled: !config.cacheEnabled })}
                  className={[
                    'relative w-12 h-6 rounded-full transition-colors',
                    config.cacheEnabled ? 'bg-blue-500' : 'bg-slate-300 dark:bg-slate-600'
                  ].join(' ')}
                >
                  <span
                    className={[
                      'absolute top-1 w-4 h-4 bg-white rounded-full transition-transform',
                      config.cacheEnabled ? 'left-7' : 'left-1'
                    ].join(' ')}
                  />
                </button>
              </div>

              <div>
                <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">
                  Cache TTL (ms)
                </label>
                <input
                  type="number"
                  value={config.cacheTTL}
                  onChange={(e) => setConfig({ ...config, cacheTTL: parseInt(e.target.value) || 60000 })}
                  className="w-full px-4 py-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">
                  Resource Page Size
                </label>
                <input
                  type="number"
                  value={config.resourcePageSize}
                  onChange={(e) => setConfig({ ...config, resourcePageSize: parseInt(e.target.value) || 250 })}
                  min={25}
                  max={1000}
                  className="w-full px-4 py-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white"
                />
              </div>
            </div>
          </div>

          <div className="p-6">
            <h2 className="text-lg font-semibold text-slate-900 dark:text-white mb-4">
              Search Settings
            </h2>
            
            <div className="flex items-center justify-between">
              <div>
                <label className="text-sm font-medium text-slate-700 dark:text-slate-300">
                  Enable Search Fallback
                </label>
                <p className="text-xs text-slate-500">
                  Scan markdown files when search index is unavailable
                </p>
              </div>
              <button
                onClick={() => setConfig({ ...config, searchFallback: !config.searchFallback })}
                className={[
                  'relative w-12 h-6 rounded-full transition-colors',
                  config.searchFallback ? 'bg-blue-500' : 'bg-slate-300 dark:bg-slate-600'
                ].join(' ')}
              >
                <span
                  className={[
                    'absolute top-1 w-4 h-4 bg-white rounded-full transition-transform',
                    config.searchFallback ? 'left-7' : 'left-1'
                  ].join(' ')}
                />
              </button>
            </div>
          </div>
        </div>

        <div className="mt-6 flex items-center justify-between">
          <div className="flex items-center gap-2">
            {saved && (
              <>
                <Check className="w-5 h-5 text-green-500" />
                <span className="text-green-600 dark:text-green-400 text-sm">
                  Settings saved
                </span>
              </>
            )}
          </div>
          <button
            onClick={saveConfig}
            className="flex items-center gap-2 px-6 py-2 bg-blue-500 hover:bg-blue-600 text-white rounded-lg font-medium transition-colors"
          >
            <Save className="w-5 h-5" />
            Save Changes
          </button>
        </div>

        <div className="mt-8 p-4 bg-amber-50 dark:bg-amber-900/20 rounded-xl border border-amber-200 dark:border-amber-800">
          <div className="flex items-start gap-3">
            <AlertCircle className="w-5 h-5 text-amber-500 mt-0.5" />
            <div>
              <h3 className="font-medium text-amber-800 dark:text-amber-200">
                Note
              </h3>
              <p className="text-sm text-amber-700 dark:text-amber-300 mt-1">
                Some settings may require restarting the plugin to take effect.
                Environment variables take precedence over these settings.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
