Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_await_in_return](/tools/linter-rules/unnecessary_await_in_return)

# unnecessary_await_in_return

Learn about the unnecessary_await_in_return linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_await_in_return)

verified_userStablebuildFix available

Unnecessary `await` keyword in return.

## Details

[#](#details)

 Avoid returning an awaited expression when the expression type is assignable to the function's return type. 

BAD:

dart

```
Future<int> future;
Future<int> f1() async => await future;
Future<int> f2() async {
  return await future;
}
```

content_copy

GOOD:

dart

```
Future<int> future;
Future<int> f1() => future;
Future<int> f2() {
  return future;
}
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_await_in_return` rule, add `unnecessary_await_in_return` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_await_in_return
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_await_in_return: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_await_in_return: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_await_in_return).
