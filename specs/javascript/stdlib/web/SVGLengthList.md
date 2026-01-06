# SVGLengthList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGLengthList&level=high)

The `SVGLengthList` interface defines a list of [SVGLength](/en-US/docs/Web/API/SVGLength) objects. It is used for the [baseVal](/en-US/docs/Web/API/SVGAnimatedLengthList/baseVal) and [animVal](/en-US/docs/Web/API/SVGAnimatedLengthList/animVal) properties of [SVGAnimatedLengthList](/en-US/docs/Web/API/SVGAnimatedLengthList).

An `SVGLengthList` object can be designated as read only, which means that attempts to modify the object will result in an exception being thrown.

An `SVGLengthList` object is indexable and can be accessed like an array.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[length](/en-US/docs/Web/API/SVGLengthList/length)

The number of items in the list.

[numberOfItems](/en-US/docs/Web/API/SVGLengthList/numberOfItems)

The number of items in the list.

## [Instance methods](#instance_methods)

[appendItem()](/en-US/docs/Web/API/SVGLengthList/appendItem)

Inserts a new item at the end of the list.

[clear()](/en-US/docs/Web/API/SVGLengthList/clear)

Clears all existing items from the list, with the result being an empty list.

[initialize()](/en-US/docs/Web/API/SVGLengthList/initialize)

Clears all existing items from the list and re-initializes the list to hold the single item specified by the parameter.

[getItem()](/en-US/docs/Web/API/SVGLengthList/getItem)

Returns the specified item from the list.

[insertItemBefore()](/en-US/docs/Web/API/SVGLengthList/insertItemBefore)

Inserts a new item into the list at the specified position.

[removeItem()](/en-US/docs/Web/API/SVGLengthList/removeItem)

Removes an existing item from the list.

[replaceItem()](/en-US/docs/Web/API/SVGLengthList/replaceItem)

Replaces an existing item in the list with a new item.

## [Examples](#examples)

### [Using SVGLengthList](#using_svglengthlist)

An `SVGLengthList` object can be retrieved from an [SVGAnimatedLengthList](/en-US/docs/Web/API/SVGAnimatedLengthList) object, which itself is retrievable from many animatable length attributes, such as [SVGTextPositioningElement.x](/en-US/docs/Web/API/SVGTextPositioningElement/x).

#### HTML

html

```
<svg
  viewBox="0 0 200 100"
  xmlns="http://www.w3.org/2000/svg"
  width="200"
  height="100">
  <text id="text1" x="10" y="50">Hello</text>
</svg>
<button id="equally-distribute">Equally distribute letters</button>
<button id="reset-spacing">Reset spacing</button>
<div>
  <b>Current <code>SVGLengthList</code></b>
  <pre><output id="output"></output></pre>
</div>
```

#### JavaScript

js

```
const text = document.getElementById("text1");
const output = document.getElementById("output");
const list = text.x.baseVal;
function equallyDistribute() {
  list.clear();
  for (let i = 0; i < text.textContent.length; i++) {
    const length = text.ownerSVGElement.createSVGLength();
    length.value = i * 20 + 10;
    list.appendItem(length);
  }
  printList();
}
function resetSpacing() {
  const length = text.ownerSVGElement.createSVGLength();
  length.value = 10;
  list.initialize(length);
  printList();
}
function printList() {
  output.textContent = "";
  for (let i = 0; i < list.length; i++) {
    output.innerText += `${list.getItem(i).value}\n`;
  }
}
printList();

document
  .getElementById("equally-distribute")
  .addEventListener("click", equallyDistribute);
document
  .getElementById("reset-spacing")
  .addEventListener("click", resetSpacing);
```

#### Result

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGLengthList](https://svgwg.org/svg2-draft/types.html#InterfaceSVGLengthList)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [SVGNumberList](/en-US/docs/Web/API/SVGNumberList)
- [SVGPointList](/en-US/docs/Web/API/SVGPointList)
- [SVGStringList](/en-US/docs/Web/API/SVGStringList)
- [SVGTransformList](/en-US/docs/Web/API/SVGTransformList)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGLengthList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svglengthlist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGLengthList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvglengthlist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGLengthList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvglengthlist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6d2000984203c51f1aad49107ebcebe14d3c1238%0A*+Document+last+modified%3A+2025-05-30T14%3A29%3A57.000Z%0A%0A%3C%2Fdetails%3E)
