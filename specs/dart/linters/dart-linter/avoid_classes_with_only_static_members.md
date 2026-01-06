Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_classes_with_only_static_members](/tools/linter-rules/avoid_classes_with_only_static_members)

# avoid_classes_with_only_static_members

Learn about the avoid_classes_with_only_static_members linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_classes_with_only_static_members)

verified_userStable

Avoid defining a class that contains only static members.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/design#avoid-defining-a-class-that-contains-only-static-members): 

AVOID defining a class that contains only static members.

 Creating classes with the sole purpose of providing utility or otherwise static methods is discouraged. Dart allows functions to exist outside of classes for this very reason. 

BAD:

dart

```
class DateUtils {
  static DateTime mostRecent(List<DateTime> dates) {
    return dates.reduce((a, b) => a.isAfter(b) ? a : b);
  }
}
​
class _Favorites {
  static const mammal = 'weasel';
}
```

content_copy

GOOD:

dart

```
DateTime mostRecent(List<DateTime> dates) {
  return dates.reduce((a, b) => a.isAfter(b) ? a : b);
}
​
const _favoriteMammal = 'weasel';
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_classes_with_only_static_members` rule, add `avoid_classes_with_only_static_members` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_classes_with_only_static_members
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_classes_with_only_static_members: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_classes_with_only_static_members: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_classes_with_only_static_members).
