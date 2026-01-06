Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [simplify_variable_pattern](/tools/linter-rules/simplify_variable_pattern)

# simplify_variable_pattern

Learn about the simplify_variable_pattern linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/simplify_variable_pattern)

verified_userStablebuildFix available

Avoid unnecessary member names in variable patterns.

## Details

[#](#details)

AVOID redundant member names in variable patterns.

 When a variable pattern declares a variable with the same name as a member of the matched type, the member name is redundant and can be omitted. 

BAD:

dart

```
void f(Object o) {
  if (o case String(length: length)) {
    print('string is $length characters long');
  }
}
```

content_copy

GOOD:

dart

```
void f(Object o) {
  if (o case String(:var length)) {
    print('string is $length characters long');
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `simplify_variable_pattern` rule, add `simplify_variable_pattern` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - simplify_variable_pattern
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `simplify_variable_pattern: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    simplify_variable_pattern: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/simplify_variable_pattern).
