Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [type_init_formals](/tools/linter-rules/type_init_formals)

# type_init_formals

Learn about the type_init_formals linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/type_init_formals)

verified_userStablethumb_upRecommendedbuildFix available

Don't type annotate initializing formals.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/design#dont-type-annotate-initializing-formals): 

DON'T type annotate initializing formals.

 If a constructor parameter is using `this.x` to initialize a field, then the type of the parameter is understood to be the same type as the field. If a a constructor parameter is using `super.x` to forward to a super constructor, then the type of the parameter is understood to be the same as the super constructor parameter. 

 Type annotating an initializing formal with a different type than that of the field is OK. 

BAD:

dart

```
class Point {
  int x, y;
  Point(int this.x, int this.y);
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

BAD:

dart

```
class A {
  int a;
  A(this.a);
}
​
class B extends A {
  B(int super.a);
}
```

content_copy

GOOD:

dart

```
class A {
  int a;
  A(this.a);
}
​
class B extends A {
  B(super.a);
}
```

content_copy

## Enable

[#](#enable)

 To enable the `type_init_formals` rule, add `type_init_formals` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - type_init_formals
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `type_init_formals: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    type_init_formals: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/type_init_formals).
