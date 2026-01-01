# Java Idioms

## Prefer try-with-resources

```java
try (var input = Files.newInputStream(path)) {
    // use input
}
```

## Use records for simple data carriers

```java
public record User(String id, String name) {}
```

## Prefer standard collections interfaces

Use `List`, `Set`, and `Map` in APIs instead of concrete types.
