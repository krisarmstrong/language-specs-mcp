# SVGFEGaussianBlurElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGFEGaussianBlurElement&level=high)

The `SVGFEGaussianBlurElement` interface corresponds to the [<feGaussianBlur>](/en-US/docs/Web/SVG/Reference/Element/feGaussianBlur) element.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent interface, [SVGElement](/en-US/docs/Web/API/SVGElement).

`SVGFEGaussianBlurElement.edgeMode`Read only

An [SVGAnimatedEnumeration](/en-US/docs/Web/API/SVGAnimatedEnumeration) corresponding to the [edgeMode](/en-US/docs/Web/SVG/Reference/Attribute/edgeMode) attribute of the given element. Returns two identical values that are one of the following values:

[SVG_EDGEMODE_UNKNOWN (0)](#svg_edgemode_unknown)

The type is not one of predefined types. It is invalid to attempt to define a new value of this type or to attempt to switch an existing value to this type.

[SVG_EDGEMODE_DUPLICATE (1)](#svg_edgemode_duplicate)

Corresponds to the `duplicate` value.

[SVG_EDGEMODE_WRAP (2)](#svg_edgemode_wrap)

Corresponds to the `wrap` value.

[SVG_EDGEMODE_NONE (3)](#svg_edgemode_none)

Corresponds to `none` value.

[SVGFEGaussianBlurElement.height](/en-US/docs/Web/API/SVGFEGaussianBlurElement/height)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [height](/en-US/docs/Web/SVG/Reference/Attribute/height) attribute of the given element.

[SVGFEGaussianBlurElement.in1](/en-US/docs/Web/API/SVGFEGaussianBlurElement/in1)Read only

An [SVGAnimatedString](/en-US/docs/Web/API/SVGAnimatedString) corresponding to the [in](/en-US/docs/Web/SVG/Reference/Attribute/in) attribute of the given element.

[SVGFEGaussianBlurElement.result](/en-US/docs/Web/API/SVGFEGaussianBlurElement/result)Read only

An [SVGAnimatedString](/en-US/docs/Web/API/SVGAnimatedString) corresponding to the [result](/en-US/docs/Web/SVG/Reference/Attribute/result) attribute of the given element.

[SVGFEGaussianBlurElement.stdDeviationX](/en-US/docs/Web/API/SVGFEGaussianBlurElement/stdDeviationX)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the (possibly automatically computed) X component of the [stdDeviation](/en-US/docs/Web/SVG/Reference/Attribute/stdDeviation) attribute of the given element.

[SVGFEGaussianBlurElement.stdDeviationY](/en-US/docs/Web/API/SVGFEGaussianBlurElement/stdDeviationY)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the (possibly automatically computed) Y component of the [stdDeviation](/en-US/docs/Web/SVG/Reference/Attribute/stdDeviation) attribute of the given element.

[SVGFEGaussianBlurElement.width](/en-US/docs/Web/API/SVGFEGaussianBlurElement/width)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [width](/en-US/docs/Web/SVG/Reference/Attribute/width) attribute of the given element.

[SVGFEGaussianBlurElement.x](/en-US/docs/Web/API/SVGFEGaussianBlurElement/x)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [x](/en-US/docs/Web/SVG/Reference/Attribute/x) attribute of the given element.

[SVGFEGaussianBlurElement.y](/en-US/docs/Web/API/SVGFEGaussianBlurElement/y)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [y](/en-US/docs/Web/SVG/Reference/Attribute/y) attribute of the given element.

## [Instance methods](#instance_methods)

This interface also inherits methods of its parent, [SVGElement](/en-US/docs/Web/API/SVGElement).

[SVGFEGaussianBlurElement.setStdDeviation()](/en-US/docs/Web/API/SVGFEGaussianBlurElement/setStdDeviation)

Sets the values for the `stdDeviation` attribute.

## [Specifications](#specifications)

Specification
[Filter Effects Module Level 1# InterfaceSVGFEGaussianBlurElement](https://drafts.fxtf.org/filter-effects/#InterfaceSVGFEGaussianBlurElement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [<feGaussianBlur>](/en-US/docs/Web/SVG/Reference/Element/feGaussianBlur)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 1, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/SVGFEGaussianBlurElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgfegaussianblurelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGFEGaussianBlurElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgfegaussianblurelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGFEGaussianBlurElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgfegaussianblurelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd525572dd0dc9b9d1f5aed68d76a19e0be48ea7e%0A*+Document+last+modified%3A+2023-03-01T08%3A59%3A11.000Z%0A%0A%3C%2Fdetails%3E)
