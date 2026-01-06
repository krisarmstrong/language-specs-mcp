# CSSLayerStatementRule

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2022⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSLayerStatementRule&level=high)

The `CSSLayerStatementRule` represents a [@layer](/en-US/docs/Web/CSS/Reference/At-rules/@layer) statement rule. Unlike [CSSLayerBlockRule](/en-US/docs/Web/API/CSSLayerBlockRule), it doesn't contain other rules and merely defines one or several layers by providing their names.

This rule allows to explicitly declare the ordering layer that is in an apparent way at the beginning of a CSS file: the layer order is defined by the order of first occurrence of each layer name. Declaring them with a statement allows the reader to understand the layer order. It also allows inline and imported layers to be interleaved, which is not possible when using the `CSSLayerBlockRule` syntax.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [CSSRule](/en-US/docs/Web/API/CSSRule).

- [CSSLayerStatementRule.nameList](/en-US/docs/Web/API/CSSLayerStatementRule/nameList)Read only

  - An array of strings, that represent the name of each cascade layer by the rule

## [Examples](#examples)

### [HTML](#html)

html

```
<p></p>
```

### [CSS](#css)

css

```
@layer layerName, layerName2;
```

### [JavaScript](#javascript)

js

```
const item = document.getElementsByTagName("p")[0];
const rules = document.getElementById("css-output").sheet.cssRules;

const layer = rules[0]; // A CSSLayerStatementRule

item.textContent = `The CSS @layer statement declares the following layers: ${layer.nameList.join(
  ", ",
)}.`;
```

### [Result](#result)

## [Specifications](#specifications)

Specification
[CSS Cascading and Inheritance Level 5# csslayerstatementrule](https://drafts.csswg.org/css-cascade-5/#csslayerstatementrule)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [@layer](/en-US/docs/Web/CSS/Reference/At-rules/@layer)
- [The @layer statement at-rule for named layers](/en-US/docs/Learn_web_development/Core/Styling_basics/Cascade_layers#the_layer_statement_at-rule_for_named_layers)
- [CSSLayerBlockRule](/en-US/docs/Web/API/CSSLayerBlockRule)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSLayerStatementRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csslayerstatementrule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSLayerStatementRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsslayerstatementrule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSLayerStatementRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsslayerstatementrule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd7e665f6202179fcccbe753a1bfd358c224c3928%0A*+Document+last+modified%3A+2025-11-10T13%3A45%3A12.000Z%0A%0A%3C%2Fdetails%3E)
