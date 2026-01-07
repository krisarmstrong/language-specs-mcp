# Rust Generation Checklist

**Read this BEFORE writing Rust code. The compiler catches a lot, but these patterns matter.**

## Critical: You Must Do These

### 1. Use `?` for Error Propagation
```rust
// BAD - verbose
let file = match File::open(path) {
    Ok(f) => f,
    Err(e) => return Err(e),
};

// GOOD - idiomatic
let file = File::open(path)?;
```

### 2. Prefer `&str` Over `String` in Function Parameters
```rust
// BAD - forces allocation
fn greet(name: String) { }

// GOOD - accepts both String and &str
fn greet(name: &str) { }
```

### 3. Use `impl Trait` for Return Types When Appropriate
```rust
// GOOD - hides concrete type, flexible
fn make_iter() -> impl Iterator<Item = i32> {
    (0..10).filter(|x| x % 2 == 0)
}
```

### 4. Derive Common Traits
```rust
// GOOD - derive what you need
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
struct User {
    id: u64,
    name: String,
}
```

### 5. Use `Option` and `Result`, Not Sentinel Values
```rust
// BAD - sentinel value
fn find_index(items: &[i32], target: i32) -> i32 {
    // returns -1 if not found
}

// GOOD - explicit optionality
fn find_index(items: &[i32], target: i32) -> Option<usize> {
    items.iter().position(|&x| x == target)
}
```

## Important: Strong Recommendations

### 6. Use `if let` and `while let` for Single-Pattern Matching
```rust
// BAD - verbose for single pattern
match optional_value {
    Some(v) => println!("{}", v),
    None => {}
}

// GOOD - concise
if let Some(v) = optional_value {
    println!("{}", v);
}
```

### 7. Prefer Iterators Over Index Loops
```rust
// BAD - C-style loop
for i in 0..items.len() {
    process(items[i]);
}

// GOOD - iterator
for item in &items {
    process(item);
}

// GOOD - with index if needed
for (i, item) in items.iter().enumerate() {
    process(i, item);
}
```

### 8. Use `collect()` with Type Annotation
```rust
// GOOD - explicit collection type
let names: Vec<String> = users.iter().map(|u| u.name.clone()).collect();

// Also GOOD - turbofish
let names = users.iter().map(|u| u.name.clone()).collect::<Vec<_>>();
```

### 9. Use `Default` Trait for Struct Initialization
```rust
#[derive(Default)]
struct Config {
    timeout: u64,
    retries: u32,
}

// GOOD - partial initialization
let config = Config {
    timeout: 30,
    ..Default::default()
};
```

### 10. Clone Sparingly, Borrow When Possible
```rust
// BAD - unnecessary clone
fn process(data: Vec<u8>) {
    let copy = data.clone();  // Why?
}

// GOOD - borrow if you don't need ownership
fn process(data: &[u8]) { }
```

## Ownership & Lifetimes

### 11. Use References for Read-Only Access
```rust
// BAD - takes ownership unnecessarily
fn print_length(s: String) {
    println!("{}", s.len());
}

// GOOD - borrows
fn print_length(s: &str) {
    println!("{}", s.len());
}
```

### 12. Use `Cow` for Optional Ownership
```rust
use std::borrow::Cow;

// GOOD - avoids allocation when not needed
fn process(input: &str) -> Cow<str> {
    if needs_modification(input) {
        Cow::Owned(modify(input))
    } else {
        Cow::Borrowed(input)
    }
}
```

### 13. Avoid Lifetime Annotations When Elision Works
```rust
// Lifetime elision handles this - don't add annotations
fn first_word(s: &str) -> &str { }

// Only add when compiler requires it
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str { }
```

## Error Handling

### 14. Use `thiserror` for Library Errors
```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum DataError {
    #[error("invalid format: {0}")]
    InvalidFormat(String),
    #[error("io error")]
    Io(#[from] std::io::Error),
}
```

### 15. Use `anyhow` for Application Errors
```rust
use anyhow::{Context, Result};

fn read_config() -> Result<Config> {
    let content = std::fs::read_to_string("config.toml")
        .context("failed to read config file")?;
    toml::from_str(&content)
        .context("failed to parse config")
}
```

## Safety & Performance

### 16. Avoid `unwrap()` in Production Code
```rust
// BAD - panics on None/Err
let value = map.get("key").unwrap();

// GOOD - handle the case
let value = map.get("key").ok_or_else(|| anyhow!("key not found"))?;

// GOOD - provide default
let value = map.get("key").unwrap_or(&default);
```

### 17. Use `#[must_use]` for Important Return Values
```rust
#[must_use]
fn validate(input: &str) -> bool {
    // Caller must check the return value
}
```

### 18. Prefer `Vec::with_capacity` When Size Is Known
```rust
// BAD - multiple reallocations
let mut items = Vec::new();
for i in 0..1000 {
    items.push(i);
}

// GOOD - single allocation
let mut items = Vec::with_capacity(1000);
for i in 0..1000 {
    items.push(i);
}
```

---

**Quick Reference - Copy This Mental Model:**
- Use `?` for error propagation
- `&str` params, `String` when ownership needed
- Derive Debug, Clone, PartialEq at minimum
- `Option`/`Result` not sentinels
- `if let` for single patterns
- Iterators over index loops
- Borrow don't clone when possible
- `thiserror` for libs, `anyhow` for apps
- No `unwrap()` in production
- Pre-allocate when size known
