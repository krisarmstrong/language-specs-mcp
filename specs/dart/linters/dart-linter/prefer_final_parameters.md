Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_final_parameters](/tools/linter-rules/prefer_final_parameters)

# prefer_final_parameters

Learn about the prefer_final_parameters linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_final_parameters)

reportDeprecatedbuildFix available

Prefer final for parameter declarations if they are not reassigned.

## Details

[#](#details)

Note: This lint rule was deprecated in Dart 3.11 and is set to be removed in a future release of the Dart SDK. Also note that the lint is not applied to code that is opted in to the `primary-constructors` language feature where using `final` for a parameter becomes a compile-time error. If you want to ensure parameters aren't reassigned in function bodies, consider enabling the [parameter_assignments](https://dart.dev/lints/parameter_assignments) lint rule instead. 

DO prefer declaring parameters as final if they are not reassigned in the function body. 

 Declaring parameters as final when possible is a good practice because it helps avoid accidental reassignments. 

BAD:

dart

```
void badParameter(String label) { // LINT
  print(label);
}
```

content_copy

GOOD:

dart

```
void goodParameter(final String label) { // OK
  print(label);
}
```

content_copy

BAD:

dart

```
void badExpression(int value) => print(value); // LINT
```

content_copy

GOOD:

dart

```
void goodExpression(final int value) => print(value); // OK
```

content_copy

BAD:

dart

```
[1, 4, 6, 8].forEach((value) => print(value + 2)); // LINT
```

content_copy

GOOD:

dart

```
[1, 4, 6, 8].forEach((final value) => print(value + 2)); // OK
```

content_copy

GOOD:

dart

```
void mutableParameter(String label) { // OK
  print(label);
  label = 'Hello Linter!';
  print(label);
}
```

content_copy

## Incompatible rules

[#](#incompatible-rules)

The `prefer_final_parameters` lint is incompatible with the following rules:

- [unnecessary_final](/tools/linter-rules/unnecessary_final)
- [avoid_final_parameters](/tools/linter-rules/avoid_final_parameters)

## Enable

[#](#enable)

 To enable the `prefer_final_parameters` rule, add `prefer_final_parameters` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_final_parameters
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_final_parameters: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_final_parameters: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_final_parameters).
