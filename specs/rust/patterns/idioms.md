# Rust Idioms

## Prefer iterators over indexing

```rust
for item in items.iter() {
    // ...
}
```

## Use `Result` and `?` for error propagation

```rust
let data = read_to_string(path)?;
```

## Favor borrowing over cloning
