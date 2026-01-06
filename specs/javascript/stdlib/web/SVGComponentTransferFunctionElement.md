# SVGComponentTransferFunctionElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGComponentTransferFunctionElement&level=high)

The `SVGComponentTransferFunctionElement` interface represents a base interface used by the component transfer function interfaces.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Static properties](#static_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent interface, [SVGElement](/en-US/docs/Web/API/SVGElement).

[SVGComponentTransferFunctionElement.type](/en-US/docs/Web/API/SVGComponentTransferFunctionElement/type)Read only

An [SVGAnimatedEnumeration](/en-US/docs/Web/API/SVGAnimatedEnumeration) corresponding to the [type](/en-US/docs/Web/SVG/Reference/Attribute/type) attribute of the given element. It takes one of the `SVG_FECOMPONENTTRANSFER_TYPE_*` constants defined on this interface.

[SVGComponentTransferFunctionElement.tableValues](/en-US/docs/Web/API/SVGComponentTransferFunctionElement/tableValues)Read only

An [SVGAnimatedNumberList](/en-US/docs/Web/API/SVGAnimatedNumberList) corresponding to the [tableValues](/en-US/docs/Web/SVG/Reference/Attribute/tableValues) attribute of the given element.

[SVGComponentTransferFunctionElement.slope](/en-US/docs/Web/API/SVGComponentTransferFunctionElement/slope)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the [slope](/en-US/docs/Web/SVG/Reference/Attribute/slope) attribute of the given element.

[SVGComponentTransferFunctionElement.intercept](/en-US/docs/Web/API/SVGComponentTransferFunctionElement/intercept)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the [intercept](/en-US/docs/Web/SVG/Reference/Attribute/intercept) attribute of the given element.

[SVGComponentTransferFunctionElement.amplitude](/en-US/docs/Web/API/SVGComponentTransferFunctionElement/amplitude)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the [amplitude](/en-US/docs/Web/SVG/Reference/Attribute/amplitude) attribute of the given element.

[SVGComponentTransferFunctionElement.exponent](/en-US/docs/Web/API/SVGComponentTransferFunctionElement/exponent)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the [exponent](/en-US/docs/Web/SVG/Reference/Attribute/exponent) attribute of the given element.

[SVGComponentTransferFunctionElement.offset](/en-US/docs/Web/API/SVGComponentTransferFunctionElement/offset)Read only

An [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber) corresponding to the `offset` attribute of the given element.

## [Instance methods](#instance_methods)

This interface does not provide any specific methods, but implements those of its parent, [SVGElement](/en-US/docs/Web/API/SVGElement).

## [Static properties](#static_properties)

[SVG_FECOMPONENTTRANSFER_TYPE_UNKNOWN (0)](#svg_fecomponenttransfer_type_unknown)

The type is not one of predefined types. It is invalid to attempt to define a new value of this type or to attempt to switch an existing value to this type.

[SVG_FECOMPONENTTRANSFER_TYPE_IDENTITY (1)](#svg_fecomponenttransfer_type_identity)

Corresponds to the value `identity`.

[SVG_FECOMPONENTTRANSFER_TYPE_TABLE (2)](#svg_fecomponenttransfer_type_table)

Corresponds to the value `table`.

[SVG_FECOMPONENTTRANSFER_TYPE_DISCRETE (3)](#svg_fecomponenttransfer_type_discrete)

Corresponds to the value `discrete`.

[SVG_FECOMPONENTTRANSFER_TYPE_LINEAR (4)](#svg_fecomponenttransfer_type_linear)

Corresponds to the value `linear`.

[SVG_FECOMPONENTTRANSFER_TYPE_GAMMA (5)](#svg_fecomponenttransfer_type_gamma)

Corresponds to the value `gamma`.

## [Specifications](#specifications)

Specification
[Filter Effects Module Level 1# InterfaceSVGComponentTransferFunctionElement](https://drafts.fxtf.org/filter-effects/#InterfaceSVGComponentTransferFunctionElement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [SVGFEFuncAElement](/en-US/docs/Web/API/SVGFEFuncAElement)
- [SVGFEFuncBElement](/en-US/docs/Web/API/SVGFEFuncBElement)
- [SVGFEFuncGElement](/en-US/docs/Web/API/SVGFEFuncGElement)
- [SVGFEFuncRElement](/en-US/docs/Web/API/SVGFEFuncRElement)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGComponentTransferFunctionElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgcomponenttransferfunctionelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGComponentTransferFunctionElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgcomponenttransferfunctionelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGComponentTransferFunctionElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgcomponenttransferfunctionelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2e39a37874913a1e3fd82999467505fd525e9177%0A*+Document+last+modified%3A+2025-05-02T19%3A48%3A16.000Z%0A%0A%3C%2Fdetails%3E)
