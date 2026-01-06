# CSSRule

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSRule&level=high)

The `CSSRule` interface represents a single CSS rule. There are several types of rules which inherit properties from `CSSRule`.

- [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule)
- [CSSStyleRule](/en-US/docs/Web/API/CSSStyleRule)
- [CSSImportRule](/en-US/docs/Web/API/CSSImportRule)
- [CSSMediaRule](/en-US/docs/Web/API/CSSMediaRule)
- [CSSFontFaceRule](/en-US/docs/Web/API/CSSFontFaceRule)
- [CSSFunctionDeclarations](/en-US/docs/Web/API/CSSFunctionDeclarations)
- [CSSPageRule](/en-US/docs/Web/API/CSSPageRule)
- [CSSNamespaceRule](/en-US/docs/Web/API/CSSNamespaceRule)
- [CSSKeyframesRule](/en-US/docs/Web/API/CSSKeyframesRule)
- [CSSKeyframeRule](/en-US/docs/Web/API/CSSKeyframeRule)
- [CSSCounterStyleRule](/en-US/docs/Web/API/CSSCounterStyleRule)
- [CSSSupportsRule](/en-US/docs/Web/API/CSSSupportsRule)
- [CSSFontFeatureValuesRule](/en-US/docs/Web/API/CSSFontFeatureValuesRule)
- [CSSFontPaletteValuesRule](/en-US/docs/Web/API/CSSFontPaletteValuesRule)
- [CSSLayerBlockRule](/en-US/docs/Web/API/CSSLayerBlockRule)
- [CSSLayerStatementRule](/en-US/docs/Web/API/CSSLayerStatementRule)
- [CSSPropertyRule](/en-US/docs/Web/API/CSSPropertyRule)
- [CSSNestedDeclarations](/en-US/docs/Web/API/CSSNestedDeclarations)

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `CSSRule` interface specifies the properties common to all rules, while properties unique to specific rule types are specified in the more specialized interfaces for those rules' respective types.

[CSSRule.cssText](/en-US/docs/Web/API/CSSRule/cssText)

Represents the textual representation of the rule, e.g., `"h1,h2 { font-size: 16pt }"` or `"@import 'url'"`. To access or modify parts of the rule (e.g., the value of "font-size" in the example) use the properties on the specialized interface for the rule's type (see above).

[CSSRule.parentRule](/en-US/docs/Web/API/CSSRule/parentRule)Read only

Returns the containing rule, otherwise `null`. E.g. if this rule is a style rule inside an [@media](/en-US/docs/Web/CSS/Reference/At-rules/@media) block, the parent rule would be that [CSSMediaRule](/en-US/docs/Web/API/CSSMediaRule).

[CSSRule.parentStyleSheet](/en-US/docs/Web/API/CSSRule/parentStyleSheet)Read only

Returns the [CSSStyleSheet](/en-US/docs/Web/API/CSSStyleSheet) object for the style sheet that contains this rule

[CSSRule.type](/en-US/docs/Web/API/CSSRule/type)Read onlyDeprecated

Returns one of the Type constants to determine which type of rule is represented.

## [Examples](#examples)

References to a `CSSRule` may be obtained by looking at a [CSSStyleSheet](/en-US/docs/Web/API/CSSStyleSheet)'s `cssRules` list.

js

```
let myRules = document.styleSheets[0].cssRules; // Returns a CSSRuleList
console.log(myRules);
```

## [Specifications](#specifications)

Specification
[CSS Object Model (CSSOM)# the-cssrule-interface](https://drafts.csswg.org/cssom/#the-cssrule-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using dynamic styling information](/en-US/docs/Web/API/CSS_Object_Model/Using_dynamic_styling_information)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssrule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssrule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssrule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F792888cd76b95a986a38d6a48bece464731dda51%0A*+Document+last+modified%3A+2025-10-15T14%3A04%3A43.000Z%0A%0A%3C%2Fdetails%3E)
