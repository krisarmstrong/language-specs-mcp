# SVGPathElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGPathElement&level=high)

The `SVGPathElement` interface corresponds to the [<path>](/en-US/docs/Web/SVG/Reference/Element/path) element.

Note: In SVG 2 the `getPathSegAtLength()` and `createSVGPathSeg*` methods were removed and the `pathLength` property and the `getTotalLength()` and `getPointAtLength()` methods were moved to [SVGGeometryElement](/en-US/docs/Web/API/SVGGeometryElement).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface inherits properties from its parent, [SVGGeometryElement](/en-US/docs/Web/API/SVGGeometryElement).

[SVGPathElement.pathLength](/en-US/docs/Web/API/SVGPathElement/pathLength)Read only

This property reflects the [pathLength](/en-US/docs/Web/SVG/Reference/Attribute/pathLength) attribute.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent, [SVGGeometryElement](/en-US/docs/Web/API/SVGGeometryElement).

[SVGPathElement.getPathData()](/en-US/docs/Web/API/SVGPathElement/getPathData)Experimental

Returns the sequence of path segments that corresponds to the path data, optionally normalizing the values and segment types.

[SVGPathElement.getPointAtLength()](/en-US/docs/Web/API/SVGPathElement/getPointAtLength)

Returns the point at a given distance along the path.

[SVGPathElement.getTotalLength()](/en-US/docs/Web/API/SVGPathElement/getTotalLength)

Returns the user agent's computed value for the total length of the path in user units.

[SVGPathElement.setPathData()](/en-US/docs/Web/API/SVGPathElement/setPathData)Experimental

Sets the sequence of path segments as the new path data.

[SVGPathElement.getPathSegmentAtLength()](/en-US/docs/Web/API/SVGPathElement/getPathSegmentAtLength)Experimental

Returns the segment at a given distance along the path.

### [Deprecated methods](#deprecated_methods)

`SVGPathElement.getPathSegAtLength()`Deprecated

Returns an unsigned long representing the index within the `pathSegList` utilizing the user agent's distance-along-a-path algorithm.

`SVGPathElement.createSVGPathSegClosePath()`Deprecated

Returns a stand-alone, parentless `SVGPathSegClosePath` object.

`SVGPathElement.createSVGPathSegMovetoAbs()`Deprecated

Returns a stand-alone, parentless `SVGPathSegMovetoAbs` object.

`SVGPathElement.createSVGPathSegMovetoRel()`Deprecated

Returns a stand-alone, parentless `SVGPathSegMovetoRel` object.

`SVGPathElement.createSVGPathSegLinetoAbs()`Deprecated

Returns a stand-alone, parentless `SVGPathSegLinetoAbs` object.

`SVGPathElement.createSVGPathSegLinetoRel()`Deprecated

Returns a stand-alone, parentless `SVGPathSegLinetoRel` object.

`SVGPathElement.createSVGPathSegCurvetoCubicAbs()`Deprecated

Returns a stand-alone, parentless `SVGPathSegCurvetoCubicAbs` object.

`SVGPathElement.createSVGPathSegCurvetoCubicRel()`Deprecated

Returns a stand-alone, parentless `SVGPathSegCurvetoCubicRel` object.

`SVGPathElement.createSVGPathSegCurvetoQuadraticAbs()`Deprecated

Returns a stand-alone, parentless `SVGPathSegCurvetoQuadraticAbs` object.

`SVGPathElement.createSVGPathSegCurvetoQuadraticRel()`Deprecated

Returns a stand-alone, parentless `SVGPathSegCurvetoQuadraticRel` object.

`SVGPathElement.createSVGPathSegArcAbs()`Deprecated

Returns a stand-alone, parentless `SVGPathSegArcAbs` object.

`SVGPathElement.createSVGPathSegArcRel()`Deprecated

Returns a stand-alone, parentless `SVGPathSegArcRel` object.

`SVGPathElement.createSVGPathSegLinetoHorizontalAbs()`Deprecated

Returns a stand-alone, parentless `SVGPathSegLinetoHorizontalAbs` object.

`SVGPathElement.createSVGPathSegLinetoHorizontalRel()`Deprecated

Returns a stand-alone, parentless `SVGPathSegLinetoHorizontalRel` object.

`SVGPathElement.createSVGPathSegLinetoVerticalAbs()`Deprecated

Returns a stand-alone, parentless `SVGPathSegLinetoVerticalAbs` object.

`SVGPathElement.createSVGPathSegLinetoVerticalRel()`Deprecated

Returns a stand-alone, parentless `SVGPathSegLinetoVerticalRel` object.

`SVGPathElement.createSVGPathSegCurvetoCubicSmoothAbs()`Deprecated

Returns a stand-alone, parentless `SVGPathSegCurvetoCubicSmoothAbs` object.

`SVGPathElement.createSVGPathSegCurvetoCubicSmoothRel()`Deprecated

Returns a stand-alone, parentless `SVGPathSegCurvetoCubicSmoothRel` object.

`SVGPathElement.createSVGPathSegCurvetoQuadraticSmoothAbs()`Deprecated

Returns a stand-alone, parentless `SVGPathSegCurvetoQuadraticSmoothAbs` object.

`SVGPathElement.createSVGPathSegCurvetoQuadraticSmoothRel()`Deprecated

Returns a stand-alone, parentless `SVGPathSegCurvetoQuadraticSmoothRel` object.

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGPathElement](https://svgwg.org/svg2-draft/paths.html#InterfaceSVGPathElement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [<path>](/en-US/docs/Web/SVG/Reference/Element/path) SVG Element

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGPathElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgpathelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGPathElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgpathelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGPathElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgpathelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F43f272adb6ac15537cff3728c78ddf234485fff8%0A*+Document+last+modified%3A+2025-04-03T04%3A28%3A47.000Z%0A%0A%3C%2Fdetails%3E)
