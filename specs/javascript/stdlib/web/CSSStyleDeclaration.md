# CSSStyleDeclaration

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSStyleDeclaration&level=high)

The `CSSStyleDeclaration` interface is the base class for objects that represent CSS declaration blocks with different supported sets of CSS style information:

- [CSSStyleProperties](/en-US/docs/Web/API/CSSStyleProperties) — CSS styles declared in stylesheet ([CSSStyleRule.style](/en-US/docs/Web/API/CSSStyleRule/style)), inline styles for an element such as [HTMLElement](/en-US/docs/Web/API/HTMLElement/style), [SVGElement](/en-US/docs/Web/API/SVGElement/style), and [MathMLElement](/en-US/docs/Web/API/MathMLElement/style), or the computed style for an element returned by [Window.getComputedStyle()](/en-US/docs/Web/API/Window/getComputedStyle).
- [CSSPageDescriptors](/en-US/docs/Web/API/CSSPageDescriptors) — Styles for CSS [at-rules](/en-US/docs/Web/CSS/Guides/Syntax/At-rules).

The interface exposes style information and various style-related methods and properties. For example, it provides [getPropertyValue()](/en-US/docs/Web/API/CSSStyleDeclaration/getPropertyValue) for getting the value of a dash-named CSS property, such as `border-top`, which can't be directly accessed using dot notation because of the hyphens in its name.

Note: Earlier versions of the specification used `CSSStyleDeclaration` to represent all CSS declaration blocks, and some browsers and browser versions may still do so (check the browser compatibility tables for the above APIs). Generally the same website code will be functional in both old and new versions, but some properties returned in a `CSSStyleDeclaration` may not be relevant in a particular context.

## In this article

- [Attributes](#attributes)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Attributes](#attributes)

[CSSStyleDeclaration.cssText](/en-US/docs/Web/API/CSSStyleDeclaration/cssText)

Textual representation of the declaration block, if and only if it is exposed via [HTMLElement.style](/en-US/docs/Web/API/HTMLElement/style). Setting this attribute changes the inline style. If you want a text representation of a computed declaration block, you can get it with `JSON.stringify()`.

[CSSStyleDeclaration.length](/en-US/docs/Web/API/CSSStyleDeclaration/length)Read only

The number of properties. See the [item()](/en-US/docs/Web/API/CSSStyleDeclaration/item) method below.

[CSSStyleDeclaration.parentRule](/en-US/docs/Web/API/CSSStyleDeclaration/parentRule)Read only

The containing [CSSRule](/en-US/docs/Web/API/CSSRule).

### [CSS Properties](#css_properties)

[CSSStyleDeclaration.cssFloat](/en-US/docs/Web/API/CSSStyleDeclaration/cssFloat)Deprecated

Special alias for the [float](/en-US/docs/Web/CSS/Reference/Properties/float) CSS property.

[CSSStyleDeclaration named properties](#cssstyledeclaration)

Dashed and camel-cased attributes for all supported CSS properties.

## [Instance methods](#instance_methods)

[CSSStyleDeclaration.getPropertyPriority()](/en-US/docs/Web/API/CSSStyleDeclaration/getPropertyPriority)

Returns the optional priority, "important".

[CSSStyleDeclaration.getPropertyValue()](/en-US/docs/Web/API/CSSStyleDeclaration/getPropertyValue)

Returns the property value given a property name.

[CSSStyleDeclaration.item()](/en-US/docs/Web/API/CSSStyleDeclaration/item)

Returns a CSS property name by its index, or the empty string if the index is out-of-bounds.

[CSSStyleDeclaration.removeProperty()](/en-US/docs/Web/API/CSSStyleDeclaration/removeProperty)

Removes a property from the CSS declaration block.

[CSSStyleDeclaration.setProperty()](/en-US/docs/Web/API/CSSStyleDeclaration/setProperty)

Modifies an existing CSS property or creates a new CSS property in the declaration block.

[CSSStyleDeclaration.getPropertyCSSValue()](/en-US/docs/Web/API/CSSStyleDeclaration/getPropertyCSSValue)Deprecated

Only supported via getComputedStyle in Firefox. Returns the property value as a [CSSPrimitiveValue](/en-US/docs/Web/API/CSSPrimitiveValue) or `null` for [shorthand properties](/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties).

## [Example](#example)

js

```
const styleObj = document.styleSheets[0].cssRules[0].style;
console.log(styleObj.cssText);

for (let i = styleObj.length; i--; ) {
  const nameString = styleObj[i];
  styleObj.removeProperty(nameString);
}

console.log(styleObj.cssText);
```

## [Specifications](#specifications)

Specification
[CSS Object Model (CSSOM)# the-cssstyledeclaration-interface](https://drafts.csswg.org/cssom/#the-cssstyledeclaration-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSStyleDeclaration/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssstyledeclaration/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSStyleDeclaration&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssstyledeclaration%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSStyleDeclaration%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssstyledeclaration%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
