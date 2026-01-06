Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_catching_errors](/tools/linter-rules/avoid_catching_errors)

# avoid_catching_errors

Learn about the avoid_catching_errors linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_catching_errors)

verified_userStable

Don't explicitly catch `Error` or types that implement it.

## Details

[#](#details)

DON'T explicitly catch `Error` or types that implement it.

 Errors differ from Exceptions in that Errors can be analyzed and prevented prior to runtime. It should almost never be necessary to catch an error at runtime. 

BAD:

dart

```
try {
  somethingRisky();
} on Error catch(e) {
  doSomething(e);
}
```

content_copy

GOOD:

dart

```
try {
  somethingRisky();
} on Exception catch(e) {
  doSomething(e);
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_catching_errors` rule, add `avoid_catching_errors` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_catching_errors
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_catching_errors: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_catching_errors: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_catching_errors).
