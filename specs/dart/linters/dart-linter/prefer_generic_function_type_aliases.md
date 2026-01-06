Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_generic_function_type_aliases](/tools/linter-rules/prefer_generic_function_type_aliases)

# prefer_generic_function_type_aliases

Learn about the prefer_generic_function_type_aliases linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_generic_function_type_aliases)

verified_userStablecirclesCorebuildFix available

Prefer generic function type aliases.

## Details

[#](#details)

PREFER generic function type aliases.

 With the introduction of generic functions, function type aliases (`typedef void F()`) couldn't express all of the possible kinds of parameterization that users might want to express. Generic function type aliases (`typedef F = void Function()`) fixed that issue. 

 For consistency and readability reasons, it's better to only use one syntax and thus prefer generic function type aliases. 

BAD:

dart

```
typedef void F();
```

content_copy

GOOD:

dart

```
typedef F = void Function();
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_generic_function_type_aliases` rule, add `prefer_generic_function_type_aliases` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_generic_function_type_aliases
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_generic_function_type_aliases: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_generic_function_type_aliases: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_generic_function_type_aliases).
