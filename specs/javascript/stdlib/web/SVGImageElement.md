# SVGImageElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGImageElement&level=high)

The `SVGImageElement` interface corresponds to the [<image>](/en-US/docs/Web/SVG/Reference/Element/image) element.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [SVGGraphicsElement](/en-US/docs/Web/API/SVGGraphicsElement).

[SVGImageElement.crossOrigin](/en-US/docs/Web/API/SVGImageElement/crossOrigin)

A string reflecting the [crossorigin](/en-US/docs/Web/SVG/Reference/Attribute/crossorigin) content attribute, which represents the CORS setting of the given [<image>](/en-US/docs/Web/SVG/Reference/Element/image) element.

[SVGImageElement.decoding](/en-US/docs/Web/API/SVGImageElement/decoding)

Represents a hint given to the browser on how it should decode the image.

[SVGImageElement.height](/en-US/docs/Web/API/SVGImageElement/height)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [height](/en-US/docs/Web/SVG/Reference/Attribute/height) attribute of the given [<image>](/en-US/docs/Web/SVG/Reference/Element/image) element.

[SVGImageElement.href](/en-US/docs/Web/API/SVGImageElement/href)Read only

An [SVGAnimatedString](/en-US/docs/Web/API/SVGAnimatedString) corresponding to the [href](/en-US/docs/Web/SVG/Reference/Attribute/href) or [xlink:href](/en-US/docs/Web/SVG/Reference/Attribute/xlink:href)Deprecated attribute of the given [<image>](/en-US/docs/Web/SVG/Reference/Element/image) element.

[SVGImageElement.preserveAspectRatio](/en-US/docs/Web/API/SVGImageElement/preserveAspectRatio)Read only

An [SVGAnimatedPreserveAspectRatio](/en-US/docs/Web/API/SVGAnimatedPreserveAspectRatio) corresponding to the [preserveAspectRatio](/en-US/docs/Web/SVG/Reference/Attribute/preserveAspectRatio) attribute of the given [<image>](/en-US/docs/Web/SVG/Reference/Element/image) element.

[SVGImageElement.width](/en-US/docs/Web/API/SVGImageElement/width)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [width](/en-US/docs/Web/SVG/Reference/Attribute/width) attribute of the given [<image>](/en-US/docs/Web/SVG/Reference/Element/image) element.

[SVGImageElement.x](/en-US/docs/Web/API/SVGImageElement/x)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [x](/en-US/docs/Web/SVG/Reference/Attribute/x) attribute of the given [<image>](/en-US/docs/Web/SVG/Reference/Element/image) element.

[SVGImageElement.y](/en-US/docs/Web/API/SVGImageElement/y)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [y](/en-US/docs/Web/SVG/Reference/Attribute/y) attribute of the given [<image>](/en-US/docs/Web/SVG/Reference/Element/image) element.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent interface, [SVGGraphicsElement](/en-US/docs/Web/API/SVGGraphicsElement).

[SVGImageElement.decode()](/en-US/docs/Web/API/SVGImageElement/decode)

Initiates asynchronous decoding of the image data. Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves once the image data is ready to be used.

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGImageElement](https://svgwg.org/svg2-draft/embedded.html#InterfaceSVGImageElement)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 26, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGImageElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgimageelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGImageElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgimageelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGImageElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgimageelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb522a0391a0152cf3f1cc57550d700c87b78ccf5%0A*+Document+last+modified%3A+2025-03-26T01%3A46%3A42.000Z%0A%0A%3C%2Fdetails%3E)
