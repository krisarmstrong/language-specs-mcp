Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [await_only_futures](/tools/linter-rules/await_only_futures)

# await_only_futures

Learn about the await_only_futures linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/await_only_futures)

verified_userStablecirclesCorebuildFix available

Await only futures.

## Details

[#](#details)

AVOID using await on anything which is not a future.

 Await is allowed on the types: `Future<X>`, `FutureOr<X>`, `Future<X>?`, `FutureOr<X>?` and `dynamic`. 

 Further, using `await null` is specifically allowed as a way to introduce a microtask delay. 

BAD:

dart

```
main() async {
  print(await 23);
}
```

content_copy

GOOD:

dart

```
main() async {
  await null; // If a delay is really intended.
  print(23);
}
```

content_copy

## Enable

[#](#enable)

 To enable the `await_only_futures` rule, add `await_only_futures` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - await_only_futures
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `await_only_futures: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    await_only_futures: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/await_only_futures).
