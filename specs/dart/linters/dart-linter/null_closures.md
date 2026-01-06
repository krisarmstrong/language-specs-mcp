Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [null_closures](/tools/linter-rules/null_closures)

# null_closures

Learn about the null_closures linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/null_closures)

verified_userStablethumb_upRecommendedbuildFix available

Do not pass `null` as an argument where a closure is expected.

## Details

[#](#details)

DON'T pass `null` as an argument where a closure is expected.

 Often a closure that is passed to a method will only be called conditionally, so that tests and "happy path" production calls do not reveal that `null` will result in an exception being thrown. 

 This rule only catches null literals being passed where closures are expected in the following locations: 

#### Constructors

[#](#constructors)

-  From `dart:async`

  - `Future` at the 0th positional parameter
  - `Future.microtask` at the 0th positional parameter
  - `Future.sync` at the 0th positional parameter
  - `Timer` at the 0th positional parameter
  - `Timer.periodic` at the 1st positional parameter

-  From `dart:core`

  - `List.generate` at the 1st positional parameter

#### Static functions

[#](#static-functions)

-  From `dart:async`

  - `scheduleMicrotask` at the 0th positional parameter
  - `Future.doWhile` at the 0th positional parameter
  - `Future.forEach` at the 0th positional parameter
  - `Future.wait` at the named parameter `cleanup`
  - `Timer.run` at the 0th positional parameter

#### Instance methods

[#](#instance-methods)

-  From `dart:async`

  - `Future.then` at the 0th positional parameter
  - `Future.complete` at the 0th positional parameter

-  From `dart:collection`

  - `Queue.removeWhere` at the 0th positional parameter
  - `Queue.retain
  - `Iterable.firstWhere` at the 0th positional parameter, and the named parameter `orElse`
  - `Iterable.forEach` at the 0th positional parameter
  - `Iterable.fold` at the 1st positional parameter
  - `Iterable.lastWhere` at the 0th positional parameter, and the named parameter `orElse`
  - `Iterable.map` at the 0th positional parameter
  - `Iterable.reduce` at the 0th positional parameter
  - `Iterable.singleWhere` at the 0th positional parameter, and the named parameter `orElse`
  - `Iterable.skipWhile` at the 0th positional parameter
  - `Iterable.takeWhile` at the 0th positional parameter
  - `Iterable.where` at the 0th positional parameter
  - `List.removeWhere` at the 0th positional parameter
  - `List.retainWhere` at the 0th positional parameter
  - `String.replaceAllMapped` at the 1st positional parameter
  - `String.replaceFirstMapped` at the 1st positional parameter
  - `String.splitMapJoin` at the named parameters `onMatch` and `onNonMatch`

BAD:

dart

```
[1, 3, 5].firstWhere((e) => e.isOdd, orElse: null);
```

content_copy

GOOD:

dart

```
[1, 3, 5].firstWhere((e) => e.isOdd, orElse: () => null);
```

content_copy

## Enable

[#](#enable)

 To enable the `null_closures` rule, add `null_closures` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - null_closures
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `null_closures: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    null_closures: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/null_closures).
