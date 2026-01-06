# SVGCircleElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGCircleElement&level=high)

The `SVGCircleElement` interface is an interface for the [<circle>](/en-US/docs/Web/SVG/Reference/Element/circle) element.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [SVGGeometryElement](/en-US/docs/Web/API/SVGGeometryElement).

[SVGCircleElement.cx](/en-US/docs/Web/API/SVGCircleElement/cx)Read only

This property defines the x-coordinate of the center of the [<circle>](/en-US/docs/Web/SVG/Reference/Element/circle) element. It is denoted by the [cx](/en-US/docs/Web/SVG/Reference/Attribute/cx) attribute of the element.

[SVGCircleElement.cy](/en-US/docs/Web/API/SVGCircleElement/cy)Read only

This property defines the y-coordinate of the center of the `<circle>` element. It is denoted by the [cy](/en-US/docs/Web/SVG/Reference/Attribute/cy) attribute of the element.

[SVGCircleElement.r](/en-US/docs/Web/API/SVGCircleElement/r)Read only

This property defines the radius of the `<circle>` element. It is denoted by the [r](/en-US/docs/Web/SVG/Reference/Attribute/r) of the element.

## [Instance methods](#instance_methods)

Inherits methods from its parent interface, [SVGGeometryElement](/en-US/docs/Web/API/SVGGeometryElement).

## [Examples](#examples)

### [Resizing a circle](#resizing_a_circle)

In this example we draw a circle and randomly increase or decrease its radius when you click it.

#### HTML

html

```
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 250 250"
  width="250"
  height="250">
  <circle cx="100" cy="100" r="50" fill="gold" id="circle" />
</svg>
```

#### JavaScript

js

```
const circle = document.getElementById("circle");

function clickCircle() {
  // Randomly determine if the circle radius will increase or decrease
  const change = Math.random() > 0.5 ? 10 : -10;
  // Clamp the circle radius to a minimum of 10 and a maximum of 250,
  // so it won't disappear or get bigger than the viewport
  const newValue = Math.min(Math.max(circle.r.baseVal.value + change, 10), 250);
  circle.setAttribute("r", newValue);
}

circle.addEventListener("click", clickCircle);
```

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGCircleElement](https://svgwg.org/svg2-draft/shapes.html#InterfaceSVGCircleElement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [<circle>](/en-US/docs/Web/SVG/Reference/Element/circle) SVG element

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGCircleElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgcircleelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGCircleElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgcircleelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGCircleElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgcircleelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F950f04d94b48f259c471175bdafb52933b2b038d%0A*+Document+last+modified%3A+2025-06-19T11%3A13%3A48.000Z%0A%0A%3C%2Fdetails%3E)
