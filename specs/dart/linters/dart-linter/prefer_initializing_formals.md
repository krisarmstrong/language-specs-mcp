Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_initializing_formals](/tools/linter-rules/prefer_initializing_formals)

# prefer_initializing_formals

Learn about the prefer_initializing_formals linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_initializing_formals)

verified_userStablethumb_upRecommendedbuildFix available

Use initializing formals when possible.

## Details

[#](#details)

DO use initializing formals when possible.

Using initializing formals when possible makes your code more terse.

BAD:

dart

```
class Point {
  num? x, y;
  Point(num x, num y) {
    this.x = x;
    this.y = y;
  }
}
```

content_copy

GOOD:

dart

```
class Point {
  num? x, y;
  Point(num this.x, num this.y);
}
```

content_copy

BAD:

dart

```
class Point {
  num? x, y;
  Point({num? x, num? y}) {
    this.x = x;
    this.y = y;
  }
}
```

content_copy

GOOD:

dart

```
class Point {
  num? x, y;
  Point({required num this.x, required num this.y});
}
```

content_copy

NOTE: This rule will not generate a lint for named parameters unless the parameter name and the field name are the same. The reason for this is that resolving such a lint would require either renaming the field or renaming the parameter, and both of those actions would potentially be a breaking change. For example, the following will not generate a lint: 

dart

```
class Point {
  bool? isEnabled;
  Point({bool? enabled}) {
    this.isEnabled = enabled; // OK
  }
}
```

content_copy

NOTE: Also note that it is possible to enforce a type that is stricter than the initialized field with an initializing formal parameter. In the following example the unnamed `Bid` constructor requires a non-null `int` despite `amount` being declared nullable (`int?`). 

dart

```
class Bid {
  final int? amount;
  Bid(int this.amount);
  Bid.pass() : amount = null;
}
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_initializing_formals` rule, add `prefer_initializing_formals` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_initializing_formals
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_initializing_formals: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_initializing_formals: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_initializing_formals).
