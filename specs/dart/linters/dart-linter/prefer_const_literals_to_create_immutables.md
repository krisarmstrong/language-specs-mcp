Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_const_literals_to_create_immutables](/tools/linter-rules/prefer_const_literals_to_create_immutables)

# prefer_const_literals_to_create_immutables

Learn about the prefer_const_literals_to_create_immutables linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_const_literals_to_create_immutables)

verified_userStablebuildFix available

Prefer const literals as parameters of constructors on @immutable classes.

## Details

[#](#details)

PREFER using `const` for instantiating list, map and set literals used as parameters in immutable class instantiations. 

BAD:

dart

```
@immutable
class A {
  A(this.v);
  final v;
}
​
A a1 = new A([1]);
A a2 = new A({});
```

content_copy

GOOD:

dart

```
A a1 = new A(const [1]);
A a2 = new A(const {});
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_const_literals_to_create_immutables` rule, add `prefer_const_literals_to_create_immutables` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_const_literals_to_create_immutables
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_const_literals_to_create_immutables: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_const_literals_to_create_immutables: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_const_literals_to_create_immutables).
