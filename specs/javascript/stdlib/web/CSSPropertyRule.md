# CSSPropertyRule

 Baseline  2024 Newly available

 Since ⁨July 2024⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPropertyRule&level=low)

The `CSSPropertyRule` interface of the [CSS Properties and Values API](/en-US/docs/Web/API/CSS_Properties_and_Values_API) represents a single CSS [@property](/en-US/docs/Web/CSS/Reference/At-rules/@property) rule.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

Inherits properties from its ancestor [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSPropertyRule.inherits](/en-US/docs/Web/API/CSSPropertyRule/inherits)Read only

Returns the inherit flag of the custom property.

[CSSPropertyRule.initialValue](/en-US/docs/Web/API/CSSPropertyRule/initialValue)Read only

Returns the initial value of the custom property.

[CSSPropertyRule.name](/en-US/docs/Web/API/CSSPropertyRule/name)Read only

Returns the name of the custom property.

[CSSPropertyRule.syntax](/en-US/docs/Web/API/CSSPropertyRule/syntax)Read only

Returns the literal syntax of the custom property.

## [Instance methods](#instance_methods)

No specific methods; inherits methods from its ancestor [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Examples](#examples)

This stylesheet contains a single [@property](/en-US/docs/Web/CSS/Reference/At-rules/@property) rule. The first [CSSRule](/en-US/docs/Web/API/CSSRule) returned will be a `CSSPropertyRule` with the properties and values as defined by the rule in CSS.

css

```
@property --property-name {
  syntax: "<color>";
  inherits: false;
  initial-value: #c0ffee;
}
```

js

```
const myRules = document.styleSheets[0].cssRules;
console.log(myRules[0]); // A CSSPropertyRule
```

## [Specifications](#specifications)

Specification
[CSS Properties and Values API Level 1# the-css-property-rule-interface](https://drafts.css-houdini.org/css-properties-values-api/#the-css-property-rule-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSPropertyRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csspropertyrule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPropertyRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsspropertyrule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPropertyRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsspropertyrule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F77d90a23ee0a3b5486a7963f68ad4e56efb06a7b%0A*+Document+last+modified%3A+2025-04-27T18%3A17%3A43.000Z%0A%0A%3C%2Fdetails%3E)
