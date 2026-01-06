Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [no_duplicate_case_values](/tools/linter-rules/no_duplicate_case_values)

# no_duplicate_case_values

Learn about the no_duplicate_case_values linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_duplicate_case_values)

verified_userStablecirclesCorebuildFix available

Don't use more than one case with same value.

## Details

[#](#details)

DON'T use more than one case with same value.

This is usually a typo or changed value of constant.

BAD:

dart

```
const int A = 1;
switch (v) {
  case 1:
  case 2:
  case A:
  case 2:
}
```

content_copy

GOOD:

dart

```
const int A = 1;
switch (v) {
  case A:
  case 2:
}
```

content_copy

 NOTE: this lint only reports duplicate cases in libraries opted in to Dart 2.19 and below. In Dart 3.0 and after, duplicate cases are reported as dead code by the analyzer. 

## Enable

[#](#enable)

 To enable the `no_duplicate_case_values` rule, add `no_duplicate_case_values` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - no_duplicate_case_values
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `no_duplicate_case_values: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    no_duplicate_case_values: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_duplicate_case_values).
