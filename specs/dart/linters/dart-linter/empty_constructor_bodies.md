Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [empty_constructor_bodies](/tools/linter-rules/empty_constructor_bodies)

# empty_constructor_bodies

Learn about the empty_constructor_bodies linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/empty_constructor_bodies)

verified_userStablethumb_upRecommendedbuildFix available

Use `;` instead of `{}` for empty constructor bodies.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/usage#do-use--instead-of--for-empty-constructor-bodies): 

DO use `;` instead of `{}` for empty constructor bodies.

 In Dart, a constructor with an empty body can be terminated with just a semicolon. This is required for const constructors. For consistency and brevity, other constructors should also do this. 

BAD:

dart

```
class Point {
  int x, y;
  Point(this.x, this.y) {}
}
```

content_copy

GOOD:

dart

```
class Point {
  int x, y;
  Point(this.x, this.y);
}
```

content_copy

## Enable

[#](#enable)

 To enable the `empty_constructor_bodies` rule, add `empty_constructor_bodies` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - empty_constructor_bodies
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `empty_constructor_bodies: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    empty_constructor_bodies: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/empty_constructor_bodies).
