# DocumentType

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocumentType&level=high)

The `DocumentType` interface represents a [Node](/en-US/docs/Web/API/Node) containing a doctype.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [Node](/en-US/docs/Web/API/Node).

[DocumentType.name](/en-US/docs/Web/API/DocumentType/name)Read only

The type of the document. It is always `"html"` for HTML documents, but will vary for XML documents.

[DocumentType.publicId](/en-US/docs/Web/API/DocumentType/publicId)Read only

A string with an identifier of the type of document. Empty if the doctype given specifies no public ID.

[DocumentType.systemId](/en-US/docs/Web/API/DocumentType/systemId)Read only

A string containing the URL to the associated DTD. Empty if the doctype given specifies no system ID.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [Node](/en-US/docs/Web/API/Node).

[DocumentType.after()](/en-US/docs/Web/API/DocumentType/after)

Inserts a set of [Node](/en-US/docs/Web/API/Node) objects or strings in the children list of the object's parent, just after this node.

[DocumentType.before()](/en-US/docs/Web/API/DocumentType/before)

Inserts a set of [Node](/en-US/docs/Web/API/Node) objects or strings in the children list of the object's parent, just before this node.

[DocumentType.remove()](/en-US/docs/Web/API/DocumentType/remove)

Removes this object from its parent children list.

[DocumentType.replaceWith()](/en-US/docs/Web/API/DocumentType/replaceWith)

Replaces the document type with a set of given nodes.

## [Specifications](#specifications)

Specification
[DOM# interface-documenttype](https://dom.spec.whatwg.org/#interface-documenttype)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [The DOM interfaces index.](/en-US/docs/Web/API/Document_Object_Model)
- [DOMImplementation.createDocumentType()](/en-US/docs/Web/API/DOMImplementation/createDocumentType) to create a new `DocumentType` node.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/DocumentType/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/documenttype/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocumentType&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdocumenttype%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocumentType%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdocumenttype%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F20bf311572eeb3dfaaec345144b81120bd9eda03%0A*+Document+last+modified%3A+2024-10-24T01%3A32%3A27.000Z%0A%0A%3C%2Fdetails%3E)
