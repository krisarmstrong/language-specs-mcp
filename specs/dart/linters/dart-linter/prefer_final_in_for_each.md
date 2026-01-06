Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_final_in_for_each](/tools/linter-rules/prefer_final_in_for_each)

# prefer_final_in_for_each

Learn about the prefer_final_in_for_each linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_final_in_for_each)

verified_userStablebuildFix available

Prefer final in for-each loop variable if reference is not reassigned.

## Details

[#](#details)

DO prefer declaring for-each loop variables as final if they are not reassigned later in the code. 

 Declaring for-each loop variables as final when possible is a good practice because it helps avoid accidental reassignments and allows the compiler to do optimizations. 

BAD:

dart

```
for (var element in elements) { // LINT
  print('Element: $element');
}
```

content_copy

GOOD:

dart

```
for (final element in elements) {
  print('Element: $element');
}
```

content_copy

GOOD:

dart

```
for (var element in elements) {
  element = element + element;
  print('Element: $element');
}
```

content_copy

## Incompatible rules

[#](#incompatible-rules)

The `prefer_final_in_for_each` lint is incompatible with the following rules:

- [unnecessary_final](/tools/linter-rules/unnecessary_final)

## Enable

[#](#enable)

 To enable the `prefer_final_in_for_each` rule, add `prefer_final_in_for_each` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_final_in_for_each
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_final_in_for_each: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_final_in_for_each: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_final_in_for_each).
