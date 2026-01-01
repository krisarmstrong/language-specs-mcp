# Go Error Handling Patterns

## Basic Pattern

```go
result, err := doSomething()
if err != nil {
    return fmt.Errorf("doing something: %w", err)
}
```

## NEVER ignore errors

```go
// BAD - fails errcheck
result, _ := doSomething()

// GOOD
result, err := doSomething()
if err != nil {
    return err
}
```

## Error wrapping (Go 1.13+)

```go
// Wrap with context
if err != nil {
    return fmt.Errorf("failed to process %s: %w", name, err)
}

// Check wrapped errors
if errors.Is(err, os.ErrNotExist) {
    // handle not found
}

// Type assert wrapped errors
var pathErr *os.PathError
if errors.As(err, &pathErr) {
    // handle path error
}
```

## Sentinel errors

```go
// Define at package level
var ErrNotFound = errors.New("not found")

// Use errors.Is to check
if errors.Is(err, ErrNotFound) {
    // handle
}
```

## Custom error types

```go
type ValidationError struct {
    Field string
    Msg   string
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("%s: %s", e.Field, e.Msg)
}
```
