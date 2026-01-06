Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_test_throws_matchers](/tools/linter-rules/use_test_throws_matchers)

# use_test_throws_matchers

Learn about the use_test_throws_matchers linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_test_throws_matchers)

verified_userStable

Use throwsA matcher instead of fail().

## Details

[#](#details)

Use the `throwsA` matcher instead of try-catch with `fail()`.

BAD:

dart

```
// sync code
try {
  someSyncFunctionThatThrows();
  fail('expected Error');
} on Error catch (error) {
  expect(error.message, contains('some message'));
}
​
// async code
try {
  await someAsyncFunctionThatThrows();
  fail('expected Error');
} on Error catch (error) {
  expect(error.message, contains('some message'));
}
```

content_copy

GOOD:

dart

```
// sync code
expect(
  () => someSyncFunctionThatThrows(),
  throwsA(isA<Error>().having((Error error) => error.message, 'message', contains('some message'))),
);
​
// async code
await expectLater(
  () => someAsyncFunctionThatThrows(),
  throwsA(isA<Error>().having((Error error) => error.message, 'message', contains('some message'))),
);
```

content_copy

## Enable

[#](#enable)

 To enable the `use_test_throws_matchers` rule, add `use_test_throws_matchers` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_test_throws_matchers
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_test_throws_matchers: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_test_throws_matchers: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_test_throws_matchers).
