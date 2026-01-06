Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [specify_nonobvious_property_types](/tools/linter-rules/specify_nonobvious_property_types)

# specify_nonobvious_property_types

Learn about the specify_nonobvious_property_types linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/specify_nonobvious_property_types)

scienceExperimentalbuildFix available

Specify non-obvious type annotations for top-level and static variables.

## Details

[#](#details)

 Do type annotate initialized top-level or static variables when the type is [non-obvious](https://dart.dev/glossary/obviously-typed). 

 Type annotations on top-level or static variables can serve as a request for type inference, documenting the expected outcome of the type inference step, and declaratively allowing the compiler and analyzer to solve the possibly complex task of finding type arguments and annotations in the initializing expression that yield the desired result. 

 Type annotations on top-level or static variables can also inform readers about the type of the initializing expression, which will allow them to proceed reading the locations in code where this variable is used with known good information about the type of the given variable (which may not be immediately evident by looking at the initializing expression). 

BAD:

dart

```
final myTopLevelVariable =
    genericFunctionWrittenByOtherFolks(with, args);
​
class A {
  static var myStaticVariable =
      myTopLevelVariable.update('foo', null);
}
```

content_copy

GOOD:

dart

```
final Map<String, Widget?> myTopLevelVariable =
    genericFunctionWrittenByOtherFolks(with, args);
​
class A {
  static Map<String, Widget?> myStaticVariable =
      myTopLevelVariable.update('foo', null);
}
```

content_copy

This rule is experimental. It is being evaluated, and it might be changed or removed. Feedback on its behavior is welcome! The primary relevant issue is [dart-lang/sdk#59550](https://github.com/dart-lang/sdk/issues/59550). 

## Enable

[#](#enable)

 To enable the `specify_nonobvious_property_types` rule, add `specify_nonobvious_property_types` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - specify_nonobvious_property_types
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `specify_nonobvious_property_types: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    specify_nonobvious_property_types: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/specify_nonobvious_property_types).
