Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_bool_in_asserts](/tools/linter-rules/prefer_bool_in_asserts)

# prefer_bool_in_asserts

Learn about the prefer_bool_in_asserts linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_bool_in_asserts)

errorRemoved

Prefer using a boolean as the assert condition.

## Details

[#](#details)

NOTE: This rule is removed in Dart 3.0.0; it is no longer functional.

DO use a boolean for assert conditions.

 Not using booleans in assert conditions can lead to code where it isn't clear what the intention of the assert statement is. 

BAD:

dart

```
assert(() {
  f();
  return true;
});
```

content_copy

GOOD:

dart

```
assert(() {
  f();
  return true;
}());
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_bool_in_asserts` rule, add `prefer_bool_in_asserts` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_bool_in_asserts
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_bool_in_asserts: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_bool_in_asserts: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_bool_in_asserts).
