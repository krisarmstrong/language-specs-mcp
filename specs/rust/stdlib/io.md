# Rust I/O (std::io and std::fs)

## File Operations (std::fs)

```rust
use std::fs;
use std::fs::File;
use std::io::{Read, Write, BufRead, BufReader, BufWriter};
use std::path::Path;

// Read entire file
let content = fs::read_to_string("file.txt")?;
let bytes = fs::read("file.bin")?;

// Write entire file
fs::write("file.txt", "Hello, World!")?;
fs::write("file.bin", &bytes)?;

// File operations
fs::copy("src.txt", "dst.txt")?;
fs::rename("old.txt", "new.txt")?;
fs::remove_file("file.txt")?;
fs::create_dir("dirname")?;
fs::create_dir_all("path/to/dir")?;
fs::remove_dir("dirname")?;
fs::remove_dir_all("dirname")?;

// Metadata
let metadata = fs::metadata("file.txt")?;
metadata.len();                 // file size in bytes
metadata.is_file();
metadata.is_dir();
metadata.modified()?;           // SystemTime
metadata.created()?;

// Read directory
for entry in fs::read_dir(".")? {
    let entry = entry?;
    let path = entry.path();
    let name = entry.file_name();
    let metadata = entry.metadata()?;
}

// Canonicalize path
let absolute = fs::canonicalize("relative/path")?;
```

## File Handles

```rust
use std::fs::{File, OpenOptions};
use std::io::{Read, Write, Seek, SeekFrom};

// Open for reading
let mut file = File::open("file.txt")?;

// Create for writing (truncates)
let mut file = File::create("file.txt")?;

// Open with options
let file = OpenOptions::new()
    .read(true)
    .write(true)
    .create(true)
    .append(true)
    .truncate(false)
    .open("file.txt")?;

// Reading
let mut contents = String::new();
file.read_to_string(&mut contents)?;

let mut buffer = [0u8; 1024];
let bytes_read = file.read(&mut buffer)?;
let bytes = file.read_exact(&mut buffer)?;  // fills buffer or errors

// Writing
file.write_all(b"Hello")?;
let bytes_written = file.write(b"Hello")?;
file.flush()?;

// Seeking
file.seek(SeekFrom::Start(0))?;      // from beginning
file.seek(SeekFrom::End(-10))?;      // from end
file.seek(SeekFrom::Current(5))?;    // from current position
let pos = file.stream_position()?;   // current position

// File size
let size = file.metadata()?.len();
file.set_len(1024)?;                 // truncate/extend
```

## Buffered I/O

```rust
use std::io::{BufReader, BufWriter, BufRead, Write};

// Buffered reading
let file = File::open("file.txt")?;
let reader = BufReader::new(file);

// Read lines
for line in reader.lines() {
    let line = line?;
    println!("{}", line);
}

// Read until delimiter
let mut buf = String::new();
reader.read_line(&mut buf)?;

let mut bytes = Vec::new();
reader.read_until(b'\n', &mut bytes)?;

// Buffered writing
let file = File::create("file.txt")?;
let mut writer = BufWriter::new(file);
writer.write_all(b"Hello\n")?;
writer.flush()?;
// automatically flushes on drop
```

## Standard I/O

```rust
use std::io::{self, Read, Write, BufRead};

// Read from stdin
let mut input = String::new();
io::stdin().read_line(&mut input)?;

// With lock (more efficient for multiple reads)
let stdin = io::stdin();
let mut handle = stdin.lock();
for line in handle.lines() {
    println!("{}", line?);
}

// Write to stdout
io::stdout().write_all(b"Hello\n")?;
print!("Hello");
println!("World");
eprint!("Error: ");       // to stderr
eprintln!("Details");     // to stderr with newline

// With lock
let stdout = io::stdout();
let mut handle = stdout.lock();
writeln!(handle, "Hello")?;

// Flush
io::stdout().flush()?;
```

## Path Operations (std::path)

```rust
use std::path::{Path, PathBuf};

// Create paths
let path = Path::new("file.txt");
let path = Path::new("/absolute/path");
let mut path_buf = PathBuf::new();
path_buf.push("dir");
path_buf.push("file.txt");

// Path components
path.file_name();           // Option<&OsStr>
path.file_stem();           // filename without extension
path.extension();           // Option<&OsStr>
path.parent();              // Option<&Path>

// Path manipulation
let joined = path.join("subdir").join("file.txt");
path_buf.set_file_name("other.txt");
path_buf.set_extension("md");

// Path queries
path.exists();
path.is_file();
path.is_dir();
path.is_absolute();
path.is_relative();

// Path conversion
path.to_str();              // Option<&str>
path.to_string_lossy();     // Cow<str>
path.display();             // for printing
let path_buf = path.to_path_buf();
let os_str = path.as_os_str();

// Iterate components
for component in path.components() {
    match component {
        Component::Prefix(prefix) => { }
        Component::RootDir => { }
        Component::CurDir => { }       // .
        Component::ParentDir => { }    // ..
        Component::Normal(name) => { }
    }
}

// Ancestors
for ancestor in path.ancestors() {
    println!("{:?}", ancestor);
}
```

## Error Handling

```rust
use std::io::{self, Error, ErrorKind};

// Creating errors
let error = Error::new(ErrorKind::NotFound, "file not found");
let error = Error::last_os_error();

// Error kinds
match error.kind() {
    ErrorKind::NotFound => { }
    ErrorKind::PermissionDenied => { }
    ErrorKind::AlreadyExists => { }
    ErrorKind::WouldBlock => { }
    ErrorKind::InvalidInput => { }
    ErrorKind::InvalidData => { }
    ErrorKind::TimedOut => { }
    ErrorKind::Interrupted => { }
    ErrorKind::UnexpectedEof => { }
    _ => { }
}

// Common pattern
fn read_file(path: &str) -> io::Result<String> {
    let content = fs::read_to_string(path)?;
    Ok(content)
}
```

## Cursor (in-memory I/O)

```rust
use std::io::{Cursor, Read, Write, Seek, SeekFrom};

// Read from bytes
let data = b"Hello, World!";
let mut cursor = Cursor::new(data);
let mut buf = [0u8; 5];
cursor.read(&mut buf)?;

// Write to Vec
let mut cursor = Cursor::new(Vec::new());
cursor.write_all(b"Hello")?;
let bytes = cursor.into_inner();

// Seek
cursor.seek(SeekFrom::Start(0))?;
cursor.position();          // current position
cursor.set_position(5);
```

## Copy and Transfer

```rust
use std::io::{copy, Read, Write};

// Copy between streams
let mut src = File::open("source.txt")?;
let mut dst = File::create("dest.txt")?;
let bytes_copied = io::copy(&mut src, &mut dst)?;

// Read/Write adapters
let limited = file.take(1024);      // read at most 1024 bytes
let chained = file1.chain(file2);   // read file1 then file2
```

## Temporary Files

```rust
use std::env;

// Temp directory
let temp_dir = env::temp_dir();

// Using tempfile crate (recommended)
use tempfile::{tempfile, NamedTempFile, tempdir};

let file = tempfile()?;              // anonymous temp file
let named = NamedTempFile::new()?;   // temp file with path
let dir = tempdir()?;                // temp directory

// Files are deleted on drop
```
