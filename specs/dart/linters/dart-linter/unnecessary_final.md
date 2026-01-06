Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_final](/tools/linter-rules/unnecessary_final)

# unnecessary_final

Learn about the unnecessary_final linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_final)

verified_userStablebuildFix available

Don't use `final` for local variables.

## Details

[#](#details)

Use `var`, not `final`, when declaring local variables.

 Per [Effective Dart](https://dart.dev/effective-dart/usage#do-follow-a-consistent-rule-for-var-and-final-on-local-variables), there are two styles in wide use. This rule enforces the `var` style. For the alternative style that prefers `final`, enable `prefer_final_locals` and `prefer_final_in_for_each` instead. 

For fields, `final` is always recommended; see the rule `prefer_final_fields`.

BAD:

dart

```
void badMethod() {
  final label = 'Final or var?';
  for (final char in ['v', 'a', 'r']) {
    print(char);
  }
}
```

content_copy

GOOD:

dart

```
void goodMethod() {
  var label = 'Final or var?';
  for (var char in ['v', 'a', 'r']) {
    print(char);
  }
}
```

content_copy

## Incompatible rules

[#](#incompatible-rules)

The `unnecessary_final` lint is incompatible with the following rules:

- [prefer_final_locals](/tools/linter-rules/prefer_final_locals)
- [prefer_final_parameters](/tools/linter-rules/prefer_final_parameters)
- [prefer_final_in_for_each](/tools/linter-rules/prefer_final_in_for_each)

## Enable

[#](#enable)

 To enable the `unnecessary_final` rule, add `unnecessary_final` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_final
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_final: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_final: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_final).
