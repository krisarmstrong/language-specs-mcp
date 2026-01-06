Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [matching_super_parameters](/tools/linter-rules/matching_super_parameters)

# matching_super_parameters

Learn about the matching_super_parameters linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/matching_super_parameters)

verified_userStable

Use matching super parameter names.

## Details

[#](#details)

DO use super parameter names that match their corresponding super constructor's parameter names. 

BAD:

dart

```
class Rectangle {
  final int width;
  final int height;
​
  Rectangle(this.width, this.height);
}
​
class ColoredRectangle extends Rectangle {
  final Color color;
​
  ColoredRectangle(
    this.color,
    super.height, // Bad, actually corresponds to the `width` parameter.
    super.width, // Bad, actually corresponds to the `height` parameter.
  );
}
```

content_copy

GOOD:

dart

```
class Rectangle {
  final int width;
  final int height;
​
  Rectangle(this.width, this.height);
}
​
class ColoredRectangle extends Rectangle {
  final Color color;
​
  ColoredRectangle(
    this.color,
    super.width,
    super.height,
  );
}
```

content_copy

## Enable

[#](#enable)

 To enable the `matching_super_parameters` rule, add `matching_super_parameters` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - matching_super_parameters
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `matching_super_parameters: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    matching_super_parameters: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/matching_super_parameters).
