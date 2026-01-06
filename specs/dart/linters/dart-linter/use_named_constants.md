Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_named_constants](/tools/linter-rules/use_named_constants)

# use_named_constants

Learn about the use_named_constants linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_named_constants)

verified_userStablebuildFix available

Use predefined named constants.

## Details

[#](#details)

Where possible, use already defined const values.

BAD:

dart

```
const Duration(seconds: 0);
```

content_copy

GOOD:

dart

```
Duration.zero;
```

content_copy

## Enable

[#](#enable)

 To enable the `use_named_constants` rule, add `use_named_constants` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_named_constants
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_named_constants: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_named_constants: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_named_constants).
