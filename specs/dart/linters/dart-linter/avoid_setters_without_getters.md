Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_setters_without_getters](/tools/linter-rules/avoid_setters_without_getters)

# avoid_setters_without_getters

Learn about the avoid_setters_without_getters linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_setters_without_getters)

verified_userStable

Avoid setters without getters.

## Details

[#](#details)

DON'T define a setter without a corresponding getter.

 Defining a setter without defining a corresponding getter can lead to logical inconsistencies. Doing this could allow you to set a property to some value, but then upon observing the property's value, it could easily be different. 

BAD:

dart

```
class Bad {
  int l, r;
​
  set length(int newLength) {
    r = l + newLength;
  }
}
```

content_copy

GOOD:

dart

```
class Good {
  int l, r;
​
  int get length => r - l;
​
  set length(int newLength) {
    r = l + newLength;
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_setters_without_getters` rule, add `avoid_setters_without_getters` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_setters_without_getters
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_setters_without_getters: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_setters_without_getters: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_setters_without_getters).
