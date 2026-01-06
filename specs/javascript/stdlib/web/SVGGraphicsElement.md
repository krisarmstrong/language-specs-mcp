# SVGGraphicsElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGGraphicsElement&level=high)

The `SVGGraphicsElement` interface represents SVG elements whose primary purpose is to directly render graphics into a group.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [SVGElement](/en-US/docs/Web/API/SVGElement).

[SVGGraphicsElement.requiredExtensions](/en-US/docs/Web/API/SVGGraphicsElement/requiredExtensions)Read only

An [SVGStringList](/en-US/docs/Web/API/SVGStringList) reflecting the [requiredExtensions](/en-US/docs/Web/SVG/Reference/Attribute/requiredExtensions) attribute of the given element.

[SVGGraphicsElement.systemLanguage](/en-US/docs/Web/API/SVGGraphicsElement/systemLanguage)Read only

An [SVGStringList](/en-US/docs/Web/API/SVGStringList) reflecting the [systemLanguage](/en-US/docs/Web/SVG/Reference/Attribute/systemLanguage) attribute of the given element.

[SVGGraphicsElement.transform](/en-US/docs/Web/API/SVGGraphicsElement/transform)Read only

An [SVGAnimatedTransformList](/en-US/docs/Web/API/SVGAnimatedTransformList) reflecting the computed value of the [transform](/en-US/docs/Web/CSS/Reference/Properties/transform) property and its corresponding [transform](/en-US/docs/Web/SVG/Reference/Attribute/transform) attribute of the given element.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent, [SVGElement](/en-US/docs/Web/API/SVGElement).

[SVGGraphicsElement.getBBox()](/en-US/docs/Web/API/SVGGraphicsElement/getBBox)

Returns a [DOMRect](/en-US/docs/Web/API/DOMRect) representing the computed bounding box of the current element.

[SVGGraphicsElement.getCTM()](/en-US/docs/Web/API/SVGGraphicsElement/getCTM)

Returns a [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) representing the matrix that transforms the current element's coordinate system to its SVG viewport's coordinate system.

[SVGGraphicsElement.getScreenCTM()](/en-US/docs/Web/API/SVGGraphicsElement/getScreenCTM)

Returns a [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) representing the matrix that transforms the current element's coordinate system to the coordinate system of the SVG viewport for the SVG document fragment.

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGGraphicsElement](https://svgwg.org/svg2-draft/types.html#InterfaceSVGGraphicsElement)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGGraphicsElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svggraphicselement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGGraphicsElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvggraphicselement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGGraphicsElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvggraphicselement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F34055723f9d2bbadfa8b0f0d27102e3adcedbd58%0A*+Document+last+modified%3A+2025-05-15T23%3A59%3A06.000Z%0A%0A%3C%2Fdetails%3E)
