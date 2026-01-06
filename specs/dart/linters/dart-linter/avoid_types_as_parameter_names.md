Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_types_as_parameter_names](/tools/linter-rules/avoid_types_as_parameter_names)

# avoid_types_as_parameter_names

Learn about the avoid_types_as_parameter_names linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_types_as_parameter_names)

verified_userStablecirclesCore

Avoid types as parameter names.

## Details

[#](#details)

AVOID using a parameter name that is the same as an existing type.

BAD:

dart

```
m(f(int));
```

content_copy

GOOD:

dart

```
m(f(int v));
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_types_as_parameter_names` rule, add `avoid_types_as_parameter_names` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_types_as_parameter_names
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_types_as_parameter_names: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_types_as_parameter_names: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_types_as_parameter_names).
