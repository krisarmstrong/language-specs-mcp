Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [provide_deprecation_message](/tools/linter-rules/provide_deprecation_message)

# provide_deprecation_message

Learn about the provide_deprecation_message linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/provide_deprecation_message)

verified_userStablecirclesCore

Provide a deprecation message, via `@Deprecated("message")`.

## Details

[#](#details)

DO specify a deprecation message (with migration instructions and/or a removal schedule) in the `Deprecated` constructor. 

BAD:

dart

```
@deprecated
void oldFunction(arg1, arg2) {}
```

content_copy

GOOD:

dart

```
@Deprecated("""
[oldFunction] is being deprecated in favor of [newFunction] (with slightly
different parameters; see [newFunction] for more information). [oldFunction]
will be removed on or after the 4.0.0 release.
""")
void oldFunction(arg1, arg2) {}
```

content_copy

## Enable

[#](#enable)

 To enable the `provide_deprecation_message` rule, add `provide_deprecation_message` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - provide_deprecation_message
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `provide_deprecation_message: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    provide_deprecation_message: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/provide_deprecation_message).
