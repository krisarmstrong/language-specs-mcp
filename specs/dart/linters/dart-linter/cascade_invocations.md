Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [cascade_invocations](/tools/linter-rules/cascade_invocations)

# cascade_invocations

Learn about the cascade_invocations linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/cascade_invocations)

verified_userStablebuildFix available

Cascade consecutive method invocations on the same reference.

## Details

[#](#details)

DO Use the cascading style when successively invoking methods on the same reference. 

BAD:

dart

```
SomeClass someReference = SomeClass();
someReference.firstMethod();
someReference.secondMethod();
```

content_copy

BAD:

dart

```
SomeClass someReference = SomeClass();
...
someReference.firstMethod();
someReference.aProperty = value;
someReference.secondMethod();
```

content_copy

GOOD:

dart

```
SomeClass someReference = SomeClass()
    ..firstMethod()
    ..aProperty = value
    ..secondMethod();
```

content_copy

GOOD:

dart

```
SomeClass someReference = SomeClass();
...
someReference
    ..firstMethod()
    ..aProperty = value
    ..secondMethod();
```

content_copy

## Enable

[#](#enable)

 To enable the `cascade_invocations` rule, add `cascade_invocations` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - cascade_invocations
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `cascade_invocations: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    cascade_invocations: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/cascade_invocations).
