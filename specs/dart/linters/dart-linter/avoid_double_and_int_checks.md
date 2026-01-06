Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_double_and_int_checks](/tools/linter-rules/avoid_double_and_int_checks)

# avoid_double_and_int_checks

Learn about the avoid_double_and_int_checks linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_double_and_int_checks)

verified_userStable

Avoid `double` and `int` checks.

## Details

[#](#details)

AVOID to check if type is `double` or `int`.

 When compiled to JS, integer values are represented as floats. That can lead to some unexpected behavior when using either `is` or `is!` where the type is either `int` or `double`. 

BAD:

dart

```
f(num x) {
  if (x is double) {
    ...
  } else if (x is int) {
    ...
  }
}
```

content_copy

GOOD:

dart

```
f(dynamic x) {
  if (x is num) {
    ...
  } else {
    ...
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_double_and_int_checks` rule, add `avoid_double_and_int_checks` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_double_and_int_checks
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_double_and_int_checks: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_double_and_int_checks: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_double_and_int_checks).
