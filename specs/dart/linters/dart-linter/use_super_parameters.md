Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_super_parameters](/tools/linter-rules/use_super_parameters)

# use_super_parameters

Learn about the use_super_parameters linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_super_parameters)

scienceExperimentalthumb_upRecommendedbuildFix available

Use super-initializer parameters where possible.

## Details

[#](#details)

 "Forwarding constructor"s, that do nothing except forward parameters to their superclass constructors should take advantage of super-initializer parameters rather than repeating the names of parameters when passing them to the superclass constructors. This makes the code more concise and easier to read and maintain. 

DO use super-initializer parameters where possible.

BAD:

dart

```
class A {
  A({int? x, int? y});
}
class B extends A {
  B({int? x, int? y}) : super(x: x, y: y);
}
```

content_copy

GOOD:

dart

```
class A {
  A({int? x, int? y});
}
class B extends A {
  B({super.x, super.y});
}
```

content_copy

## Enable

[#](#enable)

 To enable the `use_super_parameters` rule, add `use_super_parameters` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_super_parameters
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_super_parameters: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_super_parameters: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_super_parameters).
