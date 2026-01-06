Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unreachable_from_main](/tools/linter-rules/unreachable_from_main)

# unreachable_from_main

Learn about the unreachable_from_main linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unreachable_from_main)

verified_userStablebuildFix available

Unreachable top-level members in executable libraries.

## Details

[#](#details)

 Any member declared in an executable library should be used directly inside that library. An executable library is a library that contains a `main` top-level function or that contains a top-level function annotated with `@pragma('vm:entry-point')`). Executable libraries are not usually imported and it's better to avoid defining unused members. 

 This rule assumes that an executable library isn't imported by other libraries except to execute its `main` function. 

BAD:

dart

```
main() {}
void f() {}
```

content_copy

GOOD:

dart

```
main() {
  f();
}
void f() {}
```

content_copy

## Enable

[#](#enable)

 To enable the `unreachable_from_main` rule, add `unreachable_from_main` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unreachable_from_main
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unreachable_from_main: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unreachable_from_main: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unreachable_from_main).
