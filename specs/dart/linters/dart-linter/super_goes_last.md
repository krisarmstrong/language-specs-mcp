Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [super_goes_last](/tools/linter-rules/super_goes_last)

# super_goes_last

Learn about the super_goes_last linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/super_goes_last)

errorRemoved

Place the `super` call last in a constructor initialization list.

## Details

[#](#details)

NOTE: This rule is removed in Dart 3.0.0; it is no longer functional.

DO place the `super` call last in a constructor initialization list.

 Field initializers are evaluated in the order that they appear in the constructor initialization list. If you place a `super()` call in the middle of an initializer list, the superclass's initializers will be evaluated right then before evaluating the rest of the subclass's initializers. 

 What it doesn't mean is that the superclass's constructor body will be executed then. That always happens after all initializers are run regardless of where `super` appears. It's vanishingly rare that the order of initializers matters, so the placement of `super` in the list almost never matters either. 

 Getting in the habit of placing it last improves consistency, visually reinforces when the superclass's constructor body is run, and may help performance. 

BAD:dart

```
```

content_copyView(Style style, List children)

 super(style), _children = children { 

```

**GOOD:**
```dart
View(Style style, List children)
    : _children = children,
      super(style) {
```

content_copy

## Enable

[#](#enable)

 To enable the `super_goes_last` rule, add `super_goes_last` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - super_goes_last
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `super_goes_last: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    super_goes_last: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/super_goes_last).
