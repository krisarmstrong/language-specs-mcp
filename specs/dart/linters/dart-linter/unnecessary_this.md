Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_this](/tools/linter-rules/unnecessary_this)

# unnecessary_this

Learn about the unnecessary_this linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_this)

verified_userStablethumb_upRecommendedbuildFix available

Don't access members with `this` unless avoiding shadowing.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/usage#dont-use-this-when-not-needed-to-avoid-shadowing): 

DON'T use `this` when not needed to avoid shadowing.

BAD:

dart

```
class Box {
  int value;
  void update(int newValue) {
    this.value = newValue;
  }
}
```

content_copy

GOOD:

dart

```
class Box {
  int value;
  void update(int newValue) {
    value = newValue;
  }
}
```

content_copy

GOOD:

dart

```
class Box {
  int value;
  void update(int value) {
    this.value = value;
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_this` rule, add `unnecessary_this` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_this
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_this: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_this: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_this).
