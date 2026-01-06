Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_print](/tools/linter-rules/avoid_print)

# avoid_print

Learn about the avoid_print linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_print)

verified_userStableflutterFlutterbuildFix available

Avoid `print` calls in production code.

## Details

[#](#details)

DO avoid `print` calls in production code.

 For production code, consider using a logging framework. If you are using Flutter, you can use `debugPrint` or surround `print` calls with a check for `kDebugMode`

BAD:

dart

```
void f(int x) {
  print('debug: $x');
  ...
}
```

content_copy

GOOD:

dart

```
void f(int x) {
  debugPrint('debug: $x');
  ...
}
```

content_copy

GOOD:

dart

```
void f(int x) {
  log('log: $x');
  ...
}
```

content_copy

GOOD:

dart

```
void f(int x) {
  if (kDebugMode) {
      print('debug: $x');
  }
  ...
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_print` rule, add `avoid_print` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_print
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_print: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_print: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_print).
