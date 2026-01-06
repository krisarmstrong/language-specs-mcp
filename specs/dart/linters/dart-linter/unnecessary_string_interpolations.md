Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_string_interpolations](/tools/linter-rules/unnecessary_string_interpolations)

# unnecessary_string_interpolations

Learn about the unnecessary_string_interpolations linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_string_interpolations)

verified_userStablethumb_upRecommendedbuildFix available

Unnecessary string interpolation.

## Details

[#](#details)

DON'T use string interpolation if there's only a string expression in it.

BAD:

dart

```
String message;
String o = '$message';
```

content_copy

GOOD:

dart

```
String message;
String o = message;
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_string_interpolations` rule, add `unnecessary_string_interpolations` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_string_interpolations
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_string_interpolations: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_string_interpolations: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_string_interpolations).
