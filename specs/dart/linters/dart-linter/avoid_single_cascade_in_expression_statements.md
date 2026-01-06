Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_single_cascade_in_expression_statements](/tools/linter-rules/avoid_single_cascade_in_expression_statements)

# avoid_single_cascade_in_expression_statements

Learn about the avoid_single_cascade_in_expression_statements linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_single_cascade_in_expression_statements)

verified_userStablethumb_upRecommendedbuildFix available

Avoid single cascade in expression statements.

## Details

[#](#details)

AVOID single cascade in expression statements.

BAD:

dart

```
o..m();
```

content_copy

GOOD:

dart

```
o.m();
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_single_cascade_in_expression_statements` rule, add `avoid_single_cascade_in_expression_statements` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_single_cascade_in_expression_statements
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_single_cascade_in_expression_statements: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_single_cascade_in_expression_statements: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_single_cascade_in_expression_statements).
