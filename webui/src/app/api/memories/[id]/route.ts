import { readFile, stat, unlink, writeFile } from "node:fs/promises";
import { join, resolve } from "node:path";
import { type NextRequest, NextResponse } from "next/server";

const MEMORIES_DIR =
  process.env.MEMORIES_DIR || resolve(process.cwd(), "..", ".specforge", "memories");

async function fileExists(path: string): Promise<boolean> {
  try {
    await stat(path);
    return true;
  } catch {
    return false;
  }
}

type MemoryRouteContext = { params: Promise<{ id: string }> };

export async function GET(_request: NextRequest, { params }: MemoryRouteContext) {
  const { id } = await params;
  const filePath = join(MEMORIES_DIR, `${id}.md`);

  if (!(await fileExists(filePath))) {
    return NextResponse.json({ error: "Memory not found" }, { status: 404 });
  }

  const content = await readFile(filePath, "utf-8");
  const stats = await stat(filePath);

  return NextResponse.json({
    memory: {
      id,
      name: id,
      content,
      createdAt: stats.birthtime.toISOString(),
      updatedAt: stats.mtime.toISOString(),
    },
  });
}

export async function PUT(request: NextRequest, { params }: MemoryRouteContext) {
  const { id } = await params;
  const filePath = join(MEMORIES_DIR, `${id}.md`);

  if (!(await fileExists(filePath))) {
    return NextResponse.json({ error: "Memory not found" }, { status: 404 });
  }

  try {
    const body = await request.json();
    const { content } = body;

    if (typeof content !== "string") {
      return NextResponse.json({ error: "Content is required" }, { status: 400 });
    }

    await writeFile(filePath, content, "utf-8");
    const stats = await stat(filePath);

    return NextResponse.json({
      memory: {
        id,
        name: id,
        content,
        createdAt: stats.birthtime.toISOString(),
        updatedAt: stats.mtime.toISOString(),
      },
    });
  } catch (err) {
    console.error("Failed to update memory:", err);
    return NextResponse.json({ error: "Failed to update memory" }, { status: 500 });
  }
}

export async function DELETE(_request: NextRequest, { params }: MemoryRouteContext) {
  const { id } = await params;
  const filePath = join(MEMORIES_DIR, `${id}.md`);

  if (!(await fileExists(filePath))) {
    return NextResponse.json({ error: "Memory not found" }, { status: 404 });
  }

  try {
    await unlink(filePath);
    return NextResponse.json({ success: true });
  } catch (err) {
    console.error("Failed to delete memory:", err);
    return NextResponse.json({ error: "Failed to delete memory" }, { status: 500 });
  }
}
