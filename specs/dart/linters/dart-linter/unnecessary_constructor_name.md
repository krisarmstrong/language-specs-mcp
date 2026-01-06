Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_constructor_name](/tools/linter-rules/unnecessary_constructor_name)

# unnecessary_constructor_name

Learn about the unnecessary_constructor_name linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_constructor_name)

verified_userStablethumb_upRecommendedbuildFix available

Unnecessary `.new` constructor name.

## Details

[#](#details)

PREFER using the default unnamed Constructor over `.new`.

 Given a class `C`, the named unnamed constructor `C.new` refers to the same constructor as the unnamed `C`. As such it adds nothing but visual noise to invocations and should be avoided (unless being used to identify a constructor tear-off). 

BAD:

dart

```
class A {
  A.new(); // LINT
}
​
var a = A.new(); // LINT
```

content_copy

GOOD:

dart

```
class A {
  A.ok();
}
​
var a = A();
var aa = A.ok();
var makeA = A.new;
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_constructor_name` rule, add `unnecessary_constructor_name` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_constructor_name
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_constructor_name: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_constructor_name: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_constructor_name).
