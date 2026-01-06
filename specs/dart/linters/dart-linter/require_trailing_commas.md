Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [require_trailing_commas](/tools/linter-rules/require_trailing_commas)

# require_trailing_commas

Learn about the require_trailing_commas linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/require_trailing_commas)

verified_userStablebuildFix available

Use trailing commas for all parameter lists and argument lists.

## Details

[#](#details)

DO use trailing commas for all multi-line parameter lists and argument lists. A parameter list or argument list that fits on one line, including the opening parenthesis and closing parenthesis, does not require a trailing comma. 

BAD:

dart

```
void run() {
  method('does not fit on one line',
      'test test test test test test test test test test test');
}
```

content_copy

GOOD:

dart

```
void run() {
  method(
    'does not fit on one line',
    'test test test test test test test test test test test',
  );
}
```

content_copy

EXCEPTION: If the final argument in an argument list is positional (vs named) and is either a function literal with curly braces, a map literal, a set literal, or a list literal, then a trailing comma is not required. This exception only applies if the final argument does not fit entirely on one line. 

NOTE: This lint rule assumes that code has been formatted with `dart format` and may produce false positives on unformatted code. 

## Enable

[#](#enable)

 To enable the `require_trailing_commas` rule, add `require_trailing_commas` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - require_trailing_commas
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `require_trailing_commas: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    require_trailing_commas: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/require_trailing_commas).
