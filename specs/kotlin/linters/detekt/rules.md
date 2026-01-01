# Detekt Rules

## Complexity

### ComplexCondition

Condition with too many logical operators.

```kotlin
// BAD - too complex
if (a && b || c && d || e && f) { }

// GOOD - extract to variables or functions
val isValid = a && b
val isAllowed = c && d
if (isValid || isAllowed) { }
```

### ComplexMethod / CyclomaticComplexMethod

Method with high cyclomatic complexity.

```kotlin
// BAD - too many branches
fun process(input: Input): Output {
    if (input.a) {
        if (input.b) { /* ... */ }
        else { /* ... */ }
    }
    when (input.type) {
        Type.A -> { /* ... */ }
        Type.B -> { /* ... */ }
        // many more...
    }
}

// GOOD - break into smaller functions
fun process(input: Input): Output {
    validateInput(input)
    return when (input.type) {
        Type.A -> processTypeA(input)
        Type.B -> processTypeB(input)
    }
}
```

### LongMethod

Method with too many lines.

### LongParameterList

Function with too many parameters.

```kotlin
// BAD - too many parameters
fun createUser(
    name: String,
    email: String,
    age: Int,
    address: String,
    phone: String,
    country: String
): User

// GOOD - use data class
data class UserRequest(
    val name: String,
    val email: String,
    val age: Int,
    val address: String,
    val phone: String,
    val country: String
)

fun createUser(request: UserRequest): User
```

### NestedBlockDepth

Too deeply nested code.

```kotlin
// BAD - too nested
fun process() {
    if (a) {
        for (item in items) {
            if (item.valid) {
                when (item.type) {
                    // deep nesting
                }
            }
        }
    }
}

// GOOD - early returns, extract functions
fun process() {
    if (!a) return
    
    items.filter { it.valid }
         .forEach { processItem(it) }
}
```

### TooManyFunctions

Class with too many functions.

## Coroutines

### GlobalCoroutineUsage

Avoid GlobalScope.

```kotlin
// BAD - unstructured concurrency
GlobalScope.launch { doWork() }

// GOOD - structured concurrency
class MyService(private val scope: CoroutineScope) {
    fun start() {
        scope.launch { doWork() }
    }
}

// Or use lifecycle-aware scope
viewModelScope.launch { doWork() }
```

### RedundantSuspendModifier

Suspend function that doesn't call suspending functions.

```kotlin
// BAD - unnecessary suspend
suspend fun calculate(): Int {
    return 1 + 1  // no suspension point
}

// GOOD - remove suspend or add suspension
fun calculate(): Int = 1 + 1
```

### SuspendFunWithFlowReturnType

Suspend function returning Flow.

```kotlin
// BAD - suspend not needed for Flow
suspend fun getItems(): Flow<Item> = flow { /* ... */ }

// GOOD - Flow is cold, no suspend needed
fun getItems(): Flow<Item> = flow { /* ... */ }
```

## Empty Blocks

### EmptyCatchBlock

Empty catch blocks.

```kotlin
// BAD
try {
    riskyOperation()
} catch (e: Exception) {
}

// GOOD - at least log
try {
    riskyOperation()
} catch (e: Exception) {
    logger.error("Operation failed", e)
}
```

### EmptyFunctionBlock

Empty function body.

### EmptyIfBlock

Empty if block.

### EmptyWhenBlock

Empty when branch.

## Exceptions

### ExceptionRaisedInUnexpectedLocation

Exceptions in equals, hashCode, toString.

```kotlin
// BAD
override fun equals(other: Any?): Boolean {
    throw UnsupportedOperationException()  // unexpected
}

// GOOD - return proper value
override fun equals(other: Any?): Boolean {
    if (other !is MyClass) return false
    return id == other.id
}
```

### SwallowedException

Caught exception not used.

```kotlin
// BAD
try {
    process()
} catch (e: IOException) {
    throw RuntimeException("Failed")  // e not used
}

// GOOD - include cause
try {
    process()
} catch (e: IOException) {
    throw RuntimeException("Failed", e)
}
```

### ThrowingExceptionsWithoutMessageOrCause

Exceptions without context.

```kotlin
// BAD
throw IllegalStateException()

// GOOD
throw IllegalStateException("Invalid state: expected READY, was $currentState")
```

### TooGenericExceptionCaught

Catching generic Exception.

```kotlin
// BAD
try {
    process()
} catch (e: Exception) { }

// GOOD - specific exceptions
try {
    process()
} catch (e: IOException) {
    handleIO(e)
} catch (e: ParseException) {
    handleParse(e)
}
```

## Naming

### ClassNaming

Classes should be PascalCase.

```kotlin
// BAD
class myClass
class MY_CLASS

// GOOD
class MyClass
```

### FunctionNaming

Functions should be camelCase.

```kotlin
// BAD
fun MyFunction() { }
fun my_function() { }

// GOOD
fun myFunction() { }
```

### VariableNaming

Variables should be camelCase.

### MatchingDeclarationName

File name should match declaration.

```kotlin
// File: User.kt
// BAD - different name
class Customer { }

// GOOD - matching name
class User { }
```

### PackageNaming

Packages should be lowercase.

```kotlin
// BAD
package com.Example.MyApp

// GOOD
package com.example.myapp
```

## Performance

### ArrayPrimitive

Prefer primitive arrays.

```kotlin
// BAD - boxed array
val numbers: Array<Int> = arrayOf(1, 2, 3)

// GOOD - primitive array
val numbers: IntArray = intArrayOf(1, 2, 3)
```

### ForEachOnRange

forEach on range creates iterator.

```kotlin
// BAD - creates iterator
(0..10).forEach { println(it) }

// GOOD - use for loop
for (i in 0..10) { println(i) }
```

### SpreadOperator

Spread operator creates copy.

```kotlin
// BAD - creates copy
fun wrapper(vararg args: String) {
    actual(*args)  // copies array
}

// GOOD - pass list if possible
fun wrapper(args: List<String>) {
    actual(args)
}
```

### UnnecessaryTemporaryInstantiation

Unnecessary wrapper creation.

```kotlin
// BAD
Integer.valueOf(42).toString()

// GOOD
42.toString()
```

## Potential Bugs

### Deprecation

Using deprecated API.

### EqualsWithHashCodeExist

equals without hashCode.

```kotlin
// BAD - inconsistent
class Item {
    override fun equals(other: Any?): Boolean { /* ... */ }
    // missing hashCode!
}

// GOOD - both overridden
class Item {
    override fun equals(other: Any?): Boolean { /* ... */ }
    override fun hashCode(): Int { /* ... */ }
}
```

### IteratorNotThrowingNoSuchElementException

Iterator.next() should throw NoSuchElementException.

### UnconditionalJumpStatementInLoop

Break/return always executed.

```kotlin
// BAD - loop only executes once
for (item in items) {
    process(item)
    break  // always breaks
}

// GOOD - conditional
for (item in items) {
    if (shouldStop(item)) break
    process(item)
}
```

### UnsafeCallOnNullableType

Using !! operator.

```kotlin
// BAD
val length = nullableString!!.length

// GOOD
val length = nullableString?.length ?: 0
```

### UselessPostfixExpression

Postfix with no effect.

```kotlin
// BAD - increment has no effect
fun getValue(): Int {
    var i = 0
    return i++  // returns 0, then increments
}

// GOOD
fun getValue(): Int {
    var i = 0
    return ++i  // increments, then returns 1
}
```

## Style

### MagicNumber

Unexplained numeric literals.

```kotlin
// BAD
if (statusCode == 200) { }
val timeout = 30000

// GOOD
const val HTTP_OK = 200
const val TIMEOUT_MS = 30_000

if (statusCode == HTTP_OK) { }
val timeout = TIMEOUT_MS
```

### MaxLineLength

Line too long.

### NewLineAtEndOfFile

File should end with newline.

### NoTabs

Use spaces instead of tabs.

### OptionalAbstractKeyword

Redundant abstract on interface members.

```kotlin
// BAD - abstract is implicit
interface Service {
    abstract fun process()
}

// GOOD
interface Service {
    fun process()
}
```

### ReturnCount

Too many return statements.

```kotlin
// BAD - too many returns
fun validate(input: Input): Boolean {
    if (input.a) return false
    if (input.b) return false
    if (input.c) return false
    if (input.d) return false
    return true
}

// GOOD - single expression
fun validate(input: Input): Boolean =
    !input.a && !input.b && !input.c && !input.d
```

### SafeCast

Use safe cast instead of is + cast.

```kotlin
// BAD
if (obj is String) {
    val s = obj as String
}

// GOOD - smart cast
if (obj is String) {
    // obj is already String
    println(obj.length)
}

// Or safe cast
val s = obj as? String
```

### SerialVersionUIDInSerializableClass

Serializable should have serialVersionUID.

### UnnecessaryAbstractClass

Abstract class with no abstract members.

```kotlin
// BAD - could be open class
abstract class Base {
    fun method() { }  // not abstract
}

// GOOD
open class Base {
    open fun method() { }
}
```

### UnnecessaryApply

Apply with only assignments.

```kotlin
// BAD - apply not needed
val person = Person().apply {
    name = "Alice"
}

// GOOD - constructor or named arguments
val person = Person(name = "Alice")
```

### UnusedImports

Remove unused imports.

### UnusedPrivateMember

Remove unused private members.

### UseCheckOrError

Use check/error instead of throw.

```kotlin
// BAD
if (state != State.READY) {
    throw IllegalStateException("Not ready")
}

// GOOD
check(state == State.READY) { "Not ready" }
```

### UseRequire

Use require instead of throw for arguments.

```kotlin
// BAD
if (value < 0) {
    throw IllegalArgumentException("Value must be non-negative")
}

// GOOD
require(value >= 0) { "Value must be non-negative" }
```

### WildcardImport

Avoid wildcard imports.

```kotlin
// BAD
import kotlin.collections.*

// GOOD
import kotlin.collections.List
import kotlin.collections.Map
```
