Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [implicit_reopen](/tools/linter-rules/implicit_reopen)

# implicit_reopen

Learn about the implicit_reopen linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/implicit_reopen)

scienceExperimentalbuildFix available

Don't implicitly reopen classes.

## Details

[#](#details)

 Using an `interface`, `base`, `final`, or `sealed` modifier on a class, or a `base` modifier on a mixin, authors can control whether classes and mixins allow being implemented, extended, and/or mixed in from outside of the library where they're defined. In some cases, it's possible for an author to inadvertently relax these controls and implicitly "reopen" a class. (A similar reopening cannot occur with a mixin.) 

 This lint guards against unintentionally reopening a class by requiring such cases to be made explicit with the [@reopen](https://pub.dev/documentation/meta/latest/meta/reopen-constant.html) annotation in `package:meta`. 

BAD:

dart

```
interface class I {}
​
class C extends I {} // LINT
```

content_copy

GOOD:

dart

```
interface class I {}
​
final class C extends I {}
```

content_copydart

```
import 'package:meta/meta.dart';
​
interface class I {}
​
@reopen
class C extends I {}
```

content_copy

## Enable

[#](#enable)

 To enable the `implicit_reopen` rule, add `implicit_reopen` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - implicit_reopen
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `implicit_reopen: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    implicit_reopen: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/implicit_reopen).
