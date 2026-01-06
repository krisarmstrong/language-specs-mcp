Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_adjacent_string_concatenation](/tools/linter-rules/prefer_adjacent_string_concatenation)

# prefer_adjacent_string_concatenation

Learn about the prefer_adjacent_string_concatenation linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_adjacent_string_concatenation)

verified_userStablethumb_upRecommendedbuildFix available

Use adjacent strings to concatenate string literals.

## Details

[#](#details)

DO use adjacent strings to concatenate string literals.

BAD:

dart

```
raiseAlarm(
    'ERROR: Parts of the spaceship are on fire. Other ' +
    'parts are overrun by martians. Unclear which are which.');
```

content_copy

GOOD:

dart

```
raiseAlarm(
    'ERROR: Parts of the spaceship are on fire. Other '
    'parts are overrun by martians. Unclear which are which.');
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_adjacent_string_concatenation` rule, add `prefer_adjacent_string_concatenation` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_adjacent_string_concatenation
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_adjacent_string_concatenation: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_adjacent_string_concatenation: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_adjacent_string_concatenation).
