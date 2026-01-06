Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_raw_strings](/tools/linter-rules/unnecessary_raw_strings)

# unnecessary_raw_strings

Learn about the unnecessary_raw_strings linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_raw_strings)

verified_userStablebuildFix available

Unnecessary raw string.

## Details

[#](#details)

Use raw string only when needed.

BAD:

dart

```
var s1 = r'a';
```

content_copy

GOOD:

dart

```
var s1 = 'a';
var s2 = r'$a';
var s3 = r'\a';
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_raw_strings` rule, add `unnecessary_raw_strings` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_raw_strings
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_raw_strings: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_raw_strings: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_raw_strings).
