# DocumentFragment

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocumentFragment&level=high)

The `DocumentFragment` interface represents a minimal document object that has no parent.

It is used as a lightweight version of [Document](/en-US/docs/Web/API/Document) that stores a segment of a document structure comprised of nodes just like a standard document. The key difference is due to the fact that the document fragment isn't part of the active document tree structure. Changes made to the fragment don't affect the document.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Usage notes](#usage_notes)
- [Performance](#performance)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[DocumentFragment()](/en-US/docs/Web/API/DocumentFragment/DocumentFragment)

Creates and returns a new `DocumentFragment` object.

## [Instance properties](#instance_properties)

This interface has no specific properties, but inherits those of its parent, [Node](/en-US/docs/Web/API/Node).

[DocumentFragment.childElementCount](/en-US/docs/Web/API/DocumentFragment/childElementCount)Read only

Returns the amount of child [elements](/en-US/docs/Web/API/Element) the `DocumentFragment` has.

[DocumentFragment.children](/en-US/docs/Web/API/DocumentFragment/children)Read only

Returns a live [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) containing all objects of type [Element](/en-US/docs/Web/API/Element) that are children of the `DocumentFragment` object.

[DocumentFragment.firstElementChild](/en-US/docs/Web/API/DocumentFragment/firstElementChild)Read only

Returns the [Element](/en-US/docs/Web/API/Element) that is the first child of the `DocumentFragment` object, or `null` if there is none.

[DocumentFragment.lastElementChild](/en-US/docs/Web/API/DocumentFragment/lastElementChild)Read only

Returns the [Element](/en-US/docs/Web/API/Element) that is the last child of the `DocumentFragment` object, or `null` if there is none.

## [Instance methods](#instance_methods)

This interface inherits the methods of its parent, [Node](/en-US/docs/Web/API/Node).

[DocumentFragment.append()](/en-US/docs/Web/API/DocumentFragment/append)

Inserts a set of [Node](/en-US/docs/Web/API/Node) objects or strings after the last child of the document fragment.

[DocumentFragment.prepend()](/en-US/docs/Web/API/DocumentFragment/prepend)

Inserts a set of [Node](/en-US/docs/Web/API/Node) objects or strings before the first child of the document fragment.

[DocumentFragment.querySelector()](/en-US/docs/Web/API/DocumentFragment/querySelector)

Returns the first [Element](/en-US/docs/Web/API/Element) node within the `DocumentFragment`, in document order, that matches the specified selectors.

[DocumentFragment.querySelectorAll()](/en-US/docs/Web/API/DocumentFragment/querySelectorAll)

Returns a [NodeList](/en-US/docs/Web/API/NodeList) of all the [Element](/en-US/docs/Web/API/Element) nodes within the `DocumentFragment` that match the specified selectors.

[DocumentFragment.moveBefore()](/en-US/docs/Web/API/DocumentFragment/moveBefore)

Moves a given [Node](/en-US/docs/Web/API/Node) inside the invoking `DocumentFragment` as a direct child, before a given reference node, without removing and then inserting the node.

[DocumentFragment.replaceChildren()](/en-US/docs/Web/API/DocumentFragment/replaceChildren)

Replaces the existing children of a `DocumentFragment` with a specified new set of children.

[DocumentFragment.getElementById()](/en-US/docs/Web/API/DocumentFragment/getElementById)

Returns the first [Element](/en-US/docs/Web/API/Element) node within the `DocumentFragment`, in document order, that matches the specified ID. Functionally equivalent to [Document.getElementById()](/en-US/docs/Web/API/Document/getElementById).

## [Usage notes](#usage_notes)

A common use for `DocumentFragment` is to create one, assemble a DOM subtree within it, then append or insert the fragment into the DOM using [Node](/en-US/docs/Web/API/Node) interface methods such as [appendChild()](/en-US/docs/Web/API/Node/appendChild), [append()](/en-US/docs/Web/API/Element/append), or [insertBefore()](/en-US/docs/Web/API/Node/insertBefore). Doing this moves the fragment's nodes into the DOM, leaving behind an empty `DocumentFragment`.

This interface is also of great use with Web components: [<template>](/en-US/docs/Web/HTML/Reference/Elements/template) elements contain a `DocumentFragment` in their [HTMLTemplateElement.content](/en-US/docs/Web/API/HTMLTemplateElement/content) property.

An empty `DocumentFragment` can be created using the [document.createDocumentFragment()](/en-US/docs/Web/API/Document/createDocumentFragment) method or the constructor.

## [Performance](#performance)

The performance benefit of `DocumentFragment` is often overstated. In fact, in some engines, using a `DocumentFragment` is slower than appending to the document in a loop as demonstrated in [this benchmark](https://jsbench.me/02l63eic9j/1). However, the difference between these examples is so marginal that it's better to optimize for readability than performance.

## [Example](#example)

### [HTML](#html)

html

```
<ul></ul>
```

### [JavaScript](#javascript)

js

```
const ul = document.querySelector("ul");
const fruits = ["Apple", "Orange", "Banana", "Melon"];

const fragment = new DocumentFragment();

for (const fruit of fruits) {
  const li = document.createElement("li");
  li.textContent = fruit;
  fragment.append(li);
}

ul.append(fragment);
```

### [Result](#result)

## [Specifications](#specifications)

Specification
[DOM# interface-documentfragment](https://dom.spec.whatwg.org/#interface-documentfragment)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 16, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DocumentFragment/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/documentfragment/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocumentFragment&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdocumentfragment%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocumentFragment%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdocumentfragment%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcf16851e73da29823438198c4f0efcb7026b7d10%0A*+Document+last+modified%3A+2025-09-16T22%3A42%3A01.000Z%0A%0A%3C%2Fdetails%3E)
