Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [implicit_call_tearoffs](/tools/linter-rules/implicit_call_tearoffs)

# implicit_call_tearoffs

Learn about the implicit_call_tearoffs linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/implicit_call_tearoffs)

verified_userStablecirclesCorebuildFix available

Explicitly tear-off `call` methods when using an object as a Function.

## Details

[#](#details)

DO Explicitly tear off `.call` methods from objects when assigning to a Function type. There is less magic with an explicit tear off. Future language versions may remove the implicit call tear off. 

BAD:

dart

```
class Callable {
  void call() {}
}
void callIt(void Function() f) {
  f();
}
​
callIt(Callable());
```

content_copy

GOOD:

dart

```
class Callable {
  void call() {}
}
void callIt(void Function() f) {
  f();
}
​
callIt(Callable().call);
```

content_copy

## Enable

[#](#enable)

 To enable the `implicit_call_tearoffs` rule, add `implicit_call_tearoffs` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - implicit_call_tearoffs
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `implicit_call_tearoffs: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    implicit_call_tearoffs: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/implicit_call_tearoffs).
