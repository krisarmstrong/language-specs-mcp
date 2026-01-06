Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_final_parameters](/tools/linter-rules/avoid_final_parameters)

# avoid_final_parameters

Learn about the avoid_final_parameters linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_final_parameters)

verified_userStable

Avoid `final` for parameter declarations.

## Details

[#](#details)

AVOID declaring parameters as `final`.

 Declaring parameters as `final` can lead to unnecessarily verbose code, especially when using the "parameter_assignments" rule. 

BAD:

dart

```
void goodParameter(final String label) { // LINT
  print(label);
}
```

content_copy

GOOD:

dart

```
void badParameter(String label) { // OK
  print(label);
}
```

content_copy

BAD:

dart

```
void goodExpression(final int value) => print(value); // LINT
```

content_copy

GOOD:

dart

```
void badExpression(int value) => print(value); // OK
```

content_copy

BAD:

dart

```
[1, 4, 6, 8].forEach((final value) => print(value + 2)); // LINT
```

content_copy

GOOD:

dart

```
[1, 4, 6, 8].forEach((value) => print(value + 2)); // OK
```

content_copy

## Incompatible rules

[#](#incompatible-rules)

The `avoid_final_parameters` lint is incompatible with the following rules:

- [prefer_final_parameters](/tools/linter-rules/prefer_final_parameters)

## Enable

[#](#enable)

 To enable the `avoid_final_parameters` rule, add `avoid_final_parameters` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_final_parameters
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_final_parameters: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_final_parameters: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_final_parameters).
