Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [diagnostic_describe_all_properties](/tools/linter-rules/diagnostic_describe_all_properties)

# diagnostic_describe_all_properties

Learn about the diagnostic_describe_all_properties linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/diagnostic_describe_all_properties)

verified_userStablebuildFix available

DO reference all public properties in debug methods.

## Details

[#](#details)

DO reference all public properties in `debug` method implementations.

 Implementers of `Diagnosticable` should reference all public properties in a `debugFillProperties(...)` or `debugDescribeChildren(...)` method implementation to improve debuggability at runtime. 

Public properties are defined as fields and getters that are

- not package-private (e.g., prefixed with `_`)
- not `static` or overriding
- not themselves `Widget`s or collections of `Widget`s

 In addition, the "debug" prefix is treated specially for properties in Flutter. For the purposes of diagnostics, a property `foo` and a prefixed property `debugFoo` are treated as effectively describing the same property and it is sufficient to refer to one or the other. 

BAD:

dart

```
class Absorber extends Widget {
  bool get absorbing => _absorbing;
  bool _absorbing;
  bool get ignoringSemantics => _ignoringSemantics;
  bool _ignoringSemantics;
  @override
  void debugFillProperties(DiagnosticPropertiesBuilder properties) {
    super.debugFillProperties(properties);
    properties.add(DiagnosticsProperty<bool>('absorbing', absorbing));
    // Missing reference to ignoringSemantics
  }
}
```

content_copy

GOOD:

dart

```
class Absorber extends Widget {
  bool get absorbing => _absorbing;
  bool _absorbing;
  bool get ignoringSemantics => _ignoringSemantics;
  bool _ignoringSemantics;
  @override
  void debugFillProperties(DiagnosticPropertiesBuilder properties) {
    super.debugFillProperties(properties);
    properties.add(DiagnosticsProperty<bool>('absorbing', absorbing));
    properties.add(DiagnosticsProperty<bool>('ignoringSemantics', ignoringSemantics));
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `diagnostic_describe_all_properties` rule, add `diagnostic_describe_all_properties` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - diagnostic_describe_all_properties
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `diagnostic_describe_all_properties: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    diagnostic_describe_all_properties: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/diagnostic_describe_all_properties).
