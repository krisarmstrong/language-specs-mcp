# CSSStyleRule

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSStyleRule&level=high)

The `CSSStyleRule` interface represents a single CSS style rule.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

Inherits properties from its ancestors [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule) and [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSStyleRule.selectorText](/en-US/docs/Web/API/CSSStyleRule/selectorText)

Returns the textual representation of the selector for this rule, e.g., `"h1, h2"`.

[CSSStyleRule.style](/en-US/docs/Web/API/CSSStyleRule/style)Read only

Returns the [CSSStyleProperties](/en-US/docs/Web/API/CSSStyleProperties) object for the rule, which represents its styles.

[CSSStyleRule.styleMap](/en-US/docs/Web/API/CSSStyleRule/styleMap)Read only

Returns a [StylePropertyMap](/en-US/docs/Web/API/StylePropertyMap) object which provides access to the rule's property-value pairs.

## [Instance methods](#instance_methods)

Inherits methods from its ancestors [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule) and [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Examples](#examples)

### [Getting a style rule](#getting_a_style_rule)

The CSS below defines the style rule for the `h1` selector, which is represented in code by a `CSSStyleRule` instance.

css

```
h1 {
  color: pink;
}
```

Assuming the above style rule is the first rule in the document, it will be the first [CSSRule](/en-US/docs/Web/API/CSSRule) returned by `document.styleSheets[0].cssRules`. `myRules[0].style` returns a [CSSStyleProperties](/en-US/docs/Web/API/CSSStyleProperties) object representing the declarations defined for `h1`.

js

```
let myRules = document.styleSheets[0].cssRules;
console.log(myRules[0]); // a CSSStyleRule representing the h1.
```

## [Specifications](#specifications)

Specification
[CSS Object Model (CSSOM)# the-cssstylerule-interface](https://drafts.csswg.org/cssom/#the-cssstylerule-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 14, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSStyleRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssstylerule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSStyleRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssstylerule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSStyleRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssstylerule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F231152e9a749aaeba8de45f4cc712845a470dda9%0A*+Document+last+modified%3A+2025-10-14T01%3A39%3A08.000Z%0A%0A%3C%2Fdetails%3E)
