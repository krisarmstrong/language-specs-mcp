Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [specify_nonobvious_local_variable_types](/tools/linter-rules/specify_nonobvious_local_variable_types)

# specify_nonobvious_local_variable_types

Learn about the specify_nonobvious_local_variable_types linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/specify_nonobvious_local_variable_types)

scienceExperimentalbuildFix available

Specify non-obvious type annotations for local variables.

## Details

[#](#details)

 Do type annotate initialized local variables when the type is [non-obvious](https://dart.dev/glossary/obviously-typed). 

 Type annotations on local variables can serve as a request for type inference, documenting the expected outcome of the type inference step, and declaratively allowing the compiler and analyzer to solve the possibly complex task of finding type arguments and annotations in the initializing expression that yield the desired result. 

 Type annotations on local variables can also inform readers about the type of the initializing expression, which will allow them to proceed reading the subsequent lines of code with known good information about the type of the given variable (which may not be immediately evident by looking at the initializing expression). 

BAD:

dart

```
List<List<Ingredient>> possibleDesserts(Set<Ingredient> pantry) {
  var desserts = genericFunctionDeclaredFarAway(<num>[42], 'Something');
  for (final recipe in cookbook) {
    if (pantry.containsAll(recipe)) {
      desserts.add(recipe);
    }
  }
​
  return desserts;
}
​
const List<List<Ingredient>> cookbook = ...;
```

content_copy

GOOD:

dart

```
List<List<Ingredient>> possibleDesserts(Set<Ingredient> pantry) {
  List<List<Ingredient>> desserts = genericFunctionDeclaredFarAway(
    <num>[42],
    'Something',
  );
  for (final List<Ingredient> recipe in cookbook) {
    if (pantry.containsAll(recipe)) {
      desserts.add(recipe);
    }
  }
​
  return desserts;
}
​
const List<List<Ingredient>> cookbook = ...;
```

content_copy

This rule is experimental. It is being evaluated, and it might be changed or removed. Feedback on its behavior is welcome! The primary relevant issue is [dart-lang/sdk#58773](https://github.com/dart-lang/sdk/issues/58773). 

## Incompatible rules

[#](#incompatible-rules)

 The `specify_nonobvious_local_variable_types` lint is incompatible with the following rules: 

- [omit_local_variable_types](/tools/linter-rules/omit_local_variable_types)

## Enable

[#](#enable)

 To enable the `specify_nonobvious_local_variable_types` rule, add `specify_nonobvious_local_variable_types` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - specify_nonobvious_local_variable_types
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `specify_nonobvious_local_variable_types: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    specify_nonobvious_local_variable_types: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/specify_nonobvious_local_variable_types).
