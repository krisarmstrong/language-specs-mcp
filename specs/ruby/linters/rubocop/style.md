# RuboCop Style Cops

Style cops enforce consistent code style conventions.

Source: https://docs.rubocop.org/rubocop/cops_style.html

## Method & Class Definition

### Style/AccessModifierDeclarations
Checks style of access modifier declarations (inline vs group).

```ruby
# Bad (with EnforcedStyle: group)
class Foo
  private def bar; end
end

# Good
class Foo
  private

  def bar; end
end
```

### Style/AccessorGrouping
Checks for grouping of accessors in class/module bodies.

### Style/Alias
Enforces use of `alias` vs `alias_method`.

### Style/AndOr
Checks for uses of `and`/`or` vs `&&`/`||`.

```ruby
# Bad
if foo and bar
end

# Good
if foo && bar
end
```

### Style/ArgumentsForwarding
Identifies places where `...` argument forwarding should be used.

### Style/ArrayCoercion
Enforces use of `Array()` over `[*var]` or explicit conditionals.

### Style/ArrayFirstLast
Prefers `first`/`last` over `[0]`/`[-1]`.

### Style/ArrayIntersect
Prefers `intersect?` over `(a & b).any?`.

### Style/ArrayJoin
Checks for uses of `*` on arrays to join.

### Style/AsciiComments
Checks for non-ASCII characters in comments.

### Style/Attr
Checks for uses of `Module#attr`.

### Style/AutoResourceCleanup
Suggests using block forms of resource methods.

### Style/BarePercentLiterals
Checks if `%()` or `%Q()` is used for strings.

### Style/BeginBlock
Checks for BEGIN blocks.

### Style/BisectedAttrAccessor
Identifies bisected attr_accessor declarations.

### Style/BlockComments
Checks for block comments (`=begin`/`=end`).

### Style/BlockDelimiters
Checks for braces vs do/end around blocks.

```ruby
# EnforcedStyle: line_count_based
# Multi-line blocks use do/end
items.each do |item|
  process(item)
end

# Single-line blocks use braces
items.each { |item| process(item) }
```

### Style/CaseEquality
Checks for uses of `===`.

### Style/CaseLikeIf
Identifies places where if/elsif chains can be case statements.

### Style/CharacterLiteral
Checks for uses of character literals like `?x`.

### Style/ClassAndModuleChildren
Checks style of children definitions in classes/modules.

### Style/ClassCheck
Enforces consistent use of `is_a?` vs `kind_of?`.

### Style/ClassEqualityComparison
Checks for direct comparison against Class objects.

### Style/ClassMethods
Checks for uses of `self.method_name` in class method definitions.

### Style/ClassMethodsDefinitions
Enforces using `def self.method` vs `class << self`.

### Style/ClassVars
Checks for class variables (`@@var`).

### Style/CollectionCompact
Prefers `compact` over `reject(&:nil?)`.

### Style/CollectionMethods
Enforces preferred collection method names.

### Style/ColonMethodCall
Checks for `::` method calls.

### Style/ColonMethodDefinition
Checks for colon method definitions.

### Style/CombinableLoops
Checks for loops that can be combined.

### Style/CommandLiteral
Checks for consistent command literal style.

### Style/CommentAnnotation
Checks comment annotation format (TODO, FIXME, etc.).

### Style/CommentedKeyword
Checks for comments after keywords.

### Style/ComparableClamp
Prefers `Comparable#clamp` over manual min/max.

### Style/ConcatArrayLiterals
Checks for array concatenation with literals.

### Style/ConditionalAssignment
Checks for conditionals that could use conditional assignment.

```ruby
# Bad
if foo
  bar = 1
else
  bar = 2
end

# Good
bar = foo ? 1 : 2
```

### Style/ConstantVisibility
Checks that constants have visibility declarations.

### Style/Copyright
Checks for copyright notices.

### Style/DataInheritance
Checks for classes inheriting from Data.define.

### Style/DateTime
Checks for uses of DateTime vs Time.

### Style/DefWithParentheses
Checks for parentheses in method definitions.

### Style/Dir
Checks for uses of `Dir[__dir__]` patterns.

### Style/DirEmpty
Prefers `Dir.empty?` over `Dir.children.empty?`.

### Style/DisableCopsWithinSourceCodeDirective
Detects inline disabling of cops.

### Style/DocumentDynamicEvalDefinition
Checks for dynamic eval definitions without documentation.

### Style/Documentation
Checks for missing class/module documentation.

### Style/DocumentationMethod
Checks for missing method documentation.

### Style/DoubleCopDisableDirective
Checks for double cop disable directives.

### Style/DoubleNegation
Checks for uses of `!!`.

### Style/EachForSimpleLoop
Checks for simple loops using `.each`.

### Style/EachWithObject
Checks for uses of `each_with_object`.

### Style/EmptyBlockParameter
Checks for empty block parameters.

### Style/EmptyCaseCondition
Checks for empty case conditions.

### Style/EmptyElse
Checks for empty else clauses.

### Style/EmptyHeredoc
Checks for empty heredocs.

### Style/EmptyLambdaParameter
Checks for empty lambda parameters.

### Style/EmptyLiteral
Checks for empty literal constructors.

### Style/EmptyMethod
Checks for empty method definitions.

### Style/Encoding
Checks for encoding magic comments.

### Style/EndBlock
Checks for END blocks.

### Style/EndlessMethod
Checks for endless method definitions (Ruby 3.0+).

```ruby
# Good (with EnforcedStyle: allow_always)
def greeting = "Hello"
```

### Style/EnvHome
Prefers `Dir.home` over `ENV['HOME']`.

### Style/EvalWithLocation
Checks that eval passes file and line.

### Style/EvenOdd
Checks for uses of `% 2` vs `.even?`/`.odd?`.

### Style/ExactRegexpMatch
Prefers `==` over `=~` with anchored regex.

### Style/ExpandPathArguments
Checks for `File.expand_path` arguments.

### Style/ExplicitBlockArgument
Checks for explicit block arguments.

### Style/ExponentialNotation
Checks for consistent exponential notation.

### Style/FetchEnvVar
Prefers `ENV.fetch` over `ENV[]`.

### Style/FileEmpty
Prefers `File.empty?` over size comparison.

### Style/FileRead
Prefers `File.read` over `File.open` with read.

### Style/FileWrite
Prefers `File.write` over `File.open` with write.

### Style/FloatDivision
Checks for integer division that should be float.

### Style/For
Checks for uses of `for` vs `each`.

### Style/FormatString
Checks for format string style.

### Style/FormatStringToken
Checks for consistent format string tokens.

### Style/FrozenStringLiteralComment
Checks for `# frozen_string_literal` comment.

```ruby
# frozen_string_literal: true

class Foo
end
```

### Style/GlobalStdStream
Checks for `$stdout`/`$stderr`/`$stdin`.

### Style/GlobalVars
Checks for global variables.

### Style/GuardClause
Checks for guard clause style.

```ruby
# Bad
def foo
  if bar
    # ...
  end
end

# Good
def foo
  return unless bar
  # ...
end
```

### Style/HashAsLastArrayItem
Checks for hash as last array item.

### Style/HashConversion
Checks for hash conversion patterns.

### Style/HashEachMethods
Checks for `Hash#keys.each`/`Hash#values.each`.

### Style/HashExcept
Prefers `Hash#except` over reject.

### Style/HashLikeCase
Checks for hash-like case statements.

### Style/HashSlice
Prefers `Hash#slice` over select with keys.

### Style/HashSyntax
Checks hash literal syntax.

```ruby
# EnforcedStyle: ruby19
{ a: 1, b: 2 }

# EnforcedStyle: hash_rockets
{ :a => 1, :b => 2 }
```

### Style/HashTransformKeys
Prefers `transform_keys` over `each_with_object`.

### Style/HashTransformValues
Prefers `transform_values` over `each_with_object`.

### Style/IdenticalConditionalBranches
Checks for identical conditional branches.

### Style/IfInsideElse
Checks for if inside else.

### Style/IfUnlessModifier
Checks for if/unless modifier style.

### Style/IfUnlessModifierOfIfUnless
Checks for nested if/unless modifiers.

### Style/IfWithBooleanLiteralBranches
Checks for if with boolean literal branches.

### Style/IfWithSemicolon
Checks for if with semicolon.

### Style/ImplicitRuntimeError
Checks for implicit RuntimeError.

### Style/InPatternThen
Checks for `in` pattern with `then`.

### Style/InfiniteLoop
Checks for infinite loop style.

### Style/InlineComment
Checks for inline comments.

### Style/InverseMethods
Checks for inverse method usage.

### Style/InvertibleUnlessCondition
Checks for unless with invertible condition.

### Style/IpAddresses
Checks for hardcoded IP addresses.

### Style/KeywordParametersOrder
Checks keyword parameter ordering.

### Style/Lambda
Checks for lambda style.

### Style/LambdaCall
Checks for lambda call style.

### Style/LineEndConcatenation
Checks for line end concatenation.

### Style/MagicCommentFormat
Checks for magic comment format.

### Style/MapCompactWithConditionalBlock
Checks for map with compact and conditional.

### Style/MapIntoArray
Checks for map into array pattern.

### Style/MapToHash
Checks for map to hash pattern.

### Style/MapToSet
Checks for map to set pattern.

### Style/MethodCallWithArgsParentheses
Checks for method call parentheses.

### Style/MethodCallWithoutArgsParentheses
Checks for empty parentheses in method calls.

### Style/MethodCalledOnDoEndBlock
Checks for method called on do/end block.

### Style/MethodDefParentheses
Checks for method def parentheses.

### Style/MinMax
Prefers `minmax` over separate calls.

### Style/MinMaxComparison
Prefers `clamp` over min/max comparison.

### Style/MissingElse
Checks for missing else in case/if.

### Style/MissingRespondToMissing
Checks for `method_missing` without `respond_to_missing?`.

### Style/MixinGrouping
Checks for mixin grouping.

### Style/MixinUsage
Checks for mixin usage at top level.

### Style/ModuleFunction
Checks for `module_function` vs `extend self`.

### Style/MultilineBlockChain
Checks for multiline block chains.

### Style/MultilineIfModifier
Checks for multiline if modifiers.

### Style/MultilineIfThen
Checks for multiline if with then.

### Style/MultilineInPatternThen
Checks for multiline in pattern with then.

### Style/MultilineMemoization
Checks for multiline memoization.

### Style/MultilineMethodSignature
Checks for multiline method signatures.

### Style/MultilineTernaryOperator
Checks for multiline ternary operators.

### Style/MultilineWhenThen
Checks for multiline when with then.

### Style/MultipleComparison
Checks for multiple comparisons.

### Style/MutableConstant
Checks for mutable constants.

```ruby
# Bad
ARRAY = []

# Good
ARRAY = [].freeze
```

### Style/NegatedIf
Checks for negated if.

### Style/NegatedIfElseCondition
Checks for negated if/else condition.

### Style/NegatedUnless
Checks for negated unless.

### Style/NegatedWhile
Checks for negated while.

### Style/NestedFileDirname
Checks for nested File.dirname.

### Style/NestedModifier
Checks for nested modifiers.

### Style/NestedParenthesizedCalls
Checks for nested parenthesized calls.

### Style/NestedTernaryOperator
Checks for nested ternary operators.

### Style/Next
Checks for next vs if in loops.

### Style/NilComparison
Checks for nil comparison style.

### Style/NilLambda
Checks for nil lambda.

### Style/NonNilCheck
Checks for non-nil check style.

### Style/Not
Checks for `not` vs `!`.

### Style/NumberedParameters
Checks for numbered parameters style.

### Style/NumberedParametersLimit
Checks numbered parameters limit.

### Style/NumericLiteralPrefix
Checks numeric literal prefix style.

### Style/NumericLiterals
Checks for underscores in numeric literals.

### Style/NumericPredicate
Checks for numeric predicate style.

### Style/ObjectThen
Checks for `Object#then` usage.

### Style/OneLineConditional
Checks for one-line conditionals.

### Style/OpenStructUse
Checks for OpenStruct usage.

### Style/OperatorMethodCall
Checks for operator method call style.

### Style/OptionHash
Checks for option hash pattern.

### Style/OptionalArguments
Checks for optional arguments ordering.

### Style/OptionalBooleanParameter
Checks for optional boolean parameters.

### Style/OrAssignment
Checks for or-assignment style.

### Style/ParallelAssignment
Checks for parallel assignment.

### Style/ParenthesesAroundCondition
Checks for parentheses around conditions.

### Style/PercentLiteralDelimiters
Checks percent literal delimiters.

### Style/PercentQLiterals
Checks percent Q literal style.

### Style/PerlBackrefs
Checks for Perl-style backrefs.

### Style/PreferredHashMethods
Checks for preferred hash methods.

### Style/Proc
Checks for `Proc.new` vs `proc`.

### Style/QuotedSymbols
Checks quoted symbol style.

### Style/RaiseArgs
Checks raise argument style.

### Style/RandomWithOffset
Checks for random with offset.

### Style/RedundantArgument
Checks for redundant arguments.

### Style/RedundantArrayConstructor
Checks for redundant Array constructor.

### Style/RedundantAssignment
Checks for redundant assignment.

### Style/RedundantBegin
Checks for redundant begin.

### Style/RedundantCapitalW
Checks for redundant %W.

### Style/RedundantCondition
Checks for redundant conditions.

### Style/RedundantConditional
Checks for redundant conditionals.

### Style/RedundantConstantBase
Checks for redundant constant base.

### Style/RedundantCurrentDirectoryInPath
Checks for redundant `./` in path.

### Style/RedundantDoubleSplatHashBraces
Checks for redundant double splat braces.

### Style/RedundantEach
Checks for redundant each.

### Style/RedundantException
Checks for redundant exception.

### Style/RedundantFetchBlock
Checks for redundant fetch block.

### Style/RedundantFileExtensionInRequire
Checks for redundant file extension in require.

### Style/RedundantFilterChain
Checks for redundant filter chain.

### Style/RedundantFreeze
Checks for redundant freeze.

### Style/RedundantHeredocDelimiterQuotes
Checks for redundant heredoc delimiter quotes.

### Style/RedundantInitialize
Checks for redundant initialize.

### Style/RedundantInterpolation
Checks for redundant string interpolation.

### Style/RedundantLineContinuation
Checks for redundant line continuation.

### Style/RedundantParentheses
Checks for redundant parentheses.

### Style/RedundantPercentQ
Checks for redundant %q/%Q.

### Style/RedundantRegexpArgument
Checks for redundant regexp argument.

### Style/RedundantRegexpCharacterClass
Checks for redundant regexp character class.

### Style/RedundantRegexpConstructor
Checks for redundant Regexp constructor.

### Style/RedundantRegexpEscape
Checks for redundant regexp escape.

### Style/RedundantReturn
Checks for redundant return.

```ruby
# Bad
def foo
  return bar
end

# Good
def foo
  bar
end
```

### Style/RedundantSelf
Checks for redundant self.

### Style/RedundantSelfAssignment
Checks for redundant self assignment.

### Style/RedundantSelfAssignmentBranch
Checks for redundant self assignment branch.

### Style/RedundantSort
Checks for redundant sort.

### Style/RedundantSortBy
Checks for redundant sort_by.

### Style/RedundantStringEscape
Checks for redundant string escape.

### Style/RegexpLiteral
Checks regexp literal style.

### Style/RequireOrder
Checks require ordering.

### Style/RescueModifier
Checks for rescue modifier.

### Style/RescueStandardError
Checks for rescue StandardError.

### Style/ReturnNil
Checks for explicit return nil.

### Style/ReturnNilInPredicateMethodDefinition
Checks for return nil in predicate methods.

### Style/SafeNavigation
Checks for safe navigation operator usage.

### Style/Sample
Checks for sample usage.

### Style/SelectByRegexp
Checks for select by regexp.

### Style/SelfAssignment
Checks for self assignment style.

### Style/Semicolon
Checks for semicolons.

### Style/Send
Checks for send usage.

### Style/SignalException
Checks signal exception style.

### Style/SingleArgumentDig
Checks for single argument dig.

### Style/SingleLineBlockParams
Checks single line block params.

### Style/SingleLineMethods
Checks for single line methods.

### Style/SlicingWithRange
Checks for slicing with range.

### Style/SoleNestedConditional
Checks for sole nested conditional.

### Style/SpecialGlobalVars
Checks for special global vars style.

### Style/StabbyLambdaParentheses
Checks stabby lambda parentheses.

### Style/StaticClass
Checks for static classes.

### Style/StderrPuts
Checks for stderr puts.

### Style/StringChars
Checks string chars usage.

### Style/StringConcatenation
Checks string concatenation.

### Style/StringHashKeys
Checks for string hash keys.

### Style/StringLiterals
Checks string literal style.

### Style/StringLiteralsInInterpolation
Checks string literals in interpolation.

### Style/StringMethods
Checks string method style.

### Style/Strip
Checks for strip usage.

### Style/StructInheritance
Checks for struct inheritance.

### Style/SuperArguments
Checks super arguments.

### Style/SuperWithArgsParentheses
Checks super with args parentheses.

### Style/SwapValues
Checks for swap values pattern.

### Style/SymbolArray
Checks symbol array style.

### Style/SymbolLiteral
Checks symbol literal style.

### Style/SymbolProc
Checks for symbol proc.

```ruby
# Bad
items.map { |item| item.name }

# Good
items.map(&:name)
```

### Style/TernaryParentheses
Checks ternary parentheses.

### Style/TopLevelMethodDefinition
Checks for top level method definitions.

### Style/TrailingBodyOnClass
Checks for trailing body on class.

### Style/TrailingBodyOnMethodDefinition
Checks for trailing body on method definition.

### Style/TrailingBodyOnModule
Checks for trailing body on module.

### Style/TrailingCommaInArguments
Checks trailing comma in arguments.

### Style/TrailingCommaInArrayLiteral
Checks trailing comma in array literal.

### Style/TrailingCommaInBlockArgs
Checks trailing comma in block args.

### Style/TrailingCommaInHashLiteral
Checks trailing comma in hash literal.

### Style/TrailingMethodEndStatement
Checks trailing method end statement.

### Style/TrailingUnderscoreVariable
Checks trailing underscore variable.

### Style/TrivialAccessors
Checks for trivial accessors.

### Style/UnlessElse
Checks for unless with else.

### Style/UnlessLogicalOperators
Checks unless with logical operators.

### Style/UnpackFirst
Checks for unpack first.

### Style/VariableInterpolation
Checks variable interpolation style.

### Style/WhenThen
Checks when with then.

### Style/WhileUntilDo
Checks while/until with do.

### Style/WhileUntilModifier
Checks while/until modifier style.

### Style/WordArray
Checks word array style.

### Style/YAMLFileRead
Checks YAML file read.

### Style/YodaCondition
Checks for Yoda conditions.

### Style/YodaExpression
Checks for Yoda expressions.

### Style/ZeroLengthPredicate
Checks for zero length predicate.
