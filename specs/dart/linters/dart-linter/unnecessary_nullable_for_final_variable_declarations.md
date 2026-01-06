Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_nullable_for_final_variable_declarations](/tools/linter-rules/unnecessary_nullable_for_final_variable_declarations)

# unnecessary_nullable_for_final_variable_declarations

Learn about the unnecessary_nullable_for_final_variable_declarations linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_nullable_for_final_variable_declarations)

verified_userStablethumb_upRecommendedbuildFix available

Use a non-nullable type for a final variable initialized with a non-nullable value.

## Details

[#](#details)

 Use a non-nullable type for a final variable initialized with a non-nullable value. 

BAD:

dart

```
final int? i = 1;
```

content_copy

GOOD:

dart

```
final int i = 1;
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_nullable_for_final_variable_declarations` rule, add `unnecessary_nullable_for_final_variable_declarations` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_nullable_for_final_variable_declarations
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_nullable_for_final_variable_declarations: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_nullable_for_final_variable_declarations: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_nullable_for_final_variable_declarations).
