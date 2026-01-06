# SVGMarkerElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGMarkerElement&level=high)

The `SVGMarkerElement` interface provides access to the properties of [<marker>](/en-US/docs/Web/SVG/Reference/Element/marker) elements, as well as methods to manipulate them. The [<marker>](/en-US/docs/Web/SVG/Reference/Element/marker) element defines the graphics used for drawing marks on a shape.

The following properties and methods all return, or act on the attributes of the [<marker>](/en-US/docs/Web/SVG/Reference/Element/marker) element represented by `SVGMarkerElement`.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [SVGElement](/en-US/docs/Web/API/SVGElement).

[SVGMarkerElement.markerUnits](/en-US/docs/Web/API/SVGMarkerElement/markerUnits)Read only

Returns an [SVGAnimatedEnumeration](/en-US/docs/Web/API/SVGAnimatedEnumeration) object, with one of the following values:

[0](#0)

`SVG_MARKERUNITS_UNKNOWN` which means that the [markerUnits](/en-US/docs/Web/SVG/Reference/Attribute/markerUnits) attribute has a value other than the two predefined keywords.

[1](#1)

`SVG_MARKERUNITS_USERSPACEONUSE` which means that the [markerUnits](/en-US/docs/Web/SVG/Reference/Attribute/markerUnits) attribute has the keyword value `userSpaceOnUse`.

[2](#2)

`SVG_MARKERUNITS_STROKEWIDTH` which means that the [markerUnits](/en-US/docs/Web/SVG/Reference/Attribute/markerUnits) attribute has the keyword value `strokeWidth`.

[SVGMarkerElement.markerWidth](/en-US/docs/Web/API/SVGMarkerElement/markerWidth)Read only

Returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) object containing the width of the [<marker>](/en-US/docs/Web/SVG/Reference/Element/marker) viewport.

[SVGMarkerElement.markerHeight](/en-US/docs/Web/API/SVGMarkerElement/markerHeight)Read only

Returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) object containing the height of the [<marker>](/en-US/docs/Web/SVG/Reference/Element/marker) viewport.

[SVGMarkerElement.orientType](/en-US/docs/Web/API/SVGMarkerElement/orientType)Read only

Returns an [SVGAnimatedEnumeration](/en-US/docs/Web/API/SVGAnimatedEnumeration) object, with one of the following values:

[0](#0_2)

`SVG_MARKER_ORIENT_UNKNOWN` which means that the [orient](/en-US/docs/Web/SVG/Reference/Attribute/orient) attribute has a value other than the two predefined keywords.

[1](#1_2)

`SVG_MARKERUNITS_ORIENT_AUTO` which means that the [orient](/en-US/docs/Web/SVG/Reference/Attribute/orient) attribute has the keyword value `auto`.

[2](#2_2)

`SVG_MARKERUNITS_ORIENT_ANGLE` which means that the [orient](/en-US/docs/Web/SVG/Reference/Attribute/orient) attribute has an [<angle>](/en-US/docs/Web/CSS/Reference/Values/angle) or [<number>](/en-US/docs/Web/CSS/Reference/Values/number) value indicating the angle.

[SVGMarkerElement.orientAngle](/en-US/docs/Web/API/SVGMarkerElement/orientAngle)Read only

Returns an [SVGAnimatedAngle](/en-US/docs/Web/API/SVGAnimatedAngle) object containing the angle of the [orient](/en-US/docs/Web/SVG/Reference/Attribute/orient) attribute.

[SVGMarkerElement.refX](/en-US/docs/Web/API/SVGMarkerElement/refX)Read only

Returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) object containing the value of the [refX](/en-US/docs/Web/SVG/Reference/Attribute/refX) attribute of the [<marker>](/en-US/docs/Web/SVG/Reference/Element/marker).

[SVGMarkerElement.refY](/en-US/docs/Web/API/SVGMarkerElement/refY)Read only

Returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) object containing the value of the [refY](/en-US/docs/Web/SVG/Reference/Attribute/refY) attribute of the [<marker>](/en-US/docs/Web/SVG/Reference/Element/marker).

[SVGMarkerElement.viewBox](/en-US/docs/Web/API/SVGMarkerElement/viewBox)Read only

Returns an [SVGAnimatedRect](/en-US/docs/Web/API/SVGAnimatedRect) object containing an [SVGRect](/en-US/docs/Web/API/SVGRect) which contains the values set by the [viewBox](/en-US/docs/Web/SVG/Reference/Attribute/viewBox) attribute on the [<marker>](/en-US/docs/Web/SVG/Reference/Element/marker).

[SVGMarkerElement.preserveAspectRatio](/en-US/docs/Web/API/SVGMarkerElement/preserveAspectRatio)Read only

Returns an [SVGPreserveAspectRatio](/en-US/docs/Web/API/SVGPreserveAspectRatio) object which contains the values set by the [preserveAspectRatio](/en-US/docs/Web/SVG/Reference/Attribute/preserveAspectRatio) attribute on the [<marker>](/en-US/docs/Web/SVG/Reference/Element/marker) viewport.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent, [SVGElement](/en-US/docs/Web/API/SVGElement).

[SVGMarkerElement.setOrientToAuto()](/en-US/docs/Web/API/SVGMarkerElement/setOrientToAuto)

Sets the value of the [orient](/en-US/docs/Web/SVG/Reference/Attribute/orient) attribute to `auto`.

[SVGMarkerElement.setOrientToAngle()](/en-US/docs/Web/API/SVGMarkerElement/setOrientToAngle)

Sets the value of the [orient](/en-US/docs/Web/SVG/Reference/Attribute/orient) attribute to a specific angle value.

## [Examples](#examples)

The following SVG will be referenced in the examples.

html

```
<svg id="svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker
      id="arrow"
      viewBox="0 0 10 10"
      refX="5"
      refY="5"
      markerWidth="6"
      markerHeight="6"
      orient="90">
      <path d="M 0 0 L 10 5 L 0 10 z" />
    </marker>
  </defs>
</svg>
```

### [Finding the Width of the Marker](#finding_the_width_of_the_marker)

The `markerWidth` property returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) which contains an [SVGLength](/en-US/docs/Web/API/SVGLength) with the value of the [markerWidth](/en-US/docs/Web/SVG/Reference/Attribute/markerWidth) attribute.

js

```
let marker = document.getElementById("arrow");
console.log(marker.markerWidth.baseVal.value); // 6
```

### [Updating the Orientation Angle](#updating_the_orientation_angle)

In the following example the value of the `orient` attribute is updated using `setOrientToAngle()` using an [SVGAngle](/en-US/docs/Web/API/SVGAngle) created using `SVGElement.createSVGAngle()`.

js

```
let svg = document.getElementById("svg");
let marker = document.getElementById("arrow");
console.log(marker.orientAngle.baseVal.value); // value in SVG above - 90
let angle = svg.createSVGAngle();
angle.value = "110";
marker.setOrientToAngle(angle);
console.log(marker.orientAngle.baseVal.value); // new value - 110
```

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGMarkerElement](https://svgwg.org/svg2-draft/painting.html#InterfaceSVGMarkerElement)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGMarkerElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgmarkerelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGMarkerElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgmarkerelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGMarkerElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgmarkerelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
