Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_expression_function_bodies](/tools/linter-rules/prefer_expression_function_bodies)

# prefer_expression_function_bodies

Learn about the prefer_expression_function_bodies linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_expression_function_bodies)

verified_userStablebuildFix available

Use => for short members whose body is a single return statement.

## Details

[#](#details)

CONSIDER using => for short members whose body is a single return statement.

BAD:

dart

```
get width {
  return right - left;
}
```

content_copy

BAD:

dart

```
bool ready(num time) {
  return minTime == null || minTime <= time;
}
```

content_copy

BAD:

dart

```
containsValue(String value) {
  return getValues().contains(value);
}
```

content_copy

GOOD:

dart

```
get width => right - left;
```

content_copy

GOOD:

dart

```
bool ready(num time) => minTime == null || minTime <= time;
```

content_copy

GOOD:

dart

```
containsValue(String value) => getValues().contains(value);
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_expression_function_bodies` rule, add `prefer_expression_function_bodies` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_expression_function_bodies
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_expression_function_bodies: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_expression_function_bodies: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_expression_function_bodies).
