Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [implementation_imports](/tools/linter-rules/implementation_imports)

# implementation_imports

Learn about the implementation_imports linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/implementation_imports)

verified_userStablethumb_upRecommended

Don't import implementation files from another package.

## Details

[#](#details)

 From the [pub package layout doc](https://dart.dev/tools/pub/package-layout#implementation-files): 

DON'T import implementation files from another package.

 The libraries inside `lib` are publicly visible: other packages are free to import them. But much of a package's code is internal implementation libraries that should only be imported and used by the package itself. Those go inside a subdirectory of `lib` called `src`. You can create subdirectories in there if it helps you organize things. 

 You are free to import libraries that live in `lib/src` from within other Dart code in the same package (like other libraries in `lib`, scripts in `bin`, and tests) but you should never import from another package's `lib/src` directory. Those files are not part of the package's public API, and they might change in ways that could break your code. 

BAD:

dart

```
// In 'road_runner'
import 'package:acme/src/internals.dart';
```

content_copy

## Enable

[#](#enable)

 To enable the `implementation_imports` rule, add `implementation_imports` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - implementation_imports
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `implementation_imports: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    implementation_imports: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/implementation_imports).
