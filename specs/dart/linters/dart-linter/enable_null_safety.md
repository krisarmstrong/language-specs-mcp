Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [enable_null_safety](/tools/linter-rules/enable_null_safety)

# enable_null_safety

Learn about the enable_null_safety linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/enable_null_safety)

errorRemoved

Do use sound null safety.

## Details

[#](#details)

NOTE: This rule is removed in Dart 3.0.0; it is no longer functional.

DO use sound null safety, by not specifying a dart version lower than `2.12`. 

BAD:

dart

```
// @dart=2.8
a() {
}
```

content_copy

GOOD:

dart

```
b() {
}
```

content_copy

## Enable

[#](#enable)

 To enable the `enable_null_safety` rule, add `enable_null_safety` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - enable_null_safety
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `enable_null_safety: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    enable_null_safety: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/enable_null_safety).
