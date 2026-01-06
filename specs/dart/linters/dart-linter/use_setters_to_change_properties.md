Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_setters_to_change_properties](/tools/linter-rules/use_setters_to_change_properties)

# use_setters_to_change_properties

Learn about the use_setters_to_change_properties linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_setters_to_change_properties)

verified_userStable

Use a setter for operations that conceptually change a property.

## Details

[#](#details)

DO use a setter for operations that conceptually change a property.

BAD:

dart

```
rectangle.setWidth(3);
button.setVisible(false);
```

content_copy

GOOD:

dart

```
rectangle.width = 3;
button.visible = false;
```

content_copy

## Enable

[#](#enable)

 To enable the `use_setters_to_change_properties` rule, add `use_setters_to_change_properties` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_setters_to_change_properties
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_setters_to_change_properties: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_setters_to_change_properties: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_setters_to_change_properties).
