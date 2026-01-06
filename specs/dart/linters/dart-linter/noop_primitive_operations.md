Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [noop_primitive_operations](/tools/linter-rules/noop_primitive_operations)

# noop_primitive_operations

Learn about the noop_primitive_operations linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/noop_primitive_operations)

verified_userStablebuildFix available

Noop primitive operations.

## Details

[#](#details)

Some operations on primitive types are idempotent and can be removed.

BAD:

dart

```
doubleValue.toDouble();
​
intValue.toInt();
intValue.round();
intValue.ceil();
intValue.floor();
intValue.truncate();
​
string.toString();
string = 'hello\n'
    ''
    'world';
​
'string with ${x.toString()}';
```

content_copy

 Note that the empty string literals at the beginning or end of a string are allowed, as they are typically used to format the string literal across multiple lines: 

dart

```
// OK
string = ''
    'hello\n'
    'world\n';
​
// OK
string = 'hello\n'
    'world\n'
    '';
```

content_copy

## Enable

[#](#enable)

 To enable the `noop_primitive_operations` rule, add `noop_primitive_operations` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - noop_primitive_operations
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `noop_primitive_operations: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    noop_primitive_operations: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/noop_primitive_operations).
