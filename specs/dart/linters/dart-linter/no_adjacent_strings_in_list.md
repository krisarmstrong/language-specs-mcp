Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [no_adjacent_strings_in_list](/tools/linter-rules/no_adjacent_strings_in_list)

# no_adjacent_strings_in_list

Learn about the no_adjacent_strings_in_list linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_adjacent_strings_in_list)

verified_userStable

Don't use adjacent strings in list.

## Details

[#](#details)

DON'T use adjacent strings in a list.

This can indicate a forgotten comma.

BAD:

dart

```
List<String> list = <String>[
  'a'
  'b',
  'c',
];
```

content_copy

GOOD:

dart

```
List<String> list = <String>[
  'a' +
  'b',
  'c',
];
```

content_copy

## Enable

[#](#enable)

 To enable the `no_adjacent_strings_in_list` rule, add `no_adjacent_strings_in_list` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - no_adjacent_strings_in_list
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `no_adjacent_strings_in_list: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    no_adjacent_strings_in_list: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_adjacent_strings_in_list).
