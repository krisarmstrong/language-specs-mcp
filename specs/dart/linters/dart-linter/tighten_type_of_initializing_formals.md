Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [tighten_type_of_initializing_formals](/tools/linter-rules/tighten_type_of_initializing_formals)

# tighten_type_of_initializing_formals

Learn about the tighten_type_of_initializing_formals linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/tighten_type_of_initializing_formals)

verified_userStable

Tighten type of initializing formal.

## Details

[#](#details)

 Tighten the type of an initializing formal if a non-null assert exists. This allows the type system to catch problems rather than have them only be caught at run-time. 

BAD:

dart

```
class A {
  A.c1(this.p) : assert(p != null);
  A.c2(this.p);
  final String? p;
}
```

content_copy

GOOD:

dart

```
class A {
  A.c1(String this.p);
  A.c2(this.p);
  final String? p;
}
​
class B {
  String? b;
  B(this.b);
}
​
class C extends B {
  B(String super.b);
}
```

content_copy

## Enable

[#](#enable)

 To enable the `tighten_type_of_initializing_formals` rule, add `tighten_type_of_initializing_formals` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - tighten_type_of_initializing_formals
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `tighten_type_of_initializing_formals: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    tighten_type_of_initializing_formals: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/tighten_type_of_initializing_formals).
