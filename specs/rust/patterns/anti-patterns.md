# Rust Anti-Patterns

Common mistakes and code smells to avoid in Rust code.

## Overusing .unwrap() and .expect()

```rust
// BAD - Panics on None/Err
let value = some_option.unwrap();
let result = fallible_operation().unwrap();

// GOOD - Handle the error
let value = some_option.ok_or(MyError::NotFound)?;
let result = fallible_operation()?;

// GOOD - Provide context with expect in main/tests only
let config = load_config().expect("Failed to load config file");
```

## Clone to Satisfy Borrow Checker

```rust
// BAD - Unnecessary clone to avoid borrow issues
fn process(data: &Vec<String>) {
    let cloned = data.clone();  // Expensive!
    for item in cloned {
        println!("{}", item);
    }
}

// GOOD - Work with references
fn process(data: &[String]) {
    for item in data {
        println!("{}", item);
    }
}
```

## Using String When &str Suffices

```rust
// BAD - Requires allocation
fn greet(name: String) {
    println!("Hello, {}", name);
}
greet("World".to_string());  // Unnecessary allocation

// GOOD - Accept reference
fn greet(name: &str) {
    println!("Hello, {}", name);
}
greet("World");  // No allocation
```

## Ignoring Clippy Warnings

```rust
// BAD - Clippy warns about this
if vec.len() > 0 { }

// GOOD - Idiomatic
if !vec.is_empty() { }

// BAD - Manual implementation exists in std
let sum: i32 = vec.iter().fold(0, |acc, x| acc + x);

// GOOD - Use built-in
let sum: i32 = vec.iter().sum();
```

## Using Vec When Slice Works

```rust
// BAD - Requires owned Vec
fn sum(numbers: Vec<i32>) -> i32 {
    numbers.iter().sum()
}

// GOOD - Accept slice, more flexible
fn sum(numbers: &[i32]) -> i32 {
    numbers.iter().sum()
}

// Can call with Vec, array, or slice
sum(&vec![1, 2, 3]);
sum(&[1, 2, 3]);
```

## Not Using Entry API for Maps

```rust
use std::collections::HashMap;

// BAD - Double lookup
let mut map: HashMap<String, i32> = HashMap::new();
if !map.contains_key("key") {
    map.insert("key".to_string(), 0);
}
*map.get_mut("key").unwrap() += 1;

// GOOD - Single lookup with entry API
*map.entry("key".to_string()).or_insert(0) += 1;
```

## Blocking in Async Code

```rust
// BAD - Blocks the async runtime
async fn read_file(path: &str) -> String {
    std::fs::read_to_string(path).unwrap()  // Blocking!
}

// GOOD - Use async file operations
async fn read_file(path: &str) -> std::io::Result<String> {
    tokio::fs::read_to_string(path).await
}

// OR spawn blocking task
async fn read_file(path: &str) -> std::io::Result<String> {
    let path = path.to_string();
    tokio::task::spawn_blocking(move || {
        std::fs::read_to_string(path)
    }).await?
}
```

## Mutex Poisoning Panic

```rust
use std::sync::Mutex;

// BAD - Panics if mutex was poisoned
let data = mutex.lock().unwrap();

// GOOD - Handle poisoning
let data = mutex.lock().unwrap_or_else(|poisoned| {
    poisoned.into_inner()
});

// OR use parking_lot which doesn't poison
use parking_lot::Mutex;
let data = mutex.lock();  // Never panics from poisoning
```

## Creating References to Packed Fields

```rust
// BAD - Undefined behavior
#[repr(packed)]
struct Packed {
    a: u8,
    b: u32,
}

let p = Packed { a: 1, b: 2 };
let r = &p.b;  // UB! Unaligned reference

// GOOD - Copy the value
let b = { p.b };  // Copy, then use
```

## Using mem::forget to Prevent Drop

```rust
use std::mem;

// BAD - Resource leak, not drop-safe
let file = File::open("data.txt")?;
mem::forget(file);  // File handle leaked!

// GOOD - Use ManuallyDrop for explicit control
use std::mem::ManuallyDrop;
let file = ManuallyDrop::new(File::open("data.txt")?);
// Explicitly drop when ready
ManuallyDrop::into_inner(file);
```

## Returning References to Local Variables

```rust
// BAD - Won't compile, but shows the intent
fn get_string() -> &str {
    let s = String::from("hello");
    &s  // Error: returns reference to local
}

// GOOD - Return owned value
fn get_string() -> String {
    String::from("hello")
}

// OR use 'static lifetime for constants
fn get_string() -> &'static str {
    "hello"
}
```

## Unneeded Collect Into Vec

```rust
// BAD - Allocates intermediate Vec
let doubled: i32 = vec![1, 2, 3]
    .iter()
    .map(|x| x * 2)
    .collect::<Vec<_>>()  // Unnecessary!
    .iter()
    .sum();

// GOOD - Chain iterators directly
let doubled: i32 = vec![1, 2, 3]
    .iter()
    .map(|x| x * 2)
    .sum();
```

## Large Structs on Stack

```rust
// BAD - Large array on stack
struct BigData {
    buffer: [u8; 10_000_000],  // 10MB on stack!
}

let data = BigData { buffer: [0; 10_000_000] };  // Stack overflow risk

// GOOD - Use Box for heap allocation
struct BigData {
    buffer: Box<[u8]>,
}

let data = BigData {
    buffer: vec![0u8; 10_000_000].into_boxed_slice(),
};
```

## Not Using derive When Appropriate

```rust
// BAD - Manual implementations
struct Point {
    x: i32,
    y: i32,
}

impl Clone for Point {
    fn clone(&self) -> Self {
        Point { x: self.x, y: self.y }
    }
}

impl PartialEq for Point {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}

// GOOD - Use derive
#[derive(Clone, Copy, PartialEq, Eq, Debug, Hash)]
struct Point {
    x: i32,
    y: i32,
}
```

## Using String for Errors

```rust
// BAD - Loses error context
fn read_config() -> Result<Config, String> {
    let content = std::fs::read_to_string("config.toml")
        .map_err(|e| e.to_string())?;
    // ...
}

// GOOD - Use proper error types
use thiserror::Error;

#[derive(Error, Debug)]
enum ConfigError {
    #[error("failed to read config file: {0}")]
    Io(#[from] std::io::Error),
    #[error("invalid config format: {0}")]
    Parse(#[from] toml::de::Error),
}

fn read_config() -> Result<Config, ConfigError> {
    let content = std::fs::read_to_string("config.toml")?;
    // ...
}
```
