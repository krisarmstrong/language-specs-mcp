import { NextRequest, NextResponse } from 'next/server'
import { readdir, readFile, stat } from 'node:fs/promises'
import { join, resolve, relative } from 'node:path'

const SPECS_DIR = process.env.SPECS_DIR || resolve(process.cwd(), '..', 'specs')

const LANGUAGES = [
  'assembly', 'basic', 'bash', 'batch', 'c', 'cpp', 'csharp', 'css',
  'dart', 'dockerfile', 'elixir', 'clojure', 'go', 'git', 'haskell',
  'html', 'java', 'javascript', 'julia', 'kotlin', 'lua', 'markdown',
  'ocaml', 'php', 'powershell', 'python', 'r', 'ruby', 'rust',
  'scala', 'sql', 'swift', 'typescript', 'yaml', 'zig'
]

interface SearchResult {
  language: string
  category: string
  name: string
  matches: string[]
}

async function fileExists(path: string): Promise<boolean> {
  try {
    await stat(path)
    return true
  } catch {
    return false
  }
}

async function searchInFile(
  filePath: string, 
  query: string, 
  language: string, 
  category: string, 
  name: string
): Promise<SearchResult | null> {
  try {
    const content = await readFile(filePath, 'utf-8')
    const queryLower = query.toLowerCase()
    const contentLower = content.toLowerCase()
    
    if (!contentLower.includes(queryLower)) {
      return null
    }

    const lines = content.split('\n')
    const matches: string[] = []
    
    for (let i = 0; i < lines.length && matches.length < 3; i++) {
      if (lines[i]?.toLowerCase().includes(queryLower)) {
        const start = Math.max(0, i - 2)
        const end = Math.min(lines.length, i + 3)
        const context = lines.slice(start, end).join('\n')
        matches.push('Line ' + (i + 1) + ':\n' + context)
      }
    }

    return matches.length > 0 ? { language, category, name, matches } : null
  } catch {
    return null
  }
}

async function collectAndSearchFiles(
  dir: string, 
  query: string, 
  language: string, 
  category: string,
  results: SearchResult[]
): Promise<void> {
  try {
    const entries = await readdir(dir, { withFileTypes: true })
    for (const entry of entries) {
      if (results.length >= 10) return
      
      const fullPath = join(dir, entry.name)
      if (entry.isDirectory()) {
        await collectAndSearchFiles(fullPath, query, language, entry.name, results)
      } else if (entry.isFile() && entry.name.endsWith('.md')) {
        const name = entry.name.replace('.md', '')
        const result = await searchInFile(fullPath, query, language, category, name)
        if (result) {
          results.push(result)
        }
      }
    }
  } catch {
    // Directory not found or not readable
  }
}

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams
  const query = searchParams.get('q')

  if (!query || query.trim().length === 0) {
    return NextResponse.json({ error: 'Query is required' }, { status: 400 })
  }

  const results: SearchResult[] = []

  for (const language of LANGUAGES) {
    if (results.length >= 10) break
    
    const languageDir = join(SPECS_DIR, language)
    if (!(await fileExists(languageDir))) continue

    await collectAndSearchFiles(languageDir, query.trim(), language, 'spec', results)
  }

  return NextResponse.json({ results })
}
