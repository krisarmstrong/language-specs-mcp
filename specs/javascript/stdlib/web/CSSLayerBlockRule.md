# CSSLayerBlockRule

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2022⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSLayerBlockRule&level=high)

The `CSSLayerBlockRule` represents a [@layer](/en-US/docs/Web/CSS/Reference/At-rules/@layer) block rule.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its ancestors [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule) and [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSLayerBlockRule.name](/en-US/docs/Web/API/CSSLayerBlockRule/name)Read only

A string containing the name of the associated cascade layer.

## [Instance methods](#instance_methods)

Inherits methods from its ancestors [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule) and [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Examples](#examples)

### [HTML](#html)

html

```
<p>I am displayed in <code>color: rebeccapurple</code>.</p>
```

### [CSS](#css)

css

```
@layer special {
  p {
    color: rebeccapurple;
  }
}
```

### [JavaScript](#javascript)

js

```
const item = document.getElementsByTagName("p")[0];
const rules = document.getElementById("css-output").sheet.cssRules;

const layer = rules[0]; // A CSSLayerBlockRule

item.textContent = `The CSSLayerBlockRule is for the "${layer.name}" layer`;
```

### [Result](#result)

## [Specifications](#specifications)

Specification
[CSS Cascading and Inheritance Level 5# csslayerblockrule](https://drafts.csswg.org/css-cascade-5/#csslayerblockrule)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [@layer](/en-US/docs/Web/CSS/Reference/At-rules/@layer)
- [CSSLayerStatementRule](/en-US/docs/Web/API/CSSLayerStatementRule)
- [Learn CSS cascade layers](/en-US/docs/Learn_web_development/Core/Styling_basics/Cascade_layers)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSLayerBlockRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csslayerblockrule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSLayerBlockRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsslayerblockrule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSLayerBlockRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsslayerblockrule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd7e665f6202179fcccbe753a1bfd358c224c3928%0A*+Document+last+modified%3A+2025-11-10T13%3A45%3A12.000Z%0A%0A%3C%2Fdetails%3E)
