Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [constant_identifier_names](/tools/linter-rules/constant_identifier_names)

# constant_identifier_names

Learn about the constant_identifier_names linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/constant_identifier_names)

verified_userStablethumb_upRecommendedbuildFix available

Prefer using lowerCamelCase for constant names.

## Details

[#](#details)

PREFER using lowerCamelCase for constant names.

In new code, use `lowerCamelCase` for constant variables, including enum values.

 In existing code that uses `ALL_CAPS_WITH_UNDERSCORES` for constants, you may continue to use all caps to stay consistent. 

BAD:

dart

```
const PI = 3.14;
const kDefaultTimeout = 1000;
final URL_SCHEME = RegExp('^([a-z]+):');
​
class Dice {
  static final NUMBER_GENERATOR = Random();
}
```

content_copy

GOOD:

dart

```
const pi = 3.14;
const defaultTimeout = 1000;
final urlScheme = RegExp('^([a-z]+):');
​
class Dice {
  static final numberGenerator = Random();
}
```

content_copy

## Enable

[#](#enable)

 To enable the `constant_identifier_names` rule, add `constant_identifier_names` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - constant_identifier_names
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `constant_identifier_names: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    constant_identifier_names: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/constant_identifier_names).
