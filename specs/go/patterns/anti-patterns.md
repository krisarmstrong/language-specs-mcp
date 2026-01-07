# Go Anti-Patterns

Common mistakes and code smells to avoid in Go code.

## Ignoring Errors

```go
// BAD - Silent failures
data, _ := json.Marshal(obj)
file, _ := os.Open("config.json")

// GOOD - Handle errors explicitly
data, err := json.Marshal(obj)
if err != nil {
    return fmt.Errorf("marshal failed: %w", err)
}
```

## Naked Returns in Long Functions

```go
// BAD - Hard to track return values
func process(input string) (result string, count int, err error) {
    // 50+ lines of code
    result = transform(input)
    // more code
    count = len(result)
    // even more code
    return // What's being returned?
}

// GOOD - Explicit returns
func process(input string) (string, int, error) {
    result := transform(input)
    count := len(result)
    return result, count, nil
}
```

## Using init() for Complex Logic

```go
// BAD - Hidden initialization, hard to test
var db *Database

func init() {
    var err error
    db, err = ConnectDatabase()
    if err != nil {
        panic(err) // Crashes on import!
    }
}

// GOOD - Explicit initialization
func NewApp() (*App, error) {
    db, err := ConnectDatabase()
    if err != nil {
        return nil, fmt.Errorf("connect db: %w", err)
    }
    return &App{db: db}, nil
}
```

## Goroutine Leaks

```go
// BAD - Goroutine never terminates
func process() {
    ch := make(chan int)
    go func() {
        for v := range ch { // Blocks forever!
            fmt.Println(v)
        }
    }()
    // ch never closed, goroutine leaks
}

// GOOD - Ensure cleanup
func process(ctx context.Context) {
    ch := make(chan int)
    go func() {
        defer close(ch)
        for {
            select {
            case <-ctx.Done():
                return
            case ch <- getValue():
            }
        }
    }()
}
```

## Not Using defer for Cleanup

```go
// BAD - Cleanup might be skipped
func readFile(path string) ([]byte, error) {
    f, err := os.Open(path)
    if err != nil {
        return nil, err
    }

    data, err := io.ReadAll(f)
    if err != nil {
        f.Close() // Easy to forget!
        return nil, err
    }

    f.Close()
    return data, nil
}

// GOOD - defer ensures cleanup
func readFile(path string) ([]byte, error) {
    f, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer f.Close()

    return io.ReadAll(f)
}
```

## Passing Large Structs by Value

```go
// BAD - Copies entire struct
type BigStruct struct {
    Data [1000000]byte
}

func process(s BigStruct) { // Copies 1MB!
    // ...
}

// GOOD - Pass pointer
func process(s *BigStruct) {
    // ...
}
```

## Using sync.Mutex with Value Receiver

```go
// BAD - Mutex is copied, doesn't protect anything
type Counter struct {
    mu    sync.Mutex
    count int
}

func (c Counter) Increment() { // Value receiver!
    c.mu.Lock()
    defer c.mu.Unlock()
    c.count++ // Modifies copy
}

// GOOD - Pointer receiver
func (c *Counter) Increment() {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.count++
}
```

## Unbuffered Channel Misuse

```go
// BAD - Deadlock
func main() {
    ch := make(chan int)
    ch <- 1 // Blocks forever, no receiver!
    fmt.Println(<-ch)
}

// GOOD - Buffered channel or goroutine
func main() {
    ch := make(chan int, 1)
    ch <- 1
    fmt.Println(<-ch)
}

// OR
func main() {
    ch := make(chan int)
    go func() { ch <- 1 }()
    fmt.Println(<-ch)
}
```

## Empty Interface Abuse

```go
// BAD - No type safety
func process(data interface{}) interface{} {
    // Type assertions everywhere
    return nil
}

// GOOD - Use generics (Go 1.18+)
func process[T any](data T) T {
    return data
}

// OR define an interface
type Processor interface {
    Process() error
}
```

## String Concatenation in Loops

```go
// BAD - O(n²) allocations
var result string
for _, s := range items {
    result += s + ", "
}

// GOOD - Use strings.Builder
var builder strings.Builder
for _, s := range items {
    builder.WriteString(s)
    builder.WriteString(", ")
}
result := builder.String()
```

## Not Checking Type Assertions

```go
// BAD - Panics on wrong type
func getString(v interface{}) string {
    return v.(string) // Panic if not string!
}

// GOOD - Use comma-ok idiom
func getString(v interface{}) (string, bool) {
    s, ok := v.(string)
    return s, ok
}

// OR use type switch
func getString(v interface{}) string {
    switch s := v.(type) {
    case string:
        return s
    case fmt.Stringer:
        return s.String()
    default:
        return ""
    }
}
```

## Race Conditions with Maps

```go
// BAD - Concurrent map access
var cache = make(map[string]string)

func Get(key string) string {
    return cache[key] // Race!
}

func Set(key, value string) {
    cache[key] = value // Race!
}

// GOOD - Use sync.Map or mutex
var cache sync.Map

func Get(key string) (string, bool) {
    v, ok := cache.Load(key)
    if !ok {
        return "", false
    }
    return v.(string), true
}
```

## Nil Slice vs Empty Slice Confusion

```go
// BAD - Inconsistent behavior
func getItems() []string {
    return nil // JSON encodes as null
}

// GOOD - Return empty slice for consistency
func getItems() []string {
    return []string{} // JSON encodes as []
}

// ALSO GOOD - Use make
func getItems() []string {
    return make([]string, 0)
}
```

## Using time.Sleep for Synchronization

```go
// BAD - Fragile, wastes time
func waitForReady() {
    time.Sleep(100 * time.Millisecond) // Hope it's ready!
}

// GOOD - Use channels or sync primitives
func waitForReady(ready <-chan struct{}) {
    <-ready
}

// OR use sync.WaitGroup
func waitForWorkers(wg *sync.WaitGroup) {
    wg.Wait()
}
```

## Not Using context.Context

```go
// BAD - No cancellation support
func fetchData(url string) ([]byte, error) {
    resp, err := http.Get(url)
    // ...
}

// GOOD - Accept context for cancellation
func fetchData(ctx context.Context, url string) ([]byte, error) {
    req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
    if err != nil {
        return nil, err
    }
    resp, err := http.DefaultClient.Do(req)
    // ...
}
```

## Error String Formatting

```go
// BAD - Inconsistent error messages
return fmt.Errorf("Failed to open file: %s", path)
return errors.New("CANNOT CONNECT TO DATABASE")

// GOOD - Lowercase, no punctuation
return fmt.Errorf("open file %s: %w", path, err)
return errors.New("connect to database")
```
