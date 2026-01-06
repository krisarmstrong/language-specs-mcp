Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_string_buffers](/tools/linter-rules/use_string_buffers)

# use_string_buffers

Learn about the use_string_buffers linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_string_buffers)

verified_userStable

Use string buffers to compose strings.

## Details

[#](#details)

DO use string buffers to compose strings.

 In most cases, using a string buffer is preferred for composing strings due to its improved performance. 

BAD:

dart

```
String foo() {
  final buffer = '';
  for (int i = 0; i < 10; i++) {
    buffer += 'a'; // LINT
  }
  return buffer;
}
```

content_copy

GOOD:

dart

```
String foo() {
  final buffer = StringBuffer();
  for (int i = 0; i < 10; i++) {
    buffer.write('a');
  }
  return buffer.toString();
}
```

content_copy

## Enable

[#](#enable)

 To enable the `use_string_buffers` rule, add `use_string_buffers` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_string_buffers
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_string_buffers: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_string_buffers: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_string_buffers).
