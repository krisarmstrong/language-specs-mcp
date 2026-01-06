Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [directives_ordering](/tools/linter-rules/directives_ordering)

# directives_ordering

Learn about the directives_ordering linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/directives_ordering)

verified_userStablebuildFix available

Adhere to Effective Dart Guide directives sorting conventions.

## Details

[#](#details)

DO follow the directive ordering conventions in [Effective Dart](https://dart.dev/effective-dart/style#ordering): 

DO place `dart:` imports before other imports.

BAD:

dart

```
import 'package:bar/bar.dart';
import 'package:foo/foo.dart';
​
import 'dart:async';  // LINT
import 'dart:html';  // LINT
```

content_copy

BAD:

dart

```
import 'dart:html';  // OK
import 'package:bar/bar.dart';
​
import 'dart:async';  // LINT
import 'package:foo/foo.dart';
```

content_copy

GOOD:

dart

```
import 'dart:async';  // OK
import 'dart:html';  // OK
​
import 'package:bar/bar.dart';
import 'package:foo/foo.dart';
```

content_copy

DO place `package:` imports before relative imports.

BAD:

dart

```
import 'a.dart';
import 'b.dart';
​
import 'package:bar/bar.dart';  // LINT
import 'package:foo/foo.dart';  // LINT
```

content_copy

BAD:

dart

```
import 'package:bar/bar.dart';  // OK
import 'a.dart';
​
import 'package:foo/foo.dart';  // LINT
import 'b.dart';
```

content_copy

GOOD:

dart

```
import 'package:bar/bar.dart';  // OK
import 'package:foo/foo.dart';  // OK
​
import 'a.dart';
import 'b.dart';
```

content_copy

DO specify exports in a separate section after all imports.

BAD:

dart

```
import 'src/error.dart';
export 'src/error.dart'; // LINT
import 'src/string_source.dart';
```

content_copy

GOOD:

dart

```
import 'src/error.dart';
import 'src/string_source.dart';
​
export 'src/error.dart'; // OK
```

content_copy

DO sort sections alphabetically.

BAD:

dart

```
import 'package:foo/bar.dart'; // OK
import 'package:bar/bar.dart'; // LINT
​
import 'a/b.dart'; // OK
import 'a.dart'; // LINT
```

content_copy

GOOD:

dart

```
import 'package:bar/bar.dart'; // OK
import 'package:foo/bar.dart'; // OK
​
import 'a.dart'; // OK
import 'a/b.dart'; // OK
```

content_copy

## Enable

[#](#enable)

 To enable the `directives_ordering` rule, add `directives_ordering` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - directives_ordering
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `directives_ordering: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    directives_ordering: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/directives_ordering).
