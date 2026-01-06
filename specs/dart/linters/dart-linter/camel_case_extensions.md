Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [camel_case_extensions](/tools/linter-rules/camel_case_extensions)

# camel_case_extensions

Learn about the camel_case_extensions linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/camel_case_extensions)

verified_userStablecirclesCore

Name extensions using UpperCamelCase.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/style#do-name-extensions-using-uppercamelcase): 

DO name extensions using `UpperCamelCase`.

 Extensions should capitalize the first letter of each word (including the first word), and use no separators. 

GOOD:

dart

```
extension MyFancyList<T> on List<T> {
  // ...
}
​
extension SmartIterable<T> on Iterable<T> {
  // ...
}
```

content_copy

## Enable

[#](#enable)

 To enable the `camel_case_extensions` rule, add `camel_case_extensions` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - camel_case_extensions
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `camel_case_extensions: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    camel_case_extensions: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/camel_case_extensions).
