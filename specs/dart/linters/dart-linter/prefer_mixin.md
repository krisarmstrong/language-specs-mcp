Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_mixin](/tools/linter-rules/prefer_mixin)

# prefer_mixin

Learn about the prefer_mixin linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_mixin)

verified_userStable

Prefer using mixins.

## Details

[#](#details)

 Dart 2.1 introduced a new syntax for mixins that provides a safe way for a mixin to invoke inherited members using `super`. The new style of mixins should always be used for types that are to be mixed in. As a result, this lint will flag any uses of a class in a `with` clause. 

BAD:

dart

```
class A {}
class B extends Object with A {}
```

content_copy

OK:

dart

```
mixin M {}
class C with M {}
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_mixin` rule, add `prefer_mixin` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_mixin
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_mixin: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_mixin: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_mixin).
