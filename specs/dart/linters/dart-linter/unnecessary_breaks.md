Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_breaks](/tools/linter-rules/unnecessary_breaks)

# unnecessary_breaks

Learn about the unnecessary_breaks linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_breaks)

verified_userStablebuildFix available

Don't use explicit `break`s when a break is implied.

## Details

[#](#details)

 Only use a `break` in a non-empty switch case statement if you need to break before the end of the case body. Dart does not support fallthrough execution for non-empty cases, so `break`s at the end of non-empty switch case statements are unnecessary. 

BAD:

dart

```
switch (1) {
  case 1:
    print("one");
    break;
  case 2:
    print("two");
    break;
}
```

content_copy

GOOD:

dart

```
switch (1) {
  case 1:
    print("one");
  case 2:
    print("two");
}
```

content_copydart

```
switch (1) {
  case 1:
  case 2:
    print("one or two");
}
```

content_copydart

```
switch (1) {
  case 1:
    break;
  case 2:
    print("just two");
}
```

content_copy

 NOTE: This lint only reports unnecessary breaks in libraries with a [language version](https://dart.dev/resources/language/evolution#language-versioning) of 3.0 or greater. Explicit breaks are still required in Dart 2.19 and below. 

## Enable

[#](#enable)

 To enable the `unnecessary_breaks` rule, add `unnecessary_breaks` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_breaks
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_breaks: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_breaks: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_breaks).
