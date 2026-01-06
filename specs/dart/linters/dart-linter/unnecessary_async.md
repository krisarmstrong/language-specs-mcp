Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_async](/tools/linter-rules/unnecessary_async)

# unnecessary_async

Learn about the unnecessary_async linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_async)

scienceExperimentalbuildFix available

No await no async.

## Details

[#](#details)

Functions that don't do `await` don't have to be `async`.

 Usually such functions also don't have to return a `Future`, which allows an invoker to avoid `await` in its code, etc. Synchronous code in general runs faster, and is easier to reason about. 

BAD:

dart

```
void f() async {
  // await Future.delayed(const Duration(seconds: 2));
  print(0);
}
```

content_copy

GOOD:

dart

```
void f() {
  // await Future.delayed(const Duration(seconds: 2));
  print(0);
}
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_async` rule, add `unnecessary_async` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_async
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_async: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_async: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_async).
