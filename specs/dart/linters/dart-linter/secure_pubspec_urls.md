Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [secure_pubspec_urls](/tools/linter-rules/secure_pubspec_urls)

# secure_pubspec_urls

Learn about the secure_pubspec_urls linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/secure_pubspec_urls)

verified_userStablecirclesCore

Use secure urls in `pubspec.yaml`.

## Details

[#](#details)

DO Use secure urls in `pubspec.yaml`.

Use `https` instead of `http` or `git:`.

BAD:

yaml

```
repository: http://github.com/dart-lang/example
```

content_copyyaml

```
git:
  url: git://github.com/dart-lang/example/example.git
```

content_copy

GOOD:

yaml

```
repository: https://github.com/dart-lang/example
```

content_copy

## Enable

[#](#enable)

 To enable the `secure_pubspec_urls` rule, add `secure_pubspec_urls` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - secure_pubspec_urls
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `secure_pubspec_urls: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    secure_pubspec_urls: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/secure_pubspec_urls).
