Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_spread_collections](/tools/linter-rules/prefer_spread_collections)

# prefer_spread_collections

Learn about the prefer_spread_collections linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_spread_collections)

verified_userStablethumb_upRecommendedbuildFix available

Use spread collections when possible.

## Details

[#](#details)

Use spread collections when possible.

 Collection literals are excellent when you want to create a new collection out of individual items. But, when existing items are already stored in another collection, spread collection syntax leads to simpler code. 

BAD:

dart

```
Widget build(BuildContext context) {
  return CupertinoPageScaffold(
    child: ListView(
      children: [
        Tab2Header(),
      ]..addAll(buildTab2Conversation()),
    ),
  );
}
```

content_copydart

```
var ints = [1, 2, 3];
print(['a']..addAll(ints.map((i) => i.toString()))..addAll(['c']));
```

content_copydart

```
var things;
var l = ['a']..addAll(things ?? const []);
```

content_copy

GOOD:

dart

```
Widget build(BuildContext context) {
  return CupertinoPageScaffold(
    child: ListView(
      children: [
        Tab2Header(),
        ...buildTab2Conversation(),
      ],
    ),
  );
}
```

content_copydart

```
var ints = [1, 2, 3];
print(['a', ...ints.map((i) => i.toString()), 'c');
```

content_copydart

```
var things;
var l = ['a', ...?things];
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_spread_collections` rule, add `prefer_spread_collections` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_spread_collections
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_spread_collections: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_spread_collections: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_spread_collections).
