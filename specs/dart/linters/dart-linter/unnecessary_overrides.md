Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_overrides](/tools/linter-rules/unnecessary_overrides)

# unnecessary_overrides

Learn about the unnecessary_overrides linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_overrides)

verified_userStablecirclesCorebuildFix available

Don't override a method to do a super method invocation with the same parameters.

## Details

[#](#details)

DON'T override a method to do a super method invocation with same parameters.

BAD:

dart

```
class A extends B {
  @override
  void foo() {
    super.foo();
  }
}
```

content_copy

GOOD:

dart

```
class A extends B {
  @override
  void foo() {
    doSomethingElse();
  }
}
```

content_copy

It's valid to override a member in the following cases:

-  if a type (return type or a parameter type) is not the exactly the same as the super member, 
- if the `covariant` keyword is added to one of the parameters,
- if documentation comments are present on the member,
- if the member has annotations other than `@override`,
- if the member is not annotated with `@protected`, and the super member is.

`noSuchMethod` is a special method and is not checked by this rule.

## Enable

[#](#enable)

 To enable the `unnecessary_overrides` rule, add `unnecessary_overrides` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_overrides
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_overrides: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_overrides: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_overrides).
