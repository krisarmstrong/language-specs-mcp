Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [omit_local_variable_types](/tools/linter-rules/omit_local_variable_types)

# omit_local_variable_types

Learn about the omit_local_variable_types linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/omit_local_variable_types)

verified_userStablebuildFix available

Omit type annotations for local variables.

## Details

[#](#details)

DON'T redundantly type annotate initialized local variables.

 Local variables, especially in modern code where functions tend to be small, have very little scope. Omitting the type focuses the reader's attention on the more important name of the variable and its initialized value. 

BAD:

dart

```
List<List<Ingredient>> possibleDesserts(Set<Ingredient> pantry) {
  List<List<Ingredient>> desserts = <List<Ingredient>>[];
  for (final List<Ingredient> recipe in cookbook) {
    if (pantry.containsAll(recipe)) {
      desserts.add(recipe);
    }
  }
​
  return desserts;
}
```

content_copy

GOOD:

dart

```
List<List<Ingredient>> possibleDesserts(Set<Ingredient> pantry) {
  var desserts = <List<Ingredient>>[];
  for (final recipe in cookbook) {
    if (pantry.containsAll(recipe)) {
      desserts.add(recipe);
    }
  }
​
  return desserts;
}
```

content_copy

 Sometimes the inferred type is not the type you want the variable to have. For example, you may intend to assign values of other types later. In that case, annotate the variable with the type you want. 

GOOD:

dart

```
Widget build(BuildContext context) {
  Widget result = Text('You won!');
  if (applyPadding) {
    result = Padding(padding: EdgeInsets.all(8.0), child: result);
  }
  return result;
}
```

content_copy

## Incompatible rules

[#](#incompatible-rules)

The `omit_local_variable_types` lint is incompatible with the following rules:

- [always_specify_types](/tools/linter-rules/always_specify_types)
- [specify_nonobvious_local_variable_types](/tools/linter-rules/specify_nonobvious_local_variable_types)

## Enable

[#](#enable)

 To enable the `omit_local_variable_types` rule, add `omit_local_variable_types` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - omit_local_variable_types
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `omit_local_variable_types: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    omit_local_variable_types: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/omit_local_variable_types).
