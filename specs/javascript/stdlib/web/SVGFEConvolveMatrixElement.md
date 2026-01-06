# SVGFEConvolveMatrixElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGFEConvolveMatrixElement&level=high)

The `SVGFEConvolveMatrixElement` interface corresponds to the [<feConvolveMatrix>](/en-US/docs/Web/SVG/Reference/Element/feConvolveMatrix) element.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Static properties](#static_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent interface, [SVGElement](/en-US/docs/Web/API/SVGElement).

[SVGFEConvolveMatrixElement.bias](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/bias)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the [bias](/en-US/docs/Web/SVG/Reference/Attribute/bias) attribute of the given element.

[SVGFEConvolveMatrixElement.divisor](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/divisor)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the [divisor](/en-US/docs/Web/SVG/Reference/Attribute/divisor) attribute of the given element.

[SVGFEConvolveMatrixElement.edgeMode](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/edgeMode)Read only

An [SVGAnimatedEnumeration](/en-US/docs/Web/API/SVGAnimatedEnumeration) corresponding to the [edgeMode](/en-US/docs/Web/SVG/Reference/Attribute/edgeMode) attribute of the given element. Takes one of the `SVG_EDGEMODE_*` constants defined on this interface.

[SVGFEConvolveMatrixElement.height](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/height)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [height](/en-US/docs/Web/SVG/Reference/Attribute/height) attribute of the given element.

[SVGFEConvolveMatrixElement.in1](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/in1)Read only

An [SVGAnimatedString](/en-US/docs/Web/API/SVGAnimatedString) corresponding to the [in](/en-US/docs/Web/SVG/Reference/Attribute/in) attribute of the given element.

[SVGFEConvolveMatrixElement.kernelMatrix](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/kernelMatrix)Read only

An [SVGAnimatedNumberList](/en-US/docs/Web/API/SVGAnimatedNumberList) corresponding to the [kernelMatrix](/en-US/docs/Web/SVG/Reference/Attribute/kernelMatrix) attribute of the given element.

[SVGFEConvolveMatrixElement.kernelUnitLengthX](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/kernelUnitLengthX)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the [kernelUnitLength](/en-US/docs/Web/SVG/Reference/Attribute/kernelUnitLength) attribute of the given element.

[SVGFEConvolveMatrixElement.kernelUnitLengthY](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/kernelUnitLengthY)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the [kernelUnitLength](/en-US/docs/Web/SVG/Reference/Attribute/kernelUnitLength) attribute of the given element.

[SVGFEConvolveMatrixElement.orderX](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/orderX)Read only

An [SVGAnimatedInteger](/en-US/docs/Web/API/SVGAnimatedInteger) corresponding to the [order](/en-US/docs/Web/SVG/Reference/Attribute/order) attribute of the given element.

[SVGFEConvolveMatrixElement.orderY](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/orderY)Read only

An [SVGAnimatedInteger](/en-US/docs/Web/API/SVGAnimatedInteger) corresponding to the [order](/en-US/docs/Web/SVG/Reference/Attribute/order) attribute of the given element.

[SVGFEConvolveMatrixElement.preserveAlpha](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/preserveAlpha)Read only

An [SVGAnimatedBoolean](/en-US/docs/Web/API/SVGAnimatedBoolean) corresponding to the [preserveAlpha](/en-US/docs/Web/SVG/Reference/Attribute/preserveAlpha) attribute of the given element.

[SVGFEConvolveMatrixElement.result](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/result)Read only

An [SVGAnimatedString](/en-US/docs/Web/API/SVGAnimatedString) corresponding to the [result](/en-US/docs/Web/SVG/Reference/Attribute/result) attribute of the given element.

[SVGFEConvolveMatrixElement.targetX](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/targetX)Read only

An [SVGAnimatedInteger](/en-US/docs/Web/API/SVGAnimatedInteger) corresponding to the [targetX](/en-US/docs/Web/SVG/Reference/Attribute/targetX) attribute of the given element.

[SVGFEConvolveMatrixElement.targetY](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/targetY)Read only

An [SVGAnimatedInteger](/en-US/docs/Web/API/SVGAnimatedInteger) corresponding to the [targetY](/en-US/docs/Web/SVG/Reference/Attribute/targetY) attribute of the given element.

[SVGFEConvolveMatrixElement.width](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/width)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [width](/en-US/docs/Web/SVG/Reference/Attribute/width) attribute of the given element.

[SVGFEConvolveMatrixElement.x](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/x)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [x](/en-US/docs/Web/SVG/Reference/Attribute/x) attribute of the given element.

[SVGFEConvolveMatrixElement.y](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/y)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [y](/en-US/docs/Web/SVG/Reference/Attribute/y) attribute of the given element.

## [Instance methods](#instance_methods)

This interface does not provide any specific methods, but implements those of its parent, [SVGElement](/en-US/docs/Web/API/SVGElement).

## [Static properties](#static_properties)

[SVG_EDGEMODE_UNKNOWN (0)](#svg_edgemode_unknown)

The type is not one of predefined types. It is invalid to attempt to define a new value of this type or to attempt to switch an existing value to this type.

[SVG_EDGEMODE_DUPLICATE (1)](#svg_edgemode_duplicate)

Corresponds to the value `duplicate`.

[SVG_EDGEMODE_WRAP (2)](#svg_edgemode_wrap)

Corresponds to the value `wrap`.

[SVG_EDGEMODE_NONE (3)](#svg_edgemode_none)

Corresponds to the value `none`.

## [Specifications](#specifications)

Specification
[Filter Effects Module Level 1# InterfaceSVGFEConvolveMatrixElement](https://drafts.fxtf.org/filter-effects/#InterfaceSVGFEConvolveMatrixElement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [<feConvolveMatrix>](/en-US/docs/Web/SVG/Reference/Element/feConvolveMatrix)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGFEConvolveMatrixElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgfeconvolvematrixelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGFEConvolveMatrixElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgfeconvolvematrixelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGFEConvolveMatrixElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgfeconvolvematrixelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2e39a37874913a1e3fd82999467505fd525e9177%0A*+Document+last+modified%3A+2025-05-02T19%3A48%3A16.000Z%0A%0A%3C%2Fdetails%3E)
