Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_if_null_to_convert_nulls_to_bools](/tools/linter-rules/use_if_null_to_convert_nulls_to_bools)

# use_if_null_to_convert_nulls_to_bools

Learn about the use_if_null_to_convert_nulls_to_bools linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_if_null_to_convert_nulls_to_bools)

reportDeprecatedbuildFix available

Use `??` operators to convert `null`s to `bool`s.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/usage#prefer-using--to-convert-null-to-a-boolean-value): 

Use `??` operators to convert `null`s to `bool`s.

BAD:

dart

```
if (nullableBool == true) {
}
if (nullableBool != false) {
}
```

content_copy

GOOD:

dart

```
if (nullableBool ?? false) {
}
if (nullableBool ?? true) {
}
```

content_copy

## Enable

[#](#enable)

 To enable the `use_if_null_to_convert_nulls_to_bools` rule, add `use_if_null_to_convert_nulls_to_bools` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_if_null_to_convert_nulls_to_bools
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_if_null_to_convert_nulls_to_bools: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_if_null_to_convert_nulls_to_bools: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_if_null_to_convert_nulls_to_bools).
