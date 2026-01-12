import { NextRequest, NextResponse } from 'next/server'
import { readFile, writeFile, mkdir, stat } from 'node:fs/promises'
import { join, resolve } from 'node:path'

const CONFIG_DIR = process.env.CONFIG_DIR || resolve(process.cwd(), '..', '.specforge')
const CONFIG_FILE = join(CONFIG_DIR, 'config.json')

interface Config {
  specsDir: string
  cacheEnabled: boolean
  cacheTTL: number
  searchFallback: boolean
  resourcePageSize: number
  theme: 'light' | 'dark' | 'system'
}

const DEFAULT_CONFIG: Config = {
  specsDir: resolve(process.cwd(), '..', 'specs'),
  cacheEnabled: true,
  cacheTTL: 60000,
  searchFallback: true,
  resourcePageSize: 250,
  theme: 'system'
}

async function ensureDir(dir: string) {
  try {
    await mkdir(dir, { recursive: true })
  } catch {
    // Directory exists
  }
}

async function fileExists(path: string): Promise<boolean> {
  try {
    await stat(path)
    return true
  } catch {
    return false
  }
}

export async function GET() {
  await ensureDir(CONFIG_DIR)

  try {
    if (await fileExists(CONFIG_FILE)) {
      const content = await readFile(CONFIG_FILE, 'utf-8')
      const config = { ...DEFAULT_CONFIG, ...JSON.parse(content) }
      return NextResponse.json({ config })
    }
    return NextResponse.json({ config: DEFAULT_CONFIG })
  } catch (err) {
    console.error('Failed to read config:', err)
    return NextResponse.json({ config: DEFAULT_CONFIG })
  }
}

export async function PUT(request: NextRequest) {
  await ensureDir(CONFIG_DIR)

  try {
    const body = await request.json()
    const config: Config = {
      specsDir: body.specsDir || DEFAULT_CONFIG.specsDir,
      cacheEnabled: typeof body.cacheEnabled === 'boolean' ? body.cacheEnabled : DEFAULT_CONFIG.cacheEnabled,
      cacheTTL: typeof body.cacheTTL === 'number' ? body.cacheTTL : DEFAULT_CONFIG.cacheTTL,
      searchFallback: typeof body.searchFallback === 'boolean' ? body.searchFallback : DEFAULT_CONFIG.searchFallback,
      resourcePageSize: typeof body.resourcePageSize === 'number' ? body.resourcePageSize : DEFAULT_CONFIG.resourcePageSize,
      theme: ['light', 'dark', 'system'].includes(body.theme) ? body.theme : DEFAULT_CONFIG.theme
    }

    await writeFile(CONFIG_FILE, JSON.stringify(config, null, 2), 'utf-8')
    return NextResponse.json({ config })
  } catch (err) {
    console.error('Failed to save config:', err)
    return NextResponse.json({ error: 'Failed to save config' }, { status: 500 })
  }
}
