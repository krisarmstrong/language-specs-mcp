# Swift Generation Checklist

**Read this BEFORE writing Swift code. Swift is safe by design—use its features.**

## Critical: You Must Do These

### 1. Use `guard` for Early Exits
```swift
// BAD - pyramid of doom
func process(user: User?) {
    if let user = user {
        if user.isActive {
            if user.hasPermission {
                // do work
            }
        }
    }
}

// GOOD - guard for early exit
func process(user: User?) {
    guard let user = user else { return }
    guard user.isActive else { return }
    guard user.hasPermission else { return }

    // do work with unwrapped user
}
```

### 2. Never Force Unwrap in Production
```swift
// DANGEROUS - crashes on nil
let name = user.name!
let value = dictionary["key"]!

// GOOD - safe unwrapping
if let name = user.name {
    print(name)
}

// GOOD - nil coalescing
let name = user.name ?? "Unknown"

// GOOD - guard let
guard let name = user.name else { return }
```

### 3. Use `let` Over `var` When Possible
```swift
// BAD - mutable when not needed
var name = "Alice"
var count = items.count

// GOOD - immutable by default
let name = "Alice"
let count = items.count
```

### 4. Use Strong Typing, Avoid `Any`
```swift
// BAD - loses type safety
var data: Any = "hello"
func process(_ input: Any) { }

// GOOD - use generics or protocols
func process<T: Processable>(_ input: T) { }
func process(_ input: some Processable) { }  // Swift 5.7+
```

### 5. Handle All Errors
```swift
// BAD - ignores error
try? riskyOperation()

// GOOD - handle the error
do {
    try riskyOperation()
} catch {
    logger.error("Operation failed: \(error)")
    throw error
}
```

## Important: Strong Recommendations

### 6. Use `if let` and `guard let` for Optional Binding
```swift
// BAD - multiple unwraps
if user != nil && user!.name != nil {
    print(user!.name!)
}

// GOOD - optional binding
if let user = user, let name = user.name {
    print(name)
}
```

### 7. Prefer Structs Over Classes
```swift
// For value types with no identity, prefer struct
struct Point {
    let x: Double
    let y: Double
}

// Use class for:
// - Identity (two instances can be "the same object")
// - Inheritance
// - Deinitializers
// - Reference semantics needed
```

### 8. Use `Codable` for JSON
```swift
// GOOD - automatic encoding/decoding
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let user = try JSONDecoder().decode(User.self, from: jsonData)
let json = try JSONEncoder().encode(user)
```

### 9. Use Type Inference, But Be Explicit When Helpful
```swift
// GOOD - type is obvious
let name = "Alice"
let numbers = [1, 2, 3]

// GOOD - explicit when not obvious or for documentation
let result: Result<User, NetworkError> = await fetchUser()
```

### 10. Use Computed Properties Over Methods When No Parameters
```swift
// BAD - method for simple property access
func getFullName() -> String {
    return "\(firstName) \(lastName)"
}

// GOOD - computed property
var fullName: String {
    "\(firstName) \(lastName)"
}
```

## Swift Idioms

### 11. Use `map`, `filter`, `reduce` for Collections
```swift
// BAD - manual loops
var names: [String] = []
for user in users {
    if user.isActive {
        names.append(user.name)
    }
}

// GOOD - functional style
let names = users
    .filter { $0.isActive }
    .map { $0.name }
```

### 12. Use Trailing Closure Syntax
```swift
// BAD - closure as parameter
users.filter({ $0.isActive })

// GOOD - trailing closure
users.filter { $0.isActive }

// GOOD - multiple trailing closures (Swift 5.3+)
Button("Save") {
    save()
} label: {
    Text("Save")
}
```

### 13. Use `defer` for Cleanup
```swift
func processFile() throws {
    let file = try openFile()
    defer { file.close() }  // Always runs on exit

    // ... use file ...
    // File closed automatically
}
```

### 14. Use `Result` Type for Async Callbacks
```swift
// GOOD - clear success/failure
func fetchUser(completion: @escaping (Result<User, Error>) -> Void) {
    // ...
}

fetchUser { result in
    switch result {
    case .success(let user):
        print(user.name)
    case .failure(let error):
        print("Error: \(error)")
    }
}
```

## Concurrency (Swift 5.5+)

### 15. Use async/await Over Callbacks
```swift
// BAD - callback pyramid
fetchUser { user in
    fetchProfile(user) { profile in
        fetchSettings(profile) { settings in
            // deeply nested
        }
    }
}

// GOOD - async/await
let user = try await fetchUser()
let profile = try await fetchProfile(user)
let settings = try await fetchSettings(profile)
```

### 16. Use `Task` for Concurrent Work
```swift
// GOOD - structured concurrency
async let users = fetchUsers()
async let posts = fetchPosts()

let (userList, postList) = try await (users, posts)
```

### 17. Mark Actor for Shared State
```swift
// GOOD - thread-safe shared state
actor Counter {
    private var value = 0

    func increment() {
        value += 1
    }

    func getValue() -> Int {
        value
    }
}
```

---

**Quick Reference - Copy This Mental Model:**
- `guard` for early exits
- Never force unwrap (`!`)
- `let` over `var`
- Avoid `Any`, use generics/protocols
- Handle all errors explicitly
- Structs over classes (usually)
- `Codable` for JSON
- `map`/`filter`/`reduce` for collections
- Trailing closure syntax
- `defer` for cleanup
- async/await over callbacks
- Actor for shared state
