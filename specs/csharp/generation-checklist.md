# C# Generation Checklist

**Read this BEFORE writing C# code. These rules prevent the most common bugs.**

## Critical: You Must Do These

### 1. Use `using` for Disposable Resources
```csharp
// BAD - resource leak risk
var file = new StreamReader("data.txt");
// ... forget to dispose

// GOOD - using statement
using (var file = new StreamReader("data.txt"))
{
    // Automatically disposed
}

// BETTER - using declaration (C# 8+)
using var file = new StreamReader("data.txt");
// Disposed at end of scope
```

### 2. Enable Nullable Reference Types (C# 8+)
```csharp
// In project file or at top of file
#nullable enable

// Now compiler warns about null issues
string name = null;  // Warning!
string? name = null; // OK - explicitly nullable

// GOOD - check before use
if (user?.Name is string name)
{
    Console.WriteLine(name);
}
```

### 3. Use Async/Await Correctly
```csharp
// BAD - blocking on async
var result = GetDataAsync().Result;  // Deadlock risk!
GetDataAsync().Wait();               // Deadlock risk!

// GOOD - async all the way
var result = await GetDataAsync();

// GOOD - if you must sync, use GetAwaiter
var result = GetDataAsync().GetAwaiter().GetResult();
```

### 4. Use `ConfigureAwait(false)` in Libraries
```csharp
// In library code - don't capture context
public async Task<Data> GetDataAsync()
{
    var response = await httpClient.GetAsync(url)
        .ConfigureAwait(false);
    return await response.Content.ReadAsAsync<Data>()
        .ConfigureAwait(false);
}
```

### 5. Use Parameterized Queries
```csharp
// DANGEROUS - SQL injection
var query = $"SELECT * FROM Users WHERE Id = {userId}";

// SAFE - parameterized
var command = new SqlCommand(
    "SELECT * FROM Users WHERE Id = @Id",
    connection
);
command.Parameters.AddWithValue("@Id", userId);

// SAFE - with Dapper
var user = connection.QuerySingle<User>(
    "SELECT * FROM Users WHERE Id = @Id",
    new { Id = userId }
);
```

## Important: Strong Recommendations

### 6. Prefer `var` When Type Is Obvious
```csharp
// BAD - redundant
Dictionary<string, List<int>> map = new Dictionary<string, List<int>>();

// GOOD - type is obvious
var map = new Dictionary<string, List<int>>();

// GOOD - explicit when not obvious
User user = GetEntity();  // What type does GetEntity return?
```

### 7. Use Collection Expressions (C# 12+)
```csharp
// OLD - verbose
var list = new List<int> { 1, 2, 3 };
var array = new int[] { 1, 2, 3 };

// NEW - collection expressions
List<int> list = [1, 2, 3];
int[] array = [1, 2, 3];
```

### 8. Use Pattern Matching
```csharp
// BAD - type checks and casts
if (obj is User)
{
    var user = (User)obj;
    Console.WriteLine(user.Name);
}

// GOOD - pattern matching
if (obj is User user)
{
    Console.WriteLine(user.Name);
}

// GOOD - switch expression
var message = result switch
{
    Success s => $"Got: {s.Value}",
    Error e => $"Failed: {e.Message}",
    _ => "Unknown"
};
```

### 9. Use Records for Immutable Data (C# 9+)
```csharp
// BAD - verbose immutable class
public class User
{
    public string Name { get; }
    public string Email { get; }
    // + constructor, Equals, GetHashCode...
}

// GOOD - record
public record User(string Name, string Email);

// With mutation via with-expression
var updated = user with { Email = "new@test.com" };
```

### 10. Use Primary Constructors (C# 12+)
```csharp
// OLD - verbose
public class UserService
{
    private readonly ILogger _logger;
    private readonly IUserRepository _repo;

    public UserService(ILogger logger, IUserRepository repo)
    {
        _logger = logger;
        _repo = repo;
    }
}

// NEW - primary constructor
public class UserService(ILogger logger, IUserRepository repo)
{
    public void DoWork() => logger.Log("Working...");
}
```

## LINQ

### 11. Use LINQ for Collection Operations
```csharp
// BAD - manual loops
var activeNames = new List<string>();
foreach (var user in users)
{
    if (user.IsActive)
    {
        activeNames.Add(user.Name);
    }
}

// GOOD - LINQ
var activeNames = users
    .Where(u => u.IsActive)
    .Select(u => u.Name)
    .ToList();
```

### 12. Use `FirstOrDefault` with Null Check
```csharp
// BAD - assumes result exists
var user = users.First(u => u.Id == id);  // Throws if not found

// GOOD - handle not found
var user = users.FirstOrDefault(u => u.Id == id);
if (user is null)
{
    throw new UserNotFoundException(id);
}

// GOOD - with default value
var user = users.FirstOrDefault(u => u.Id == id)
    ?? User.Anonymous;
```

## Async Best Practices

### 13. Return Task, Not void
```csharp
// BAD - fire and forget, exceptions lost
public async void ProcessAsync() { }

// GOOD - caller can await and catch exceptions
public async Task ProcessAsync() { }
```

### 14. Use ValueTask for Hot Paths
```csharp
// GOOD - avoids allocation when result is cached
public ValueTask<Data> GetDataAsync()
{
    if (_cache.TryGetValue(key, out var data))
    {
        return ValueTask.FromResult(data);
    }
    return new ValueTask<Data>(FetchDataAsync());
}
```

### 15. Cancellation Token Support
```csharp
// GOOD - support cancellation
public async Task<Data> FetchDataAsync(CancellationToken ct = default)
{
    var response = await httpClient.GetAsync(url, ct);
    ct.ThrowIfCancellationRequested();
    return await response.Content.ReadAsAsync<Data>(ct);
}
```

## Error Handling

### 16. Use Specific Exception Types
```csharp
// BAD - generic exception
throw new Exception("User not found");

// GOOD - specific exception
throw new UserNotFoundException(userId);

// GOOD - with custom exception
public class UserNotFoundException : Exception
{
    public long UserId { get; }
    public UserNotFoundException(long userId)
        : base($"User not found: {userId}")
    {
        UserId = userId;
    }
}
```

---

**Quick Reference - Copy This Mental Model:**
- `using` for disposables
- `#nullable enable` for null safety
- `await`, never `.Result` or `.Wait()`
- ConfigureAwait(false) in libraries
- Parameterized SQL queries
- `var` when type is obvious
- Pattern matching for type checks
- Records for immutable data
- LINQ for collections
- `Task` not `async void`
- CancellationToken support
- Specific exception types
