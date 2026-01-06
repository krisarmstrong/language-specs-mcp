Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [test_types_in_equals](/tools/linter-rules/test_types_in_equals)

# test_types_in_equals

Learn about the test_types_in_equals linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/test_types_in_equals)

verified_userStable

Test type of argument in `operator ==(Object other)`.

## Details

[#](#details)

DO test type of argument in `operator ==(Object other)`.

 Not testing the type might result in runtime type errors which will be unexpected for consumers of your class. 

BAD:

dart

```
class Field {
}
​
class Bad {
  final Field someField;
​
  Bad(this.someField);
​
  @override
  bool operator ==(Object other) {
    Bad otherBad = other as Bad; // LINT
    bool areEqual = otherBad != null && otherBad.someField == someField;
    return areEqual;
  }
​
  @override
  int get hashCode {
    return someField.hashCode;
  }
}
```

content_copy

GOOD:

dart

```
class Field {
}
​
class Good {
  final Field someField;
​
  Good(this.someField);
​
  @override
  bool operator ==(Object other) {
    if (identical(this, other)) {
      return true;
    }
    return other is Good &&
        this.someField == other.someField;
  }
​
  @override
  int get hashCode {
    return someField.hashCode;
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `test_types_in_equals` rule, add `test_types_in_equals` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - test_types_in_equals
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `test_types_in_equals: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    test_types_in_equals: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/test_types_in_equals).
