Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_truncating_division](/tools/linter-rules/use_truncating_division)

# use_truncating_division

Learn about the use_truncating_division linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_truncating_division)

verified_userStablebuildFix available

Use truncating division.

## Details

[#](#details)

DO use truncating division, '~/', instead of regular division ('/') followed by 'toInt()'. 

 Dart features a "truncating division" operator which is the same operation as division followed by truncation, but which is more concise and expressive, and may be more performant on some platforms, for certain inputs. 

BAD:

dart

```
var x = (2 / 3).toInt();
```

content_copy

GOOD:

dart

```
var x = 2 ~/ 3;
```

content_copy

## Enable

[#](#enable)

 To enable the `use_truncating_division` rule, add `use_truncating_division` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_truncating_division
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_truncating_division: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_truncating_division: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_truncating_division).
