Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_build_context_synchronously](/tools/linter-rules/use_build_context_synchronously)

# use_build_context_synchronously

Learn about the use_build_context_synchronously linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_build_context_synchronously)

verified_userStableflutterFlutter

Do not use `BuildContext` across asynchronous gaps.

## Details

[#](#details)

DON'T use `BuildContext` across asynchronous gaps.

 Storing `BuildContext` for later usage can easily lead to difficult-to-diagnose crashes. Asynchronous gaps are implicitly storing `BuildContext` and are some of the easiest to overlook when writing code. 

 When a `BuildContext` is used, a `mounted` property must be checked after an asynchronous gap, depending on how the `BuildContext` is accessed: 

-  When using a `State`'s `context` property, the `State`'s `mounted` property must be checked. 
-  For other `BuildContext` instances (like a local variable or function argument), the `BuildContext`'s `mounted` property must be checked. 

BAD:

dart

```
void onButtonTapped(BuildContext context) async {
  await Future.delayed(const Duration(seconds: 1));
  Navigator.of(context).pop();
}
```

content_copy

GOOD:

dart

```
void onButtonTapped(BuildContext context) {
  Navigator.of(context).pop();
}
```

content_copy

GOOD:

dart

```
void onButtonTapped(BuildContext context) async {
  await Future.delayed(const Duration(seconds: 1));
​
  if (!context.mounted) return;
  Navigator.of(context).pop();
}
```

content_copy

GOOD:

dart

```
abstract class MyState extends State<MyWidget> {
  void foo() async {
    await Future.delayed(const Duration(seconds: 1));
    if (!mounted) return; // Checks `this.mounted`, not `context.mounted`.
    Navigator.of(context).pop();
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `use_build_context_synchronously` rule, add `use_build_context_synchronously` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_build_context_synchronously
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_build_context_synchronously: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_build_context_synchronously: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_build_context_synchronously).
