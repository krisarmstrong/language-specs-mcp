# RuboCop Metrics Cops

Metrics cops measure code complexity and size.

Source: https://docs.rubocop.org/rubocop/cops_metrics.html

### Metrics/AbcSize
Checks ABC (Assignment, Branch, Condition) size of methods.

```yaml
Metrics/AbcSize:
  Max: 17
```

### Metrics/BlockLength
Checks block length.

```yaml
Metrics/BlockLength:
  Max: 25
  AllowedMethods: ['describe', 'context', 'it']
```

### Metrics/BlockNesting
Checks block nesting depth.

```yaml
Metrics/BlockNesting:
  Max: 3
```

### Metrics/ClassLength
Checks class length.

```yaml
Metrics/ClassLength:
  Max: 100
  CountComments: false
```

### Metrics/CollectionLiteralLength
Checks collection literal length.

### Metrics/CyclomaticComplexity
Checks cyclomatic complexity.

```yaml
Metrics/CyclomaticComplexity:
  Max: 7
```

### Metrics/MethodLength
Checks method length.

```yaml
Metrics/MethodLength:
  Max: 10
  CountComments: false
```

### Metrics/ModuleLength
Checks module length.

### Metrics/ParameterLists
Checks parameter list length.

```yaml
Metrics/ParameterLists:
  Max: 5
  CountKeywordArgs: true
```

### Metrics/PerceivedComplexity
Checks perceived complexity.

```yaml
Metrics/PerceivedComplexity:
  Max: 8
```
