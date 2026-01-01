# Kotlin Idioms

## Prefer data classes for simple models

```kotlin
data class User(val id: String, val name: String)
```

## Use sealed classes for closed hierarchies

```kotlin
sealed interface Result
data class Success(val value: String) : Result
data class Failure(val error: Throwable) : Result
```

## Use `let`, `apply`, and `also` for scoped operations
