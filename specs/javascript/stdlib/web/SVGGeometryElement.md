# SVGGeometryElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGGeometryElement&level=high)

The `SVGGeometryElement` interface represents SVG elements whose rendering is defined by geometry with an equivalent path, and which can be filled and stroked. This includes paths and the basic shapes.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [SVGGraphicsElement](/en-US/docs/Web/API/SVGGraphicsElement).

[SVGGeometryElement.pathLength](/en-US/docs/Web/API/SVGGeometryElement/pathLength)Read only

This property reflects the [pathLength](/en-US/docs/Web/SVG/Reference/Attribute/pathLength) attribute.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent, [SVGGraphicsElement](/en-US/docs/Web/API/SVGGraphicsElement).

[SVGGeometryElement.isPointInFill()](/en-US/docs/Web/API/SVGGeometryElement/isPointInFill)

Determines whether a given point is within the fill shape of an element. Normal hit testing rules apply; the value of the [pointer-events](/en-US/docs/Web/CSS/Reference/Properties/pointer-events) property on the element determines whether a point is considered to be within the fill.

[SVGGeometryElement.isPointInStroke()](/en-US/docs/Web/API/SVGGeometryElement/isPointInStroke)

Determines whether a given point is within the stroke shape of an element. Normal hit testing rules apply; the value of the [pointer-events](/en-US/docs/Web/CSS/Reference/Properties/pointer-events) property on the element determines whether a point is considered to be within the stroke.

[SVGGeometryElement.getTotalLength()](/en-US/docs/Web/API/SVGGeometryElement/getTotalLength)

Returns the user agent's computed value for the total length of the path in user units.

[SVGGeometryElement.getPointAtLength()](/en-US/docs/Web/API/SVGGeometryElement/getPointAtLength)

Returns the point at a given distance along the path.

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGGeometryElement](https://svgwg.org/svg2-draft/types.html#InterfaceSVGGeometryElement)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 19, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/SVGGeometryElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svggeometryelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGGeometryElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvggeometryelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGGeometryElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvggeometryelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F226ac33eb70ed5411dd2d68bd602c80cafd780b6%0A*+Document+last+modified%3A+2023-02-19T08%3A53%3A53.000Z%0A%0A%3C%2Fdetails%3E)
