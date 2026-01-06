# SVG API

SVG provides elements for circles, rectangles, and simple and complex curves. The elements' attribute values specify how these must be drawn. The SVG API is the subset of the DOM connecting these SVG elements and their attribute values to scripts or programming languages by representing them in memory. The SVG API thus provides methods that allow programmatic access to the SVG elements and their attribute values.

The SVG API is a set of interfaces that have been categorized into the following broad categories:

1. [The element interfaces](#svg_element_interfaces) provide access to the properties of SVG elements and methods to manipulate them.
2. [The static data type](#svg_data_type_interfaces) interfaces provide access to element attribute values and methods to manipulate them.
3. For attributes that can be animated, the [animated data type interfaces](#svg_data_type_interfaces) provide read only access to the current animated value of an attribute.
4. [The Synchronized Multimedia Integration Language (SMIL) interfaces](#smil-related_interfaces)
5. [Others](#other_svg_interfaces)

## In this article

- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [See also](#see_also)

## [Interfaces](#interfaces)

### [SVG element interfaces](#svg_element_interfaces)

- [SVGAElement](/en-US/docs/Web/API/SVGAElement)
- [SVGAnimationElement](/en-US/docs/Web/API/SVGAnimationElement)
- [SVGAnimateElement](/en-US/docs/Web/API/SVGAnimateElement)
- [SVGAnimateMotionElement](/en-US/docs/Web/API/SVGAnimateMotionElement)
- [SVGAnimateTransformElement](/en-US/docs/Web/API/SVGAnimateTransformElement)
- [SVGCircleElement](/en-US/docs/Web/API/SVGCircleElement)
- [SVGClipPathElement](/en-US/docs/Web/API/SVGClipPathElement)
- [SVGComponentTransferFunctionElement](/en-US/docs/Web/API/SVGComponentTransferFunctionElement)
- [SVGDefsElement](/en-US/docs/Web/API/SVGDefsElement)
- [SVGDescElement](/en-US/docs/Web/API/SVGDescElement)
- [SVGDiscardElement](/en-US/docs/Web/API/SVGDiscardElement)
- [SVGElement](/en-US/docs/Web/API/SVGElement)
- [SVGEllipseElement](/en-US/docs/Web/API/SVGEllipseElement)
- [SVGFEBlendElement](/en-US/docs/Web/API/SVGFEBlendElement)
- [SVGFEColorMatrixElement](/en-US/docs/Web/API/SVGFEColorMatrixElement)
- [SVGFEComponentTransferElement](/en-US/docs/Web/API/SVGFEComponentTransferElement)
- [SVGFECompositeElement](/en-US/docs/Web/API/SVGFECompositeElement)
- [SVGFEConvolveMatrixElement](/en-US/docs/Web/API/SVGFEConvolveMatrixElement)
- [SVGFEDiffuseLightingElement](/en-US/docs/Web/API/SVGFEDiffuseLightingElement)
- [SVGFEDisplacementMapElement](/en-US/docs/Web/API/SVGFEDisplacementMapElement)
- [SVGFEDistantLightElement](/en-US/docs/Web/API/SVGFEDistantLightElement)
- [SVGFEDropShadowElement](/en-US/docs/Web/API/SVGFEDropShadowElement)
- [SVGFEFloodElement](/en-US/docs/Web/API/SVGFEFloodElement)
- [SVGFEFuncAElement](/en-US/docs/Web/API/SVGFEFuncAElement)
- [SVGFEFuncBElement](/en-US/docs/Web/API/SVGFEFuncBElement)
- [SVGFEFuncGElement](/en-US/docs/Web/API/SVGFEFuncGElement)
- [SVGFEFuncRElement](/en-US/docs/Web/API/SVGFEFuncRElement)
- [SVGFEGaussianBlurElement](/en-US/docs/Web/API/SVGFEGaussianBlurElement)
- [SVGFEImageElement](/en-US/docs/Web/API/SVGFEImageElement)
- [SVGFEMergeElement](/en-US/docs/Web/API/SVGFEMergeElement)
- [SVGFEMergeNodeElement](/en-US/docs/Web/API/SVGFEMergeNodeElement)
- [SVGFEMorphologyElement](/en-US/docs/Web/API/SVGFEMorphologyElement)
- [SVGFEOffsetElement](/en-US/docs/Web/API/SVGFEOffsetElement)
- [SVGFEPointLightElement](/en-US/docs/Web/API/SVGFEPointLightElement)
- [SVGFESpecularLightingElement](/en-US/docs/Web/API/SVGFESpecularLightingElement)
- [SVGFESpotLightElement](/en-US/docs/Web/API/SVGFESpotLightElement)
- [SVGFETileElement](/en-US/docs/Web/API/SVGFETileElement)
- [SVGFETurbulenceElement](/en-US/docs/Web/API/SVGFETurbulenceElement)
- [SVGFilterElement](/en-US/docs/Web/API/SVGFilterElement)
- [SVGForeignObjectElement](/en-US/docs/Web/API/SVGForeignObjectElement)
- [SVGGElement](/en-US/docs/Web/API/SVGGElement)
- [SVGGeometryElement](/en-US/docs/Web/API/SVGGeometryElement)
- [SVGGradientElement](/en-US/docs/Web/API/SVGGradientElement)
- [SVGGraphicsElement](/en-US/docs/Web/API/SVGGraphicsElement)
- [SVGImageElement](/en-US/docs/Web/API/SVGImageElement)
- [SVGLinearGradientElement](/en-US/docs/Web/API/SVGLinearGradientElement)
- [SVGLineElement](/en-US/docs/Web/API/SVGLineElement)
- [SVGMarkerElement](/en-US/docs/Web/API/SVGMarkerElement)Experimental
- [SVGMaskElement](/en-US/docs/Web/API/SVGMaskElement)
- [SVGMetadataElement](/en-US/docs/Web/API/SVGMetadataElement)
- [SVGMPathElement](/en-US/docs/Web/API/SVGMPathElement)
- [SVGPathElement](/en-US/docs/Web/API/SVGPathElement)
- [SVGPatternElement](/en-US/docs/Web/API/SVGPatternElement)
- [SVGPolylineElement](/en-US/docs/Web/API/SVGPolylineElement)
- [SVGPolygonElement](/en-US/docs/Web/API/SVGPolygonElement)
- [SVGRadialGradientElement](/en-US/docs/Web/API/SVGRadialGradientElement)
- [SVGRectElement](/en-US/docs/Web/API/SVGRectElement)
- [SVGScriptElement](/en-US/docs/Web/API/SVGScriptElement)
- [SVGSetElement](/en-US/docs/Web/API/SVGSetElement)
- [SVGStopElement](/en-US/docs/Web/API/SVGStopElement)
- [SVGStyleElement](/en-US/docs/Web/API/SVGStyleElement)
- [SVGSVGElement](/en-US/docs/Web/API/SVGSVGElement)
- [SVGSwitchElement](/en-US/docs/Web/API/SVGSwitchElement)
- [SVGSymbolElement](/en-US/docs/Web/API/SVGSymbolElement)
- [SVGTextContentElement](/en-US/docs/Web/API/SVGTextContentElement)
- [SVGTextElement](/en-US/docs/Web/API/SVGTextElement)
- [SVGTextPathElement](/en-US/docs/Web/API/SVGTextPathElement)
- [SVGTextPositioningElement](/en-US/docs/Web/API/SVGTextPositioningElement)
- [SVGTitleElement](/en-US/docs/Web/API/SVGTitleElement)
- [SVGTSpanElement](/en-US/docs/Web/API/SVGTSpanElement)
- [SVGUseElement](/en-US/docs/Web/API/SVGUseElement)
- [SVGViewElement](/en-US/docs/Web/API/SVGViewElement)

### [SVG data type interfaces](#svg_data_type_interfaces)

Here are the DOM APIs for data types used in the definitions of SVG properties and attributes.

#### Static type

- [SVGAngle](/en-US/docs/Web/API/SVGAngle)
- [SVGLength](/en-US/docs/Web/API/SVGLength)
- [SVGLengthList](/en-US/docs/Web/API/SVGLengthList)
- [SVGNumber](/en-US/docs/Web/API/SVGNumber)
- [SVGNumberList](/en-US/docs/Web/API/SVGNumberList)
- [SVGPreserveAspectRatio](/en-US/docs/Web/API/SVGPreserveAspectRatio)
- [SVGStringList](/en-US/docs/Web/API/SVGStringList)
- [SVGTransform](/en-US/docs/Web/API/SVGTransform)
- [SVGTransformList](/en-US/docs/Web/API/SVGTransformList)

#### Animated type

- [SVGAnimatedAngle](/en-US/docs/Web/API/SVGAnimatedAngle)
- [SVGAnimatedBoolean](/en-US/docs/Web/API/SVGAnimatedBoolean)
- [SVGAnimatedEnumeration](/en-US/docs/Web/API/SVGAnimatedEnumeration)
- [SVGAnimatedInteger](/en-US/docs/Web/API/SVGAnimatedInteger)
- [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength)
- [SVGAnimatedLengthList](/en-US/docs/Web/API/SVGAnimatedLengthList)
- [SVGAnimatedNumber](/en-US/docs/Web/API/SVGAnimatedNumber)
- [SVGAnimatedNumberList](/en-US/docs/Web/API/SVGAnimatedNumberList)
- [SVGAnimatedPreserveAspectRatio](/en-US/docs/Web/API/SVGAnimatedPreserveAspectRatio)
- [SVGAnimatedRect](/en-US/docs/Web/API/SVGAnimatedRect)
- [SVGAnimatedString](/en-US/docs/Web/API/SVGAnimatedString)
- [SVGAnimatedTransformList](/en-US/docs/Web/API/SVGAnimatedTransformList)

### [SMIL-related interfaces](#smil-related_interfaces)

- [TimeEvent](/en-US/docs/Web/API/TimeEvent)

### [Other SVG interfaces](#other_svg_interfaces)

- `ShadowAnimation`
- [SVGUnitTypes](/en-US/docs/Web/API/SVGUnitTypes)
- `SVGUseElementShadowRoot`

## [Specifications](#specifications)

Specification[Scalable Vector Graphics (SVG) 2](https://svgwg.org/svg2-draft/)

## [See also](#see_also)

- [Getting Started with SVG](/en-US/docs/Web/SVG)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVG_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svg_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVG_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvg_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVG_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvg_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc486da8298cdfdba0556a190d8e3f92e9aa117bb%0A*+Document+last+modified%3A+2025-04-19T01%3A44%3A37.000Z%0A%0A%3C%2Fdetails%3E)
