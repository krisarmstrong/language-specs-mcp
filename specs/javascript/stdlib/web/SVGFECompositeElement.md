# SVGFECompositeElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGFECompositeElement&level=high)

The `SVGFECompositeElement` interface corresponds to the [<feComposite>](/en-US/docs/Web/SVG/Reference/Element/feComposite) element.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Static properties](#static_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent interface, [SVGElement](/en-US/docs/Web/API/SVGElement).

[SVGFECompositeElement.height](/en-US/docs/Web/API/SVGFECompositeElement/height)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [height](/en-US/docs/Web/SVG/Reference/Attribute/height) attribute of the given element.

[SVGFECompositeElement.in1](/en-US/docs/Web/API/SVGFECompositeElement/in1)Read only

An [SVGAnimatedString](/en-US/docs/Web/API/SVGAnimatedString) corresponding to the [in](/en-US/docs/Web/SVG/Reference/Attribute/in) attribute of the given element.

[SVGFECompositeElement.in2](/en-US/docs/Web/API/SVGFECompositeElement/in2)Read only

An [SVGAnimatedString](/en-US/docs/Web/API/SVGAnimatedString) corresponding to the [in2](/en-US/docs/Web/SVG/Reference/Attribute/in2) attribute of the given element.

[SVGFECompositeElement.operator](/en-US/docs/Web/API/SVGFECompositeElement/operator)Read only

An [SVGAnimatedEnumeration](/en-US/docs/Web/API/SVGAnimatedEnumeration) corresponding to the [operator](/en-US/docs/Web/SVG/Reference/Attribute/operator) attribute of the given element.

[SVGFECompositeElement.k1](/en-US/docs/Web/API/SVGFECompositeElement/k1)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the [k1](/en-US/docs/Web/SVG/Reference/Attribute/k1) attribute of the given element.

[SVGFECompositeElement.k2](/en-US/docs/Web/API/SVGFECompositeElement/k2)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the [k2](/en-US/docs/Web/SVG/Reference/Attribute/k2) attribute of the given element.

[SVGFECompositeElement.k3](/en-US/docs/Web/API/SVGFECompositeElement/k3)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the [k3](/en-US/docs/Web/SVG/Reference/Attribute/k3) attribute of the given element.

[SVGFECompositeElement.k4](/en-US/docs/Web/API/SVGFECompositeElement/k4)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the [k4](/en-US/docs/Web/SVG/Reference/Attribute/k4) attribute of the given element.

[SVGFECompositeElement.result](/en-US/docs/Web/API/SVGFECompositeElement/result)Read only

An [SVGAnimatedString](/en-US/docs/Web/API/SVGAnimatedString) corresponding to the [result](/en-US/docs/Web/SVG/Reference/Attribute/result) attribute of the given element.

`SVGFECompositeElement.type`Read only

An [SVGAnimatedEnumeration](/en-US/docs/Web/API/SVGAnimatedEnumeration) corresponding to the [type](/en-US/docs/Web/SVG/Reference/Attribute/type) attribute of the given element. It takes one of the `SVG_FECOMPOSITE_OPERATOR_*` constants defined on this interface.

`SVGFECompositeElement.values`Read only

An [SVGAnimatedNumberList](/en-US/docs/Web/API/SVGAnimatedNumberList) corresponding to the [values](/en-US/docs/Web/SVG/Reference/Attribute/values) attribute of the given element.

[SVGFECompositeElement.width](/en-US/docs/Web/API/SVGFECompositeElement/width)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [width](/en-US/docs/Web/SVG/Reference/Attribute/width) attribute of the given element.

[SVGFECompositeElement.x](/en-US/docs/Web/API/SVGFECompositeElement/x)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [x](/en-US/docs/Web/SVG/Reference/Attribute/x) attribute of the given element.

[SVGFECompositeElement.y](/en-US/docs/Web/API/SVGFECompositeElement/y)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [y](/en-US/docs/Web/SVG/Reference/Attribute/y) attribute of the given element.

## [Instance methods](#instance_methods)

This interface does not provide any specific methods, but implements those of its parent, [SVGElement](/en-US/docs/Web/API/SVGElement).

## [Static properties](#static_properties)

[SVG_FECOMPOSITE_OPERATOR_UNKNOWN (0)](#svg_fecomposite_operator_unknown)

The type is not one of predefined types. It is invalid to attempt to define a new value of this type or to attempt to switch an existing value to this type.

[SVG_FECOMPOSITE_OPERATOR_OVER (1)](#svg_fecomposite_operator_over)

Corresponds to the value `over`.

[SVG_FECOMPOSITE_OPERATOR_IN (2)](#svg_fecomposite_operator_in)

Corresponds to the value `in`.

[SVG_FECOMPOSITE_OPERATOR_OUT (3)](#svg_fecomposite_operator_out)

Corresponds to the value `out`.

[SVG_FECOMPOSITE_OPERATOR_ATOP (4)](#svg_fecomposite_operator_atop)

Corresponds to the value `atop`.

[SVG_FECOMPOSITE_OPERATOR_XOR (5)](#svg_fecomposite_operator_xor)

Corresponds to the value `xor`.

[SVG_FECOMPOSITE_OPERATOR_ARITHMETIC (6)](#svg_fecomposite_operator_arithmetic)

Corresponds to the value `arithmetic`.

## [Specifications](#specifications)

Specification
[Filter Effects Module Level 1# InterfaceSVGFECompositeElement](https://drafts.fxtf.org/filter-effects/#InterfaceSVGFECompositeElement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [<feComposite>](/en-US/docs/Web/SVG/Reference/Element/feComposite)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGFECompositeElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgfecompositeelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGFECompositeElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgfecompositeelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGFECompositeElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgfecompositeelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2e39a37874913a1e3fd82999467505fd525e9177%0A*+Document+last+modified%3A+2025-05-02T19%3A48%3A16.000Z%0A%0A%3C%2Fdetails%3E)
