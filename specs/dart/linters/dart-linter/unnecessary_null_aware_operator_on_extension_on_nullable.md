Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_null_aware_operator_on_extension_on_nullable](/tools/linter-rules/unnecessary_null_aware_operator_on_extension_on_nullable)

# unnecessary_null_aware_operator_on_extension_on_nullable

Learn about the unnecessary_null_aware_operator_on_extension_on_nullable linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_null_aware_operator_on_extension_on_nullable)

verified_userStable

Unnecessary null aware operator on extension on a nullable type.

## Details

[#](#details)

 Avoid null aware operators for members defined in an extension on a nullable type. 

BAD:

dart

```
extension E on int? {
  int m() => 1;
}
f(int? i) => i?.m();
```

content_copy

GOOD:

dart

```
extension E on int? {
  int m() => 1;
}
f(int? i) => i.m();
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_null_aware_operator_on_extension_on_nullable` rule, add `unnecessary_null_aware_operator_on_extension_on_nullable` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_null_aware_operator_on_extension_on_nullable
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_null_aware_operator_on_extension_on_nullable: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_null_aware_operator_on_extension_on_nullable: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_null_aware_operator_on_extension_on_nullable).
