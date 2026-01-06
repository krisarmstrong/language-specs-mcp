Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [one_member_abstracts](/tools/linter-rules/one_member_abstracts)

# one_member_abstracts

Learn about the one_member_abstracts linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/one_member_abstracts)

verified_userStable

Avoid defining a one-member abstract class when a simple function will do.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/design#avoid-defining-a-one-member-abstract-class-when-a-simple-function-will-do): 

AVOID defining a one-member abstract class when a simple function will do.

 Unlike Java, Dart has first-class functions, closures, and a nice light syntax for using them. If all you need is something like a callback, just use a function. If you're defining a class and it only has a single abstract member with a meaningless name like `call` or `invoke`, there is a good chance you just want a function. 

BAD:

dart

```
abstract class Predicate {
  bool test(item);
}
```

content_copy

GOOD:

dart

```
typedef Predicate = bool Function(item);
```

content_copy

## Enable

[#](#enable)

 To enable the `one_member_abstracts` rule, add `one_member_abstracts` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - one_member_abstracts
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `one_member_abstracts: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    one_member_abstracts: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/one_member_abstracts).
