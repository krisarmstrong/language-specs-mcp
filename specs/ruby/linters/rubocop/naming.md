# RuboCop Naming Cops

Naming cops enforce consistent naming conventions.

Source: https://docs.rubocop.org/rubocop/cops_naming.html

### Naming/AccessorMethodName
Checks accessor method names (get_/set_ prefixes).

### Naming/AsciiIdentifiers
Checks for non-ASCII characters in identifiers.

### Naming/BinaryOperatorParameterName
Checks binary operator parameter naming (other).

### Naming/BlockForwarding
Checks for consistent block forwarding style.

### Naming/BlockParameterName
Checks block parameter naming.

```yaml
Naming/BlockParameterName:
  MinNameLength: 1
  AllowedNames: ['e', 'i', 'k', 'v', 'x', 'y']
```

### Naming/ClassAndModuleCamelCase
Enforces CamelCase for class/module names.

### Naming/ConstantName
Enforces SCREAMING_SNAKE_CASE for constants.

### Naming/FileName
Checks file naming conventions.

### Naming/HeredocDelimiterCase
Checks heredoc delimiter case.

### Naming/HeredocDelimiterNaming
Checks heredoc delimiter naming.

### Naming/InclusiveLanguage
Checks for non-inclusive language.

### Naming/MemoizedInstanceVariableName
Checks memoized instance variable naming.

### Naming/MethodName
Enforces snake_case for method names.

### Naming/MethodParameterName
Checks method parameter naming.

### Naming/PredicateName
Checks predicate method naming (is_/has_ prefixes).

### Naming/RescuedExceptionsVariableName
Checks rescued exception variable naming.

### Naming/VariableName
Enforces snake_case for variable names.

### Naming/VariableNumber
Checks variable number style (snake_case vs normalCase).
