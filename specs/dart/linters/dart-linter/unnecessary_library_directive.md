Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_library_directive](/tools/linter-rules/unnecessary_library_directive)

# unnecessary_library_directive

Learn about the unnecessary_library_directive linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_library_directive)

verified_userStablebuildFix available

Avoid library directives unless they have documentation comments or annotations.

## Details

[#](#details)

DO use library directives if you want to document a library and/or annotate a library. 

BAD:

dart

```
library;
```

content_copy

GOOD:

dart

```
/// This library does important things
library;
```

content_copydart

```
@TestOn('js')
library;
```

content_copy

 NOTE: Due to limitations with this lint, libraries with parts will not be flagged for unnecessary library directives. 

## Enable

[#](#enable)

 To enable the `unnecessary_library_directive` rule, add `unnecessary_library_directive` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_library_directive
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_library_directive: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_library_directive: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_library_directive).
