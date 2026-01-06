Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_rethrow_when_possible](/tools/linter-rules/use_rethrow_when_possible)

# use_rethrow_when_possible

Learn about the use_rethrow_when_possible linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_rethrow_when_possible)

verified_userStablethumb_upRecommendedbuildFix available

Use rethrow to rethrow a caught exception.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/usage#do-use-rethrow-to-rethrow-a-caught-exception): 

DO use rethrow to rethrow a caught exception.

 As Dart provides rethrow as a feature, it should be used to improve terseness and readability. 

BAD:

dart

```
try {
  somethingRisky();
} catch(e) {
  if (!canHandle(e)) throw e;
  handle(e);
}
```

content_copy

GOOD:

dart

```
try {
  somethingRisky();
} catch(e) {
  if (!canHandle(e)) rethrow;
  handle(e);
}
```

content_copy

## Enable

[#](#enable)

 To enable the `use_rethrow_when_possible` rule, add `use_rethrow_when_possible` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_rethrow_when_possible
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_rethrow_when_possible: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_rethrow_when_possible: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_rethrow_when_possible).
