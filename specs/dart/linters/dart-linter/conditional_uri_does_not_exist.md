Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [conditional_uri_does_not_exist](/tools/linter-rules/conditional_uri_does_not_exist)

# conditional_uri_does_not_exist

Learn about the conditional_uri_does_not_exist linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/conditional_uri_does_not_exist)

verified_userStable

Missing conditional import.

## Details

[#](#details)

DON'T reference files that do not exist in conditional imports.

 Code may fail at runtime if the condition evaluates such that the missing file needs to be imported. 

BAD:

dart

```
import 'file_that_does_exist.dart'
  if (condition) 'file_that_does_not_exist.dart';
```

content_copy

GOOD:

dart

```
import 'file_that_does_exist.dart'
  if (condition) 'file_that_also_does_exist.dart';
```

content_copy

## Enable

[#](#enable)

 To enable the `conditional_uri_does_not_exist` rule, add `conditional_uri_does_not_exist` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - conditional_uri_does_not_exist
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `conditional_uri_does_not_exist: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    conditional_uri_does_not_exist: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/conditional_uri_does_not_exist).
