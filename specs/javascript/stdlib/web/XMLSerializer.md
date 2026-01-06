# XMLSerializer

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLSerializer&level=high)

The `XMLSerializer` interface provides the [serializeToString()](/en-US/docs/Web/API/XMLSerializer/serializeToString) method to construct an XML string representing a [DOM](/en-US/docs/Glossary/DOM) tree.

Note: The resulting XML string is not guaranteed to be well-formed XML.

## In this article

- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[XMLSerializer()](/en-US/docs/Web/API/XMLSerializer/XMLSerializer)

Creates a new `XMLSerializer` object.

## [Instance methods](#instance_methods)

[serializeToString()](/en-US/docs/Web/API/XMLSerializer/serializeToString)

Returns the serialized subtree of a string.

## [Examples](#examples)

### [Serializing XML into a string](#serializing_xml_into_a_string)

This example just serializes an entire document into a string containing XML.

js

```
const s = new XMLSerializer();
const str = s.serializeToString(document);
saveXML(str);
```

This involves creating a new `XMLSerializer` object, then passing the [Document](/en-US/docs/Web/API/Document) to be serialized into [serializeToString()](/en-US/docs/Web/API/XMLSerializer/serializeToString), which returns the XML equivalent of the document. `saveXML()` represents a function that would then save the serialized string.

### [Inserting nodes into a DOM based on XML](#inserting_nodes_into_a_dom_based_on_xml)

This example uses the [Element.insertAdjacentHTML()](/en-US/docs/Web/API/Element/insertAdjacentHTML) method to insert a new DOM [Node](/en-US/docs/Web/API/Node) into the body of the [Document](/en-US/docs/Web/API/Document), based on XML created by serializing an [Element](/en-US/docs/Web/API/Element) object.

Note: In the real world, you should usually instead call [importNode()](/en-US/docs/Web/API/Document/importNode) method to import the new node into the DOM, then call one of the following methods to add the node to the DOM tree:

- The [Element.append()](/en-US/docs/Web/API/Element/append)/[Element.prepend()](/en-US/docs/Web/API/Element/prepend) and [Document.append()](/en-US/docs/Web/API/Document/append)/[Document.prepend()](/en-US/docs/Web/API/Document/prepend) methods.
- The [Element.replaceWith](/en-US/docs/Web/API/Element/replaceWith) method (to replace an existing node with the new one)
- The [Element.insertAdjacentElement()](/en-US/docs/Web/API/Element/insertAdjacentElement) method.

Because `insertAdjacentHTML()` accepts a string and not a `Node` as its second parameter, `XMLSerializer` is used to first convert the node into a string.

js

```
const inp = document.createElement("input");
const XMLS = new XMLSerializer();
const inpSerialized = XMLS.serializeToString(inp); // First convert DOM node into a string

// Insert the newly created node into the document's body
document.body.insertAdjacentHTML("afterbegin", inpSerialized);
```

The code creates a new [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) element by calling [Document.createElement()](/en-US/docs/Web/API/Document/createElement), then serializes it into XML using [serializeToString()](/en-US/docs/Web/API/XMLSerializer/serializeToString).

Once that's done, `insertAdjacentHTML()` is used to insert the `<input>` element into the DOM.

## [Specifications](#specifications)

Specification
[HTML# xmlserializer](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#xmlserializer)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Parsing and serializing XML](/en-US/docs/Web/XML/Guides/Parsing_and_serializing_XML)
- [DOMParser](/en-US/docs/Web/API/DOMParser)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/XMLSerializer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xmlserializer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLSerializer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxmlserializer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLSerializer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxmlserializer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff336c5b6795a562c64fe859aa9ee2becf223ad8a%0A*+Document+last+modified%3A+2025-11-03T18%3A29%3A25.000Z%0A%0A%3C%2Fdetails%3E)
