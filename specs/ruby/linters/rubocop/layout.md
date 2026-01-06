# RuboCop Layout Cops

Layout cops enforce consistent code formatting and whitespace.

Source: https://docs.rubocop.org/rubocop/cops_layout.html

## Indentation

### Layout/AccessModifierIndentation
Checks indentation of access modifiers (public, private, protected).

### Layout/ArgumentAlignment
Checks alignment of arguments in multi-line method calls.

### Layout/ArrayAlignment
Checks alignment of array elements.

### Layout/AssignmentIndentation
Checks indentation of assignment right-hand side.

### Layout/BlockAlignment
Checks alignment of block end with expression starting the block.

### Layout/BlockEndNewline
Checks for newline after block end.

### Layout/CaseIndentation
Checks indentation of when in case statements.

### Layout/ClassStructure
Enforces consistent class structure ordering.

### Layout/ClosingHeredocIndentation
Checks heredoc closing delimiter indentation.

### Layout/ClosingParenthesisIndentation
Checks closing parenthesis indentation.

### Layout/CommentIndentation
Checks comment indentation.

### Layout/ConditionPosition
Checks condition position for if/while/until.

### Layout/DefEndAlignment
Checks alignment of def and end keywords.

### Layout/DotPosition
Checks dot position in multi-line method chains.

```ruby
# EnforcedStyle: leading
foo
  .bar
  .baz

# EnforcedStyle: trailing
foo.
  bar.
  baz
```

### Layout/ElseAlignment
Checks alignment of else keyword.

### Layout/EmptyComment
Checks for empty comments.

### Layout/EmptyLineAfterGuardClause
Checks for empty line after guard clause.

### Layout/EmptyLineAfterMagicComment
Checks for empty line after magic comment.

### Layout/EmptyLineAfterMultilineCondition
Checks for empty line after multiline condition.

### Layout/EmptyLineBetweenDefs
Checks for empty line between method definitions.

### Layout/EmptyLines
Checks for multiple consecutive empty lines.

### Layout/EmptyLinesAroundAccessModifier
Checks for empty lines around access modifiers.

### Layout/EmptyLinesAroundArguments
Checks for empty lines around arguments.

### Layout/EmptyLinesAroundAttributeAccessor
Checks for empty lines around attribute accessors.

### Layout/EmptyLinesAroundBeginBody
Checks for empty lines around begin body.

### Layout/EmptyLinesAroundBlockBody
Checks for empty lines around block body.

### Layout/EmptyLinesAroundClassBody
Checks for empty lines around class body.

### Layout/EmptyLinesAroundExceptionHandlingKeywords
Checks for empty lines around exception handling keywords.

### Layout/EmptyLinesAroundMethodBody
Checks for empty lines around method body.

### Layout/EmptyLinesAroundModuleBody
Checks for empty lines around module body.

### Layout/EndAlignment
Checks alignment of end keyword.

### Layout/EndOfLine
Checks for consistent line endings.

### Layout/ExtraSpacing
Checks for extra spacing.

### Layout/FirstArgumentIndentation
Checks indentation of first argument.

### Layout/FirstArrayElementIndentation
Checks indentation of first array element.

### Layout/FirstArrayElementLineBreak
Checks for line break after first array element.

### Layout/FirstHashElementIndentation
Checks indentation of first hash element.

### Layout/FirstHashElementLineBreak
Checks for line break after first hash element.

### Layout/FirstMethodArgumentLineBreak
Checks for line break after first method argument.

### Layout/FirstMethodParameterLineBreak
Checks for line break after first method parameter.

### Layout/FirstParameterIndentation
Checks indentation of first parameter.

### Layout/HashAlignment
Checks alignment of hash elements.

### Layout/HeredocArgumentClosingParenthesis
Checks heredoc argument closing parenthesis position.

### Layout/HeredocIndentation
Checks heredoc indentation.

### Layout/IndentationConsistency
Checks for consistent indentation style.

### Layout/IndentationStyle
Checks for tabs vs spaces.

### Layout/IndentationWidth
Checks indentation width.

### Layout/InitialIndentation
Checks initial indentation.

### Layout/LeadingCommentSpace
Checks for space after `#` in comments.

### Layout/LeadingEmptyLines
Checks for leading empty lines.

### Layout/LineContinuationLeadingSpace
Checks leading space in line continuation.

### Layout/LineContinuationSpacing
Checks spacing in line continuation.

### Layout/LineEndStringConcatenationIndentation
Checks line end string concatenation indentation.

### Layout/LineLength
Checks line length.

```yaml
Layout/LineLength:
  Max: 120
  AllowedPatterns: ['^# ']
```

### Layout/MultilineArrayBraceLayout
Checks multiline array brace layout.

### Layout/MultilineArrayLineBreaks
Checks multiline array line breaks.

### Layout/MultilineAssignmentLayout
Checks multiline assignment layout.

### Layout/MultilineBlockLayout
Checks multiline block layout.

### Layout/MultilineHashBraceLayout
Checks multiline hash brace layout.

### Layout/MultilineHashKeyLineBreaks
Checks multiline hash key line breaks.

### Layout/MultilineMethodArgumentLineBreaks
Checks multiline method argument line breaks.

### Layout/MultilineMethodCallBraceLayout
Checks multiline method call brace layout.

### Layout/MultilineMethodCallIndentation
Checks multiline method call indentation.

### Layout/MultilineMethodDefinitionBraceLayout
Checks multiline method definition brace layout.

### Layout/MultilineMethodParameterLineBreaks
Checks multiline method parameter line breaks.

### Layout/MultilineOperationIndentation
Checks multiline operation indentation.

### Layout/ParameterAlignment
Checks parameter alignment.

### Layout/RedundantLineBreak
Checks for redundant line breaks.

### Layout/RescueEnsureAlignment
Checks rescue/ensure alignment.

### Layout/SingleLineBlockChain
Checks single line block chain.

### Layout/SpaceAfterColon
Checks space after colon.

### Layout/SpaceAfterComma
Checks space after comma.

### Layout/SpaceAfterMethodName
Checks space after method name.

### Layout/SpaceAfterNot
Checks space after not.

### Layout/SpaceAfterSemicolon
Checks space after semicolon.

### Layout/SpaceAroundBlockParameters
Checks space around block parameters.

### Layout/SpaceAroundEqualsInParameterDefault
Checks space around equals in parameter default.

### Layout/SpaceAroundKeyword
Checks space around keywords.

### Layout/SpaceAroundMethodCallOperator
Checks space around method call operator.

### Layout/SpaceAroundOperators
Checks space around operators.

### Layout/SpaceBeforeBlockBraces
Checks space before block braces.

### Layout/SpaceBeforeBrackets
Checks space before brackets.

### Layout/SpaceBeforeComma
Checks space before comma.

### Layout/SpaceBeforeComment
Checks space before comment.

### Layout/SpaceBeforeFirstArg
Checks space before first argument.

### Layout/SpaceBeforeSemicolon
Checks space before semicolon.

### Layout/SpaceInLambdaLiteral
Checks space in lambda literal.

### Layout/SpaceInsideArrayLiteralBrackets
Checks space inside array literal brackets.

### Layout/SpaceInsideArrayPercentLiteral
Checks space inside array percent literal.

### Layout/SpaceInsideBlockBraces
Checks space inside block braces.

### Layout/SpaceInsideHashLiteralBraces
Checks space inside hash literal braces.

### Layout/SpaceInsideParens
Checks space inside parentheses.

### Layout/SpaceInsidePercentLiteralDelimiters
Checks space inside percent literal delimiters.

### Layout/SpaceInsideRangeLiteral
Checks space inside range literal.

### Layout/SpaceInsideReferenceBrackets
Checks space inside reference brackets.

### Layout/SpaceInsideStringInterpolation
Checks space inside string interpolation.

### Layout/TrailingEmptyLines
Checks for trailing empty lines.

### Layout/TrailingWhitespace
Checks for trailing whitespace.
