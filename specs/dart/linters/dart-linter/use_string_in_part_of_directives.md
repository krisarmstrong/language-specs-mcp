Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_string_in_part_of_directives](/tools/linter-rules/use_string_in_part_of_directives)

# use_string_in_part_of_directives

Learn about the use_string_in_part_of_directives linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_string_in_part_of_directives)

verified_userStablecirclesCorebuildFix available

Use string in part of directives.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/usage#do-use-strings-in-part-of-directives): 

DO use strings in `part of` directives.

BAD:

dart

```
part of my_library;
```

content_copy

GOOD:

dart

```
part of '../../my_library.dart';
```

content_copy

## Enable

[#](#enable)

 To enable the `use_string_in_part_of_directives` rule, add `use_string_in_part_of_directives` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_string_in_part_of_directives
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_string_in_part_of_directives: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_string_in_part_of_directives: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_string_in_part_of_directives).
