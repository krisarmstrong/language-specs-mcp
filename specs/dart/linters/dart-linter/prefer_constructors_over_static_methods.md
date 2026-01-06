Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_constructors_over_static_methods](/tools/linter-rules/prefer_constructors_over_static_methods)

# prefer_constructors_over_static_methods

Learn about the prefer_constructors_over_static_methods linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_constructors_over_static_methods)

verified_userStable

Prefer defining constructors instead of static methods to create instances.

## Details

[#](#details)

PREFER defining constructors instead of static methods to create instances.

 In most cases, it makes more sense to use a named constructor rather than a static method because it makes instantiation clearer. 

BAD:

dart

```
class Point {
  num x, y;
  Point(this.x, this.y);
  static Point polar(num theta, num radius) {
    return Point(radius * math.cos(theta),
        radius * math.sin(theta));
  }
}
```

content_copy

GOOD:

dart

```
class Point {
  num x, y;
  Point(this.x, this.y);
  Point.polar(num theta, num radius)
      : x = radius * math.cos(theta),
        y = radius * math.sin(theta);
}
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_constructors_over_static_methods` rule, add `prefer_constructors_over_static_methods` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_constructors_over_static_methods
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_constructors_over_static_methods: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_constructors_over_static_methods: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_constructors_over_static_methods).
