Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [cancel_subscriptions](/tools/linter-rules/cancel_subscriptions)

# cancel_subscriptions

Learn about the cancel_subscriptions linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/cancel_subscriptions)

verified_userStable

Cancel instances of `dart:async``StreamSubscription`.

## Details

[#](#details)

DO invoke `cancel` on instances of `dart:async``StreamSubscription`. 

 Cancelling instances of StreamSubscription prevents memory leaks and unexpected behavior. 

BAD:

dart

```
class A {
  StreamSubscription _subscriptionA; // LINT
  void init(Stream stream) {
    _subscriptionA = stream.listen((_) {});
  }
}
```

content_copy

BAD:

dart

```
void someFunction() {
  StreamSubscription _subscriptionF; // LINT
}
```

content_copy

GOOD:

dart

```
class B {
  StreamSubscription _subscriptionB; // OK
  void init(Stream stream) {
    _subscriptionB = stream.listen((_) {});
  }
​
  void dispose(filename) {
    _subscriptionB.cancel();
  }
}
```

content_copy

GOOD:

dart

```
void someFunctionOK() {
  StreamSubscription _subscriptionB; // OK
  _subscriptionB.cancel();
}
```

content_copy

Known limitations

 This rule does not track all patterns of StreamSubscription instantiations and cancellations. See [linter#317](https://github.com/dart-lang/sdk/issues/57387) for more information. 

## Enable

[#](#enable)

 To enable the `cancel_subscriptions` rule, add `cancel_subscriptions` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - cancel_subscriptions
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `cancel_subscriptions: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    cancel_subscriptions: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/cancel_subscriptions).
