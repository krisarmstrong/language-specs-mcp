listOn this pagechevron_rightdart format[vertical_align_top
                dart format](#site-content-title)

- [Specify files to format](#specify-files-to-format)

  - [Specify one path](#specify-one-path)
  - [Specify multiple paths](#specify-multiple-paths)
  - [Prevent overwriting Dart files](#prevent-overwriting-dart-files)

- [Notify when changes occur](#notify-when-changes-occur)
- [What changes?](#what-changes)

  - [Configuring formatter page width](#configuring-formatter-page-width)

- [Learn more](#learn-more)

 Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

listOn this page

- [Specify files to format](#specify-files-to-format)

  - [Specify one path](#specify-one-path)
  - [Specify multiple paths](#specify-multiple-paths)
  - [Prevent overwriting Dart files](#prevent-overwriting-dart-files)

- [Notify when changes occur](#notify-when-changes-occur)
- [What changes?](#what-changes)

  - [Configuring formatter page width](#configuring-formatter-page-width)

- [Learn more](#learn-more)

1. [Tools](/tools)chevron_right
2. [dart format](/tools/dart-format)

# dart format

Command-line tool for formatting Dart source code.

more_vert

- copyCopy link
- [docsView source](https://github.com/dart-lang/site-www/blob/main/src/content/tools/dart-format.md)
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/dart-format&page-source=https://github.com/dart-lang/site-www/blob/main/src/content/tools/dart-format.md)

 To update your code to follow the [Dart formatting guidelines](/effective-dart/style#formatting), use the `dart format` command. This formatting follows what you get when using an IDE or editor with Dart support. 

lightbulbTip

 To learn more information about this and other `dart` commands, check out the [Dart command-line tool page](/tools/dart-tool). 

## Specify files to format

[#](#specify-files-to-format)

 To reformat one or more Dart files, provide a list of paths to the desired files or directories. 

### Specify one path

[#](#specify-one-path)

 Provide the path to one file or directory. If you pass a directory path, `dart format` recurses into its subdirectories as well. 

Example: To format all the Dart files in or under the current directory:

```
$ dart format .
```

content_copy

### Specify multiple paths

[#](#specify-multiple-paths)

To specify multiple files or directories, use a space-delimited list.

Example: To format all Dart files under the `lib` directory, plus one Dart file under the `bin` directory: 

```
$ dart format lib bin/updater.dart
```

content_copy

### Prevent overwriting Dart files

[#](#prevent-overwriting-dart-files)

By default, `dart format`overwrites the Dart files.

- To not overwrite the files, add the `--output` or `-o` flag.
- To get the contents of the formatted files, add `-o show` or `-o json`.
- To see only which files would change, add `-o none`.

```
$ dart format -o show bin/my_app.dart
```

content_copy

## Notify when changes occur

[#](#notify-when-changes-occur)

 To make `dart format` return an exit code when formatting changes occur, add the `--set-exit-if-changed` flag. 

- If changes occur, the `dart format` command returns an exit code of `1`.
- If changes don't occur, the `dart format` command returns an exit code of `0`.

 Use exit codes with continuous integration (CI) systems so they can trigger another action in response to the exit code. 

```
$ dart format -o none --set-exit-if-changed bin/my_app.dart
```

content_copy

## What changes?

[#](#what-changes)

`dart format` makes the following formatting changes:

- Removes whitespace.
- Wraps every line to 80 characters long or shorter.
-  Adds trailing commas to any argument or parameter list that splits across multiple lines, and removes them from ones that don't. 
- Might move comments before or after a comma.

 To learn more about best practices for writing and styling Dart code, check out the [Dart style guide](/effective-dart/style). 

### Configuring formatter page width

[#](#configuring-formatter-page-width)

 When you run `dart format`, the formatter defaults to 80 character line length or shorter. If you'd like to configure the line length for your project, you can add a top-level `formatter` section to the [analysis_options.yaml](/tools/analysis) file, like so: 

analysis_options.yamlyaml

```
formatter:
  page_width: 123
```

content_copy

 With the analysis options file typically at the root, the configured line length will apply to everything in the package. 

 You can also configure individual files' line length, overriding the analysis options file, with a marker comment at the top of the file before any other code: 

dart

```
// dart format width=123
```

content_copymerge_typeVersion note

 Configurable page width requires a [language version](/resources/language/evolution#language-versioning) of at least 3.7. 

## Learn more

[#](#learn-more)

 To learn about additional command-line options, use the `dart help` command or see the documentation for the [dart_style package](https://pub.dev/packages/dart_style)

```
$ dart help format
```

content_copy

 Check out the [formatter FAQ](https://github.com/dart-lang/dart_style/wiki/FAQ) for more context behind formatting decisions. 

Was this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. Page last updated on 2025-1-31. [View source](https://github.com/dart-lang/site-www/blob/main/src/content/tools/dart-format.md) or [report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/dart-format&page-source=https://github.com/dart-lang/site-www/blob/main/src/content/tools/dart-format.md).
