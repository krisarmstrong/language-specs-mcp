Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_return_types_on_setters](/tools/linter-rules/avoid_return_types_on_setters)

# avoid_return_types_on_setters

Learn about the avoid_return_types_on_setters linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_return_types_on_setters)

verified_userStablethumb_upRecommendedbuildFix available

Avoid return types on setters.

## Details

[#](#details)

AVOID return types on setters.

As setters do not return a value, declaring the return type of one is redundant.

BAD:

dart

```
void set speed(int ms);
```

content_copy

GOOD:

dart

```
set speed(int ms);
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_return_types_on_setters` rule, add `avoid_return_types_on_setters` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_return_types_on_setters
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_return_types_on_setters: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_return_types_on_setters: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_return_types_on_setters).
