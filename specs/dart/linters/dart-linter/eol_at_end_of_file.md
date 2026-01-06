Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [eol_at_end_of_file](/tools/linter-rules/eol_at_end_of_file)

# eol_at_end_of_file

Learn about the eol_at_end_of_file linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/eol_at_end_of_file)

verified_userStablebuildFix available

Put a single newline at end of file.

## Details

[#](#details)

DO put a single newline at the end of non-empty files.

BAD:

dart

```
a {
}
```

content_copy

GOOD:

dart

```
b {
}
    <-- newline
```

content_copy

## Enable

[#](#enable)

 To enable the `eol_at_end_of_file` rule, add `eol_at_end_of_file` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - eol_at_end_of_file
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `eol_at_end_of_file: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    eol_at_end_of_file: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/eol_at_end_of_file).
