Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [camel_case_types](/tools/linter-rules/camel_case_types)

# camel_case_types

Learn about the camel_case_types linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/camel_case_types)

verified_userStablecirclesCore

Name types using UpperCamelCase.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/style#do-name-types-using-uppercamelcase): 

DO name types using UpperCamelCase.

 Classes and typedefs should capitalize the first letter of each word (including the first word), and use no separators. 

GOOD:

dart

```
class SliderMenu {
  // ...
}
​
class HttpRequest {
  // ...
}
​
typedef num Adder(num x, num y);
```

content_copy

## Enable

[#](#enable)

 To enable the `camel_case_types` rule, add `camel_case_types` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - camel_case_types
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `camel_case_types: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    camel_case_types: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/camel_case_types).
