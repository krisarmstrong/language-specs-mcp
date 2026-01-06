Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [deprecated_consistency](/tools/linter-rules/deprecated_consistency)

# deprecated_consistency

Learn about the deprecated_consistency linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/deprecated_consistency)

verified_userStable

Missing deprecated annotation.

## Details

[#](#details)

DO apply `@Deprecated()` consistently:

- if a class is deprecated, its constructors should also be deprecated.
-  if a field is deprecated, the constructor parameter pointing to it should also be deprecated. 
-  if a constructor parameter pointing to a field is deprecated, the field should also be deprecated. 

BAD:

dart

```
@deprecated
class A {
  A();
}
​
class B {
  B({this.field});
  @deprecated
  Object field;
}
```

content_copy

GOOD:

dart

```
@deprecated
class A {
  @deprecated
  A();
}
​
class B {
  B({@deprecated this.field});
  @deprecated
  Object field;
}
​
class C extends B {
  C({@deprecated super.field});
}
```

content_copy

## Enable

[#](#enable)

 To enable the `deprecated_consistency` rule, add `deprecated_consistency` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - deprecated_consistency
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `deprecated_consistency: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    deprecated_consistency: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/deprecated_consistency).
