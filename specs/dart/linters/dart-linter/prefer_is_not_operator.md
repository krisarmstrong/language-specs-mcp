Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_is_not_operator](/tools/linter-rules/prefer_is_not_operator)

# prefer_is_not_operator

Learn about the prefer_is_not_operator linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_is_not_operator)

verified_userStablethumb_upRecommendedbuildFix available

Prefer is! operator.

## Details

[#](#details)

When checking if an object is not of a specified type, it is preferable to use the 'is!' operator.

BAD:

dart

```
if (!(foo is Foo)) {
  ...
}
```

content_copy

GOOD:

dart

```
if (foo is! Foo) {
  ...
}
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_is_not_operator` rule, add `prefer_is_not_operator` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_is_not_operator
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_is_not_operator: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_is_not_operator: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_is_not_operator).
