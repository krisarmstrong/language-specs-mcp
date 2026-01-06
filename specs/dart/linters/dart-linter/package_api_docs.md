Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [package_api_docs](/tools/linter-rules/package_api_docs)

# package_api_docs

Learn about the package_api_docs linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/package_api_docs)

errorRemoved

Provide doc comments for all public APIs.

## Details

[#](#details)

NOTE: This lint has been removed because it is has not been fully functional since at least Dart 2.0. Remove all inclusions of this lint from your analysis options. 

DO provide doc comments for all public APIs.

 As described in the [pub package layout doc](https://dart.dev/tools/pub/package-layout#implementation-files), public APIs consist in everything in your package's `lib` folder, minus implementation files in `lib/src`, adding elements explicitly exported with an `export` directive. 

For example, given `lib/foo.dart`:

dart

```
export 'src/bar.dart' show Bar;
export 'src/baz.dart';
​
class Foo { }
​
class _Foo { }
```

content_copy

its API includes:

- `Foo` (but not `_Foo`)
- `Bar` (exported) and
- all public elements in `src/baz.dart`

All public API members should be documented with `///` doc-style comments.

BAD:

dart

```
class Bar {
  void bar();
}
```

content_copy

GOOD:

dart

```
/// A Foo.
abstract class Foo {
  /// Start foo-ing.
  void start() => _start();
​
  _start();
}
```

content_copy

 Advice for writing good doc comments can be found in the [Doc Writing Guidelines](https://dart.dev/effective-dart/documentation). 

## Enable

[#](#enable)

 To enable the `package_api_docs` rule, add `package_api_docs` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - package_api_docs
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `package_api_docs: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    package_api_docs: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/package_api_docs).
