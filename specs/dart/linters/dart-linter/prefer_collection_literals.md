Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_collection_literals](/tools/linter-rules/prefer_collection_literals)

# prefer_collection_literals

Learn about the prefer_collection_literals linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_collection_literals)

verified_userStablethumb_upRecommendedbuildFix available

Use collection literals when possible.

## Details

[#](#details)

DO use collection literals when possible.

BAD:

dart

```
var addresses = Map<String, String>();
var uniqueNames = Set<String>();
var ids = LinkedHashSet<int>();
var coordinates = LinkedHashMap<int, int>();
```

content_copy

GOOD:

dart

```
var addresses = <String, String>{};
var uniqueNames = <String>{};
var ids = <int>{};
var coordinates = <int, int>{};
```

content_copy

EXCEPTIONS:

 When a `LinkedHashSet` or `LinkedHashMap` is expected, a collection literal is not preferred (or allowed). 

dart

```
void main() {
  LinkedHashSet<int> linkedHashSet =  LinkedHashSet.from([1, 2, 3]); // OK
  LinkedHashMap linkedHashMap = LinkedHashMap(); // OK
​
  printSet(LinkedHashSet<int>()); // LINT
  printHashSet(LinkedHashSet<int>()); // OK
​
  printMap(LinkedHashMap<int, int>()); // LINT
  printHashMap(LinkedHashMap<int, int>()); // OK
}
​
void printSet(Set<int> ids) => print('$ids!');
void printHashSet(LinkedHashSet<int> ids) => printSet(ids);
void printMap(Map map) => print('$map!');
void printHashMap(LinkedHashMap map) => printMap(map);
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_collection_literals` rule, add `prefer_collection_literals` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_collection_literals
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_collection_literals: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_collection_literals: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_collection_literals).
