Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_null_checks_in_equality_operators](/tools/linter-rules/avoid_null_checks_in_equality_operators)

# avoid_null_checks_in_equality_operators

Learn about the avoid_null_checks_in_equality_operators linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_null_checks_in_equality_operators)

reportDeprecatedbuildFix available

Don't check for `null` in custom `==` operators.

## Details

[#](#details)

NOTE: This lint has been replaced by the `non_nullable_equals_parameter` warning and is deprecated. Remove all inclusions of this lint from your analysis options. 

DON'T check for `null` in custom `==` operators.

 As `null` is a special value, no instance of any class (other than `Null`) can be equivalent to it. Thus, it is redundant to check whether the other instance is `null`. 

BAD:

dart

```
class Person {
  final String? name;
​
  @override
  operator ==(Object? other) =>
      other != null && other is Person && name == other.name;
}
```

content_copy

GOOD:

dart

```
class Person {
  final String? name;
​
  @override
  operator ==(Object? other) => other is Person && name == other.name;
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_null_checks_in_equality_operators` rule, add `avoid_null_checks_in_equality_operators` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_null_checks_in_equality_operators
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_null_checks_in_equality_operators: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_null_checks_in_equality_operators: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_null_checks_in_equality_operators).
