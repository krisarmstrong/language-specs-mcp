Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [missing_whitespace_between_adjacent_strings](/tools/linter-rules/missing_whitespace_between_adjacent_strings)

# missing_whitespace_between_adjacent_strings

Learn about the missing_whitespace_between_adjacent_strings linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/missing_whitespace_between_adjacent_strings)

verified_userStable

Missing whitespace between adjacent strings.

## Details

[#](#details)

 Add a trailing whitespace to prevent missing whitespace between adjacent strings. 

 With long text split across adjacent strings it's easy to forget a whitespace between strings. 

BAD:

dart

```
var s =
  'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed'
  'do eiusmod tempor incididunt ut labore et dolore magna';
```

content_copy

GOOD:

dart

```
var s =
  'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed '
  'do eiusmod tempor incididunt ut labore et dolore magna';
```

content_copy

## Enable

[#](#enable)

 To enable the `missing_whitespace_between_adjacent_strings` rule, add `missing_whitespace_between_adjacent_strings` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - missing_whitespace_between_adjacent_strings
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `missing_whitespace_between_adjacent_strings: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    missing_whitespace_between_adjacent_strings: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/missing_whitespace_between_adjacent_strings).
