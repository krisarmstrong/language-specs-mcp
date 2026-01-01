# Go Language Specification Summary

Source: https://go.dev/ref/spec

## Lexical Elements

### Keywords

```
break        default      func         interface    select
case         defer        go           map          struct
chan         else         goto         package      switch
const        fallthrough  if           range        type
continue     for          import       return       var
```

### Operators and Punctuation

```
+    &     +=    &=     &&    ==    !=    (    )
-    |     -=    |=     ||    <     <=    [    ]
*    ^     *=    ^=     <-    >     >=    {    }
/    <<    /=    <<=    ++    =     :=    ,    ;
%    >>    %=    >>=    --    !     ...   .    :
     &^          &^=          ~
```

## Types

### Basic Types

```go
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8
rune // alias for int32

float32 float64

complex64 complex128
```

### Zero Values

| Type | Zero Value |
|------|------------|
| boolean | `false` |
| numeric | `0` |
| string | `""` |
| pointer | `nil` |
| function | `nil` |
| interface | `nil` |
| slice | `nil` |
| channel | `nil` |
| map | `nil` |

### Composite Types

```go
// Array - fixed length
[N]T

// Slice - dynamic length
[]T

// Map
map[K]V

// Struct
struct {
    Field1 T1
    Field2 T2
}

// Pointer
*T

// Function
func(params) returns

// Interface
interface {
    Method(params) returns
}

// Channel
chan T      // bidirectional
chan<- T    // send only
<-chan T    // receive only
```

## Declarations

### Variables

```go
var name T = value
var name = value      // type inferred
var name T            // zero value
name := value         // short declaration (inside functions only)
```

### Constants

```go
const Pi = 3.14159
const (
    A = iota  // 0
    B         // 1
    C         // 2
)
```

### Functions

```go
func name(params) returnType {
    // body
}

func name(params) (named returnType, err error) {
    // body
    return
}

// Variadic
func name(args ...T) {
    // args is []T
}
```

### Methods

```go
// Value receiver
func (t T) Method() {}

// Pointer receiver
func (t *T) Method() {}
```

## Control Flow

### If

```go
if condition {
    // body
}

if init; condition {
    // body
}

if condition {
    // body
} else if condition {
    // body
} else {
    // body
}
```

### For

```go
// C-style
for i := 0; i < n; i++ {
    // body
}

// While-style
for condition {
    // body
}

// Infinite
for {
    // body
}

// Range
for index, value := range collection {
    // body
}

for index := range collection {
    // index only
}

for _, value := range collection {
    // value only
}
```

### Switch

```go
switch value {
case a:
    // no fallthrough by default
case b, c:
    // multiple values
default:
    // optional
}

switch {
case condition1:
    // like if-else chain
case condition2:
    // body
}

// Type switch
switch v := x.(type) {
case int:
    // v is int
case string:
    // v is string
}
```

### Select

```go
select {
case msg := <-ch1:
    // received from ch1
case ch2 <- value:
    // sent to ch2
default:
    // non-blocking
}
```

### Defer

```go
defer cleanup()  // runs when function returns, LIFO order
```

## Interfaces

```go
type Reader interface {
    Read(p []byte) (n int, err error)
}

// Empty interface accepts any type
interface{}  // deprecated
any          // Go 1.18+

// Type assertion
value, ok := x.(T)

// Type must implement all methods
var r Reader = &MyReader{}  // *MyReader must have Read method
```

## Generics (Go 1.18+)

```go
func Print[T any](value T) {
    fmt.Println(value)
}

func Sum[T int | float64](values []T) T {
    var sum T
    for _, v := range values {
        sum += v
    }
    return sum
}

type Stack[T any] struct {
    items []T
}

// Constraints
type Number interface {
    int | int64 | float64
}
```

## Concurrency

### Goroutines

```go
go function()
go func() {
    // anonymous
}()
```

### Channels

```go
ch := make(chan int)      // unbuffered
ch := make(chan int, 10)  // buffered

ch <- value  // send
value := <-ch  // receive
close(ch)    // close

// Range over channel
for value := range ch {
    // receives until closed
}
```

## Error Handling

```go
// Errors are values
if err != nil {
    return err
}

// Wrapping (Go 1.13+)
return fmt.Errorf("context: %w", err)

// Checking wrapped errors
errors.Is(err, target)
errors.As(err, &target)

// Sentinel errors
var ErrNotFound = errors.New("not found")
```

## Packages

```go
package main  // executable
package name  // library

import "fmt"
import (
    "fmt"
    "os"
    
    "github.com/external/pkg"
    
    alias "long/package/name"
    . "dot/import"  // avoid
    _ "side/effects/only"
)
```

## Init Functions

```go
func init() {
    // runs before main
    // multiple init() allowed per file
    // runs in order of declaration
}
```
