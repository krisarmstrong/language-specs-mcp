Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [void_checks](/tools/linter-rules/void_checks)

# void_checks

Learn about the void_checks linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/void_checks)

verified_userStablecirclesCore

Don't assign to `void`.

## Details

[#](#details)

DON'T assign to `void`.

BAD:

dart

```
class A<T> {
  T value;
  void test(T arg) { }
}
​
void main() {
  A<void> a = A<void>();
  a.value = 1; // LINT
  a.test(1); // LINT
}
```

content_copy

## Enable

[#](#enable)

 To enable the `void_checks` rule, add `void_checks` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - void_checks
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `void_checks: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    void_checks: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/void_checks).
