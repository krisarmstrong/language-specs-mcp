Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_as](/tools/linter-rules/avoid_as)

# avoid_as

Learn about the avoid_as linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_as)

errorRemoved

Avoid using `as`.

## Details

[#](#details)

 NOTE: This rule was removed from the SDK in Dart 3; it is no longer functional. Its advice is compiler-specific and mostly obsolete with null safety. 

AVOID using `as`.

 If you know the type is correct, use an assertion or assign to a more narrowly-typed variable (this avoids the type check in release mode; `as` is not compiled out in release mode). If you don't know whether the type is correct, check using `is` (this avoids the exception that `as` raises). 

BAD:

dart

```
(pm as Person).firstName = 'Seth';
```

content_copy

GOOD:

dart

```
if (pm is Person)
  pm.firstName = 'Seth';
```

content_copy

but certainly not

BAD:

dart

```
try {
   (pm as Person).firstName = 'Seth';
} on CastError { }
```

content_copy

 Note that an exception is made in the case of `dynamic` since the cast has no performance impact. 

OK:

dart

```
HasScrollDirection scrollable = renderObject as dynamic;
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_as` rule, add `avoid_as` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_as
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_as: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_as: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_as).
