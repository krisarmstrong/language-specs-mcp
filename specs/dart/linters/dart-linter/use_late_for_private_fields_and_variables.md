Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_late_for_private_fields_and_variables](/tools/linter-rules/use_late_for_private_fields_and_variables)

# use_late_for_private_fields_and_variables

Learn about the use_late_for_private_fields_and_variables linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_late_for_private_fields_and_variables)

scienceExperimental

Use late for private members with a non-nullable type.

## Details

[#](#details)

 Use `late` for private members with non-nullable types that are always expected to be non-null. Thus it's clear that the field is not expected to be `null` and it avoids null checks. 

BAD:

dart

```
int? _i;
m() {
  _i!.abs();
}
```

content_copy

GOOD:

dart

```
late int _i;
m() {
  _i.abs();
}
```

content_copy

OK:

dart

```
int? _i;
m() {
  _i?.abs();
  _i = null;
}
```

content_copy

## Enable

[#](#enable)

 To enable the `use_late_for_private_fields_and_variables` rule, add `use_late_for_private_fields_and_variables` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_late_for_private_fields_and_variables
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_late_for_private_fields_and_variables: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_late_for_private_fields_and_variables: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_late_for_private_fields_and_variables).
