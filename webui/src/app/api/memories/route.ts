import { NextRequest, NextResponse } from 'next/server'
import { readdir, readFile, writeFile, mkdir, unlink, stat } from 'node:fs/promises'
import { join, resolve } from 'node:path'

const MEMORIES_DIR = process.env.MEMORIES_DIR || resolve(process.cwd(), '..', '.specforge', 'memories')

interface Memory {
  id: string
  name: string
  content: string
  createdAt: string
  updatedAt: string
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
  await ensureDir(MEMORIES_DIR)
  
  try {
    const files = await readdir(MEMORIES_DIR)
    const memories: Memory[] = []

    for (const file of files) {
      if (!file.endsWith('.md')) continue
      
      const filePath = join(MEMORIES_DIR, file)
      const content = await readFile(filePath, 'utf-8')
      const stats = await stat(filePath)
      
      memories.push({
        id: file.replace('.md', ''),
        name: file.replace('.md', ''),
        content,
        createdAt: stats.birthtime.toISOString(),
        updatedAt: stats.mtime.toISOString()
      })
    }

    return NextResponse.json({ memories })
  } catch (err) {
    console.error('Failed to list memories:', err)
    return NextResponse.json({ memories: [] })
  }
}

export async function POST(request: NextRequest) {
  await ensureDir(MEMORIES_DIR)
  
  try {
    const body = await request.json()
    const { name, content = '' } = body

    if (!name || typeof name !== 'string') {
      return NextResponse.json({ error: 'Name is required' }, { status: 400 })
    }

    const safeName = name.replace(/[^a-zA-Z0-9-_]/g, '-')
    const filePath = join(MEMORIES_DIR, safeName + '.md')

    if (await fileExists(filePath)) {
      return NextResponse.json({ error: 'Memory already exists' }, { status: 409 })
    }

    await writeFile(filePath, content, 'utf-8')
    
    return NextResponse.json({ 
      memory: {
        id: safeName,
        name: safeName,
        content,
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString()
      }
    })
  } catch (err) {
    console.error('Failed to create memory:', err)
    return NextResponse.json({ error: 'Failed to create memory' }, { status: 500 })
  }
}
