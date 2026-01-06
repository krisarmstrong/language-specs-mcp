Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_const_constructors](/tools/linter-rules/prefer_const_constructors)

# prefer_const_constructors

Learn about the prefer_const_constructors linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_const_constructors)

verified_userStablebuildFix available

Prefer `const` with constant constructors.

## Details

[#](#details)

PREFER using `const` for instantiating constant constructors.

 If a constructor can be invoked as const to produce a canonicalized instance, it's preferable to do so. 

BAD:

dart

```
class A {
  const A();
}
​
void accessA() {
  A a = new A();
}
```

content_copy

GOOD:

dart

```
class A {
  const A();
}
​
void accessA() {
  A a = const A();
}
```

content_copy

GOOD:

dart

```
class A {
  final int x;
​
  const A(this.x);
}
​
A foo(int x) => new A(x);
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_const_constructors` rule, add `prefer_const_constructors` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_const_constructors
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_const_constructors: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_const_constructors: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_const_constructors).
