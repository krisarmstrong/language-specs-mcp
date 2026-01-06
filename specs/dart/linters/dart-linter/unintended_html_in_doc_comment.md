Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unintended_html_in_doc_comment](/tools/linter-rules/unintended_html_in_doc_comment)

# unintended_html_in_doc_comment

Learn about the unintended_html_in_doc_comment linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unintended_html_in_doc_comment)

verified_userStablecirclesCore

Use of angle brackets in a doc comment is treated as HTML by Markdown.

## Details

[#](#details)

DON'T use angle-bracketed text, `<…>`, in a doc comment unless you want to write an HTML tag or link. 

 Markdown allows HTML tags as part of the Markdown code, so you can write, for example, `T<sub>1</sub>`. Markdown does not restrict the allowed tags, it just includes the tags verbatim in the output. 

 Dartdoc only allows some known and valid HTML tags, and will omit any disallowed HTML tag from the output. See the list of allowed tags and directives below. Your doc comment should not contain any HTML tags that are not on this list. 

 Markdown also allows you to write an "auto-link" to an URL as for example `<https://example.com/page.html>`, delimited only by `<...>`. Such a link is allowed by Dartdoc as well. A `<...>` delimited text is an auto-link if it is a valid absolute URL, starting with a scheme of at least two characters followed by a colon, like `<mailto:mr_example@example.com>`. 

 Any other other occurrence of `<word...>` or `</word...>` is likely a mistake and this lint will warn about it. If something looks like an HTML tag, meaning it starts with `<` or `</` and then a letter, and it has a later matching `>`, then it's considered an invalid HTML tag unless it is an auto-link, or it starts with an allowed HTML tag. 

 Such a mistake can, for example, happen if writing Dart code with type arguments outside of a code span, for example `The type List<int> is ...`, where `<int>` looks like an HTML tag. Missing the end quote of a code span can have the same effect: `The type `List<int> is ...` will also treat `<int>` as an HTML tag. 

 Allows the following HTML directives: HTML comments, `<!-- text -->`, processing instructions, `<?...?>`, CDATA-sections, and `<[CDATA...]>`. Allows DartDoc links like `[List<int>]` which are not after a `]` or before a `[` or `(`, and allows the following recognized HTML tags: `a`, `abbr`, `address`, `area`, `article`, `aside`, `audio`, `b`, `bdi`, `bdo`, `blockquote`, `br`, `button`, `canvas`, `caption`, `cite`, `code`, `col`, `colgroup`, `data`, `datalist`, `dd`, `del`, `dfn`, `div`, `dl`, `dt`, `em`, `fieldset`, `figcaption`, `figure`, `footer`, `form`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `header`, `hr`, `i`, `iframe`, `img`, `input`, `ins`, `kbd`, `keygen`, `label`, `legend`, `li`, `link`, `main`, `map`, `mark`, `meta`, `meter`, `nav`, `noscript`, `object`, `ol`, `optgroup`, `option`, `output`, `p`, `param`, `pre`, `progress`, `q`, `s`, `samp`, `script`, `section`, `select`, `small`, `source`, `span`, `strong`, `style`, `sub`, `sup`, `table`, `tbody`, `td`, `template`, `textarea`, `tfoot`, `th`, `thead`, `time`, `title`, `tr`, `track`, `u`, `ul`, `var`, `video` and `wbr`. 

BAD:

dart

```
/// The type List<int>.
/// <assignment> -> <variable> = <expression>
```

content_copy

GOOD:

dart

```
/// The type `List<int>`.
/// The type [List<int>]
/// `<assignment> -> <variable> = <expression>`
/// \<assignment\> -> \<variable\> = \<expression\>`
/// <https://example.com/example>
```

content_copy

## Enable

[#](#enable)

 To enable the `unintended_html_in_doc_comment` rule, add `unintended_html_in_doc_comment` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unintended_html_in_doc_comment
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unintended_html_in_doc_comment: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unintended_html_in_doc_comment: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unintended_html_in_doc_comment).
