Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [always_declare_return_types](/tools/linter-rules/always_declare_return_types)

# always_declare_return_types

Learn about the always_declare_return_types linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/always_declare_return_types)

verified_userStablebuildFix available

Declare method return types.

## Details

[#](#details)

DO declare method return types.

 When declaring a method or function always specify a return type. Declaring return types for functions helps improve your codebase by allowing the analyzer to more adequately check your code for errors that could occur during runtime. 

BAD:

dart

```
main() { }
​
_bar() => _Foo();
​
class _Foo {
  _foo() => 42;
}
```

content_copy

GOOD:

dart

```
void main() { }
​
_Foo _bar() => _Foo();
​
class _Foo {
  int _foo() => 42;
}
​
typedef predicate = bool Function(Object o);
```

content_copy

## Enable

[#](#enable)

 To enable the `always_declare_return_types` rule, add `always_declare_return_types` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - always_declare_return_types
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `always_declare_return_types: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    always_declare_return_types: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/always_declare_return_types).
