Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [overridden_fields](/tools/linter-rules/overridden_fields)

# overridden_fields

Learn about the overridden_fields linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/overridden_fields)

verified_userStablethumb_upRecommended

Don't override fields.

## Details

[#](#details)

DON'T override fields.

 Overriding fields is almost always done unintentionally. Regardless, it is a bad practice to do so. 

BAD:

dart

```
class Base {
  Object field = 'lorem';
​
  Object something = 'change';
}
​
class Bad1 extends Base {
  @override
  final field = 'ipsum'; // LINT
}
​
class Bad2 extends Base {
  @override
  Object something = 'done'; // LINT
}
```

content_copy

GOOD:

dart

```
class Base {
  Object field = 'lorem';
​
  Object something = 'change';
}
​
class Ok extends Base {
  Object newField; // OK
​
  final Object newFinal = 'ignore'; // OK
}
```

content_copy

GOOD:

dart

```
abstract class BaseLoggingHandler {
  Base transformer;
}
​
class LogPrintHandler implements BaseLoggingHandler {
  @override
  Derived transformer; // OK
}
```

content_copy

## Enable

[#](#enable)

 To enable the `overridden_fields` rule, add `overridden_fields` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - overridden_fields
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `overridden_fields: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    overridden_fields: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/overridden_fields).
