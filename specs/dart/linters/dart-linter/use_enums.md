Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_enums](/tools/linter-rules/use_enums)

# use_enums

Learn about the use_enums linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_enums)

verified_userStablebuildFix available

Use enums rather than classes that behave like enums.

## Details

[#](#details)

Classes that look like enumerations should be declared as `enum`s.

DO use enums where appropriate.

Candidates for enums are classes that:

- are concrete,
- are private or have only private generative constructors,
- have two or more static const fields with the same type as the class,
-  have generative constructors that are only invoked at the top-level of the initialization expression of these static fields, 
- do not define `hashCode`, `==`, `values` or `index`,
- do not extend any class other than `Object`, and
- have no subclasses declared in the defining library.

 To learn more about creating and using these enums, check out [Declaring enhanced enums](https://dart.dev/language/enums#declaring-enhanced-enums). 

BAD:

dart

```
class LogPriority {
  static const error = LogPriority._(1, 'Error');
  static const warning = LogPriority._(2, 'Warning');
  static const log = LogPriority._unknown('Log');
​
  final String prefix;
  final int priority;
  const LogPriority._(this.priority, this.prefix);
  const LogPriority._unknown(String prefix) : this._(-1, prefix);
}
```

content_copy

GOOD:

dart

```
enum LogPriority {
  error(1, 'Error'),
  warning(2, 'Warning'),
  log.unknown('Log');
​
  final String prefix;
  final int priority;
  const LogPriority(this.priority, this.prefix);
  const LogPriority.unknown(String prefix) : this(-1, prefix);
}
```

content_copy

## Enable

[#](#enable)

 To enable the `use_enums` rule, add `use_enums` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_enums
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_enums: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_enums: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_enums).
