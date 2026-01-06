Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_void_async](/tools/linter-rules/avoid_void_async)

# avoid_void_async

Learn about the avoid_void_async linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_void_async)

verified_userStablebuildFix available

Avoid `async` functions that return `void`.

## Details

[#](#details)

DO mark `async` functions as returning `Future<void>`.

 When declaring an `async` method or function which does not return a value, declare that it returns `Future<void>` and not just `void`. 

BAD:

dart

```
void f() async {}
void f2() async => null;
```

content_copy

GOOD:

dart

```
Future<void> f() async {}
Future<void> f2() async => null;
```

content_copy

EXCEPTION:

 An exception is made for top-level `main` functions, where the `Future` annotation can (and generally should) be dropped in favor of `void`. 

GOOD:

dart

```
Future<void> f() async {}
​
void main() async {
  await f();
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_void_async` rule, add `avoid_void_async` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_void_async
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_void_async: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_void_async: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_void_async).
