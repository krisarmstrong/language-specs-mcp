Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_function_type_syntax_for_parameters](/tools/linter-rules/use_function_type_syntax_for_parameters)

# use_function_type_syntax_for_parameters

Learn about the use_function_type_syntax_for_parameters linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_function_type_syntax_for_parameters)

verified_userStablethumb_upRecommendedbuildFix available

Use generic function type syntax for parameters.

## Details

[#](#details)

Use generic function type syntax for parameters.

BAD:

dart

```
Iterable<T> where(bool predicate(T element)) {}
```

content_copy

GOOD:

dart

```
Iterable<T> where(bool Function(T) predicate) {}
```

content_copy

## Enable

[#](#enable)

 To enable the `use_function_type_syntax_for_parameters` rule, add `use_function_type_syntax_for_parameters` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_function_type_syntax_for_parameters
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_function_type_syntax_for_parameters: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_function_type_syntax_for_parameters: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_function_type_syntax_for_parameters).
