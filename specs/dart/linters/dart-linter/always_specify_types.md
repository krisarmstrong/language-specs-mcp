Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [always_specify_types](/tools/linter-rules/always_specify_types)

# always_specify_types

Learn about the always_specify_types linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/always_specify_types)

verified_userStablebuildFix available

Specify type annotations.

## Details

[#](#details)

From the [style guide for the flutter repo](https://flutter.dev/style-guide/):

DO specify type annotations.

 Avoid `var` when specifying that a type is unknown and short-hands that elide type annotations. Use `dynamic` if you are being explicit that the type is unknown. Use `Object` if you are being explicit that you want an object that implements `==` and `hashCode`. 

BAD:

dart

```
var foo = 10;
final bar = Bar();
const quux = 20;
```

content_copy

GOOD:

dart

```
int foo = 10;
final Bar bar = Bar();
String baz = 'hello';
const int quux = 20;
```

content_copy

 NOTE: Using the `@optionalTypeArgs` annotation in the `meta` package, API authors can special-case type parameters whose type needs to be dynamic but whose declaration should be treated as optional. For example, suppose you have a `Key` object whose type parameter you'd like to treat as optional. Using the `@optionalTypeArgs` would look like this: 

dart

```
import 'package:meta/meta.dart';
​
@optionalTypeArgs
class Key<T> {
 ...
}
​
void main() {
  Key s = Key(); // OK!
}
```

content_copy

## Incompatible rules

[#](#incompatible-rules)

The `always_specify_types` lint is incompatible with the following rules:

- [avoid_types_on_closure_parameters](/tools/linter-rules/avoid_types_on_closure_parameters)
- [omit_local_variable_types](/tools/linter-rules/omit_local_variable_types)
- [omit_obvious_local_variable_types](/tools/linter-rules/omit_obvious_local_variable_types)
- [omit_obvious_property_types](/tools/linter-rules/omit_obvious_property_types)

## Enable

[#](#enable)

 To enable the `always_specify_types` rule, add `always_specify_types` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - always_specify_types
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `always_specify_types: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    always_specify_types: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/always_specify_types).
