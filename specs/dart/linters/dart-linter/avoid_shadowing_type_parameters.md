Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_shadowing_type_parameters](/tools/linter-rules/avoid_shadowing_type_parameters)

# avoid_shadowing_type_parameters

Learn about the avoid_shadowing_type_parameters linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_shadowing_type_parameters)

verified_userStablecirclesCore

Avoid shadowing type parameters.

## Details

[#](#details)

AVOID shadowing type parameters.

BAD:

dart

```
class A<T> {
  void fn<T>() {}
}
```

content_copy

GOOD:

dart

```
class A<T> {
  void fn<U>() {}
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_shadowing_type_parameters` rule, add `avoid_shadowing_type_parameters` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_shadowing_type_parameters
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_shadowing_type_parameters: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_shadowing_type_parameters: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_shadowing_type_parameters).
