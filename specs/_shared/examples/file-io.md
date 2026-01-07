# File I/O Examples

Common patterns for reading and writing files across languages.

## Read Text File

### TypeScript/JavaScript (Node.js)

```typescript
import { readFile, readFileSync } from "fs/promises";

// Async (preferred)
async function readTextFile(path: string): Promise<string> {
  return readFile(path, "utf-8");
}

// With error handling
async function readConfig(path: string): Promise<Config | null> {
  try {
    const content = await readFile(path, "utf-8");
    return JSON.parse(content);
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code === "ENOENT") {
      return null; // File not found
    }
    throw error;
  }
}
```

### Python

```python
from pathlib import Path

# Simple read
def read_text_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")

# With context manager
def read_config(path: str) -> dict | None:
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

# Async read
async def read_text_async(path: str) -> str:
    import aiofiles
    async with aiofiles.open(path, encoding="utf-8") as f:
        return await f.read()
```

### Go

```go
import (
    "os"
    "io"
)

func ReadTextFile(path string) (string, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return "", err
    }
    return string(data), nil
}

// With error handling
func ReadConfig(path string) (*Config, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        if os.IsNotExist(err) {
            return nil, nil // File not found
        }
        return nil, fmt.Errorf("read config: %w", err)
    }

    var config Config
    if err := json.Unmarshal(data, &config); err != nil {
        return nil, fmt.Errorf("parse config: %w", err)
    }

    return &config, nil
}
```

### Rust

```rust
use std::fs;
use std::io::{self, Read};
use std::path::Path;

fn read_text_file(path: &str) -> io::Result<String> {
    fs::read_to_string(path)
}

// With error handling
fn read_config(path: &str) -> Result<Option<Config>, Box<dyn std::error::Error>> {
    match fs::read_to_string(path) {
        Ok(content) => Ok(Some(serde_json::from_str(&content)?)),
        Err(e) if e.kind() == io::ErrorKind::NotFound => Ok(None),
        Err(e) => Err(e.into()),
    }
}
```

## Write Text File

### TypeScript

```typescript
import { writeFile, mkdir } from "fs/promises";
import { dirname } from "path";

async function writeTextFile(path: string, content: string): Promise<void> {
  await mkdir(dirname(path), { recursive: true });
  await writeFile(path, content, "utf-8");
}

// Write JSON with formatting
async function writeJson(path: string, data: unknown): Promise<void> {
  const content = JSON.stringify(data, null, 2);
  await writeFile(path, content, "utf-8");
}
```

### Python

```python
from pathlib import Path
import json

def write_text_file(path: str, content: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def write_json(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
```

### Go

```go
import (
    "os"
    "path/filepath"
)

func WriteTextFile(path, content string) error {
    if err := os.MkdirAll(filepath.Dir(path), 0755); err != nil {
        return err
    }
    return os.WriteFile(path, []byte(content), 0644)
}

func WriteJSON(path string, data any) error {
    content, err := json.MarshalIndent(data, "", "  ")
    if err != nil {
        return err
    }
    return WriteTextFile(path, string(content))
}
```

## Read Lines (Streaming)

### TypeScript

```typescript
import { createReadStream } from "fs";
import { createInterface } from "readline";

async function* readLines(path: string): AsyncGenerator<string> {
  const stream = createReadStream(path, "utf-8");
  const rl = createInterface({ input: stream, crlfDelay: Infinity });

  for await (const line of rl) {
    yield line;
  }
}

// Usage
for await (const line of readLines("large-file.txt")) {
  process(line);
}
```

### Python

```python
from typing import Iterator

def read_lines(path: str) -> Iterator[str]:
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")

# Usage
for line in read_lines("large-file.txt"):
    process(line)
```

### Go

```go
import (
    "bufio"
    "os"
)

func ReadLines(path string, fn func(string) error) error {
    file, err := os.Open(path)
    if err != nil {
        return err
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        if err := fn(scanner.Text()); err != nil {
            return err
        }
    }

    return scanner.Err()
}

// Usage
err := ReadLines("large-file.txt", func(line string) error {
    return process(line)
})
```

## Copy File

### TypeScript

```typescript
import { copyFile, mkdir } from "fs/promises";
import { dirname } from "path";

async function copyFileSafe(src: string, dest: string): Promise<void> {
  await mkdir(dirname(dest), { recursive: true });
  await copyFile(src, dest);
}
```

### Python

```python
import shutil
from pathlib import Path

def copy_file(src: str, dest: str) -> None:
    Path(dest).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)  # Preserves metadata
```

### Go

```go
func CopyFile(src, dest string) error {
    if err := os.MkdirAll(filepath.Dir(dest), 0755); err != nil {
        return err
    }

    source, err := os.Open(src)
    if err != nil {
        return err
    }
    defer source.Close()

    destination, err := os.Create(dest)
    if err != nil {
        return err
    }
    defer destination.Close()

    _, err = io.Copy(destination, source)
    return err
}
```

## List Directory

### TypeScript

```typescript
import { readdir, stat } from "fs/promises";
import { join } from "path";

async function listFiles(dir: string): Promise<string[]> {
  const entries = await readdir(dir, { withFileTypes: true });
  return entries.filter((e) => e.isFile()).map((e) => e.name);
}

// Recursive
async function* walkDir(dir: string): AsyncGenerator<string> {
  const entries = await readdir(dir, { withFileTypes: true });
  for (const entry of entries) {
    const path = join(dir, entry.name);
    if (entry.isDirectory()) {
      yield* walkDir(path);
    } else {
      yield path;
    }
  }
}
```

### Python

```python
from pathlib import Path
from typing import Iterator

def list_files(directory: str) -> list[str]:
    return [f.name for f in Path(directory).iterdir() if f.is_file()]

# Recursive
def walk_dir(directory: str) -> Iterator[Path]:
    for path in Path(directory).rglob("*"):
        if path.is_file():
            yield path
```

### Go

```go
func ListFiles(dir string) ([]string, error) {
    entries, err := os.ReadDir(dir)
    if err != nil {
        return nil, err
    }

    var files []string
    for _, entry := range entries {
        if !entry.IsDir() {
            files = append(files, entry.Name())
        }
    }
    return files, nil
}

// Recursive
func WalkDir(dir string, fn func(string) error) error {
    return filepath.WalkDir(dir, func(path string, d fs.DirEntry, err error) error {
        if err != nil {
            return err
        }
        if !d.IsDir() {
            return fn(path)
        }
        return nil
    })
}
```
