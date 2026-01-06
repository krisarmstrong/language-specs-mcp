Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [omit_obvious_property_types](/tools/linter-rules/omit_obvious_property_types)

# omit_obvious_property_types

Learn about the omit_obvious_property_types linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/omit_obvious_property_types)

scienceExperimentalbuildFix available

Omit obvious type annotations for top-level and static variables.

## Details

[#](#details)

 Don't type annotate initialized top-level or static variables when the type is [obvious](https://dart.dev/glossary/obviously-typed). 

BAD:

dart

```
final int myTopLevelVariable = 7;
​
class A {
  static String myStaticVariable = 'Hello';
}
```

content_copy

GOOD:

dart

```
final myTopLevelVariable = 7;
​
class A {
  static myStaticVariable = 'Hello';
}
```

content_copy

 Sometimes the inferred type is not the type you want the variable to have. For example, you may intend to assign values of other types later. You may also wish to write a type annotation explicitly because the type of the initializing expression is non-obvious and it will be helpful for future readers of the code to document this type. Or you may wish to commit to a specific type such that future updates of dependencies (in nearby code, in imports, anywhere) will not silently change the type of that variable, thus introducing compile-time errors or run-time bugs in locations where this variable is used. In those cases, go ahead and annotate the variable with the type you want. 

GOOD:

dart

```
final num myTopLevelVariable = 7;
​
class A {
  static String? myStaticVariable = 'Hello';
}
```

content_copy

This rule is experimental. It is being evaluated, and it might be changed or removed. Feedback on its behavior is welcome! The primary relevant issue is [dart-lang/sdk#59550](https://github.com/dart-lang/sdk/issues/59550). 

## Incompatible rules

[#](#incompatible-rules)

The `omit_obvious_property_types` lint is incompatible with the following rules:

- [always_specify_types](/tools/linter-rules/always_specify_types)
- [type_annotate_public_apis](/tools/linter-rules/type_annotate_public_apis)

## Enable

[#](#enable)

 To enable the `omit_obvious_property_types` rule, add `omit_obvious_property_types` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - omit_obvious_property_types
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `omit_obvious_property_types: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    omit_obvious_property_types: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/omit_obvious_property_types).
