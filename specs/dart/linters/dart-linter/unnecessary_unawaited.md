Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_unawaited](/tools/linter-rules/unnecessary_unawaited)

# unnecessary_unawaited

Learn about the unnecessary_unawaited linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_unawaited)

verified_userStablebuildFix available

Unnecessary use of 'unawaited'.

## Details

[#](#details)

 A call to a function, method, or operator, or a reference to a field, getter, or top-level variable which is annotated with `@awaitNotRequired` does not need to be wrapped in a call to `unawaited()`. 

BAD:

dart

```
@awaitNotRequired
Future<LogMessage> log(String message) { ... }
​
void f() {
  unawaited(log('Message.'));
}
```

content_copy

GOOD:

dart

```
@awaitNotRequired
Future<LogMessage> log(String message) { ... }
​
void f() {
  log('Message.');
}
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_unawaited` rule, add `unnecessary_unawaited` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_unawaited
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_unawaited: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_unawaited: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_unawaited).
