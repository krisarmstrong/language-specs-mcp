Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_multiple_declarations_per_line](/tools/linter-rules/avoid_multiple_declarations_per_line)

# avoid_multiple_declarations_per_line

Learn about the avoid_multiple_declarations_per_line linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_multiple_declarations_per_line)

verified_userStablebuildFix available

Don't declare multiple variables on a single line.

## Details

[#](#details)

DON'T declare multiple variables on a single line.

BAD:

dart

```
String? foo, bar, baz;
```

content_copy

GOOD:

dart

```
String? foo;
String? bar;
String? baz;
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_multiple_declarations_per_line` rule, add `avoid_multiple_declarations_per_line` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_multiple_declarations_per_line
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_multiple_declarations_per_line: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_multiple_declarations_per_line: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_multiple_declarations_per_line).
