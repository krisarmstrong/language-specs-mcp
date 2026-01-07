# Go Generation Checklist

**Read this BEFORE writing Go code. These rules prevent the most common bugs.**

## Critical: You Must Do These

### 1. Always Handle Errors - Never Ignore Them
```go
// BAD - error silently ignored
result, _ := doSomething()

// GOOD - handle the error
result, err := doSomething()
if err != nil {
    return fmt.Errorf("doSomething failed: %w", err)
}
```

### 2. Use `%w` for Error Wrapping (Go 1.13+)
```go
// BAD - loses error chain
return fmt.Errorf("failed: %v", err)

// GOOD - preserves error chain for errors.Is/As
return fmt.Errorf("failed: %w", err)
```

### 3. Close Resources with `defer`
```go
// BAD - might not close on error
f, err := os.Open(filename)
// ... use f ...
f.Close()

// GOOD - guaranteed cleanup
f, err := os.Open(filename)
if err != nil {
    return err
}
defer f.Close()
```

### 4. Check `defer` Errors for Writes
```go
// BAD - write errors silently ignored
defer f.Close()

// GOOD - capture close error for writes
defer func() {
    if cerr := f.Close(); cerr != nil && err == nil {
        err = cerr
    }
}()
```

### 5. Use Context for Cancellation and Timeouts
```go
// BAD - no cancellation support
func fetch(url string) (*Response, error)

// GOOD - respects cancellation
func fetch(ctx context.Context, url string) (*Response, error) {
    req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
    // ...
}
```

## Important: Strong Recommendations

### 6. Prefer Short Variable Names in Small Scopes
```go
// Go idiom - short names for local scope
for i, v := range items { }
for k, v := range m { }

// Longer names for wider scope
type CustomerRepository struct { }
```

### 7. Return Early, Avoid Deep Nesting
```go
// BAD - deep nesting
func process(x int) error {
    if x > 0 {
        if x < 100 {
            // do work
        }
    }
    return nil
}

// GOOD - guard clauses
func process(x int) error {
    if x <= 0 {
        return errors.New("x must be positive")
    }
    if x >= 100 {
        return errors.New("x must be less than 100")
    }
    // do work
    return nil
}
```

### 8. Use Table-Driven Tests
```go
func TestAdd(t *testing.T) {
    tests := []struct {
        name string
        a, b int
        want int
    }{
        {"positive", 1, 2, 3},
        {"negative", -1, -2, -3},
        {"zero", 0, 0, 0},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            if got := Add(tt.a, tt.b); got != tt.want {
                t.Errorf("Add(%d, %d) = %d, want %d", tt.a, tt.b, got, tt.want)
            }
        })
    }
}
```

### 9. Accept Interfaces, Return Structs
```go
// GOOD - flexible input, concrete output
func Process(r io.Reader) (*Result, error) {
    // Can accept files, buffers, network connections...
}
```

### 10. Use `make` for Slices with Known Capacity
```go
// BAD - grows repeatedly
var items []Item
for _, v := range source {
    items = append(items, transform(v))
}

// GOOD - pre-allocate
items := make([]Item, 0, len(source))
for _, v := range source {
    items = append(items, transform(v))
}
```

## Concurrency: Get It Right

### 11. Never Start Goroutines Without Knowing When They Stop
```go
// BAD - goroutine leak
go func() {
    for {
        doWork()
    }
}()

// GOOD - controlled lifecycle
func worker(ctx context.Context) {
    for {
        select {
        case <-ctx.Done():
            return
        default:
            doWork()
        }
    }
}
```

### 12. Use `sync.WaitGroup` for Goroutine Coordination
```go
var wg sync.WaitGroup
for _, item := range items {
    wg.Add(1)
    go func(item Item) {
        defer wg.Done()
        process(item)
    }(item)
}
wg.Wait()
```

### 13. Protect Shared State with Mutex or Channels
```go
// Option 1: Mutex
type Counter struct {
    mu    sync.Mutex
    value int
}

func (c *Counter) Inc() {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.value++
}

// Option 2: Channel (share by communicating)
updates := make(chan int)
go func() {
    count := 0
    for delta := range updates {
        count += delta
    }
}()
```

### 14. Always Pass Loop Variables to Goroutines
```go
// BAD - all goroutines see final value
for _, v := range items {
    go func() {
        process(v)  // Bug: v changes!
    }()
}

// GOOD - capture value
for _, v := range items {
    go func(v Item) {
        process(v)
    }(v)
}
```

## Security & Safety

### 15. Validate All External Input
```go
// BAD - trusts input
func handler(w http.ResponseWriter, r *http.Request) {
    id := r.URL.Query().Get("id")
    db.Query("SELECT * FROM users WHERE id = " + id)  // SQL injection!
}

// GOOD - parameterized query
db.Query("SELECT * FROM users WHERE id = ?", id)
```

### 16. Use `crypto/rand` Not `math/rand` for Security
```go
// BAD - predictable
token := fmt.Sprintf("%d", rand.Int())

// GOOD - cryptographically secure
b := make([]byte, 32)
crypto_rand.Read(b)
token := base64.URLEncoding.EncodeToString(b)
```

---

**Quick Reference - Copy This Mental Model:**
- Handle ALL errors, wrap with `%w`
- `defer` for cleanup, check write errors
- Context for cancellation/timeouts
- Return early, avoid nesting
- Table-driven tests
- Accept interfaces, return structs
- Know when goroutines stop
- Mutex or channels for shared state
- Pass loop vars to goroutines
- Parameterize queries
