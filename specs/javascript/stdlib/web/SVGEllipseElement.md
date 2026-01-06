# SVGEllipseElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGEllipseElement&level=high)

The `SVGEllipseElement` interface provides access to the properties of [<ellipse>](/en-US/docs/Web/SVG/Reference/Element/ellipse) elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits methods from its parent interface, [SVGGeometryElement](/en-US/docs/Web/API/SVGGeometryElement).

[SVGEllipseElement.cx](/en-US/docs/Web/API/SVGEllipseElement/cx)Read only

This property returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) reflecting the [cx](/en-US/docs/Web/SVG/Reference/Attribute/cx) attribute of the given [<ellipse>](/en-US/docs/Web/SVG/Reference/Element/ellipse) element.

[SVGEllipseElement.cy](/en-US/docs/Web/API/SVGEllipseElement/cy)Read only

This property returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) reflecting the [cy](/en-US/docs/Web/SVG/Reference/Attribute/cy) attribute of the given [<ellipse>](/en-US/docs/Web/SVG/Reference/Element/ellipse) element.

[SVGEllipseElement.rx](/en-US/docs/Web/API/SVGEllipseElement/rx)Read only

This property returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) reflecting the [rx](/en-US/docs/Web/SVG/Reference/Attribute/rx) attribute of the given [<ellipse>](/en-US/docs/Web/SVG/Reference/Element/ellipse) element.

[SVGEllipseElement.ry](/en-US/docs/Web/API/SVGEllipseElement/ry)Read only

This property returns an [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) reflecting the [ry](/en-US/docs/Web/SVG/Reference/Attribute/ry) attribute of the given [<ellipse>](/en-US/docs/Web/SVG/Reference/Element/ellipse) element.

## [Instance methods](#instance_methods)

Inherits methods from its parent interface, [SVGGeometryElement](/en-US/docs/Web/API/SVGGeometryElement).

## [Example](#example)

### [SVG](#svg)

html

```
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="100" cy="100" rx="100" ry="60" id="ellipse" />
</svg>
```

### [JavaScript](#javascript)

js

```
const ellipse = document.getElementById("ellipse");

function outputSize() {
  // Outputs "horizontal radius: 100 vertical radius: 60"
  console.log(
    `horizontal radius: ${ellipse.rx.baseVal.valueAsString}`,
    `vertical radius: ${ellipse.ry.baseVal.valueAsString}`,
  );
}

ellipse.addEventListener("click", outputSize);
```

### [Result](#result)

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGEllipseElement](https://svgwg.org/svg2-draft/shapes.html#InterfaceSVGEllipseElement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [<ellipse>](/en-US/docs/Web/SVG/Reference/Element/ellipse) SVG Element

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGEllipseElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgellipseelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGEllipseElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgellipseelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGEllipseElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgellipseelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F950f04d94b48f259c471175bdafb52933b2b038d%0A*+Document+last+modified%3A+2025-06-19T11%3A13%3A48.000Z%0A%0A%3C%2Fdetails%3E)
