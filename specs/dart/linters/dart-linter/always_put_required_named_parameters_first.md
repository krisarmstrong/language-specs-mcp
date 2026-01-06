Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [always_put_required_named_parameters_first](/tools/linter-rules/always_put_required_named_parameters_first)

# always_put_required_named_parameters_first

Learn about the always_put_required_named_parameters_first linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/always_put_required_named_parameters_first)

verified_userStablebuildFix available

Put required named parameters first.

## Details

[#](#details)

DO specify `required` on named parameter before other named parameters.

BAD:

dart

```
m({b, c, required a}) ;
```

content_copy

GOOD:

dart

```
m({required a, b, c}) ;
```

content_copy

BAD:

dart

```
m({b, c, @required a}) ;
```

content_copy

GOOD:

dart

```
m({@required a, b, c}) ;
```

content_copy

## Enable

[#](#enable)

 To enable the `always_put_required_named_parameters_first` rule, add `always_put_required_named_parameters_first` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - always_put_required_named_parameters_first
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `always_put_required_named_parameters_first: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    always_put_required_named_parameters_first: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/always_put_required_named_parameters_first).
