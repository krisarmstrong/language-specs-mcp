Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_types_on_closure_parameters](/tools/linter-rules/avoid_types_on_closure_parameters)

# avoid_types_on_closure_parameters

Learn about the avoid_types_on_closure_parameters linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_types_on_closure_parameters)

verified_userStablebuildFix available

Avoid annotating types for function expression parameters.

## Details

[#](#details)

AVOID annotating types for function expression parameters.

 Annotating types for function expression parameters is usually unnecessary because the parameter types can almost always be inferred from the context, thus making the practice redundant. 

BAD:

dart

```
var names = people.map((Person person) => person.name);
```

content_copy

GOOD:

dart

```
var names = people.map((person) => person.name);
```

content_copy

## Incompatible rules

[#](#incompatible-rules)

The `avoid_types_on_closure_parameters` lint is incompatible with the following rules:

- [always_specify_types](/tools/linter-rules/always_specify_types)

## Enable

[#](#enable)

 To enable the `avoid_types_on_closure_parameters` rule, add `avoid_types_on_closure_parameters` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_types_on_closure_parameters
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_types_on_closure_parameters: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_types_on_closure_parameters: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_types_on_closure_parameters).
