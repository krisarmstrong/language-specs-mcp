Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_if_null_operators](/tools/linter-rules/prefer_if_null_operators)

# prefer_if_null_operators

Learn about the prefer_if_null_operators linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_if_null_operators)

verified_userStablethumb_upRecommendedbuildFix available

Prefer using `??` operators.

## Details

[#](#details)

PREFER using `??` operators instead of `null` checks and conditional expressions. 

BAD:

dart

```
v = a == null ? b : a;
```

content_copy

GOOD:

dart

```
v = a ?? b;
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_if_null_operators` rule, add `prefer_if_null_operators` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_if_null_operators
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_if_null_operators: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_if_null_operators: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_if_null_operators).
