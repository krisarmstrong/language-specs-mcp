import { readdir, readFile, stat } from "node:fs/promises";
import { join, resolve } from "node:path";
import { type NextRequest, NextResponse } from "next/server";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

const SPECS_DIR =
  process.env.SPECS_DIR || resolve(/* turbopackIgnore: true */ process.cwd(), "..", "specs");

async function fileExists(path: string): Promise<boolean> {
  try {
    await stat(path);
    return true;
  } catch {
    return false;
  }
}

async function collectMarkdownFiles(dir: string, files: string[]): Promise<void> {
  const entries = await readdir(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = join(/* turbopackIgnore: true */ dir, entry.name);
    if (entry.isDirectory()) {
      await collectMarkdownFiles(fullPath, files);
    } else if (entry.isFile() && entry.name.endsWith(".md")) {
      files.push(entry.name.replace(".md", ""));
    }
  }
}

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  const language = searchParams.get("language");
  const category = searchParams.get("category");
  const topic = searchParams.get("topic");

  if (!language) {
    return NextResponse.json({ error: "Language is required" }, { status: 400 });
  }

  const languageDir = join(/* turbopackIgnore: true */ SPECS_DIR, language);

  if (!(await fileExists(languageDir))) {
    return NextResponse.json({ error: "Language not found" }, { status: 404 });
  }

  // If topic is specified, return spec content
  if (topic && category) {
    const specPath = join(/* turbopackIgnore: true */ languageDir, category, topic + ".md");
    const altPath = join(/* turbopackIgnore: true */ languageDir, topic + ".md");

    let content = "";
    if (await fileExists(specPath)) {
      content = await readFile(specPath, "utf-8");
    } else if (await fileExists(altPath)) {
      content = await readFile(altPath, "utf-8");
    } else {
      return NextResponse.json({ error: "Spec not found" }, { status: 404 });
    }

    return NextResponse.json({ content });
  }

  // If category is specified, list specs in category
  if (category) {
    const categoryDir = join(/* turbopackIgnore: true */ languageDir, category);
    if (!(await fileExists(categoryDir))) {
      return NextResponse.json({ specs: [] });
    }

    const files: string[] = [];
    await collectMarkdownFiles(categoryDir, files);
    return NextResponse.json({ specs: files });
  }

  // Otherwise list available categories
  const entries = await readdir(languageDir, { withFileTypes: true });
  const categories = entries.filter((e) => e.isDirectory()).map((e) => e.name);

  return NextResponse.json({ categories });
}
