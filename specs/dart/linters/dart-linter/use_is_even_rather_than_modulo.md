Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_is_even_rather_than_modulo](/tools/linter-rules/use_is_even_rather_than_modulo)

# use_is_even_rather_than_modulo

Learn about the use_is_even_rather_than_modulo linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_is_even_rather_than_modulo)

verified_userStable

Prefer intValue.isOdd/isEven instead of checking the result of % 2.

## Details

[#](#details)

PREFER the use of intValue.isOdd/isEven to check for evenness.

BAD:

dart

```
bool isEven = 1 % 2 == 0;
bool isOdd = 13 % 2 == 1;
```

content_copy

GOOD:

dart

```
bool isEven = 1.isEven;
bool isOdd = 13.isOdd;
```

content_copy

## Enable

[#](#enable)

 To enable the `use_is_even_rather_than_modulo` rule, add `use_is_even_rather_than_modulo` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_is_even_rather_than_modulo
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_is_even_rather_than_modulo: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_is_even_rather_than_modulo: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_is_even_rather_than_modulo).
