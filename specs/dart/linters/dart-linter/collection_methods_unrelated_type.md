Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [collection_methods_unrelated_type](/tools/linter-rules/collection_methods_unrelated_type)

# collection_methods_unrelated_type

Learn about the collection_methods_unrelated_type linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/collection_methods_unrelated_type)

verified_userStablecirclesCore

Invocation of various collection methods with arguments of unrelated types.

## Details

[#](#details)

DON'T invoke certain collection method with an argument with an unrelated type. 

 Doing this will invoke `==` on the collection's elements and most likely will return `false`. 

 An argument passed to a collection method should relate to the collection type as follows: 

- an argument to `Iterable<E>.contains` should be related to `E`
- an argument to `List<E>.remove` should be related to `E`
- an argument to `Map<K, V>.containsKey` should be related to `K`
- an argument to `Map<K, V>.containsValue` should be related to `V`
- an argument to `Map<K, V>.remove` should be related to `K`
- an argument to `Map<K, V>.[]` should be related to `K`
- an argument to `Queue<E>.remove` should be related to `E`
- an argument to `Set<E>.lookup` should be related to `E`
- an argument to `Set<E>.remove` should be related to `E`

BAD:

dart

```
void someFunction() {
  var list = <int>[];
  if (list.contains('1')) print('someFunction'); // LINT
}
```

content_copy

BAD:

dart

```
void someFunction() {
  var set = <int>{};
  set.remove('1'); // LINT
}
```

content_copy

GOOD:

dart

```
void someFunction() {
  var list = <int>[];
  if (list.contains(1)) print('someFunction'); // OK
}
```

content_copy

GOOD:

dart

```
void someFunction() {
  var set = <int>{};
  set.remove(1); // OK
}
```

content_copy

## Enable

[#](#enable)

 To enable the `collection_methods_unrelated_type` rule, add `collection_methods_unrelated_type` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - collection_methods_unrelated_type
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `collection_methods_unrelated_type: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    collection_methods_unrelated_type: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/collection_methods_unrelated_type).
