Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [no_default_cases](/tools/linter-rules/no_default_cases)

# no_default_cases

Learn about the no_default_cases linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_default_cases)

scienceExperimental

No default cases.

## Details

[#](#details)

Switches on enums and enum-like classes should not use a `default` clause.

Enum-like classes are defined as concrete (non-abstract) classes that have:

- only private non-factory constructors
- two or more static const fields whose type is the enclosing class and
- no subclasses of the class in the defining library

DO define default behavior outside switch statements.

BAD:

dart

```
  switch (testEnum) {
    case TestEnum.A:
      return '123';
    case TestEnum.B:
      return 'abc';
    default:
      return null;
  }
```

content_copy

GOOD:

dart

```
  switch (testEnum) {
    case TestEnum.A:
      return '123';
    case TestEnum.B:
      return 'abc';
  }
  // Default here.
  return null;
```

content_copy

## Enable

[#](#enable)

 To enable the `no_default_cases` rule, add `no_default_cases` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - no_default_cases
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `no_default_cases: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    no_default_cases: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_default_cases).
