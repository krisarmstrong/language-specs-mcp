Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_bool_literals_in_conditional_expressions](/tools/linter-rules/avoid_bool_literals_in_conditional_expressions)

# avoid_bool_literals_in_conditional_expressions

Learn about the avoid_bool_literals_in_conditional_expressions linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_bool_literals_in_conditional_expressions)

verified_userStablebuildFix available

Avoid `bool` literals in conditional expressions.

## Details

[#](#details)

AVOID`bool` literals in conditional expressions.

BAD:

dart

```
condition ? true : boolExpression
condition ? false : boolExpression
condition ? boolExpression : true
condition ? boolExpression : false
```

content_copy

GOOD:

dart

```
condition || boolExpression
!condition && boolExpression
!condition || boolExpression
condition && boolExpression
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_bool_literals_in_conditional_expressions` rule, add `avoid_bool_literals_in_conditional_expressions` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_bool_literals_in_conditional_expressions
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_bool_literals_in_conditional_expressions: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_bool_literals_in_conditional_expressions: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_bool_literals_in_conditional_expressions).
