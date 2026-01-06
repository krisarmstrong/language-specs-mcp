# Scalafix

Scalafix is a refactoring and linting tool for Scala.

Version: 0.13.0
Source: https://scalacenter.github.io/scalafix/

## Installation

Add to `project/plugins.sbt`:

```scala
addSbtPlugin("ch.epfl.scala" % "sbt-scalafix" % "0.13.0")
```

## Usage

```bash
# Check for issues
sbt scalafix --check

# Apply fixes
sbt scalafix

# Run specific rule
sbt "scalafix RemoveUnused"
```

## Configuration

Create `.scalafix.conf`:

```hocon
rules = [
  RemoveUnused
  DisableSyntax
  LeakingImplicitClassVal
  NoValInForComprehension
  ProcedureSyntax
]

RemoveUnused.imports = true
RemoveUnused.privates = true
RemoveUnused.locals = true

DisableSyntax.noVars = true
DisableSyntax.noThrows = true
DisableSyntax.noNulls = true
DisableSyntax.noReturns = true
DisableSyntax.noWhileLoops = true
DisableSyntax.noAsInstanceOf = true
DisableSyntax.noIsInstanceOf = true
DisableSyntax.noXml = true
DisableSyntax.noFinalize = true
DisableSyntax.noValPatterns = true
```

## Built-in Rules

### RemoveUnused
Removes unused imports, private members, and local definitions.

### DisableSyntax
Disables specific Scala syntax features:
- `noVars` - Mutable variables
- `noThrows` - Throw expressions
- `noNulls` - Null literals
- `noReturns` - Return statements
- `noWhileLoops` - While loops
- `noAsInstanceOf` - Type casts
- `noIsInstanceOf` - Type checks
- `noXml` - XML literals
- `noFinalize` - Finalize method
- `noValPatterns` - Val patterns

### LeakingImplicitClassVal
Warns about leaking implicit class values.

### NoValInForComprehension
Discourages val in for comprehensions.

### ProcedureSyntax
Rewrites procedure syntax to explicit Unit return.

```scala
// Before
def foo() { println("hello") }

// After
def foo(): Unit = { println("hello") }
```

### ExplicitResultTypes
Adds explicit result types to public members.

### NoAutoTupling
Warns about auto-tupling.

### RedundantSyntax
Removes redundant syntax.

## Custom Rules

```scala
import scalafix.v1._

class MyRule extends SemanticRule("MyRule") {
  override def fix(implicit doc: SemanticDocument): Patch = {
    // Rule implementation
    Patch.empty
  }
}
```

## Suppressing Warnings

```scala
// scalafix:off
code here
// scalafix:on

// scalafix:ok
val x = mutable // suppress for this line

@SuppressWarnings(Array("scalafix:DisableSyntax.noVars"))
var mutableVar = 1
```

## WartRemover Integration

WartRemover is another popular Scala linter:

```scala
// project/plugins.sbt
addSbtPlugin("org.wartremover" % "sbt-wartremover" % "3.2.5")

// build.sbt
wartremoverErrors ++= Warts.unsafe
```

### Common Warts
- `Wart.Any` - Inferred Any type
- `Wart.AsInstanceOf` - Type casts
- `Wart.IsInstanceOf` - Type checks
- `Wart.Null` - Null values
- `Wart.Return` - Return statements
- `Wart.Var` - Mutable variables
- `Wart.MutableDataStructures` - Mutable collections
- `Wart.Throw` - Throw expressions
