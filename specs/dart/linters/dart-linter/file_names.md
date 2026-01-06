Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [file_names](/tools/linter-rules/file_names)

# file_names

Learn about the file_names linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/file_names)

verified_userStablecirclesCore

Name source files using `lowercase_with_underscores`.

## Details

[#](#details)

DO name source files using `lowercase_with_underscores`.

 Some file systems are not case-sensitive, so many projects require filenames to be all lowercase. Using a separating character allows names to still be readable in that form. Using underscores as the separator ensures that the name is still a valid Dart identifier, which may be helpful if the language later supports symbolic imports. 

BAD:

- `SliderMenu.dart`
- `filesystem.dart`
- `file-system.dart`

GOOD:

- `slider_menu.dart`
- `file_system.dart`

Files without a strict `.dart` extension are ignored. For example:

OK:

- `file-system.g.dart`
- `SliderMenu.css.dart`

 The lint `library_names` can be used to enforce the same kind of naming on the library. 

## Enable

[#](#enable)

 To enable the `file_names` rule, add `file_names` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - file_names
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `file_names: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    file_names: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/file_names).
