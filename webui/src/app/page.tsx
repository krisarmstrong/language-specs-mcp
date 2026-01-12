import Link from 'next/link'
import { Book, Search, Brain, Settings, Shield, FileCode } from 'lucide-react'

const features = [
  {
    name: 'Spec Browser',
    description: 'Browse language specifications for 35+ languages',
    href: '/specs',
    icon: Book,
    color: 'bg-blue-500',
  },
  {
    name: 'Search',
    description: 'Search across all specifications and patterns',
    href: '/search',
    icon: Search,
    color: 'bg-green-500',
  },
  {
    name: 'Memories',
    description: 'Store and manage project-specific notes',
    href: '/memories',
    icon: Brain,
    color: 'bg-purple-500',
  },
  {
    name: 'Security',
    description: 'OWASP security checklist and guidelines',
    href: '/specs?category=security',
    icon: Shield,
    color: 'bg-red-500',
  },
  {
    name: 'Linter Rules',
    description: 'Detailed linter rule explanations',
    href: '/specs?category=linters',
    icon: FileCode,
    color: 'bg-orange-500',
  },
  {
    name: 'Configuration',
    description: 'Plugin settings and preferences',
    href: '/config',
    icon: Settings,
    color: 'bg-slate-500',
  },
]

export default function Home() {
  return (
    <div className="min-h-screen p-8">
      <div className="max-w-6xl mx-auto">
        <header className="mb-12">
          <h1 className="text-4xl font-bold text-slate-900 dark:text-white mb-4">
            SpecForge
          </h1>
          <p className="text-xl text-slate-600 dark:text-slate-300">
            Authoritative language specifications, linter rules, and coding patterns for LLMs.
            Replace Stack Overflow with actual best practices.
          </p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((feature) => (
            <Link
              key={feature.name}
              href={feature.href}
              className="group block p-6 bg-white dark:bg-slate-800 rounded-xl shadow-sm hover:shadow-md transition-shadow border border-slate-200 dark:border-slate-700"
            >
              <div className={`${feature.color} w-12 h-12 rounded-lg flex items-center justify-center mb-4`}>
                <feature.icon className="w-6 h-6 text-white" />
              </div>
              <h2 className="text-lg font-semibold text-slate-900 dark:text-white mb-2 group-hover:text-blue-600 dark:group-hover:text-blue-400">
                {feature.name}
              </h2>
              <p className="text-slate-600 dark:text-slate-300">
                {feature.description}
              </p>
            </Link>
          ))}
        </div>

        <section className="mt-12 p-6 bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700">
          <h2 className="text-2xl font-semibold text-slate-900 dark:text-white mb-4">
            Quick Start
          </h2>
          <div className="space-y-4 text-slate-600 dark:text-slate-300">
            <p>
              <strong>Before writing code:</strong> Use <code className="bg-slate-100 dark:bg-slate-700 px-2 py-1 rounded">/checklist &lt;language&gt;</code> to get the pre-coding checklist.
            </p>
            <p>
              <strong>For linter help:</strong> Use <code className="bg-slate-100 dark:bg-slate-700 px-2 py-1 rounded">/lint-rule &lt;language&gt; &lt;linter&gt; &lt;rule&gt;</code> to understand why a rule exists.
            </p>
            <p>
              <strong>Search specs:</strong> Use <code className="bg-slate-100 dark:bg-slate-700 px-2 py-1 rounded">/search-specs &lt;query&gt;</code> to find patterns across all languages.
            </p>
          </div>
        </section>

        <section className="mt-8 p-6 bg-blue-50 dark:bg-blue-900/20 rounded-xl border border-blue-200 dark:border-blue-800">
          <h3 className="text-lg font-semibold text-blue-900 dark:text-blue-100 mb-2">
            Supported Languages
          </h3>
          <p className="text-blue-800 dark:text-blue-200 text-sm">
            assembly, basic, bash, batch, c, cpp, csharp, css, go, javascript, html, git, java, kotlin, lua, php, ruby, dart, r, julia, scala, elixir, clojure, haskell, zig, ocaml, markdown, yaml, dockerfile, powershell, python, rust, sql, swift, typescript
          </p>
        </section>
      </div>
    </div>
  )
}
