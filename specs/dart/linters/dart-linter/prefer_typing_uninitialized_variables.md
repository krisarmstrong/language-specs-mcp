Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_typing_uninitialized_variables](/tools/linter-rules/prefer_typing_uninitialized_variables)

# prefer_typing_uninitialized_variables

Learn about the prefer_typing_uninitialized_variables linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_typing_uninitialized_variables)

verified_userStablecirclesCorebuildFix available

Prefer typing uninitialized variables and fields.

## Details

[#](#details)

PREFER specifying a type annotation for uninitialized variables and fields.

 Forgoing type annotations for uninitialized variables is a bad practice because you may accidentally assign them to a type that you didn't originally intend to. 

BAD:

dart

```
class BadClass {
  static var bar; // LINT
  var foo; // LINT
​
  void method() {
    var bar; // LINT
    bar = 5;
    print(bar);
  }
}
```

content_copy

BAD:

dart

```
void aFunction() {
  var bar; // LINT
  bar = 5;
  ...
}
```

content_copy

GOOD:

dart

```
class GoodClass {
  static var bar = 7;
  var foo = 42;
  int baz; // OK
​
  void method() {
    int baz;
    var bar = 5;
    ...
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_typing_uninitialized_variables` rule, add `prefer_typing_uninitialized_variables` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_typing_uninitialized_variables
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_typing_uninitialized_variables: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_typing_uninitialized_variables: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_typing_uninitialized_variables).
