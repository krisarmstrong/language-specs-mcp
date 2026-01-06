Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_returning_this](/tools/linter-rules/avoid_returning_this)

# avoid_returning_this

Learn about the avoid_returning_this linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_returning_this)

verified_userStable

Avoid returning this from methods just to enable a fluent interface.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/design#avoid-returning-this-from-methods-just-to-enable-a-fluent-interface): 

AVOID returning this from methods just to enable a fluent interface.

 Returning `this` from a method is redundant; Dart has a cascade operator which allows method chaining universally. 

Returning `this` is allowed for:

- operators
- methods with a return type different of the current class
- methods defined in parent classes / mixins or interfaces
- methods defined in extensions

BAD:

dart

```
var buffer = StringBuffer()
  .write('one')
  .write('two')
  .write('three');
```

content_copy

GOOD:

dart

```
var buffer = StringBuffer()
  ..write('one')
  ..write('two')
  ..write('three');
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_returning_this` rule, add `avoid_returning_this` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_returning_this
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_returning_this: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_returning_this: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_returning_this).
