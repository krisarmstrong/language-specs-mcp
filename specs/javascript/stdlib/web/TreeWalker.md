# TreeWalker

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTreeWalker&level=high)

The `TreeWalker` object represents the nodes of a document subtree and a position within them.

A `TreeWalker` can be created using the [Document.createTreeWalker()](/en-US/docs/Web/API/Document/createTreeWalker) method.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface doesn't inherit any property.

[TreeWalker.root](/en-US/docs/Web/API/TreeWalker/root)Read only

Returns the root [Node](/en-US/docs/Web/API/Node) as specified when the `TreeWalker` was created.

[TreeWalker.whatToShow](/en-US/docs/Web/API/TreeWalker/whatToShow)Read only

Returns an `unsigned long` which is a bitmask made of constants describing the types of [Node](/en-US/docs/Web/API/Node) that must be presented. Non-matching nodes are skipped, but their children may be included, if relevant.

[TreeWalker.filter](/en-US/docs/Web/API/TreeWalker/filter)Read only

Returns the `NodeFilter` associated with this `TreeWalker` used to select the relevant nodes.

[TreeWalker.currentNode](/en-US/docs/Web/API/TreeWalker/currentNode)

Is the [Node](/en-US/docs/Web/API/Node) on which the `TreeWalker` is currently pointing at.

## [Instance methods](#instance_methods)

This interface doesn't inherit any method.

Note: In the context of a `TreeWalker`, a node is visible if it exists in the logical view determined by the `whatToShow` and `filter` parameter arguments. (Whether or not the node is visible on the screen is irrelevant.)

[TreeWalker.parentNode()](/en-US/docs/Web/API/TreeWalker/parentNode)

Moves the current [Node](/en-US/docs/Web/API/Node) to the first visible ancestor node in the document order, and returns the found node. It also moves the current node to this one. If no such node exists, or if it is before that the root node defined at the object construction, returns `null` and the current node is not changed.

[TreeWalker.firstChild()](/en-US/docs/Web/API/TreeWalker/firstChild)

Moves the current [Node](/en-US/docs/Web/API/Node) to the first visible child of the current node, and returns the found child. It also moves the current node to this child. If no such child exists, returns `null` and the current node is not changed. Note that the node returned by `firstChild()` is dependent on the value of `whatToShow` set during instantiation of the `TreeWalker` object. Assuming the following HTML tree, and if you set the `whatToShow` to `NodeFilter.SHOW_ALL` a call to `firstChild()` will return a `Text` node and not an `HTMLDivElement` object.

html

```
<!doctype html>
<html lang="en">
  <head>
    <title>Demo</title>
  </head>
  <body>
    <div id="container"></div>
  </body>
</html>
```

js

```
let walker = document.createTreeWalker(document.body, NodeFilter.SHOW_ALL);
let node = walker.firstChild(); // nodeName: "#text"
```

But if we do:

js

```
let walker = document.createTreeWalker(
  document.body,
  NodeFilter.SHOW_ELEMENT,
);
let node = walker.firstChild(); // nodeName: "DIV"
```

The same applies to `nextSibling()`, `previousSibling()`, `firstChild()` and `lastChild()`

[TreeWalker.lastChild()](/en-US/docs/Web/API/TreeWalker/lastChild)

Moves the current [Node](/en-US/docs/Web/API/Node) to the last visible child of the current node, and returns the found child. It also moves the current node to this child. If no such child exists, `null` is returned and the current node is not changed.

[TreeWalker.previousSibling()](/en-US/docs/Web/API/TreeWalker/previousSibling)

Moves the current [Node](/en-US/docs/Web/API/Node) to its previous sibling, if any, and returns the found sibling. If there is no such node, return `null` and the current node is not changed.

[TreeWalker.nextSibling()](/en-US/docs/Web/API/TreeWalker/nextSibling)

Moves the current [Node](/en-US/docs/Web/API/Node) to its next sibling, if any, and returns the found sibling. If there is no such node, `null` is returned and the current node is not changed.

[TreeWalker.previousNode()](/en-US/docs/Web/API/TreeWalker/previousNode)

Moves the current [Node](/en-US/docs/Web/API/Node) to the previous visible node in the document order, and returns the found node. It also moves the current node to this one. If no such node exists, or if it is before that the root node defined at the object construction, returns `null` and the current node is not changed.

[TreeWalker.nextNode()](/en-US/docs/Web/API/TreeWalker/nextNode)

Moves the current [Node](/en-US/docs/Web/API/Node) to the next visible node in the document order, and returns the found node. It also moves the current node to this one. If no such node exists, returns `null` and the current node is not changed.

## [Specifications](#specifications)

Specification
[DOM# interface-treewalker](https://dom.spec.whatwg.org/#interface-treewalker)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The creator method: [Document.createTreeWalker()](/en-US/docs/Web/API/Document/createTreeWalker).
- Related interface: [NodeIterator](/en-US/docs/Web/API/NodeIterator).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TreeWalker/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/treewalker/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTreeWalker&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftreewalker%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTreeWalker%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftreewalker%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F30ae43a0c98ab92f750fd571d7a3a8ee8b15b4c0%0A*+Document+last+modified%3A+2025-10-23T03%3A17%3A42.000Z%0A%0A%3C%2Fdetails%3E)
