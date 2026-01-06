Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_conditional_assignment](/tools/linter-rules/prefer_conditional_assignment)

# prefer_conditional_assignment

Learn about the prefer_conditional_assignment linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_conditional_assignment)

verified_userStablethumb_upRecommendedbuildFix available

Prefer using `??=` over testing for `null`.

## Details

[#](#details)

PREFER using `??=` over testing for `null`.

 As Dart has the `??=` operator, it is advisable to use it where applicable to improve the brevity of your code. 

BAD:

dart

```
String get fullName {
  if (_fullName == null) {
    _fullName = getFullUserName(this);
  }
  return _fullName;
}
```

content_copy

GOOD:

dart

```
String get fullName {
  return _fullName ??= getFullUserName(this);
}
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_conditional_assignment` rule, add `prefer_conditional_assignment` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_conditional_assignment
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_conditional_assignment: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_conditional_assignment: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_conditional_assignment).
