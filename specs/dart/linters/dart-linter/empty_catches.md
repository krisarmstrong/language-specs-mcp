Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [empty_catches](/tools/linter-rules/empty_catches)

# empty_catches

Learn about the empty_catches linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/empty_catches)

verified_userStablecirclesCorebuildFix available

Avoid empty catch blocks.

## Details

[#](#details)

AVOID empty catch blocks.

 In general, empty catch blocks should be avoided. In cases where they are intended, a comment should be provided to explain why exceptions are being caught and suppressed. Alternatively, the exception identifier can be named with underscores (e.g., `_`) to indicate that we intend to skip it. 

BAD:

dart

```
try {
  ...
} catch(exception) { }
```

content_copy

GOOD:

dart

```
try {
  ...
} catch(e) {
  // ignored, really.
}
​
// Alternatively:
try {
  ...
} catch(_) { }
​
// Better still:
try {
  ...
} catch(e) {
  doSomething(e);
}
```

content_copy

## Enable

[#](#enable)

 To enable the `empty_catches` rule, add `empty_catches` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - empty_catches
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `empty_catches: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    empty_catches: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/empty_catches).
