# SVGTransformList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGTransformList&level=high)

The `SVGTransformList` interface defines a list of [SVGTransform](/en-US/docs/Web/API/SVGTransform) objects.

An `SVGTransformList` object can be designated as read only, which means that attempts to modify the object will result in an exception being thrown.

An `SVGTransformList` is indexable and can be accessed like an array.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[numberOfItems](/en-US/docs/Web/API/SVGTransformList/numberOfItems)

The number of items in the list.

[length](/en-US/docs/Web/API/SVGTransformList/length)

The number of items in the list.

## [Instance methods](#instance_methods)

[clear()](/en-US/docs/Web/API/SVGTransformList/clear)

Clears all existing current items from the list, with the result being an empty list.

[initialize()](/en-US/docs/Web/API/SVGTransformList/initialize)

Clears all existing current items from the list and re-initializes the list to hold the single item specified by the parameter. If the inserted item is already in a list, it is removed from its previous list before it is inserted into this list. The inserted item is the item itself and not a copy. The return value is the item inserted into the list.

[getItem()](/en-US/docs/Web/API/SVGTransformList/getItem)

Returns the specified item from the list. The returned item is the item itself and not a copy. Any changes made to the item are immediately reflected in the list. The first item is number `0`.

[insertItemBefore()](/en-US/docs/Web/API/SVGTransformList/insertItemBefore)

Inserts a new item into the list at the specified position. The first item is number `0`. If `newItem` is already in a list, it is removed from its previous list before it is inserted into this list. The inserted item is the item itself and not a copy. If the item is already in this list, note that the index of the item to insert before is before the removal of the item. If the `index` is equal to 0, then the new item is inserted at the front of the list. If the index is greater than or equal to `numberOfItems`, then the new item is appended to the end of the list.

[replaceItem()](/en-US/docs/Web/API/SVGTransformList/replaceItem)

Replaces an existing item in the list with a new item. If `newItem` is already in a list, it is removed from its previous list before it is inserted into this list. The inserted item is the item itself and not a copy. If the item is already in this list, note that the index of the item to replace is before the removal of the item.

[removeItem()](/en-US/docs/Web/API/SVGTransformList/removeItem)

Removes an existing item from the list.

[appendItem()](/en-US/docs/Web/API/SVGTransformList/appendItem)

Inserts a new item at the end of the list. If `newItem` is already in a list it is removed from its previous list before it is inserted into this list. The inserted item is the item itself and not a copy.

[createSVGTransformFromMatrix()](/en-US/docs/Web/API/SVGTransformList/createSVGTransformFromMatrix)

Creates an `SVGTransform` object which is initialized to transform of type `SVG_TRANSFORM_MATRIX` and whose values are the given matrix. The values from the parameter matrix are copied, the matrix parameter is not adopted as `SVGTransform::matrix`.

[consolidate()](/en-US/docs/Web/API/SVGTransformList/consolidate)

Consolidates the list of separate `SVGTransform` objects by multiplying the equivalent transformation matrices together to result in a list consisting of a single `SVGTransform` object of type `SVG_TRANSFORM_MATRIX`. The consolidation operation creates new `SVGTransform` object as the first and only item in the list. The returned item is the item itself and not a copy. Any changes made to the item are immediately reflected in the list.

## [Examples](#examples)

### [Using multiple SVGTransform objects](#using_multiple_svgtransform_objects)

In this example we create a function that will apply three different transformations to the SVG element that has been clicked on. In order to do this we create a separate [SVGTransform](/en-US/docs/Web/API/SVGTransform) object for each transformation — such as `translate`, `rotate`, and `scale`. We apply multiple transformation by appending the transform object to the `SVGTransformList` associated with an SVG element.

html

```
<svg
  id="my-svg"
  viewBox="0 0 300 280"
  xmlns="http://www.w3.org/2000/svg"
  version="1.1">
  <desc>
    Example showing how to transform svg elements that using SVGTransform
    objects
  </desc>
  <polygon
    fill="orange"
    stroke="black"
    stroke-width="5"
    points="100,225 100,115 130,115 70,15 70,15 10,115 40,115 40,225" />
  <rect
    x="200"
    y="100"
    width="100"
    height="100"
    fill="yellow"
    stroke="black"
    stroke-width="5" />
  <text x="40" y="250" font-family="Verdana" font-size="16" fill="green">
    Click on a shape to transform it
  </text>
</svg>
```

js

```
function transformMe(evt) {
  // svg root element to access the createSVGTransform() function
  const svgRoot = evt.target.parentNode;
  // SVGTransformList of the element that has been clicked on
  const tfmList = evt.target.transform.baseVal;

  // Create a separate transform object for each transform
  const translate = svgRoot.createSVGTransform();
  translate.setTranslate(50, 5);
  const rotate = svgRoot.createSVGTransform();
  rotate.setRotate(10, 0, 0);
  const scale = svgRoot.createSVGTransform();
  scale.setScale(0.8, 0.8);

  // apply the transformations by appending the SVGTransform objects to the SVGTransformList associated with the element
  tfmList.appendItem(translate);
  tfmList.appendItem(rotate);
  tfmList.appendItem(scale);
}

document.querySelector("polygon").addEventListener("click", transformMe);
document.querySelector("rect").addEventListener("click", transformMe);
```

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGTransformList](https://svgwg.org/svg2-draft/coords.html#InterfaceSVGTransformList)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGTransformList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgtransformlist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGTransformList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgtransformlist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGTransformList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgtransformlist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F950f04d94b48f259c471175bdafb52933b2b038d%0A*+Document+last+modified%3A+2025-06-19T11%3A13%3A48.000Z%0A%0A%3C%2Fdetails%3E)
