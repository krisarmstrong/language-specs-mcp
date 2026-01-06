Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [type_literal_in_constant_pattern](/tools/linter-rules/type_literal_in_constant_pattern)

# type_literal_in_constant_pattern

Learn about the type_literal_in_constant_pattern linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/type_literal_in_constant_pattern)

verified_userStablecirclesCorebuildFix available

Don't use constant patterns with type literals.

## Details

[#](#details)

If you meant to test if the object has type `Foo`, instead write `Foo _`.

BAD:

dart

```
void f(Object? x) {
  if (x case num) {
    print('int or double');
  }
}
```

content_copy

GOOD:

dart

```
void f(Object? x) {
  if (x case num _) {
    print('int or double');
  }
}
```

content_copy

 If you do mean to test that the matched value (which you expect to have the type `Type`) is equal to the type literal `Foo`, then this lint can be silenced using `const (Foo)`. 

BAD:

dart

```
void f(Object? x) {
  if (x case int) {
    print('int');
  }
}
```

content_copy

GOOD:

dart

```
void f(Object? x) {
  if (x case const (int)) {
    print('int');
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `type_literal_in_constant_pattern` rule, add `type_literal_in_constant_pattern` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - type_literal_in_constant_pattern
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `type_literal_in_constant_pattern: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    type_literal_in_constant_pattern: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/type_literal_in_constant_pattern).
