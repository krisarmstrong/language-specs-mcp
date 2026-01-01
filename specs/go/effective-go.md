# Effective Go - Idiomatic Patterns

Source: https://go.dev/doc/effective_go

## Formatting

- Use `gofmt` - no debate
- Tabs for indentation
- No line length limit (but be reasonable)

## Names

### Package Names

```go
// GOOD - short, lowercase, no underscores
package http
package json
package user

// BAD
package httpUtils
package json_parser
package myPackage
```

### Getters/Setters

```go
// GOOD - no Get prefix for getters
func (u *User) Name() string { return u.name }
func (u *User) SetName(name string) { u.name = name }

// BAD
func (u *User) GetName() string { return u.name }
```

### Interface Names

```go
// Single-method interfaces: method name + "er"
type Reader interface { Read(p []byte) (n int, err error) }
type Writer interface { Write(p []byte) (n int, err error) }
type Stringer interface { String() string }
```

### MixedCaps

```go
// GOOD
var userID string
var htmlParser Parser
var XMLHTTPRequest Request

// BAD
var userId string
var user_id string
```

## Semicolons

Lexer inserts semicolons. Opening brace must be on same line:

```go
// GOOD
if condition {
    // body
}

// WON'T COMPILE
if condition
{
    // body
}
```

## Control Structures

### If

```go
// Prefer early returns
func process(data []byte) error {
    if len(data) == 0 {
        return errors.New("empty data")
    }
    // main logic here
    return nil
}

// Init statement useful for scoping
if err := doSomething(); err != nil {
    return err
}
```

### For

```go
// Reverse loop
for i := len(a) - 1; i >= 0; i-- {
    // process a[i]
}

// Parallel assignment
for i, j := 0, len(a)-1; i < j; i, j = i+1, j-1 {
    a[i], a[j] = a[j], a[i]
}
```

### Switch

```go
// No automatic fallthrough
switch c {
case ' ', '\t', '\n':
    // whitespace
case 'a', 'e', 'i', 'o', 'u':
    // vowel
}

// Type switch
switch t := value.(type) {
case bool:
    // t is bool
case int:
    // t is int
default:
    // t is interface{}
}
```

## Functions

### Multiple Return Values

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}
```

### Named Results

```go
// Use for documentation, not magic returns
func ReadFull(r Reader, buf []byte) (n int, err error) {
    for len(buf) > 0 && err == nil {
        var nr int
        nr, err = r.Read(buf)
        n += nr
        buf = buf[nr:]
    }
    return
}
```

### Defer

```go
// LIFO order
func process() {
    defer fmt.Println("third")
    defer fmt.Println("second")
    defer fmt.Println("first")
}
// Output: first, second, third

// Common pattern: open/close
func ReadFile(filename string) ([]byte, error) {
    f, err := os.Open(filename)
    if err != nil {
        return nil, err
    }
    defer f.Close()
    return io.ReadAll(f)
}

// Defer evaluates arguments immediately
func trace(msg string) func() {
    start := time.Now()
    log.Printf("enter %s", msg)
    return func() {
        log.Printf("exit %s (%s)", msg, time.Since(start))
    }
}

func foo() {
    defer trace("foo")()
    // work
}
```

## Data

### Allocation with new

```go
// new(T) returns *T pointing to zeroed T
p := new(SyncedBuffer)  // *SyncedBuffer, ready to use
```

### Allocation with make

```go
// make(T, args) returns T (not *T), initialized
s := make([]int, 10)      // len=10, cap=10
s := make([]int, 0, 10)   // len=0, cap=10
m := make(map[string]int)
ch := make(chan int)
ch := make(chan int, 10)  // buffered
```

### Arrays vs Slices

```go
// Arrays: value type, fixed size
var a [10]int

// Slices: reference type, dynamic
var s []int = a[0:5]

// Slice internals: pointer, length, capacity
// Appending may allocate new backing array
s = append(s, 1, 2, 3)
```

### Maps

```go
m := make(map[string]int)
m["key"] = 1

value, ok := m["key"]  // comma-ok idiom
if !ok {
    // key not present
}

delete(m, "key")
```

## Initialization

### Constants

```go
const (
    _           = iota  // ignore first
    KB ByteSize = 1 << (10 * iota)
    MB
    GB
    TB
)
```

### Variables

```go
var (
    home   = os.Getenv("HOME")
    user   = os.Getenv("USER")
    gopath = os.Getenv("GOPATH")
)
```

### Init Functions

```go
func init() {
    if user == "" {
        log.Fatal("$USER not set")
    }
    if home == "" {
        home = "/home/" + user
    }
}
```

## Methods

### Pointers vs Values

```go
// Value receiver: method can't modify receiver
func (s Stack) Len() int { return len(s) }

// Pointer receiver: method can modify receiver
func (s *Stack) Push(v int) { *s = append(*s, v) }

// Rule: if any method has pointer receiver, all should
```

## Interfaces

### Implicit Satisfaction

```go
// No "implements" keyword
// Type satisfies interface by having all methods

type Writer interface {
    Write([]byte) (int, error)
}

// *os.File satisfies Writer because it has Write method
var w Writer = os.Stdout
```

### Interface Conversions

```go
type Stringer interface {
    String() string
}

// Type assertion
s, ok := value.(Stringer)
if ok {
    fmt.Println(s.String())
}
```

### Empty Interface

```go
// Holds any value
func Printf(format string, args ...any) {
    // use type switches or reflection
}
```

## Embedding

```go
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}

// Interface embedding
type ReadWriter interface {
    Reader
    Writer
}

// Struct embedding
type ReadWriter struct {
    *Reader
    *Writer
}
```

## Concurrency

### Share by Communicating

> Don't communicate by sharing memory; share memory by communicating.

```go
// Instead of mutex-protected data:
var data map[string]int
var mu sync.Mutex

// Use channels:
type request struct {
    key  string
    resp chan int
}

func server(reqs <-chan request) {
    data := make(map[string]int)
    for req := range reqs {
        req.resp <- data[req.key]
    }
}
```

### Goroutines

```go
// Cheap - thousands are fine
go serve(conn)

// Anonymous function
go func() {
    // capture variables carefully
}()
```

### Channels

```go
// Unbuffered: synchronous
c := make(chan int)

// Buffered: async up to capacity
c := make(chan int, 100)

// Receive from closed channel returns zero value
close(c)
v, ok := <-c  // ok is false if closed and empty
```

### Parallelization

```go
func process(items []Item) {
    var wg sync.WaitGroup
    for _, item := range items {
        wg.Add(1)
        go func(item Item) {
            defer wg.Done()
            handle(item)
        }(item)
    }
    wg.Wait()
}
```

## Errors

### Error Type

```go
type error interface {
    Error() string
}
```

### Error Handling

```go
// Always check errors
f, err := os.Open(name)
if err != nil {
    return err
}
defer f.Close()

// Add context
if err != nil {
    return fmt.Errorf("opening %s: %w", name, err)
}
```

### Panic and Recover

```go
// Panic: unrecoverable errors
func MustCompile(pattern string) *Regexp {
    re, err := Compile(pattern)
    if err != nil {
        panic(err)
    }
    return re
}

// Recover: catch panics (rarely needed)
func protect(f func()) {
    defer func() {
        if err := recover(); err != nil {
            log.Printf("recovered: %v", err)
        }
    }()
    f()
}
```
