# CSSPositionTryRule

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPositionTryRule&level=not)

The `CSSPositionTryRule` interface describes an object representing a [@position-try](/en-US/docs/Web/CSS/Reference/At-rules/@position-try)[at-rule](/en-US/docs/Web/CSS/Guides/Syntax/At-rules).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its ancestor [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSPositionTryRule.name](/en-US/docs/Web/API/CSSPositionTryRule/name)Read only

Represents the name of the position try option specified by the `@position-try` at-rule's [<dashed-ident>](/en-US/docs/Web/CSS/Reference/Values/dashed-ident).

[CSSPositionTryRule.style](/en-US/docs/Web/API/CSSPositionTryRule/style)Read only

A [CSSPositionTryDescriptors](/en-US/docs/Web/API/CSSPositionTryDescriptors) object that represents the declarations set in the body of the `@position-try` at-rule.

## [Instance methods](#instance_methods)

No specific methods; inherits methods from its ancestor [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Examples](#examples)

The CSS includes a `@position-try` at-rule with a name of `--custom-left` and three descriptors.

css

```
@position-try --custom-left {
  position-area: left;
  width: 20%;
  max-width: 200px;
  margin-right: 10px;
}
```

js

```
const myRules = document.styleSheets[0].cssRules;
const tryOption = myRules[0]; // a CSSPositionTryRule
console.log(tryOption); // "[object CSSPositionTryRule]"
console.log(tryOption.name); // "--custom-left"
console.log(tryOption.style); // "[object CSSPositionTryDescriptors]"
console.log(tryOption.style.maxWidth); // "200px"
```

## [Specifications](#specifications)

Specification
[CSS Anchor Positioning# csspositiontryrule](https://drafts.csswg.org/css-anchor-position-1/#csspositiontryrule)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CSSPositionTryDescriptors](/en-US/docs/Web/API/CSSPositionTryDescriptors)
- [@position-try](/en-US/docs/Web/CSS/Reference/At-rules/@position-try)
- [position-try-fallbacks](/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks)
- [CSS anchor positioning](/en-US/docs/Web/CSS/Guides/Anchor_positioning) module
- [Using CSS anchor positioning](/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
- [Handling overflow: try options and conditional hiding](/en-US/docs/Web/CSS/Guides/Anchor_positioning/Try_options_hiding)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSPositionTryRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csspositiontryrule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPositionTryRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsspositiontryrule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPositionTryRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsspositiontryrule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
