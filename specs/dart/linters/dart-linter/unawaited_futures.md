Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unawaited_futures](/tools/linter-rules/unawaited_futures)

# unawaited_futures

Learn about the unawaited_futures linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unawaited_futures)

verified_userStablebuildFix available

`Future` results in `async` function bodies must be `await`ed or marked `unawaited` using `dart:async`. 

## Details

[#](#details)

DO await functions that return a `Future` inside of an async function body. 

 It's easy to forget await in async methods as naming conventions usually don't tell us if a method is sync or async (except for some in `dart:io`). 

 When you really do want to start a fire-and-forget `Future`, the recommended way is to use `unawaited` from `dart:async`. The `// ignore` and `// ignore_for_file` comments also work. 

BAD:

dart

```
void main() async {
  doSomething(); // Likely a bug.
}
```

content_copy

GOOD:

dart

```
Future doSomething() => ...;
​
void main() async {
  await doSomething();
​
  unawaited(doSomething()); // Explicitly-ignored fire-and-forget.
}
```

content_copy

## Enable

[#](#enable)

 To enable the `unawaited_futures` rule, add `unawaited_futures` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unawaited_futures
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unawaited_futures: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unawaited_futures: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unawaited_futures).
