Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unsafe_html](/tools/linter-rules/unsafe_html)

# unsafe_html

Learn about the unsafe_html linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unsafe_html)

errorRemoved

Avoid unsafe HTML APIs.

## Details

[#](#details)

NOTE: This lint is deprecated and will be removed in a future release. Remove all inclusions of this lint from your analysis options. 

AVOID

- assigning directly to the `href` field of an AnchorElement
-  assigning directly to the `src` field of an EmbedElement, IFrameElement, or ScriptElement 
- assigning directly to the `srcdoc` field of an IFrameElement
- calling the `createFragment` method of Element
- calling the `open` method of Window
- calling the `setInnerHtml` method of Element
- calling the `Element.html` constructor
- calling the `DocumentFragment.html` constructor

BAD:

dart

```
var script = ScriptElement()..src = 'foo.js';
```

content_copy

This rule has been removed.

## Enable

[#](#enable)

 To enable the `unsafe_html` rule, add `unsafe_html` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unsafe_html
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unsafe_html: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unsafe_html: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unsafe_html).
