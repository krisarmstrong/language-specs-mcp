Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_contains](/tools/linter-rules/prefer_contains)

# prefer_contains

Learn about the prefer_contains linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_contains)

verified_userStablethumb_upRecommendedbuildFix available

Use contains for `List` and `String` instances.

## Details

[#](#details)

DON'T use `indexOf` to see if a collection contains an element.

 Calling `indexOf` to see if a collection contains something is difficult to read and may have poor performance. 

Instead, prefer `contains`.

BAD:

dart

```
if (lunchBox.indexOf('sandwich') == -1) return 'so hungry...';
```

content_copy

GOOD:

dart

```
if (!lunchBox.contains('sandwich')) return 'so hungry...';
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_contains` rule, add `prefer_contains` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_contains
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_contains: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_contains: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_contains).
