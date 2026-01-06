Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [type_annotate_public_apis](/tools/linter-rules/type_annotate_public_apis)

# type_annotate_public_apis

Learn about the type_annotate_public_apis linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/type_annotate_public_apis)

verified_userStablebuildFix available

Type annotate public APIs.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/design#do-type-annotate-fields-and-top-level-variables-if-the-type-isnt-obvious): 

PREFER type annotating public APIs.

 Type annotations are important documentation for how a library should be used. Annotating the parameter and return types of public methods and functions helps users understand what the API expects and what it provides. 

 Note that if a public API accepts a range of values that Dart's type system cannot express, then it is acceptable to leave that untyped. In that case, the implicit `dynamic` is the correct type for the API. 

 For code internal to a library (either private, or things like nested functions) annotate where you feel it helps, but don't feel that you must provide them. 

BAD:

dart

```
install(id, destination) {
  // ...
}
```

content_copy

 Here, it's unclear what `id` is. A string? And what is `destination`? A string or a `File` object? Is this method synchronous or asynchronous? 

GOOD:

dart

```
Future<bool> install(PackageId id, String destination) {
  // ...
}
```

content_copy

With types, all of this is clarified.

## Incompatible rules

[#](#incompatible-rules)

The `type_annotate_public_apis` lint is incompatible with the following rules:

- [omit_obvious_property_types](/tools/linter-rules/omit_obvious_property_types)

## Enable

[#](#enable)

 To enable the `type_annotate_public_apis` rule, add `type_annotate_public_apis` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - type_annotate_public_apis
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `type_annotate_public_apis: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    type_annotate_public_apis: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/type_annotate_public_apis).
