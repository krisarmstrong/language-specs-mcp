# SVGRectElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGRectElement&level=high)

The `SVGRectElement` interface provides access to the properties of [<rect>](/en-US/docs/Web/SVG/Reference/Element/rect) elements, as well as methods to manipulate them.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [SVGGeometryElement](/en-US/docs/Web/API/SVGGeometryElement).

[SVGRectElement.x](/en-US/docs/Web/API/SVGRectElement/x)Read only

Returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [x](/en-US/docs/Web/SVG/Reference/Attribute/x) attribute of the given [<rect>](/en-US/docs/Web/SVG/Reference/Element/rect) element.

[SVGRectElement.y](/en-US/docs/Web/API/SVGRectElement/y)Read only

Returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [y](/en-US/docs/Web/SVG/Reference/Attribute/y) attribute of the given [<rect>](/en-US/docs/Web/SVG/Reference/Element/rect) element.

[SVGRectElement.width](/en-US/docs/Web/API/SVGRectElement/width)Read only

Returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [width](/en-US/docs/Web/SVG/Reference/Attribute/width) attribute of the given [<rect>](/en-US/docs/Web/SVG/Reference/Element/rect) element.

[SVGRectElement.height](/en-US/docs/Web/API/SVGRectElement/height)Read only

Returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [height](/en-US/docs/Web/SVG/Reference/Attribute/height) attribute of the given [<rect>](/en-US/docs/Web/SVG/Reference/Element/rect) element.

[SVGRectElement.rx](/en-US/docs/Web/API/SVGRectElement/rx)Read only

Returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [rx](/en-US/docs/Web/SVG/Reference/Attribute/rx) attribute of the given [<rect>](/en-US/docs/Web/SVG/Reference/Element/rect) element.

[SVGRectElement.ry](/en-US/docs/Web/API/SVGRectElement/ry)Read only

Returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [ry](/en-US/docs/Web/SVG/Reference/Attribute/ry) attribute of the given [<rect>](/en-US/docs/Web/SVG/Reference/Element/rect) element.

## [Instance methods](#instance_methods)

This interface doesn't implement any specific methods, but inherits methods from its parent, [SVGGeometryElement](/en-US/docs/Web/API/SVGGeometryElement).

## [Examples](#examples)

### [Changing the color of an SVG rectangle](#changing_the_color_of_an_svg_rectangle)

This example sets the fill color of an `SVGRectElement` to a random value whenever the user clicks it.

#### HTML

html

```
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
  <rect width="300" height="100" id="myrect" />
  <text x="60" y="40" fill="white" font-size="40">Click Me</text>
</svg>
```

#### CSS

css

```
#myrect {
  fill: blue;
  stroke-width: 1;
  stroke: black;
}
```

#### JavaScript

js

```
const myRect = document.querySelector("#myrect");

myRect.addEventListener("click", () => {
  const r = Math.floor(Math.random() * 255);
  const g = Math.floor(Math.random() * 255);
  const b = Math.floor(Math.random() * 255);
  myRect.style.fill = `rgb(${r} ${g} ${b})`;
});
```

#### Result

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGRectElement](https://svgwg.org/svg2-draft/shapes.html#InterfaceSVGRectElement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [<rect>](/en-US/docs/Web/SVG/Reference/Element/rect)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGRectElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgrectelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGRectElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgrectelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGRectElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgrectelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F950f04d94b48f259c471175bdafb52933b2b038d%0A*+Document+last+modified%3A+2025-06-19T11%3A13%3A48.000Z%0A%0A%3C%2Fdetails%3E)
