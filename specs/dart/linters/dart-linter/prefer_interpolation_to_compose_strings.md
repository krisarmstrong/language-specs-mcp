Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_interpolation_to_compose_strings](/tools/linter-rules/prefer_interpolation_to_compose_strings)

# prefer_interpolation_to_compose_strings

Learn about the prefer_interpolation_to_compose_strings linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_interpolation_to_compose_strings)

verified_userStablethumb_upRecommendedbuildFix available

Use interpolation to compose strings and values.

## Details

[#](#details)

PREFER using interpolation to compose strings and values.

 Using interpolation when composing strings and values is usually easier to write and read than concatenation. 

BAD:

dart

```
'Hello, ' + person.name + ' from ' + person.city + '.';
```

content_copy

GOOD:

dart

```
'Hello, ${person.name} from ${person.city}.'
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_interpolation_to_compose_strings` rule, add `prefer_interpolation_to_compose_strings` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_interpolation_to_compose_strings
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_interpolation_to_compose_strings: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_interpolation_to_compose_strings: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_interpolation_to_compose_strings).
