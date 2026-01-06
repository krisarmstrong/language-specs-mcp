Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [join_return_with_assignment](/tools/linter-rules/join_return_with_assignment)

# join_return_with_assignment

Learn about the join_return_with_assignment linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/join_return_with_assignment)

verified_userStable

Join return statement with assignment when possible.

## Details

[#](#details)

DO join return statement with assignment when possible.

BAD:

dart

```
class A {
  B _lazyInstance;
  static B get instance {
    _lazyInstance ??= B(); // LINT
    return _lazyInstance;
  }
}
```

content_copy

GOOD:

dart

```
class A {
  B _lazyInstance;
  static B get instance => _lazyInstance ??= B();
}
```

content_copy

## Enable

[#](#enable)

 To enable the `join_return_with_assignment` rule, add `join_return_with_assignment` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - join_return_with_assignment
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `join_return_with_assignment: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    join_return_with_assignment: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/join_return_with_assignment).
