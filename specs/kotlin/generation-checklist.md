# Kotlin Generation Checklist

**Read this BEFORE writing Kotlin code. Kotlin prevents many bugs by design—use its features.**

## Critical: You Must Do These

### 1. Use `val` Over `var`
```kotlin
// BAD - mutable when not needed
var name = "Alice"
var count = items.size

// GOOD - immutable by default
val name = "Alice"
val count = items.size
```

### 2. Use Null Safety Features
```kotlin
// BAD - defeats null safety
val name: String = user!!.name!!

// GOOD - safe call operator
val name = user?.name

// GOOD - Elvis operator for defaults
val name = user?.name ?: "Unknown"

// GOOD - safe let block
user?.let {
    println(it.name)
}
```

### 3. Use Data Classes for DTOs
```kotlin
// BAD - verbose Java-style class
class User {
    var id: Long = 0
    var name: String = ""
    // + equals, hashCode, toString, copy...
}

// GOOD - data class
data class User(
    val id: Long,
    val name: String,
    val email: String
)
// Gets: equals, hashCode, toString, copy, componentN
```

### 4. Use `when` Instead of `if-else` Chains
```kotlin
// BAD - verbose
val result = if (x == 1) {
    "one"
} else if (x == 2) {
    "two"
} else {
    "other"
}

// GOOD - when expression
val result = when (x) {
    1 -> "one"
    2 -> "two"
    else -> "other"
}

// GOOD - when with sealed class (exhaustive)
val result = when (state) {
    is Loading -> showSpinner()
    is Success -> showData(state.data)
    is Error -> showError(state.message)
}
```

### 5. Use Sealed Classes for Restricted Hierarchies
```kotlin
// GOOD - compiler ensures exhaustive when
sealed class Result<out T> {
    data class Success<T>(val data: T) : Result<T>()
    data class Error(val message: String) : Result<Nothing>()
    object Loading : Result<Nothing>()
}
```

## Important: Strong Recommendations

### 6. Use Extension Functions
```kotlin
// GOOD - extends existing types cleanly
fun String.isValidEmail(): Boolean {
    return this.contains("@") && this.contains(".")
}

val email = "test@example.com"
if (email.isValidEmail()) { }
```

### 7. Use `apply`, `let`, `run`, `with`, `also` Appropriately
```kotlin
// apply - configure object, return it
val user = User().apply {
    name = "Alice"
    email = "alice@test.com"
}

// let - transform nullable, scoped variable
user?.let { println(it.name) }

// run - execute block, return result
val length = str.run {
    trim()
    length
}

// also - side effects, return original
val user = createUser().also { logger.info("Created: $it") }
```

### 8. Use Named Arguments for Clarity
```kotlin
// BAD - unclear parameters
createUser("Alice", "alice@test.com", true, false)

// GOOD - self-documenting
createUser(
    name = "Alice",
    email = "alice@test.com",
    isAdmin = true,
    sendWelcome = false
)
```

### 9. Use Default Parameter Values
```kotlin
// BAD - overloaded functions
fun greet(name: String) = greet(name, "Hello")
fun greet(name: String, greeting: String) = println("$greeting, $name!")

// GOOD - default values
fun greet(name: String, greeting: String = "Hello") {
    println("$greeting, $name!")
}
```

### 10. Use Collection Functions
```kotlin
// BAD - manual loops
val names = mutableListOf<String>()
for (user in users) {
    if (user.isActive) {
        names.add(user.name)
    }
}

// GOOD - functional style
val names = users
    .filter { it.isActive }
    .map { it.name }
```

## Kotlin Idioms

### 11. Use String Templates
```kotlin
// BAD - concatenation
val message = "Hello, " + name + "! You have " + count + " messages."

// GOOD - string template
val message = "Hello, $name! You have $count messages."
val message = "User: ${user.name}, Age: ${user.age}"
```

### 12. Use `require` and `check` for Validation
```kotlin
fun process(data: String) {
    // Throws IllegalArgumentException
    require(data.isNotEmpty()) { "Data cannot be empty" }

    // Throws IllegalStateException
    check(isInitialized) { "Must initialize first" }
}
```

### 13. Use Destructuring Declarations
```kotlin
// GOOD - destructure data classes
val (id, name, email) = user

// GOOD - in loops
for ((key, value) in map) {
    println("$key -> $value")
}

// GOOD - from functions
val (result, error) = fetchData()
```

### 14. Use Object for Singletons
```kotlin
// GOOD - thread-safe singleton
object DatabaseConnection {
    fun connect() { }
}

// Use directly
DatabaseConnection.connect()
```

## Coroutines

### 15. Use Coroutines for Async Work
```kotlin
// GOOD - structured concurrency
suspend fun fetchUserData(): User {
    return withContext(Dispatchers.IO) {
        api.fetchUser()
    }
}

// GOOD - parallel execution
coroutineScope {
    val user = async { fetchUser() }
    val posts = async { fetchPosts() }

    processData(user.await(), posts.await())
}
```

### 16. Use `Flow` for Streams
```kotlin
// GOOD - cold stream
fun observeUsers(): Flow<List<User>> = flow {
    while (true) {
        emit(fetchUsers())
        delay(5000)
    }
}

// Collect
observeUsers().collect { users ->
    updateUI(users)
}
```

### 17. Always Use SupervisorJob for Independent Children
```kotlin
// GOOD - one failure doesn't cancel siblings
val scope = CoroutineScope(SupervisorJob() + Dispatchers.Main)
```

---

**Quick Reference - Copy This Mental Model:**
- `val` over `var`
- Safe calls `?.` and Elvis `?:`
- Data classes for DTOs
- `when` over if-else chains
- Sealed classes for state
- Extension functions
- Scope functions (apply, let, run, also)
- Named arguments for clarity
- Default parameter values
- Collection functions over loops
- String templates
- require/check for validation
- Coroutines for async
- Flow for streams
