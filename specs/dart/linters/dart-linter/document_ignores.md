Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [document_ignores](/tools/linter-rules/document_ignores)

# document_ignores

Learn about the document_ignores linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/document_ignores)

verified_userStable

Document ignore comments.

## Details

[#](#details)

DO document all ignored diagnostic reports.

BAD:

dart

```
// ignore: unused_element
int _x = 1;
```

content_copy

GOOD:

dart

```
// This private field will be used later.
// ignore: unused_element
int _x = 1;
```

content_copy

## Enable

[#](#enable)

 To enable the `document_ignores` rule, add `document_ignores` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - document_ignores
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `document_ignores: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    document_ignores: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/document_ignores).
