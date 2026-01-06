Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_futureor_void](/tools/linter-rules/avoid_futureor_void)

# avoid_futureor_void

Learn about the avoid_futureor_void linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_futureor_void)

scienceExperimental

Avoid using 'FutureOr' as the type of a result.

## Details

[#](#details)

AVOID using `FutureOr<void>` as the type of a result. This type is problematic because it may appear to encode that a result is either a `Future<void>`, or the result should be discarded (when it is `void`). However, there is no safe way to detect whether we have one or the other case (because an expression of type `void` can evaluate to any object whatsoever, including a future of any type). 

 It is also conceptually unsound to have a type whose meaning is something like "ignore this object; also, take a look because it might be a future". 

 An exception is made for contravariant occurrences of the type `FutureOr<void>` (e.g., for the type of a formal parameter), and no warning is emitted for these occurrences. The reason for this exception is that the type does not describe a result, it describes a constraint on a value provided by others. Similarly, an exception is made for type alias declarations, because they may well be used in a contravariant position (e.g., as the type of a formal parameter). Hence, in type alias declarations, only the type parameter bounds are checked. 

 A replacement for the type `FutureOr<void>` which is often useful is `Future<void>?`. This type encodes that the result is either a `Future<void>` or it is null, and there is no ambiguity at run time since no object can have both types. 

 It may not always be possible to use the type `Future<void>?` as a replacement for the type `FutureOr<void>`, because the latter is a supertype of all types, and the former is not. In this case it may be a useful remedy to replace `FutureOr<void>` by the type `void`. 

BAD:

dart

```
FutureOr<void> m() {...}
```

content_copy

GOOD:

dart

```
Future<void>? m() {...}
```

content_copy

This rule is experimental. It is being evaluated, and it might be changed or removed. Feedback on its behavior is welcome! The primary relevant issue is [dart-lang/sdk#59232](https://github.com/dart-lang/sdk/issues/59232). 

## Enable

[#](#enable)

 To enable the `avoid_futureor_void` rule, add `avoid_futureor_void` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_futureor_void
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_futureor_void: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_futureor_void: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_futureor_void).
