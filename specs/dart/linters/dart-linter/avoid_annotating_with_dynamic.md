Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_annotating_with_dynamic](/tools/linter-rules/avoid_annotating_with_dynamic)

# avoid_annotating_with_dynamic

Learn about the avoid_annotating_with_dynamic linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_annotating_with_dynamic)

verified_userStablebuildFix available

Avoid annotating with `dynamic` when not required.

## Details

[#](#details)

AVOID annotating with `dynamic` when not required.

 As `dynamic` is the assumed return value of a function or method, it is usually not necessary to annotate it. 

BAD:

dart

```
dynamic lookUpOrDefault(String name, Map map, dynamic defaultValue) {
  var value = map[name];
  if (value != null) return value;
  return defaultValue;
}
```

content_copy

GOOD:

dart

```
lookUpOrDefault(String name, Map map, defaultValue) {
  var value = map[name];
  if (value != null) return value;
  return defaultValue;
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_annotating_with_dynamic` rule, add `avoid_annotating_with_dynamic` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_annotating_with_dynamic
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_annotating_with_dynamic: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_annotating_with_dynamic: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_annotating_with_dynamic).
