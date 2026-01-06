# DOMImplementation

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMImplementation&level=high)

The `DOMImplementation` interface represents an object providing methods which are not dependent on any particular document. Such an object is returned by the [Document.implementation](/en-US/docs/Web/API/Document/implementation) property.

## In this article

- [Property](#property)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Property](#property)

This interface has no specific property and doesn't inherit any.

## [Instance methods](#instance_methods)

No inherited method.

[DOMImplementation.createDocument()](/en-US/docs/Web/API/DOMImplementation/createDocument)

Creates and returns an [XMLDocument](/en-US/docs/Web/API/XMLDocument).

[DOMImplementation.createDocumentType()](/en-US/docs/Web/API/DOMImplementation/createDocumentType)

Creates and returns a [DocumentType](/en-US/docs/Web/API/DocumentType).

[DOMImplementation.createHTMLDocument()](/en-US/docs/Web/API/DOMImplementation/createHTMLDocument)

Creates and returns an HTML [Document](/en-US/docs/Web/API/Document).

[DOMImplementation.hasFeature()](/en-US/docs/Web/API/DOMImplementation/hasFeature)Deprecated

Returns a boolean value indicating if a given feature is supported or not. This function is unreliable and kept for compatibility purpose alone: except for SVG-related queries, it always returns `true`. Old browsers are very inconsistent in their behavior.

## [Specifications](#specifications)

Specification
[DOM# interface-domimplementation](https://dom.spec.whatwg.org/#interface-domimplementation)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [The DOM interfaces index.](/en-US/docs/Web/API/Document_Object_Model)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 20, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/DOMImplementation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/domimplementation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMImplementation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdomimplementation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMImplementation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdomimplementation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff45409ba2169ff05e433d21aa4ee0424079916b8%0A*+Document+last+modified%3A+2023-02-20T07%3A35%3A10.000Z%0A%0A%3C%2Fdetails%3E)
