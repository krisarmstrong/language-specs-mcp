Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [deprecated_member_use_from_same_package](/tools/linter-rules/deprecated_member_use_from_same_package)

# deprecated_member_use_from_same_package

Learn about the deprecated_member_use_from_same_package linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/deprecated_member_use_from_same_package)

verified_userStablebuildFix available

Avoid using deprecated elements from within the package in which they are declared.

## Details

[#](#details)

 Elements that are annotated with `@Deprecated` should not be referenced from within the package in which they are declared. 

AVOID using deprecated elements.

...

BAD:

dart

```
// Declared in one library:
class Foo {
  @Deprecated("Use 'm2' instead")
  void m1() {}
​
  void m2({
      @Deprecated('This is an old parameter') int? p,
  })
}
​
@Deprecated('Do not use')
int x = 0;
​
// In the same or another library, but within the same package:
void m(Foo foo) {
  foo.m1();
  foo.m2(p: 7);
  x = 1;
}
```

content_copy

 Deprecated elements can be used from within other deprecated elements, in order to allow for the deprecation of a collection of APIs together as one unit. 

GOOD:

dart

```
// Declared in one library:
class Foo {
  @Deprecated("Use 'm2' instead")
  void m1() {}
​
  void m2({
      @Deprecated('This is an old parameter') int? p,
  })
}
​
@Deprecated('Do not use')
int x = 0;
​
// In the same or another library, but within the same package:
@Deprecated('Do not use')
void m(Foo foo) {
  foo.m1();
  foo.m2(p: 7);
  x = 1;
}
```

content_copy

## Enable

[#](#enable)

 To enable the `deprecated_member_use_from_same_package` rule, add `deprecated_member_use_from_same_package` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - deprecated_member_use_from_same_package
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `deprecated_member_use_from_same_package: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    deprecated_member_use_from_same_package: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/deprecated_member_use_from_same_package).
