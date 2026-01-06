Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_asserts_with_message](/tools/linter-rules/prefer_asserts_with_message)

# prefer_asserts_with_message

Learn about the prefer_asserts_with_message linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_asserts_with_message)

verified_userStable

Prefer asserts with message.

## Details

[#](#details)

 When assertions fail it's not always simple to understand why. Adding a message to the `assert` helps the developer to understand why the AssertionError occurs. 

BAD:

dart

```
f(a) {
  assert(a != null);
}
​
class A {
  A(a) : assert(a != null);
}
```

content_copy

GOOD:

dart

```
f(a) {
  assert(a != null, 'a must not be null');
}
​
class A {
  A(a) : assert(a != null, 'a must not be null');
}
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_asserts_with_message` rule, add `prefer_asserts_with_message` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_asserts_with_message
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_asserts_with_message: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_asserts_with_message: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_asserts_with_message).
