Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [package_names](/tools/linter-rules/package_names)

# package_names

Learn about the package_names linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/package_names)

verified_userStablethumb_upRecommended

Use `lowercase_with_underscores` for package names.

## Details

[#](#details)

From the [Pubspec format description](https://dart.dev/tools/pub/pubspec):

DO use `lowercase_with_underscores` for package names.

 Package names should be all lowercase, with underscores to separate words, `just_like_this`. Use only basic Latin letters and Arabic digits: [a-z0-9_]. Also, make sure the name is a valid Dart identifier -- that it doesn't start with digits and isn't a reserved word. 

## Enable

[#](#enable)

 To enable the `package_names` rule, add `package_names` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - package_names
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `package_names: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    package_names: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/package_names).
