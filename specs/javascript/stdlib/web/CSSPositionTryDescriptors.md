# CSSPositionTryDescriptors

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPositionTryDescriptors&level=not)

The `CSSPositionTryDescriptors` interface defines properties that represent the list of CSS descriptors that can be set in the body of a [@position-try](/en-US/docs/Web/CSS/Reference/At-rules/@position-try)[at-rule](/en-US/docs/Web/CSS/Guides/Syntax/At-rules).

Each descriptor in the body of the corresponding [@position-try](/en-US/docs/Web/CSS/Reference/At-rules/@position-try) at-rule can be accessed using either its property name in [bracket notation](/en-US/docs/Learn_web_development/Core/Scripting/Object_basics#bracket_notation) or the camel-case version of the property name "propertyName" in [dot notation](/en-US/docs/Learn_web_development/Core/Scripting/Object_basics#dot_notation). For example, you can access the CSS property "property-name" as `style["property-name"]` or `style.propertyName`, where `style` is a `CSSPositionTryDescriptors` instance. A property with a single-word name like [height](/en-US/docs/Web/CSS/Reference/Properties/height) can be accessed using either notation: `style["height"]` or `style.height`.

Note: The [CSSPositionTryRule](/en-US/docs/Web/API/CSSPositionTryRule) interface represents a [@position-try](/en-US/docs/Web/CSS/Reference/At-rules/@position-try) at-rule, and the [CSSPositionTryRule.style](/en-US/docs/Web/API/CSSPositionTryRule/style) property is an instance of this object.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its ancestor [CSSStyleDeclaration](/en-US/docs/Web/API/CSSStyleDeclaration).

The following property names, in snake-case (accessed using bracket notation) and camel-case (accessed using dot notation), each represent the value of a descriptor in the corresponding `@position-try` at-rule:

[align-self or alignSelf](#align-self)

A string representing the value of an [align-self](/en-US/docs/Web/CSS/Reference/Properties/align-self) descriptor.

[block-size or blockSize](#block-size)

A string representing the value of a [block-size](/en-US/docs/Web/CSS/Reference/Properties/block-size) descriptor.

[bottom](#bottom)

A string representing the value of a [bottom](/en-US/docs/Web/CSS/Reference/Properties/bottom) descriptor.

[height](#height)

A string representing the value of a [height](/en-US/docs/Web/CSS/Reference/Properties/height) descriptor.

[inline-size or inlineSize](#inline-size)

A string representing the value of an [inline-size](/en-US/docs/Web/CSS/Reference/Properties/inline-size) descriptor.

[inset](#inset)

A string representing the value of an [inset](/en-US/docs/Web/CSS/Reference/Properties/inset) descriptor.

[position-area or positionArea](#position-area)

A string representing the value of a [position-area](/en-US/docs/Web/CSS/Reference/Properties/position-area) descriptor.

[inset-block or insetBlock](#inset-block)

A string representing the value of an [inset-block](/en-US/docs/Web/CSS/Reference/Properties/inset-block) descriptor.

[inset-block-end or insetBlockEnd](#inset-block-end)

A string representing the value of an [inset-block-end](/en-US/docs/Web/CSS/Reference/Properties/inset-block-end) descriptor.

[inset-block-start or insetBlockStart](#inset-block-start)

A string representing the value of an [inset-block-start](/en-US/docs/Web/CSS/Reference/Properties/inset-block-start) descriptor.

[inset-inline or insetInline](#inset-inline)

A string representing the value of an [inset-inline](/en-US/docs/Web/CSS/Reference/Properties/inset-inline) descriptor.

[inset-inline-end or insetInlineEnd](#inset-inline-end)

A string representing the value of an [inset-inline-end](/en-US/docs/Web/CSS/Reference/Properties/inset-inline-end) descriptor.

[inset-inline-start or insetInlineStart](#inset-inline-start)

A string representing the value of an [inset-inline-start](/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start) descriptor.

[justify-self or justifySelf](#justify-self)

A string representing the value of a [justify-self](/en-US/docs/Web/CSS/Reference/Properties/justify-self) descriptor.

[left](#left)

A string representing the value of a [left](/en-US/docs/Web/CSS/Reference/Properties/left) descriptor.

[margin](#margin)

A string representing the value of a [margin](/en-US/docs/Web/CSS/Reference/Properties/margin) descriptor.

[margin-block or marginBlock](#margin-block)

A string representing the value of a [margin-block](/en-US/docs/Web/CSS/Reference/Properties/margin-block) descriptor.

[margin-block-end or marginBlockEnd](#margin-block-end)

A string representing the value of a [margin-block-end](/en-US/docs/Web/CSS/Reference/Properties/margin-block-end) descriptor.

[margin-block-start or marginBlockStart](#margin-block-start)

A string representing the value of a [margin-block-start](/en-US/docs/Web/CSS/Reference/Properties/margin-block-start) descriptor.

[margin-bottom or marginBottom](#margin-bottom)

A string representing the value of a [margin-bottom](/en-US/docs/Web/CSS/Reference/Properties/margin-bottom) descriptor.

[margin-inline or marginInline](#margin-inline)

A string representing the value of a [margin-inline](/en-US/docs/Web/CSS/Reference/Properties/margin-inline) descriptor.

[margin-inline-end or marginInlineEnd](#margin-inline-end)

A string representing the value of a [margin-inline-end](/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end) descriptor.

[margin-inline-start or marginInlineStart](#margin-inline-start)

A string representing the value of a [margin-inline-start](/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start) descriptor.

[margin-left or marginLeft](#margin-left)

A string representing the value of a [margin-left](/en-US/docs/Web/CSS/Reference/Properties/margin-left) descriptor.

[margin-right or marginRight](#margin-right)

A string representing the value of a [margin-right](/en-US/docs/Web/CSS/Reference/Properties/margin-right) descriptor.

[margin-top or marginTop](#margin-top)

A string representing the value of a [margin-top](/en-US/docs/Web/CSS/Reference/Properties/margin-top) descriptor.

[max-block-size or maxBlockSize](#max-block-size)

A string representing the value of a [max-block-size](/en-US/docs/Web/CSS/Reference/Properties/max-block-size) descriptor.

[max-height or maxHeight](#max-height)

A string representing the value of a [max-height](/en-US/docs/Web/CSS/Reference/Properties/max-height) descriptor.

[max-inline-size or maxInlineSize](#max-inline-size)

A string representing the value of a [max-inline-size](/en-US/docs/Web/CSS/Reference/Properties/max-inline-size) descriptor.

[max-width or maxWidth](#max-width)

A string representing the value of a [max-width](/en-US/docs/Web/CSS/Reference/Properties/max-width) descriptor.

[min-block-size or minBlockSize](#min-block-size)

A string representing the value of a [min-block-size](/en-US/docs/Web/CSS/Reference/Properties/min-block-size) descriptor.

[min-height or minHeight](#min-height)

A string representing the value of a [min-height](/en-US/docs/Web/CSS/Reference/Properties/min-height) descriptor.

[min-inline-size or minInlineSize](#min-inline-size)

A string representing the value of a [min-inline-size](/en-US/docs/Web/CSS/Reference/Properties/min-inline-size) descriptor.

[min-width or minWidth](#min-width)

A string representing the value of a [min-width](/en-US/docs/Web/CSS/Reference/Properties/min-width) descriptor.

[place-self or placeSelf](#place-self)

A string representing the value of a [place-self](/en-US/docs/Web/CSS/Reference/Properties/place-self) descriptor.

[position-anchor or positionAnchor](#position-anchor)

A string representing the value of a [position-anchor](/en-US/docs/Web/CSS/Reference/Properties/position-anchor) descriptor.

[right](#right)

A string representing the value of a [right](/en-US/docs/Web/CSS/Reference/Properties/right) descriptor.

[top](#top)

A string representing the value of a [top](/en-US/docs/Web/CSS/Reference/Properties/top) descriptor.

[width](#width)

A string representing the value of a [width](/en-US/docs/Web/CSS/Reference/Properties/width) descriptor.

## [Instance methods](#instance_methods)

No specific methods; inherits methods from its ancestor [CSSStyleDeclaration](/en-US/docs/Web/API/CSSStyleDeclaration).

## [Examples](#examples)

The CSS includes a `@position-try` at-rule with a name of `--custom-right` and three descriptors.

css

```
@position-try --custom-right {
  position-area: right;
  width: 100px;
  margin-left: 10px;
}
```

js

```
const myRules = document.styleSheets[0].cssRules;
const tryOption = myRules[0]; // a CSSPositionTryRule
console.log(tryOption.style); // "[object CSSPositionTryDescriptors]"
console.log(tryOption.style.margin); // "0 0 0 10px"
console.log(tryOption.style["position-area"]); // "right"
```

## [Specifications](#specifications)

Specification
[CSS Anchor Positioning# csspositiontrydescriptors](https://drafts.csswg.org/css-anchor-position-1/#csspositiontrydescriptors)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CSSPositionTryRule](/en-US/docs/Web/API/CSSPositionTryRule)
- [@position-try](/en-US/docs/Web/CSS/Reference/At-rules/@position-try)
- [position-try-fallbacks](/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks)
- [CSS anchor positioning](/en-US/docs/Web/CSS/Guides/Anchor_positioning) module
- [Using CSS anchor positioning](/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
- [Handling overflow: try options and conditional hiding](/en-US/docs/Web/CSS/Guides/Anchor_positioning/Try_options_hiding)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSPositionTryDescriptors/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csspositiontrydescriptors/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPositionTryDescriptors&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsspositiontrydescriptors%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPositionTryDescriptors%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsspositiontrydescriptors%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
