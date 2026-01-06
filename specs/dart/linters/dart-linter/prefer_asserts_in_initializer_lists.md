Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_asserts_in_initializer_lists](/tools/linter-rules/prefer_asserts_in_initializer_lists)

# prefer_asserts_in_initializer_lists

Learn about the prefer_asserts_in_initializer_lists linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_asserts_in_initializer_lists)

verified_userStable

Prefer putting asserts in initializer lists.

## Details

[#](#details)

DO put asserts in initializer lists.

BAD:

dart

```
class A {
  A(int a) {
    assert(a != 0);
  }
}
```

content_copy

GOOD:

dart

```
class A {
  A(int a) : assert(a != 0);
}
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_asserts_in_initializer_lists` rule, add `prefer_asserts_in_initializer_lists` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_asserts_in_initializer_lists
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_asserts_in_initializer_lists: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_asserts_in_initializer_lists: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_asserts_in_initializer_lists).
