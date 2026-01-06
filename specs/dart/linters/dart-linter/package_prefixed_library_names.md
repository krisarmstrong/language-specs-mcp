Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [package_prefixed_library_names](/tools/linter-rules/package_prefixed_library_names)

# package_prefixed_library_names

Learn about the package_prefixed_library_names linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/package_prefixed_library_names)

verified_userStable

Prefix library names with the package name and a dot-separated path.

## Details

[#](#details)

DO prefix library names with the package name and a dot-separated path.

 This guideline helps avoid the warnings you get when two libraries have the same name. Here are the rules we recommend: 

- Prefix all library names with the package name.
- Make the entry library have the same name as the package.
-  For all other libraries in a package, after the package name add the dot-separated path to the library's Dart file. 
- For libraries under `lib`, omit the top directory name.

 For example, say the package name is `my_package`. Here are the library names for various files in the package: 

GOOD:

dart

```
// In lib/my_package.dart
library my_package;
​
// In lib/other.dart
library my_package.other;
​
// In lib/foo/bar.dart
library my_package.foo.bar;
​
// In example/foo/bar.dart
library my_package.example.foo.bar;
​
// In lib/src/private.dart
library my_package.src.private;
```

content_copy

## Enable

[#](#enable)

 To enable the `package_prefixed_library_names` rule, add `package_prefixed_library_names` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - package_prefixed_library_names
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `package_prefixed_library_names: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    package_prefixed_library_names: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/package_prefixed_library_names).
