# C# Idioms

## Use async/await for I/O

Prefer async APIs for network and disk operations.

## Prefer `using` declarations for disposal

```csharp
using var stream = File.OpenRead(path);
```

## Embrace nullable reference types

Enable nullable and use `string?` when values can be null.

## Use records for immutable data

```csharp
public record User(string Id, string Name);
```
