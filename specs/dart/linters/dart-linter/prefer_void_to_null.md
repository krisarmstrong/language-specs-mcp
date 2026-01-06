Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_void_to_null](/tools/linter-rules/prefer_void_to_null)

# prefer_void_to_null

Learn about the prefer_void_to_null linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_void_to_null)

verified_userStablebuildFix available

Don't use the Null type, unless you are positive that you don't want void.

## Details

[#](#details)

DON'T use the type Null where void would work.

BAD:

dart

```
Null f() {}
Future<Null> f() {}
Stream<Null> f() {}
f(Null x) {}
```

content_copy

GOOD:

dart

```
void f() {}
Future<void> f() {}
Stream<void> f() {}
f(void x) {}
```

content_copy

Some exceptions include formulating special function types:

dart

```
Null Function(Null, Null);
```

content_copy

 and for making empty literals which are safe to pass into read-only locations for any type of map or list: 

dart

```
<Null>[];
<int, Null>{};
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_void_to_null` rule, add `prefer_void_to_null` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_void_to_null
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_void_to_null: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_void_to_null: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_void_to_null).
