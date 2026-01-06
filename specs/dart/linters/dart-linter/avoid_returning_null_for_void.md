Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_returning_null_for_void](/tools/linter-rules/avoid_returning_null_for_void)

# avoid_returning_null_for_void

Learn about the avoid_returning_null_for_void linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_returning_null_for_void)

verified_userStablethumb_upRecommendedbuildFix available

Avoid returning `null` for `void`.

## Details

[#](#details)

AVOID returning `null` for `void`.

 In a large variety of languages `void` as return type is used to indicate that a function doesn't return anything. Dart allows returning `null` in functions with `void` return type but it also allow using `return;` without specifying any value. To have a consistent way you should not return `null` and only use an empty return. 

BAD:

dart

```
void f1() {
  return null;
}
Future<void> f2() async {
  return null;
}
```

content_copy

GOOD:

dart

```
void f1() {
  return;
}
Future<void> f2() async {
  return;
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_returning_null_for_void` rule, add `avoid_returning_null_for_void` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_returning_null_for_void
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_returning_null_for_void: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_returning_null_for_void: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_returning_null_for_void).
