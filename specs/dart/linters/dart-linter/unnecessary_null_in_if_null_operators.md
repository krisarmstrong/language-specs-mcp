Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_null_in_if_null_operators](/tools/linter-rules/unnecessary_null_in_if_null_operators)

# unnecessary_null_in_if_null_operators

Learn about the unnecessary_null_in_if_null_operators linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_null_in_if_null_operators)

verified_userStablethumb_upRecommendedbuildFix available

Avoid using `null` in `??` operators.

## Details

[#](#details)

AVOID using `null` as an operand in `??` operators.

 Using `null` in an `if null` operator is redundant, regardless of which side `null` is used on. 

BAD:

dart

```
var x = a ?? null;
var y = null ?? 1;
```

content_copy

GOOD:

dart

```
var x = a ?? 1;
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_null_in_if_null_operators` rule, add `unnecessary_null_in_if_null_operators` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_null_in_if_null_operators
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_null_in_if_null_operators: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_null_in_if_null_operators: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_null_in_if_null_operators).
