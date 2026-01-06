Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_returning_null_for_future](/tools/linter-rules/avoid_returning_null_for_future)

# avoid_returning_null_for_future

Learn about the avoid_returning_null_for_future linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_returning_null_for_future)

errorRemoved

Avoid returning null for Future.

## Details

[#](#details)

NOTE: This rule is removed in Dart 3.3.0; it is no longer functional.

AVOID returning null for Future.

 It is almost always wrong to return `null` for a `Future`. Most of the time the developer simply forgot to put an `async` keyword on the function. 

## Enable

[#](#enable)

 To enable the `avoid_returning_null_for_future` rule, add `avoid_returning_null_for_future` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_returning_null_for_future
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_returning_null_for_future: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_returning_null_for_future: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_returning_null_for_future).
