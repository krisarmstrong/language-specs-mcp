Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_private_typedef_functions](/tools/linter-rules/avoid_private_typedef_functions)

# avoid_private_typedef_functions

Learn about the avoid_private_typedef_functions linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_private_typedef_functions)

verified_userStablebuildFix available

Avoid private typedef functions.

## Details

[#](#details)

AVOID private typedef functions used only once. Prefer inline function syntax. 

BAD:

dart

```
typedef void _F();
m(_F f);
```

content_copy

GOOD:

dart

```
m(void Function() f);
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_private_typedef_functions` rule, add `avoid_private_typedef_functions` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_private_typedef_functions
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_private_typedef_functions: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_private_typedef_functions: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_private_typedef_functions).
