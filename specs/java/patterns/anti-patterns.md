# Java Anti-Patterns

Common mistakes and code smells to avoid in Java code.

## Catching Generic Exception

```java
// BAD - Catches everything including RuntimeException
try {
    riskyOperation();
} catch (Exception e) {
    log.error("Error", e);
}

// GOOD - Catch specific exceptions
try {
    riskyOperation();
} catch (IOException e) {
    log.error("IO error: {}", e.getMessage());
    throw new ServiceException("Failed to read file", e);
} catch (SQLException e) {
    log.error("Database error: {}", e.getMessage());
    throw new ServiceException("Database operation failed", e);
}
```

## Empty Catch Blocks

```java
// BAD - Swallows exception silently
try {
    file.delete();
} catch (IOException e) {
    // Do nothing
}

// GOOD - At minimum, log the error
try {
    file.delete();
} catch (IOException e) {
    log.warn("Failed to delete file: {}", file.getName(), e);
}
```

## String Concatenation in Loops

```java
// BAD - Creates new String object each iteration
String result = "";
for (String item : items) {
    result += item + ", ";  // O(n²)
}

// GOOD - Use StringBuilder
StringBuilder sb = new StringBuilder();
for (String item : items) {
    sb.append(item).append(", ");
}
String result = sb.toString();

// BETTER - Use String.join() or streams
String result = String.join(", ", items);
String result = items.stream().collect(Collectors.joining(", "));
```

## Using == for String Comparison

```java
// BAD - Compares references, not content
String a = new String("hello");
String b = new String("hello");
if (a == b) {  // false!
    // ...
}

// GOOD - Use equals()
if (a.equals(b)) {  // true
    // ...
}

// BETTER - Null-safe comparison
if (Objects.equals(a, b)) {
    // ...
}
```

## Returning Null from Collections

```java
// BAD - Caller must null-check
public List<User> findUsers(String query) {
    if (query.isEmpty()) {
        return null;  // Leads to NullPointerException
    }
    return userRepository.search(query);
}

// GOOD - Return empty collection
public List<User> findUsers(String query) {
    if (query.isEmpty()) {
        return Collections.emptyList();
    }
    return userRepository.search(query);
}
```

## Mutable Static Fields

```java
// BAD - Shared mutable state
public class Config {
    public static List<String> ALLOWED_HOSTS = new ArrayList<>();
}
// Anyone can modify: Config.ALLOWED_HOSTS.add("evil.com");

// GOOD - Immutable
public class Config {
    public static final List<String> ALLOWED_HOSTS =
        List.of("localhost", "example.com");
}
```

## Not Closing Resources

```java
// BAD - Resource leak if exception thrown
FileInputStream fis = new FileInputStream("file.txt");
byte[] data = fis.readAllBytes();
fis.close();  // Never reached if exception!

// GOOD - Try-with-resources
try (FileInputStream fis = new FileInputStream("file.txt")) {
    byte[] data = fis.readAllBytes();
}
```

## Synchronizing on Non-Final Field

```java
// BAD - Lock object can change
private Object lock = new Object();

public void process() {
    synchronized (lock) {  // Another thread might change lock!
        // ...
    }
}

// GOOD - Final lock object
private final Object lock = new Object();

public void process() {
    synchronized (lock) {
        // ...
    }
}
```

## Double-Checked Locking Without Volatile

```java
// BAD - Broken without volatile
private static Singleton instance;

public static Singleton getInstance() {
    if (instance == null) {
        synchronized (Singleton.class) {
            if (instance == null) {
                instance = new Singleton();  // May see partial object!
            }
        }
    }
    return instance;
}

// GOOD - Use volatile
private static volatile Singleton instance;

// BETTER - Use holder pattern
private static class Holder {
    static final Singleton INSTANCE = new Singleton();
}

public static Singleton getInstance() {
    return Holder.INSTANCE;
}
```

## Raw Types

```java
// BAD - No type safety
List users = new ArrayList();
users.add("not a user");  // Compiles!
User user = (User) users.get(0);  // ClassCastException at runtime

// GOOD - Use generics
List<User> users = new ArrayList<>();
users.add("not a user");  // Compile error!
```

## Ignoring InterruptedException

```java
// BAD - Breaks interrupt handling
try {
    Thread.sleep(1000);
} catch (InterruptedException e) {
    // Ignored - thread won't respond to interrupts
}

// GOOD - Restore interrupt status
try {
    Thread.sleep(1000);
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
    throw new RuntimeException("Interrupted", e);
}
```

## Hardcoded Passwords/Secrets

```java
// BAD - Secret in source code
private static final String DB_PASSWORD = "secret123";

// GOOD - Use environment or config
private static final String DB_PASSWORD = System.getenv("DB_PASSWORD");

// BETTER - Use secret management
@Value("${database.password}")
private String dbPassword;
```

## Using Float for Money

```java
// BAD - Floating point errors
float price = 0.1f + 0.2f;  // 0.30000001192092896

// GOOD - Use BigDecimal
BigDecimal price = new BigDecimal("0.1")
    .add(new BigDecimal("0.2"));  // 0.3 exactly

// Or use cents as long
long priceInCents = 10 + 20;  // 30 cents
```

## God Classes

```java
// BAD - Class does everything
public class UserManager {
    public void createUser() { }
    public void deleteUser() { }
    public void sendEmail() { }
    public void generateReport() { }
    public void processPayment() { }
    public void validateInput() { }
    // 50 more methods...
}

// GOOD - Single responsibility
public class UserService { }
public class EmailService { }
public class ReportGenerator { }
public class PaymentProcessor { }
```

## Exposing Internal Collections

```java
// BAD - Caller can modify internal state
public class Order {
    private List<Item> items = new ArrayList<>();

    public List<Item> getItems() {
        return items;  // Caller can add/remove items!
    }
}

// GOOD - Return unmodifiable view
public List<Item> getItems() {
    return Collections.unmodifiableList(items);
}

// OR return a copy
public List<Item> getItems() {
    return new ArrayList<>(items);
}
```

## Overusing Inheritance

```java
// BAD - Deep hierarchy
class Animal { }
class Mammal extends Animal { }
class Carnivore extends Mammal { }
class Canine extends Carnivore { }
class Dog extends Canine { }

// GOOD - Favor composition
class Dog {
    private final Diet diet;
    private final Movement movement;

    public Dog(Diet diet, Movement movement) {
        this.diet = diet;
        this.movement = movement;
    }
}
```
