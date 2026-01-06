Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_positional_boolean_parameters](/tools/linter-rules/avoid_positional_boolean_parameters)

# avoid_positional_boolean_parameters

Learn about the avoid_positional_boolean_parameters linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_positional_boolean_parameters)

verified_userStable

Avoid positional boolean parameters.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/design#avoid-positional-boolean-parameters): 

AVOID positional boolean parameters.

 Positional boolean parameters are a bad practice because they are very ambiguous. Using named boolean parameters is much more readable because it inherently describes what the boolean value represents. 

BAD:

dart

```
Task(true);
Task(false);
ListBox(false, true, true);
Button(false);
```

content_copy

GOOD:

dart

```
Task.oneShot();
Task.repeating();
ListBox(scroll: true, showScrollbars: true);
Button(ButtonState.enabled);
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_positional_boolean_parameters` rule, add `avoid_positional_boolean_parameters` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_positional_boolean_parameters
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_positional_boolean_parameters: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_positional_boolean_parameters: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_positional_boolean_parameters).
