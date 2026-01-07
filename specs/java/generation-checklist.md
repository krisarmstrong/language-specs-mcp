# Java Generation Checklist

**Read this BEFORE writing Java code. These rules prevent the most common bugs.**

## Critical: You Must Do These

### 1. Use `equals()` Not `==` for Object Comparison
```java
// BAD - compares references
if (str1 == str2)

// GOOD - compares values
if (str1.equals(str2))

// GOOD - null-safe with Objects.equals
if (Objects.equals(str1, str2))
```

### 2. Always Close Resources with try-with-resources
```java
// BAD - resource leak risk
FileInputStream fis = new FileInputStream(file);
// ... use fis ...
fis.close();

// GOOD - automatic cleanup
try (FileInputStream fis = new FileInputStream(file)) {
    // ... use fis ...
}
```

### 3. Check for Null Before Dereferencing
```java
// BAD - NullPointerException risk
String upper = getValue().toUpperCase();

// GOOD - null check
String value = getValue();
if (value != null) {
    String upper = value.toUpperCase();
}

// GOOD - Optional (Java 8+)
Optional.ofNullable(getValue())
    .map(String::toUpperCase)
    .orElse("DEFAULT");
```

### 4. Override `hashCode()` When Overriding `equals()`
```java
// REQUIRED - must override both together
@Override
public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof User)) return false;
    User user = (User) o;
    return id == user.id;
}

@Override
public int hashCode() {
    return Objects.hash(id);
}
```

### 5. Use StringBuilder for String Concatenation in Loops
```java
// BAD - creates many String objects
String result = "";
for (String s : items) {
    result += s;
}

// GOOD - efficient
StringBuilder sb = new StringBuilder();
for (String s : items) {
    sb.append(s);
}
String result = sb.toString();
```

## Important: Strong Recommendations

### 6. Prefer List Interface Over ArrayList
```java
// BAD - ties to implementation
ArrayList<String> items = new ArrayList<>();

// GOOD - program to interface
List<String> items = new ArrayList<>();
```

### 7. Use Diamond Operator (Java 7+)
```java
// BAD - redundant type
Map<String, List<Integer>> map = new HashMap<String, List<Integer>>();

// GOOD - inferred type
Map<String, List<Integer>> map = new HashMap<>();
```

### 8. Prefer `var` for Local Variables with Obvious Types (Java 10+)
```java
// Verbose
HashMap<String, List<Integer>> map = new HashMap<>();

// GOOD - type is obvious from right side
var map = new HashMap<String, List<Integer>>();
```

### 9. Use Streams for Collection Processing
```java
// BAD - imperative
List<String> names = new ArrayList<>();
for (User user : users) {
    if (user.isActive()) {
        names.add(user.getName());
    }
}

// GOOD - declarative
List<String> names = users.stream()
    .filter(User::isActive)
    .map(User::getName)
    .collect(Collectors.toList());
```

### 10. Prefer `Optional` Over Returning Null
```java
// BAD - caller might forget null check
public User findById(long id) {
    // returns null if not found
}

// GOOD - explicit optionality
public Optional<User> findById(long id) {
    // returns Optional.empty() if not found
}
```

## Concurrency

### 11. Use ConcurrentHashMap for Thread-Safe Maps
```java
// BAD - not thread-safe
Map<String, Integer> map = new HashMap<>();

// GOOD - thread-safe
Map<String, Integer> map = new ConcurrentHashMap<>();
```

### 12. Prefer ExecutorService Over Raw Threads
```java
// BAD - manual thread management
new Thread(() -> doWork()).start();

// GOOD - managed thread pool
ExecutorService executor = Executors.newFixedThreadPool(4);
executor.submit(() -> doWork());
executor.shutdown();
```

### 13. Use `volatile` or Atomic Classes for Shared Flags
```java
// BAD - visibility issues
private boolean running = true;

// GOOD - guarantees visibility
private volatile boolean running = true;

// GOOD - atomic operations
private AtomicBoolean running = new AtomicBoolean(true);
```

## Modern Java (11+)

### 14. Use `List.of()`, `Set.of()`, `Map.of()` for Immutable Collections
```java
// GOOD - immutable, concise
List<String> items = List.of("a", "b", "c");
Set<Integer> numbers = Set.of(1, 2, 3);
Map<String, Integer> scores = Map.of("Alice", 100, "Bob", 95);
```

### 15. Use Text Blocks for Multi-line Strings (Java 15+)
```java
// GOOD - readable multi-line
String json = """
    {
        "name": "Alice",
        "age": 30
    }
    """;
```

### 16. Use Records for Data Classes (Java 16+)
```java
// Instead of verbose POJO
public record User(long id, String name, String email) { }
// Automatically gets: constructor, getters, equals, hashCode, toString
```

## Security

### 17. Never Build SQL with String Concatenation
```java
// DANGEROUS - SQL injection
String query = "SELECT * FROM users WHERE id = " + userId;

// SAFE - parameterized query
PreparedStatement stmt = conn.prepareStatement(
    "SELECT * FROM users WHERE id = ?"
);
stmt.setLong(1, userId);
```

### 18. Validate All External Input
```java
// GOOD - validate before use
public void setAge(int age) {
    if (age < 0 || age > 150) {
        throw new IllegalArgumentException("Invalid age: " + age);
    }
    this.age = age;
}
```

---

**Quick Reference - Copy This Mental Model:**
- `equals()` not `==` for objects
- try-with-resources for all resources
- Null check or use Optional
- Override hashCode with equals
- StringBuilder in loops
- Program to interfaces
- Streams for collection processing
- Optional over null returns
- ConcurrentHashMap for thread-safe maps
- PreparedStatement for SQL
