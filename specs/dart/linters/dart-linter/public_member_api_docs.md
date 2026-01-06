Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [public_member_api_docs](/tools/linter-rules/public_member_api_docs)

# public_member_api_docs

Learn about the public_member_api_docs linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/public_member_api_docs)

verified_userStable

Document all public members.

## Details

[#](#details)

DO document all public members.

 All non-overriding public members should be documented with `///` doc-style comments. 

BAD:

dart

```
class Bad {
  void meh() { }
}
```

content_copy

GOOD:

dart

```
/// A good thing.
abstract class Good {
  /// Start doing your thing.
  void start() => _start();
​
  _start();
}
```

content_copy

 In case a public member overrides a member it is up to the declaring member to provide documentation. For example, in the following, `Sub` needn't document `init` (though it certainly may, if there's need). 

GOOD:

dart

```
/// Base of all things.
abstract class Base {
  /// Initialize the base.
  void init();
}
​
/// A sub base.
class Sub extends Base {
  @override
  void init() { ... }
}
```

content_copy

 Note that consistent with `dart doc`, an exception to the rule is made when documented getters have corresponding undocumented setters. In this case the setters inherit the docs from the getters. 

## Enable

[#](#enable)

 To enable the `public_member_api_docs` rule, add `public_member_api_docs` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - public_member_api_docs
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `public_member_api_docs: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    public_member_api_docs: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/public_member_api_docs).
