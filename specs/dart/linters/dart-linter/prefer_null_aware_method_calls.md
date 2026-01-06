Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_null_aware_method_calls](/tools/linter-rules/prefer_null_aware_method_calls)

# prefer_null_aware_method_calls

Learn about the prefer_null_aware_method_calls linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_null_aware_method_calls)

verified_userStable

Prefer `null`-aware method calls.

## Details

[#](#details)

 Instead of checking nullability of a function/method `f` before calling it, you can use `f?.call()`. 

BAD:

dart

```
if (f != null) f!();
```

content_copy

GOOD:

dart

```
f?.call();
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_null_aware_method_calls` rule, add `prefer_null_aware_method_calls` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_null_aware_method_calls
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_null_aware_method_calls: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_null_aware_method_calls: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_null_aware_method_calls).
