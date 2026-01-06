# NodeIterator

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNodeIterator&level=high)

The `NodeIterator` interface represents an iterator to traverse nodes of a DOM subtree in document order.

A `NodeIterator` can be created using the [Document.createNodeIterator()](/en-US/docs/Web/API/Document/createNodeIterator) method, as follows:

js

```
const nodeIterator = document.createNodeIterator(root, whatToShow, filter);
```

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface doesn't inherit any property.

[NodeIterator.root](/en-US/docs/Web/API/NodeIterator/root)Read only

Returns a [Node](/en-US/docs/Web/API/Node) representing the root node, as specified when the `NodeIterator` was created.

[NodeIterator.whatToShow](/en-US/docs/Web/API/NodeIterator/whatToShow)Read only

Returns an `unsigned long` bitmask that describes the types of [Node](/en-US/docs/Web/API/Node) to be matched. Non-matching nodes are skipped, but relevant child nodes may be included.

[NodeIterator.filter](/en-US/docs/Web/API/NodeIterator/filter)Read only

Returns a `NodeFilter` used to select the relevant nodes.

[NodeIterator.referenceNode](/en-US/docs/Web/API/NodeIterator/referenceNode)Read only

Returns the [Node](/en-US/docs/Web/API/Node) to which the iterator is anchored.

[NodeIterator.pointerBeforeReferenceNode](/en-US/docs/Web/API/NodeIterator/pointerBeforeReferenceNode)Read only

Returns a boolean indicating whether or not the `NodeIterator` is anchored before the [NodeIterator.referenceNode](/en-US/docs/Web/API/NodeIterator/referenceNode). If `false`, it indicates that the iterator is anchored after the reference node.

## [Instance methods](#instance_methods)

This interface doesn't inherit any method.

[NodeIterator.detach()](/en-US/docs/Web/API/NodeIterator/detach)Deprecated

This is a legacy method, and no longer has any effect. Previously it served to mark a `NodeIterator` as disposed, so it could be reclaimed by garbage collection.

[NodeIterator.previousNode()](/en-US/docs/Web/API/NodeIterator/previousNode)

Returns the previous [Node](/en-US/docs/Web/API/Node) in the document, or `null` if there are none.

[NodeIterator.nextNode()](/en-US/docs/Web/API/NodeIterator/nextNode)

Returns the next [Node](/en-US/docs/Web/API/Node) in the document, or `null` if there are none.

## [Specifications](#specifications)

Specification
[DOM# interface-nodeiterator](https://dom.spec.whatwg.org/#interface-nodeiterator)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The creator method: [Document.createNodeIterator()](/en-US/docs/Web/API/Document/createNodeIterator).
- Related interface: [TreeWalker](/en-US/docs/Web/API/TreeWalker)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/NodeIterator/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/nodeiterator/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNodeIterator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnodeiterator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNodeIterator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnodeiterator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F30ae43a0c98ab92f750fd571d7a3a8ee8b15b4c0%0A*+Document+last+modified%3A+2025-10-23T03%3A17%3A42.000Z%0A%0A%3C%2Fdetails%3E)
