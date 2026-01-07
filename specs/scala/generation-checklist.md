# Scala Generation Checklist

**Read this BEFORE writing Scala code. Embrace functional patterns—they prevent bugs.**

## Critical: You Must Do These

### 1. Use `val` Over `var`
```scala
// BAD - mutable
var count = 0
var name = "Alice"

// GOOD - immutable by default
val count = 0
val name = "Alice"
```

### 2. Use `Option` Instead of Null
```scala
// BAD - null propagation
def findUser(id: Long): User = {
  // returns null if not found
}
val name = findUser(1).name  // NullPointerException!

// GOOD - Option makes nullability explicit
def findUser(id: Long): Option[User] = {
  // returns Some(user) or None
}
findUser(1).map(_.name).getOrElse("Unknown")
```

### 3. Use Pattern Matching Over Type Checks
```scala
// BAD - manual type checking
if (animal.isInstanceOf[Dog]) {
  val dog = animal.asInstanceOf[Dog]
  dog.bark()
}

// GOOD - pattern matching
animal match {
  case dog: Dog => dog.bark()
  case cat: Cat => cat.meow()
  case _ => println("Unknown animal")
}
```

### 4. Use Case Classes for Data
```scala
// BAD - regular class for data
class User(val id: Long, val name: String) {
  // Need to implement equals, hashCode, toString...
}

// GOOD - case class
case class User(id: Long, name: String)
// Gets: equals, hashCode, toString, copy, pattern matching
```

### 5. Use Sealed Traits for ADTs
```scala
// GOOD - algebraic data type
sealed trait Result[+A]
case class Success[A](value: A) extends Result[A]
case class Failure(error: String) extends Result[Nothing]

// Compiler warns if match is not exhaustive
def handle[A](result: Result[A]): String = result match {
  case Success(v) => s"Got: $v"
  case Failure(e) => s"Error: $e"
}
```

## Important: Strong Recommendations

### 6. Use `for` Comprehensions for Monadic Operations
```scala
// BAD - nested flatMap/map
user.flatMap { u =>
  fetchProfile(u.id).flatMap { profile =>
    fetchSettings(profile.id).map { settings =>
      (u, profile, settings)
    }
  }
}

// GOOD - for comprehension
for {
  u <- user
  profile <- fetchProfile(u.id)
  settings <- fetchSettings(profile.id)
} yield (u, profile, settings)
```

### 7. Prefer Immutable Collections
```scala
// BAD - mutable collections
import scala.collection.mutable.ListBuffer
val items = ListBuffer[String]()
items += "item"

// GOOD - immutable collections
val items = List("item1")
val newItems = items :+ "item2"  // Creates new list
```

### 8. Use `Either` for Error Handling
```scala
// GOOD - explicit error handling
def divide(a: Int, b: Int): Either[String, Int] = {
  if (b == 0) Left("Division by zero")
  else Right(a / b)
}

divide(10, 2) match {
  case Right(result) => println(s"Result: $result")
  case Left(error) => println(s"Error: $error")
}
```

### 9. Use Default Parameters Over Overloading
```scala
// BAD - multiple overloads
def greet(name: String): String = greet(name, "Hello")
def greet(name: String, greeting: String): String = s"$greeting, $name!"

// GOOD - default parameters
def greet(name: String, greeting: String = "Hello"): String = {
  s"$greeting, $name!"
}
```

### 10. Use Named Arguments for Clarity
```scala
// BAD - unclear parameters
createUser("Alice", "alice@test.com", true, false, 30)

// GOOD - named arguments
createUser(
  name = "Alice",
  email = "alice@test.com",
  isAdmin = true,
  isVerified = false,
  age = 30
)
```

## Functional Patterns

### 11. Use Higher-Order Functions
```scala
// BAD - manual loop
var total = 0
for (item <- items) {
  if (item.isActive) {
    total += item.price
  }
}

// GOOD - functional style
val total = items
  .filter(_.isActive)
  .map(_.price)
  .sum
```

### 12. Use `map`, `flatMap`, `fold` Appropriately
```scala
// map - transform values
val names: List[String] = users.map(_.name)

// flatMap - transform and flatten
val emails: List[String] = users.flatMap(_.emails)

// fold - reduce with accumulator
val total: Int = numbers.fold(0)(_ + _)

// foldLeft - with explicit accumulator type
val concat: String = items.foldLeft("")(_ + _.name)
```

### 13. Use `collect` for Partial Functions
```scala
// GOOD - filter and transform in one step
val activeNames: List[String] = users.collect {
  case user if user.isActive => user.name
}
```

### 14. Use `lazy val` for Expensive Computations
```scala
// GOOD - computed only when first accessed
lazy val expensiveData: Data = computeExpensiveData()
```

## Type Safety

### 15. Use Type Aliases for Clarity
```scala
// GOOD - self-documenting types
type UserId = Long
type Email = String
type UserMap = Map[UserId, User]

def findUser(id: UserId): Option[User]
```

### 16. Use Value Classes to Avoid Primitive Obsession
```scala
// GOOD - type-safe wrappers with no runtime overhead
case class UserId(value: Long) extends AnyVal
case class Email(value: String) extends AnyVal

def findUser(id: UserId): Option[User]
// Cannot accidentally pass Email where UserId expected
```

### 17. Prefer Explicit Return Types for Public Methods
```scala
// BAD - inferred type may surprise
def process(data: String) = {
  // Complex logic...
}

// GOOD - explicit contract
def process(data: String): Result[ProcessedData] = {
  // Complex logic...
}
```

## Concurrency

### 18. Use `Future` for Async Operations
```scala
import scala.concurrent.Future
import scala.concurrent.ExecutionContext.Implicits.global

// GOOD - non-blocking
def fetchUser(id: Long): Future[User] = Future {
  // Async operation
}

// Combine futures
for {
  user <- fetchUser(1)
  profile <- fetchProfile(user.id)
} yield UserWithProfile(user, profile)
```

---

**Quick Reference - Copy This Mental Model:**
- `val` over `var`
- `Option` not null
- Pattern matching over type checks
- Case classes for data
- Sealed traits for ADTs
- For comprehensions for monads
- Immutable collections
- `Either` for errors
- Default parameters over overloads
- Named arguments for clarity
- Higher-order functions
- `lazy val` for expensive computations
- Value classes for type safety
- `Future` for async
