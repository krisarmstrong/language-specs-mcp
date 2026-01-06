# Credo Checks Reference

Complete list of Credo checks for Elixir.

Source: https://hexdocs.pm/credo/

## Consistency Checks

### Credo.Check.Consistency.ExceptionNames
Ensures consistent exception naming (Error vs Exception suffix).

### Credo.Check.Consistency.LineEndings
Ensures consistent line endings (unix vs windows).

### Credo.Check.Consistency.MultiAliasImportRequireUse
Ensures consistent multi-alias syntax.

### Credo.Check.Consistency.ParameterPatternMatching
Ensures consistent parameter pattern matching style.

### Credo.Check.Consistency.SpaceAroundOperators
Ensures consistent spacing around operators.

### Credo.Check.Consistency.SpaceInParentheses
Ensures consistent spacing in parentheses.

### Credo.Check.Consistency.TabsOrSpaces
Ensures consistent use of tabs or spaces.

### Credo.Check.Consistency.UnusedVariableNames
Ensures consistent unused variable naming.

## Design Checks

### Credo.Check.Design.AliasUsage
Suggests using aliases for frequently used modules.

### Credo.Check.Design.DuplicatedCode
Detects duplicated code blocks.

### Credo.Check.Design.SkipTestWithoutComment
Ensures skipped tests have explanatory comments.

### Credo.Check.Design.TagFIXME
Warns about FIXME tags in comments.

### Credo.Check.Design.TagTODO
Warns about TODO tags in comments.

## Readability Checks

### Credo.Check.Readability.AliasAs
Suggests using :as option for clearer aliases.

### Credo.Check.Readability.AliasOrder
Ensures aliases are alphabetically ordered.

### Credo.Check.Readability.BlockPipe
Discourages piping into blocks.

### Credo.Check.Readability.FunctionNames
Ensures function names follow conventions.

### Credo.Check.Readability.ImplTrue
Warns about @impl true without specifying behavior.

### Credo.Check.Readability.LargeNumbers
Suggests underscores in large numbers.

### Credo.Check.Readability.MaxLineLength
Enforces maximum line length.

### Credo.Check.Readability.ModuleAttributeNames
Ensures module attribute naming conventions.

### Credo.Check.Readability.ModuleDoc
Ensures modules have documentation.

### Credo.Check.Readability.ModuleNames
Ensures module naming conventions.

### Credo.Check.Readability.MultiAlias
Suggests multi-alias syntax.

### Credo.Check.Readability.NestedFunctionCalls
Discourages deeply nested function calls.

### Credo.Check.Readability.OneArityFunctionInPipe
Ensures one-arity functions in pipes have parentheses.

### Credo.Check.Readability.OnePipePerLine
Ensures one pipe per line.

### Credo.Check.Readability.ParenthesesInCondition
Discourages parentheses in if/unless conditions.

### Credo.Check.Readability.ParenthesesOnZeroArityDefs
Ensures consistent parentheses on zero-arity functions.

### Credo.Check.Readability.PipeIntoAnonymousFunctions
Discourages piping into anonymous functions.

### Credo.Check.Readability.PredicateFunctionNames
Ensures predicate functions end with ?.

### Credo.Check.Readability.PreferImplicitTry
Suggests implicit try in function bodies.

### Credo.Check.Readability.PreferUnquotedAtoms
Prefers unquoted atoms when possible.

### Credo.Check.Readability.RedundantBlankLines
Removes redundant blank lines.

### Credo.Check.Readability.Semicolons
Discourages semicolons.

### Credo.Check.Readability.SeparateAliasRequire
Suggests separating alias and require.

### Credo.Check.Readability.SingleFunctionToBlockPipe
Discourages single function to block pipes.

### Credo.Check.Readability.SinglePipe
Discourages single pipe usage.

### Credo.Check.Readability.SpaceAfterCommas
Ensures space after commas.

### Credo.Check.Readability.Specs
Encourages typespecs for public functions.

### Credo.Check.Readability.StrictModuleLayout
Enforces strict module layout ordering.

### Credo.Check.Readability.StringSigils
Suggests sigils for strings with quotes.

### Credo.Check.Readability.TrailingBlankLine
Ensures trailing blank line.

### Credo.Check.Readability.TrailingWhiteSpace
Removes trailing whitespace.

### Credo.Check.Readability.UnnecessaryAliasExpansion
Removes unnecessary alias expansion.

### Credo.Check.Readability.VariableNames
Ensures variable naming conventions.

### Credo.Check.Readability.WithCustomTaggedTuple
Suggests custom tagged tuples over ok/error.

### Credo.Check.Readability.WithSingleClause
Discourages with with single clause.

## Refactor Checks

### Credo.Check.Refactor.ABCSize
Checks ABC (Assignment, Branch, Condition) complexity.

### Credo.Check.Refactor.AppendSingleItem
Suggests using ++ [item] alternatives.

### Credo.Check.Refactor.Apply
Suggests using apply for dynamic function calls.

### Credo.Check.Refactor.CaseTrivialMatches
Simplifies trivial case matches.

### Credo.Check.Refactor.CondStatements
Suggests cond over nested if statements.

### Credo.Check.Refactor.CyclomaticComplexity
Checks cyclomatic complexity.

### Credo.Check.Refactor.DoubleBooleanNegation
Removes double boolean negation.

### Credo.Check.Refactor.FilterCount
Suggests Enum.count/2 over filter then count.

### Credo.Check.Refactor.FilterFilter
Combines multiple filters.

### Credo.Check.Refactor.FilterReject
Simplifies filter/reject combinations.

### Credo.Check.Refactor.FunctionArity
Checks function arity limits.

### Credo.Check.Refactor.IoPuts
Warns about IO.puts for debugging.

### Credo.Check.Refactor.LongQuoteBlocks
Warns about long quote blocks.

### Credo.Check.Refactor.MapInto
Suggests Map.new over Enum.into.

### Credo.Check.Refactor.MapJoin
Suggests Enum.map_join.

### Credo.Check.Refactor.MapMap
Combines multiple maps.

### Credo.Check.Refactor.MatchInCondition
Avoids match in condition.

### Credo.Check.Refactor.ModuleDependencies
Checks module dependencies.

### Credo.Check.Refactor.NegatedConditionsInUnless
Simplifies negated unless conditions.

### Credo.Check.Refactor.NegatedConditionsWithElse
Simplifies negated if/else.

### Credo.Check.Refactor.NegatedIsNil
Suggests is_nil alternatives.

### Credo.Check.Refactor.Nesting
Checks nesting depth.

### Credo.Check.Refactor.PassAsyncInTestCases
Ensures async: true in test cases.

### Credo.Check.Refactor.PipeChainStart
Ensures proper pipe chain start.

### Credo.Check.Refactor.RedundantWithClauseResult
Removes redundant with clause results.

### Credo.Check.Refactor.RejectFilter
Simplifies reject/filter combinations.

### Credo.Check.Refactor.RejectReject
Combines multiple rejects.

### Credo.Check.Refactor.UnlessWithElse
Discourages unless with else.

### Credo.Check.Refactor.UtcNowTruncate
Suggests DateTime.utc_now with truncate option.

### Credo.Check.Refactor.VariableRebinding
Warns about variable rebinding.

### Credo.Check.Refactor.WithClauses
Simplifies with clauses.

## Warning Checks

### Credo.Check.Warning.ApplicationConfigInModuleAttribute
Warns about config in module attributes.

### Credo.Check.Warning.BoolOperationOnSameValues
Detects boolean operations on same values.

### Credo.Check.Warning.Dbg
Warns about dbg calls.

### Credo.Check.Warning.ExpensiveEmptyEnumCheck
Suggests efficient empty enum checks.

### Credo.Check.Warning.ForbiddenModule
Warns about forbidden module usage.

### Credo.Check.Warning.IExPry
Warns about IEx.pry calls.

### Credo.Check.Warning.IoInspect
Warns about IO.inspect calls.

### Credo.Check.Warning.LazyLogging
Suggests lazy logging.

### Credo.Check.Warning.LeakyEnvironment
Warns about leaky environment.

### Credo.Check.Warning.MapGetUnsafePass
Warns about unsafe Map.get patterns.

### Credo.Check.Warning.MissedMetadataKeyInLoggerConfig
Checks logger config metadata.

### Credo.Check.Warning.MixEnv
Warns about Mix.env at compile time.

### Credo.Check.Warning.OperationOnSameValues
Detects operations on same values.

### Credo.Check.Warning.OperationWithConstantResult
Detects operations with constant results.

### Credo.Check.Warning.RaiseInsideRescue
Warns about raise inside rescue.

### Credo.Check.Warning.SpecWithStruct
Warns about specs with structs.

### Credo.Check.Warning.UnsafeExec
Warns about unsafe command execution.

### Credo.Check.Warning.UnsafeToAtom
Warns about unsafe String.to_atom.

### Credo.Check.Warning.UnusedEnumOperation
Detects unused enum operations.

### Credo.Check.Warning.UnusedFileOperation
Detects unused file operations.

### Credo.Check.Warning.UnusedKeywordOperation
Detects unused keyword operations.

### Credo.Check.Warning.UnusedListOperation
Detects unused list operations.

### Credo.Check.Warning.UnusedPathOperation
Detects unused path operations.

### Credo.Check.Warning.UnusedRegexOperation
Detects unused regex operations.

### Credo.Check.Warning.UnusedStringOperation
Detects unused string operations.

### Credo.Check.Warning.UnusedTupleOperation
Detects unused tuple operations.

### Credo.Check.Warning.WrongTestFileExtension
Ensures correct test file extensions.
