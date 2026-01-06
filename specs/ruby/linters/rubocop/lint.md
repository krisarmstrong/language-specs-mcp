# RuboCop Lint Cops

Lint cops check for potential errors, code smells, and possible bugs.

Source: https://docs.rubocop.org/rubocop/cops_lint.html

## Error Detection

### Lint/AmbiguousAssignment
Checks for mistyped shorthand assignments.

```ruby
# Bad
x =- 1  # Did you mean x = -1 or x -= 1?

# Good
x = -1
x -= 1
```

### Lint/AmbiguousBlockAssociation
Checks for ambiguous block association with method calls.

### Lint/AmbiguousOperator
Checks for ambiguous operators.

### Lint/AmbiguousOperatorPrecedence
Checks for operators with ambiguous precedence.

### Lint/AmbiguousRange
Checks for ambiguous ranges.

### Lint/AmbiguousRegexpLiteral
Checks for ambiguous regexp literals.

### Lint/AssignmentInCondition
Checks for assignment in conditionals.

```ruby
# Bad
if foo = bar
end

# Good
foo = bar
if foo
end
```

### Lint/BigDecimalNew
Checks for `BigDecimal.new`.

### Lint/BinaryOperatorWithIdenticalOperands
Checks for binary operators with identical operands.

### Lint/BooleanSymbol
Checks for `:true` and `:false` symbols.

### Lint/CircularArgumentReference
Checks for circular argument references.

### Lint/ConstantDefinitionInBlock
Checks for constant definitions in blocks.

### Lint/ConstantOverwrittenInRescue
Checks for constants overwritten in rescue.

### Lint/ConstantResolution
Checks for constant resolution.

### Lint/Debugger
Checks for debugger calls.

```ruby
# Bad
binding.pry
byebug
debugger
```

### Lint/DeprecatedClassMethods
Checks for deprecated class methods.

### Lint/DeprecatedConstants
Checks for deprecated constants.

### Lint/DeprecatedOpenSSLConstant
Checks for deprecated OpenSSL constants.

### Lint/DisjunctiveAssignmentInConstructor
Checks for disjunctive assignment in constructors.

### Lint/DuplicateBranch
Checks for duplicate branches.

### Lint/DuplicateCaseCondition
Checks for duplicate case conditions.

### Lint/DuplicateElsifCondition
Checks for duplicate elsif conditions.

### Lint/DuplicateHashKey
Checks for duplicate hash keys.

```ruby
# Bad
{ a: 1, a: 2 }
```

### Lint/DuplicateMagicComment
Checks for duplicate magic comments.

### Lint/DuplicateMatchPattern
Checks for duplicate match patterns.

### Lint/DuplicateMethods
Checks for duplicate method definitions.

### Lint/DuplicateRegexpCharacterClassElement
Checks for duplicate regexp character class elements.

### Lint/DuplicateRequire
Checks for duplicate requires.

### Lint/DuplicateRescueException
Checks for duplicate rescue exceptions.

### Lint/EachWithObjectArgument
Checks for each_with_object argument.

### Lint/ElseLayout
Checks for else layout.

### Lint/EmptyBlock
Checks for empty blocks.

### Lint/EmptyClass
Checks for empty classes.

### Lint/EmptyConditionalBody
Checks for empty conditional bodies.

### Lint/EmptyEnsure
Checks for empty ensure.

### Lint/EmptyExpression
Checks for empty expressions.

### Lint/EmptyFile
Checks for empty files.

### Lint/EmptyInPattern
Checks for empty in patterns.

### Lint/EmptyInterpolation
Checks for empty interpolation.

### Lint/EmptyWhen
Checks for empty when.

### Lint/EnsureReturn
Checks for return in ensure.

```ruby
# Bad
def foo
  # ...
ensure
  return bar  # This suppresses exceptions!
end
```

### Lint/ErbNewArguments
Checks for ERB.new arguments.

### Lint/FlipFlop
Checks for flip-flop operator usage.

### Lint/FloatComparison
Checks for float comparison.

```ruby
# Bad
x == 0.1

# Good
(x - 0.1).abs < Float::EPSILON
```

### Lint/FloatOutOfRange
Checks for float out of range.

### Lint/FormatParameterMismatch
Checks for format parameter mismatch.

### Lint/HashCompareByIdentity
Checks for Hash#compare_by_identity issues.

### Lint/HeredocMethodCallPosition
Checks for heredoc method call position.

### Lint/IdentityComparison
Checks for identity comparison.

### Lint/ImplicitStringConcatenation
Checks for implicit string concatenation.

```ruby
# Bad (probably unintended)
array = ['foo' 'bar']  # Results in ['foobar']
```

### Lint/IncompatibleIoSelectWithFiberScheduler
Checks for IO.select incompatible with fiber scheduler.

### Lint/IneffectiveAccessModifier
Checks for ineffective access modifiers.

### Lint/InheritException
Checks for inheriting from Exception vs StandardError.

### Lint/InterpolationCheck
Checks for interpolation in single-quoted strings.

### Lint/ItWithoutArgumentsInBlock
Checks for `it` without arguments in blocks.

### Lint/LambdaWithoutLiteralBlock
Checks for lambda without literal block.

### Lint/LiteralAsCondition
Checks for literal as condition.

```ruby
# Bad
if true
end
```

### Lint/LiteralAssignmentInCondition
Checks for literal assignment in condition.

### Lint/LiteralInInterpolation
Checks for literal in interpolation.

### Lint/Loop
Checks for begin/end/while or begin/end/until.

### Lint/MissingCopEnableDirective
Checks for missing cop enable directive.

### Lint/MissingSuper
Checks for missing super calls.

### Lint/MixedCaseRange
Checks for mixed case ranges.

### Lint/MixedRegexpCaptureTypes
Checks for mixed regexp capture types.

### Lint/MultipleComparison
Checks for multiple comparison.

### Lint/NestedMethodDefinition
Checks for nested method definitions.

### Lint/NestedPercentLiteral
Checks for nested percent literals.

### Lint/NextWithoutAccumulator
Checks for next without accumulator.

### Lint/NoReturnInBeginEndBlocks
Checks for no return in begin/end blocks.

### Lint/NonAtomicFileOperation
Checks for non-atomic file operations.

### Lint/NonDeterministicRequireOrder
Checks for non-deterministic require order.

### Lint/NonLocalExitFromIterator
Checks for non-local exit from iterator.

### Lint/NumberConversion
Checks for implicit number conversion.

### Lint/NumberedParameterAssignment
Checks for numbered parameter assignment.

### Lint/OrAssignmentToConstant
Checks for or-assignment to constant.

### Lint/OrderedMagicComments
Checks for ordered magic comments.

### Lint/OutOfRangeRegexpRef
Checks for out of range regexp reference.

### Lint/ParenthesesAsGroupedExpression
Checks for parentheses as grouped expression.

### Lint/PercentStringArray
Checks for percent string array issues.

### Lint/PercentSymbolArray
Checks for percent symbol array issues.

### Lint/RaiseException
Checks for raising Exception class.

```ruby
# Bad
raise Exception, 'message'

# Good
raise StandardError, 'message'
```

### Lint/RandOne
Checks for `rand(1)`.

### Lint/RedundantCopDisableDirective
Checks for redundant cop disable directive.

### Lint/RedundantCopEnableDirective
Checks for redundant cop enable directive.

### Lint/RedundantDirGlobSort
Checks for redundant Dir.glob sort.

### Lint/RedundantRegexpQuantifiers
Checks for redundant regexp quantifiers.

### Lint/RedundantRequireStatement
Checks for redundant require statement.

### Lint/RedundantSafeNavigation
Checks for redundant safe navigation.

### Lint/RedundantSplatExpansion
Checks for redundant splat expansion.

### Lint/RedundantStringCoercion
Checks for redundant string coercion.

### Lint/RedundantWithIndex
Checks for redundant with_index.

### Lint/RedundantWithObject
Checks for redundant with_object.

### Lint/RefinementImportMethods
Checks for refinement import methods.

### Lint/RegexpAsCondition
Checks for regexp as condition.

### Lint/RequireParentheses
Checks for require parentheses.

### Lint/RequireRangeParentheses
Checks for require range parentheses.

### Lint/RequireRelativeSelfPath
Checks for require_relative with self path.

### Lint/RescueException
Checks for rescuing Exception.

```ruby
# Bad
begin
rescue Exception => e
end

# Good
begin
rescue StandardError => e
end
```

### Lint/RescueType
Checks for rescue type.

### Lint/ReturnInVoidContext
Checks for return in void context.

### Lint/SafeNavigationChain
Checks for safe navigation chain issues.

### Lint/SafeNavigationConsistency
Checks for safe navigation consistency.

### Lint/SafeNavigationWithEmpty
Checks for safe navigation with empty.

### Lint/ScriptPermission
Checks for script permission.

### Lint/SelfAssignment
Checks for self assignment.

### Lint/SendWithMixinArgument
Checks for send with mixin argument.

### Lint/ShadowedArgument
Checks for shadowed arguments.

### Lint/ShadowedException
Checks for shadowed exceptions.

### Lint/ShadowingOuterLocalVariable
Checks for shadowing outer local variables.

### Lint/SharedIteratorVariable
Checks for shared iterator variables.

### Lint/StructNewOverride
Checks for Struct.new override.

### Lint/SuppressedException
Checks for suppressed exceptions.

```ruby
# Bad
begin
  do_something
rescue
end  # Exception silently swallowed
```

### Lint/SymbolConversion
Checks for symbol conversion.

### Lint/Syntax
Checks for syntax errors.

### Lint/ToEnumArguments
Checks for to_enum arguments.

### Lint/ToJSON
Checks for to_json implementation.

### Lint/TopLevelReturnWithArgument
Checks for top-level return with argument.

### Lint/TrailingCommaInAttributeDeclaration
Checks for trailing comma in attribute declaration.

### Lint/TripleQuotes
Checks for triple quotes.

### Lint/UnderscorePrefixedVariableName
Checks for underscore-prefixed variable names.

### Lint/UnexpectedBlockArity
Checks for unexpected block arity.

### Lint/UnifiedInteger
Checks for Fixnum/Bignum usage.

### Lint/UnmodifiedReduceAccumulator
Checks for unmodified reduce accumulator.

### Lint/UnreachableCode
Checks for unreachable code.

```ruby
# Bad
def foo
  return
  bar  # Never executed
end
```

### Lint/UnreachableLoop
Checks for unreachable loop.

### Lint/UnusedBlockArgument
Checks for unused block arguments.

### Lint/UnusedMethodArgument
Checks for unused method arguments.

### Lint/UriEscapeUnescape
Checks for deprecated URI methods.

### Lint/UriRegexp
Checks for URI.regexp.

### Lint/UselessAccessModifier
Checks for useless access modifiers.

### Lint/UselessAssignment
Checks for useless assignments.

```ruby
# Bad
def foo
  x = 1  # x is never used
end
```

### Lint/UselessElseWithoutRescue
Checks for useless else without rescue.

### Lint/UselessMethodDefinition
Checks for useless method definitions.

### Lint/UselessNumericOperation
Checks for useless numeric operations.

### Lint/UselessRescue
Checks for useless rescue.

### Lint/UselessRuby2Keywords
Checks for useless ruby2_keywords.

### Lint/UselessSetterCall
Checks for useless setter calls.

### Lint/UselessTimes
Checks for useless times.

### Lint/Void
Checks for void context operations.
