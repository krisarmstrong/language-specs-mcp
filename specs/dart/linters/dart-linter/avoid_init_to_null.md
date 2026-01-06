Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_init_to_null](/tools/linter-rules/avoid_init_to_null)

# avoid_init_to_null

Learn about the avoid_init_to_null linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_init_to_null)

verified_userStablethumb_upRecommendedbuildFix available

Don't explicitly initialize variables to `null`.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/usage#dont-explicitly-initialize-variables-to-null): 

DON'T explicitly initialize variables to `null`.

 If a variable has a non-nullable type or is `final`, Dart reports a compile error if you try to use it before it has been definitely initialized. If the variable is nullable and not `const` or `final`, then it is implicitly initialized to `null` for you. There's no concept of "uninitialized memory" in Dart and no need to explicitly initialize a variable to `null` to be "safe". Adding `= null` is redundant and unneeded. 

BAD:

dart

```
Item? bestDeal(List<Item> cart) {
  Item? bestItem = null;
​
  for (final item in cart) {
    if (bestItem == null || item.price < bestItem.price) {
      bestItem = item;
    }
  }
​
  return bestItem;
}
```

content_copy

GOOD:

dart

```
Item? bestDeal(List<Item> cart) {
  Item? bestItem;
​
  for (final item in cart) {
    if (bestItem == null || item.price < bestItem.price) {
      bestItem = item;
    }
  }
​
  return bestItem;
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_init_to_null` rule, add `avoid_init_to_null` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_init_to_null
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_init_to_null: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_init_to_null: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_init_to_null).
