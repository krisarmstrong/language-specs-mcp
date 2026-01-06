Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [sort_unnamed_constructors_first](/tools/linter-rules/sort_unnamed_constructors_first)

# sort_unnamed_constructors_first

Learn about the sort_unnamed_constructors_first linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/sort_unnamed_constructors_first)

verified_userStablebuildFix available

Sort unnamed constructor declarations first.

## Details

[#](#details)

DO sort unnamed constructor declarations first, before named ones.

BAD:

dart

```
class _PriorityItem {
  factory _PriorityItem.forName(bool isStatic, String name, _MemberKind kind) => ...
  _PriorityItem(this.isStatic, this.kind, this.isPrivate);
  ...
}
```

content_copy

GOOD:

dart

```
abstract class CancelableFuture<T> implements Future<T>  {
  factory CancelableFuture(computation()) => ...
  factory CancelableFuture.delayed(Duration duration, [computation()]) => ...
  ...
}
```

content_copy

## Enable

[#](#enable)

 To enable the `sort_unnamed_constructors_first` rule, add `sort_unnamed_constructors_first` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - sort_unnamed_constructors_first
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `sort_unnamed_constructors_first: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    sort_unnamed_constructors_first: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/sort_unnamed_constructors_first).
