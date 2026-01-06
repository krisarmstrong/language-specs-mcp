# SVGTextContentElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGTextContentElement&level=high)

The `SVGTextContentElement` interface is implemented by elements that support rendering child text content. It is inherited by various text-related interfaces, such as [SVGTextElement](/en-US/docs/Web/API/SVGTextElement), [SVGTSpanElement](/en-US/docs/Web/API/SVGTSpanElement), and [SVGTextPathElement](/en-US/docs/Web/API/SVGTextPathElement).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Static properties](#static_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [SVGGraphicsElement](/en-US/docs/Web/API/SVGGraphicsElement).

[SVGTextContentElement.textLength](/en-US/docs/Web/API/SVGTextContentElement/textLength)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) reflecting the [textLength](/en-US/docs/Web/SVG/Reference/Attribute/textLength) attribute of the given element.

[SVGTextContentElement.lengthAdjust](/en-US/docs/Web/API/SVGTextContentElement/lengthAdjust)Read only

An [SVGAnimatedEnumeration](/en-US/docs/Web/API/SVGAnimatedEnumeration) reflecting the [lengthAdjust](/en-US/docs/Web/SVG/Reference/Attribute/lengthAdjust) attribute of the given element. The numeric type values represent one of the `LENGTHADJUST_*` constant values.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent, [SVGGraphicsElement](/en-US/docs/Web/API/SVGGraphicsElement).

[SVGTextContentElement.getNumberOfChars()](/en-US/docs/Web/API/SVGTextContentElement/getNumberOfChars)

Returns a long representing the total number of addressable characters available for rendering within the current element, regardless of whether they will be rendered.

[SVGTextContentElement.getComputedTextLength()](/en-US/docs/Web/API/SVGTextContentElement/getComputedTextLength)

Returns a float representing the computed length for the text within the element.

[SVGTextContentElement.getSubStringLength()](/en-US/docs/Web/API/SVGTextContentElement/getSubStringLength)

Returns a float representing the computed length of the formatted text advance distance for a substring of text within the element. Note that this method only accounts for the widths of the glyphs in the substring and any extra spacing inserted by the CSS 'letter-spacing' and 'word-spacing' properties. Visual spacing adjustments made by the 'x' attribute is ignored.

[SVGTextContentElement.getStartPositionOfChar()](/en-US/docs/Web/API/SVGTextContentElement/getStartPositionOfChar)

Returns a [DOMPoint](/en-US/docs/Web/API/DOMPoint) representing the position of a typographic character after text layout has been performed.

[SVGTextContentElement.getEndPositionOfChar()](/en-US/docs/Web/API/SVGTextContentElement/getEndPositionOfChar)

Returns a [DOMPoint](/en-US/docs/Web/API/DOMPoint) representing the trailing position of a typographic character after text layout has been performed.

[SVGTextContentElement.getExtentOfChar()](/en-US/docs/Web/API/SVGTextContentElement/getExtentOfChar)

Returns a [DOMRect](/en-US/docs/Web/API/DOMRect) representing the computed tight bounding box of the glyph cell that corresponds to a given typographic character.

[SVGTextContentElement.getRotationOfChar()](/en-US/docs/Web/API/SVGTextContentElement/getRotationOfChar)

Returns a float representing the rotation of typographic character.

[SVGTextContentElement.getCharNumAtPosition()](/en-US/docs/Web/API/SVGTextContentElement/getCharNumAtPosition)

Returns a long representing the character which caused a text glyph to be rendered at a given position in the coordinate system. Because the relationship between characters and glyphs is not one-to-one, only the first character of the relevant typographic character is returned.

`SVGTextContentElement.selectSubString()`Deprecated

Selects text within the element.

## [Static properties](#static_properties)

[LENGTHADJUST_UNKNOWN (0)](#lengthadjust_unknown)

The type is not one of predefined types. It is invalid to attempt to define a new value of this type or to attempt to switch an existing value to this type.

[LENGTHADJUST_SPACING (1)](#lengthadjust_spacing)

Corresponds to the value `spacing`.

[LENGTHADJUST_SPACINGANDGLYPHS (2)](#lengthadjust_spacingandglyphs)

Corresponds to the value `spacingAndGlyphs`.

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGTextContentElement](https://svgwg.org/svg2-draft/text.html#InterfaceSVGTextContentElement)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGTextContentElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgtextcontentelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGTextContentElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgtextcontentelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGTextContentElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgtextcontentelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F43a8839abdfb01d4388f11a028582bec4e7ead18%0A*+Document+last+modified%3A+2025-06-08T10%3A11%3A23.000Z%0A%0A%3C%2Fdetails%3E)
