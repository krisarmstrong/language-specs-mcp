Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [no_literal_bool_comparisons](/tools/linter-rules/no_literal_bool_comparisons)

# no_literal_bool_comparisons

Learn about the no_literal_bool_comparisons linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_literal_bool_comparisons)

verified_userStablebuildFix available

Don't compare boolean expressions to boolean literals.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/usage#dont-use-true-or-false-in-equality-operations): 

DON'T use `true` or `false` in equality operations.

This lint applies only if the expression is of a non-nullable `bool` type.

BAD:

dart

```
if (someBool == true) {
  print('true!');
}
while (someBool == false) {
  print('still false!');
}
```

content_copy

GOOD:

dart

```
if (someBool) {
  print('true!');
}
while (!someBool) {
  print('still false!');
}
```

content_copy

## Enable

[#](#enable)

 To enable the `no_literal_bool_comparisons` rule, add `no_literal_bool_comparisons` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - no_literal_bool_comparisons
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `no_literal_bool_comparisons: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    no_literal_bool_comparisons: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_literal_bool_comparisons).
