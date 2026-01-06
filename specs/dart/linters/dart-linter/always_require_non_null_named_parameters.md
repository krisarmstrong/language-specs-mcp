Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [always_require_non_null_named_parameters](/tools/linter-rules/always_require_non_null_named_parameters)

# always_require_non_null_named_parameters

Learn about the always_require_non_null_named_parameters linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/always_require_non_null_named_parameters)

errorRemoved

Specify `@required` on named parameters without defaults.

## Details

[#](#details)

NOTE: This rule is removed in Dart 3.3.0; it is no longer functional.

DO specify `@required` on named parameters without a default value on which an `assert(param != null)` is done. 

BAD:

dart

```
m1({a}) {
  assert(a != null);
}
```

content_copy

GOOD:

dart

```
m1({@required a}) {
  assert(a != null);
}
​
m2({a: 1}) {
  assert(a != null);
}
```

content_copy

NOTE: Only asserts at the start of the bodies will be taken into account.

## Enable

[#](#enable)

 To enable the `always_require_non_null_named_parameters` rule, add `always_require_non_null_named_parameters` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - always_require_non_null_named_parameters
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `always_require_non_null_named_parameters: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    always_require_non_null_named_parameters: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/always_require_non_null_named_parameters).
