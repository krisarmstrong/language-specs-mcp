Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_slow_async_io](/tools/linter-rules/avoid_slow_async_io)

# avoid_slow_async_io

Learn about the avoid_slow_async_io linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_slow_async_io)

verified_userStable

Avoid slow asynchronous `dart:io` methods.

## Details

[#](#details)

AVOID using the following asynchronous file I/O methods because they are much slower than their synchronous counterparts. 

- `Directory.exists`
- `Directory.stat`
- `File.lastModified`
- `File.exists`
- `File.stat`
- `FileSystemEntity.isDirectory`
- `FileSystemEntity.isFile`
- `FileSystemEntity.isLink`
- `FileSystemEntity.type`

BAD:

dart

```
import 'dart:io';
​
Future<Null> someFunction() async {
  var file = File('/path/to/my/file');
  var now = DateTime.now();
  if ((await file.lastModified()).isBefore(now)) print('before'); // LINT
}
```

content_copy

GOOD:

dart

```
import 'dart:io';
​
Future<Null> someFunction() async {
  var file = File('/path/to/my/file');
  var now = DateTime.now();
  if (file.lastModifiedSync().isBefore(now)) print('before'); // OK
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_slow_async_io` rule, add `avoid_slow_async_io` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_slow_async_io
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_slow_async_io: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_slow_async_io: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_slow_async_io).
