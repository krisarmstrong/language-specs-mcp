Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [exhaustive_cases](/tools/linter-rules/exhaustive_cases)

# exhaustive_cases

Learn about the exhaustive_cases linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/exhaustive_cases)

verified_userStablethumb_upRecommendedbuildFix available

Define case clauses for all constants in enum-like classes.

## Details

[#](#details)

Switching on instances of enum-like classes should be exhaustive.

Enum-like classes are defined as concrete (non-abstract) classes that have:

- only private non-factory constructors
- two or more static const fields whose type is the enclosing class and
- no subclasses of the class in the defining library

DO define case clauses for all constants in enum-like classes.

BAD:

dart

```
class EnumLike {
  final int i;
  const EnumLike._(this.i);
​
  static const e = EnumLike._(1);
  static const f = EnumLike._(2);
  static const g = EnumLike._(3);
}
​
void bad(EnumLike e) {
  // Missing case.
  switch(e) { // LINT
    case EnumLike.e :
      print('e');
      break;
    case EnumLike.f :
      print('f');
      break;
  }
}
```

content_copy

GOOD:

dart

```
class EnumLike {
  final int i;
  const EnumLike._(this.i);
​
  static const e = EnumLike._(1);
  static const f = EnumLike._(2);
  static const g = EnumLike._(3);
}
​
void ok(EnumLike e) {
  // All cases covered.
  switch(e) { // OK
    case EnumLike.e :
      print('e');
      break;
    case EnumLike.f :
      print('f');
      break;
    case EnumLike.g :
      print('g');
      break;
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `exhaustive_cases` rule, add `exhaustive_cases` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - exhaustive_cases
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `exhaustive_cases: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    exhaustive_cases: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/exhaustive_cases).
