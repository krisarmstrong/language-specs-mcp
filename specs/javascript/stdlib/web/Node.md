# Node

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNode&level=high)

The [DOM](/en-US/docs/Glossary/DOM)`Node` interface is an abstract base class upon which many other DOM API objects are based, thus letting those object types be used similarly and often interchangeably. As an abstract class, there is no such thing as a plain `Node` object. All objects that implement `Node` functionality are based on one of its subclasses. Most notable are [Document](/en-US/docs/Web/API/Document), [Element](/en-US/docs/Web/API/Element), and [DocumentFragment](/en-US/docs/Web/API/DocumentFragment).

In addition, every kind of DOM node is represented by an interface based on `Node`. These include [Attr](/en-US/docs/Web/API/Attr), [CharacterData](/en-US/docs/Web/API/CharacterData) (which [Text](/en-US/docs/Web/API/Text), [Comment](/en-US/docs/Web/API/Comment), [CDATASection](/en-US/docs/Web/API/CDATASection) and [ProcessingInstruction](/en-US/docs/Web/API/ProcessingInstruction) are all based on), and [DocumentType](/en-US/docs/Web/API/DocumentType).

In some cases, a particular feature of the base `Node` interface may not apply to one of its child interfaces; in that case, the inheriting node may return `null` or throw an exception, depending on circumstances. For example, attempting to add children to a node type that cannot have children will throw an exception.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

In addition to the properties below, `Node` inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[Node.baseURI](/en-US/docs/Web/API/Node/baseURI)Read only

Returns a string representing the base URL of the document containing the `Node`.

[Node.childNodes](/en-US/docs/Web/API/Node/childNodes)Read only

Returns a live [NodeList](/en-US/docs/Web/API/NodeList) containing all the children of this node (including elements, text and comments). [NodeList](/en-US/docs/Web/API/NodeList) being live means that if the children of the `Node` change, the [NodeList](/en-US/docs/Web/API/NodeList) object is automatically updated.

[Node.firstChild](/en-US/docs/Web/API/Node/firstChild)Read only

Returns a `Node` representing the first direct child node of the node, or `null` if the node has no child.

[Node.isConnected](/en-US/docs/Web/API/Node/isConnected)Read only

A boolean indicating whether or not the Node is connected (directly or indirectly) to the context object, e.g., the [Document](/en-US/docs/Web/API/Document) object in the case of the normal DOM, or the [ShadowRoot](/en-US/docs/Web/API/ShadowRoot) in the case of a shadow DOM.

[Node.lastChild](/en-US/docs/Web/API/Node/lastChild)Read only

Returns a `Node` representing the last direct child node of the node, or `null` if the node has no child.

[Node.nextSibling](/en-US/docs/Web/API/Node/nextSibling)Read only

Returns a `Node` representing the next node in the tree, or `null` if there isn't such node.

[Node.nodeName](/en-US/docs/Web/API/Node/nodeName)Read only

Returns a string containing the name of the `Node`. The structure of the name will differ with the node type. E.g. An [HTMLElement](/en-US/docs/Web/API/HTMLElement) will contain the name of the corresponding tag, like `'AUDIO'` for an [HTMLAudioElement](/en-US/docs/Web/API/HTMLAudioElement), a [Text](/en-US/docs/Web/API/Text) node will have the `'#text'` string, or a [Document](/en-US/docs/Web/API/Document) node will have the `'#document'` string.

[Node.nodeType](/en-US/docs/Web/API/Node/nodeType)Read only

Returns an `unsigned short` representing the type of the node. Possible values are:

NameValue`ELEMENT_NODE``1``ATTRIBUTE_NODE``2``TEXT_NODE``3``CDATA_SECTION_NODE``4``PROCESSING_INSTRUCTION_NODE``7``COMMENT_NODE``8``DOCUMENT_NODE``9``DOCUMENT_TYPE_NODE``10``DOCUMENT_FRAGMENT_NODE``11`[Node.nodeValue](/en-US/docs/Web/API/Node/nodeValue)

Returns / Sets the value of the current node.

[Node.ownerDocument](/en-US/docs/Web/API/Node/ownerDocument)Read only

Returns the [Document](/en-US/docs/Web/API/Document) that this node belongs to. If the node is itself a document, returns `null`.

[Node.parentNode](/en-US/docs/Web/API/Node/parentNode)Read only

Returns a `Node` that is the parent of this node. If there is no such node — for example, if this node is the top of the tree, or if it doesn't participate in a tree — this property returns `null`.

[Node.parentElement](/en-US/docs/Web/API/Node/parentElement)Read only

Returns an [Element](/en-US/docs/Web/API/Element) that is the parent of this node. If the node has no parent, or if that parent is not an [Element](/en-US/docs/Web/API/Element), this property returns `null`.

[Node.previousSibling](/en-US/docs/Web/API/Node/previousSibling)Read only

Returns a `Node` representing the previous node in the tree, or `null` if there isn't such node.

[Node.textContent](/en-US/docs/Web/API/Node/textContent)

Returns / Sets the textual content of an element and all its descendants.

## [Instance methods](#instance_methods)

In addition to the methods below, `Node` inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[Node.appendChild()](/en-US/docs/Web/API/Node/appendChild)

Adds the specified `childNode` argument as the last child to the current node. If the argument referenced an existing node on the DOM tree, the node will be detached from its current position and attached at the new position.

[Node.cloneNode()](/en-US/docs/Web/API/Node/cloneNode)

Clone a `Node`, and optionally, all of its contents. By default, it clones the content of the node.

[Node.compareDocumentPosition()](/en-US/docs/Web/API/Node/compareDocumentPosition)

Compares the position of the current node against another node in any other document.

[Node.contains()](/en-US/docs/Web/API/Node/contains)

Returns `true` or `false` value indicating whether or not a node is a descendant of the calling node.

[Node.getRootNode()](/en-US/docs/Web/API/Node/getRootNode)

Returns the context object's root which optionally includes the shadow root if it is available.

[Node.hasChildNodes()](/en-US/docs/Web/API/Node/hasChildNodes)

Returns a boolean value indicating whether or not the element has any child nodes.

[Node.insertBefore()](/en-US/docs/Web/API/Node/insertBefore)

Inserts a `Node` before the reference node as a child of a specified parent node.

[Node.isDefaultNamespace()](/en-US/docs/Web/API/Node/isDefaultNamespace)

Accepts a namespace URI as an argument and returns a boolean value with a value of `true` if the namespace is the default namespace on the given node or `false` if not.

[Node.isEqualNode()](/en-US/docs/Web/API/Node/isEqualNode)

Returns a boolean value which indicates whether or not two nodes are of the same type and all their defining data points match.

[Node.isSameNode()](/en-US/docs/Web/API/Node/isSameNode)

Returns a boolean value indicating whether or not the two nodes are the same (that is, they reference the same object).

[Node.lookupPrefix()](/en-US/docs/Web/API/Node/lookupPrefix)

Returns a string containing the prefix for a given namespace URI, if present, and `null` if not. When multiple prefixes are possible, the result is implementation-dependent.

[Node.lookupNamespaceURI()](/en-US/docs/Web/API/Node/lookupNamespaceURI)

Accepts a prefix and returns the namespace URI associated with it on the given node if found (and `null` if not). Supplying `null` for the prefix will return the default namespace.

[Node.normalize()](/en-US/docs/Web/API/Node/normalize)

Clean up all the text nodes under this element (merge adjacent, remove empty).

[Node.removeChild()](/en-US/docs/Web/API/Node/removeChild)

Removes a child node from the current element, which must be a child of the current node.

[Node.replaceChild()](/en-US/docs/Web/API/Node/replaceChild)

Replaces one child `Node` of the current one with the second one given in parameter.

## [Events](#events)

[selectstart](/en-US/docs/Web/API/Node/selectstart_event)

Fires when the user starts a new selection in this node.

## [Examples](#examples)

### [Remove all children nested within a node](#remove_all_children_nested_within_a_node)

This function remove each first child of an element, until there are none left.

js

```
function removeAllChildren(element) {
  while (element.firstChild) {
    element.removeChild(element.firstChild);
  }
}
```

Using this function is a single call. Here we empty the body of the document:

js

```
removeAllChildren(document.body);
```

An alternative could be to set the textContent to the empty string: `document.body.textContent = ""`.

### [Recurse through child nodes](#recurse_through_child_nodes)

The following function recursively calls a callback function for each node contained by a root node (including the root itself):

js

```
function eachNode(rootNode, callback) {
  if (!callback) {
    const nodes = [];
    eachNode(rootNode, (node) => {
      nodes.push(node);
    });
    return nodes;
  }

  if (callback(rootNode) === false) {
    return false;
  }

  if (rootNode.hasChildNodes()) {
    for (const node of rootNode.childNodes) {
      if (eachNode(node, callback) === false) {
        return;
      }
    }
  }
}
```

The function recursively calls a function for each descendant node of `rootNode` (including the root itself).

If `callback` is omitted, the function returns an [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) instead, which contains `rootNode` and all nodes contained within.

If `callback` is provided, and it returns `false` when called, the current recursion level is aborted, and the function resumes execution at the last parent's level. This can be used to abort loops once a node has been found (such as searching for a text node which contains a certain string).

The function has two parameters:

[rootNode](#rootnode)

The `Node` object whose descendants will be recursed through.

[callback Optional](#callback)

An optional callback [function](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function) that receives a `Node` as its only argument. If omitted, `eachNode` returns an [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of every node contained within `rootNode` (including the root itself).

The following demonstrates a real-world use of the `eachNode()` function: searching for text on a web-page.

We use a wrapper function named `grep` to do the searching:

js

```
function grep(parentNode, pattern) {
  let matches = [];
  let endScan = false;

  eachNode(parentNode, (node) => {
    if (endScan) {
      return false;
    }

    // Ignore anything which isn't a text node
    if (node.nodeType !== Node.TEXT_NODE) {
      return;
    }

    if (typeof pattern === "string" && node.textContent.includes(pattern)) {
      matches.push(node);
    } else if (pattern.test(node.textContent)) {
      if (!pattern.global) {
        endScan = true;
        matches = node;
      } else {
        matches.push(node);
      }
    }
  });

  return matches;
}
```

## [Specifications](#specifications)

Specification
[DOM# interface-node](https://dom.spec.whatwg.org/#interface-node)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Node/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/node/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5cfd038b0d37452042461cfe169c0c9ab87be94d%0A*+Document+last+modified%3A+2025-08-18T20%3A15%3A39.000Z%0A%0A%3C%2Fdetails%3E)
