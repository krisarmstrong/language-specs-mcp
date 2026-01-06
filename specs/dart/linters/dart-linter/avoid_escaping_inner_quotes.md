Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_escaping_inner_quotes](/tools/linter-rules/avoid_escaping_inner_quotes)

# avoid_escaping_inner_quotes

Learn about the avoid_escaping_inner_quotes linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_escaping_inner_quotes)

verified_userStablebuildFix available

Avoid escaping inner quotes by converting surrounding quotes.

## Details

[#](#details)

Avoid escaping inner quotes by converting surrounding quotes.

BAD:

dart

```
var s = 'It\'s not fun';
```

content_copy

GOOD:

dart

```
var s = "It's not fun";
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_escaping_inner_quotes` rule, add `avoid_escaping_inner_quotes` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_escaping_inner_quotes
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_escaping_inner_quotes: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_escaping_inner_quotes: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_escaping_inner_quotes).
