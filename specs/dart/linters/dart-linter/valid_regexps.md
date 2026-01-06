Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [valid_regexps](/tools/linter-rules/valid_regexps)

# valid_regexps

Learn about the valid_regexps linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/valid_regexps)

verified_userStablecirclesCore

Use valid regular expression syntax.

## Details

[#](#details)

DO use valid regular expression syntax when creating regular expression instances. 

 Regular expressions created with invalid syntax will throw a `FormatException` at runtime so should be avoided. 

BAD:

dart

```
print(RegExp(r'(').hasMatch('foo()'));
```

content_copy

GOOD:

dart

```
print(RegExp(r'\(').hasMatch('foo()'));
```

content_copy

## Enable

[#](#enable)

 To enable the `valid_regexps` rule, add `valid_regexps` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - valid_regexps
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `valid_regexps: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    valid_regexps: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/valid_regexps).
