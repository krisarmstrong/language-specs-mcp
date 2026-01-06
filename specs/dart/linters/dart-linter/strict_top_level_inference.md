Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [strict_top_level_inference](/tools/linter-rules/strict_top_level_inference)

# strict_top_level_inference

Learn about the strict_top_level_inference linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/strict_top_level_inference)

verified_userStablecirclesCorebuildFix available

Specify type annotations.

## Details

[#](#details)

 Do type annotate top-level and class-like member declarations, where types are not inferred from super-interfaces or initializers. 

 The lint warns about every omitted return type, parameter type, and variable type of a top-level declaration or class-like-namespace-level declaration (static or instance member or constructor declaration), which is not given a type by inference, and which therefore defaults to dynamic. 

 The only omitted types that can be given a type by top-level inference, are those of variable declarations with initializer expressions, and return and parameter types of instance members that override a consistent combined super-interface signature. 

Setters do not need a return type, as it is always assumed to be `void`.

BAD:

dart

```
var _zeroPointCache;
class Point {
  get zero => ...;
  final x, y;
  Point(x, y) {}
  closest(b, c) => distance(b) <= distance(c) ? b : c;
  distance(other) => ...;
}
_sq(v) => v * v;
```

content_copy

GOOD:

dart

```
Point? _zeroPointCache;
class Point {
  Point get zero => ...;
  final int x, y;
  Point(int x, int y) {}
  closest(Point b, Point c) =>
      distance(b) <= distance(c) ? b : c;
  distance(Point other) => ...;
}
int _sq(int v) => v * v;
```

content_copy

## Enable

[#](#enable)

 To enable the `strict_top_level_inference` rule, add `strict_top_level_inference` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - strict_top_level_inference
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `strict_top_level_inference: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    strict_top_level_inference: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/strict_top_level_inference).
