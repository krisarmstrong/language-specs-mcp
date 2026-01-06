# StaticRange

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStaticRange&level=high)

The [DOM](/en-US/docs/Web/API/Document_Object_Model)`StaticRange` interface extends [AbstractRange](/en-US/docs/Web/API/AbstractRange) to provide a method to specify a range of content in the DOM whose contents don't update to reflect changes which occur within the DOM tree.

This interface offers the same set of properties and methods as `AbstractRange`.

`AbstractRange` and `StaticRange` are not available from [web workers](/en-US/docs/Web/API/Web_Workers_API).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Usage notes](#usage_notes)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[StaticRange()](/en-US/docs/Web/API/StaticRange/StaticRange)

Creates a new `StaticRange` object given options specifying the default values for its properties.

## [Instance properties](#instance_properties)

The properties below are inherited from its parent interface, [AbstractRange](/en-US/docs/Web/API/AbstractRange).

[StaticRange.collapsed](/en-US/docs/Web/API/StaticRange/collapsed)Read only

Returns a Boolean value that is `true` if the range's start and end positions are the same, resulting in a range of length 0.

[StaticRange.endContainer](/en-US/docs/Web/API/StaticRange/endContainer)Read only

Returns the DOM [Node](/en-US/docs/Web/API/Node) which contains the ending point of the range. The offset into the node at which the end position is located is indicated by `endOffset`.

[StaticRange.endOffset](/en-US/docs/Web/API/StaticRange/endOffset)Read only

Returns an integer value indicating the offset into the node given by `endContainer` at which the last character of the range is found.

[StaticRange.startContainer](/en-US/docs/Web/API/StaticRange/startContainer)Read only

Returns the DOM [Node](/en-US/docs/Web/API/Node) which contains the starting point of the range (which is in turn identified by `startOffset`.

[StaticRange.startOffset](/en-US/docs/Web/API/StaticRange/startOffset)Read only

Returns an integer value indicating the offset into the node specified by `startContainer` at which the first character of the range is located.

## [Usage notes](#usage_notes)

A DOM range specifies a span of content in a document, potentially beginning inside one node (or element) and ending inside another one. Unlike a [Range](/en-US/docs/Web/API/Range), a `StaticRange` represents a range which is fixed in time; it does not change to try to keep the same content within it as the document changes. If any changes are made to the DOM, the actual data contained within the range specified by a `StaticRange` may change. This lets the [user agent](/en-US/docs/Glossary/User_agent) avoid a lot of work that is unnecessary if the web app or site doesn't need a live-updating range.

## [Specifications](#specifications)

Specification
[DOM# interface-staticrange](https://dom.spec.whatwg.org/#interface-staticrange)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- Live updating range of content within the DOM: [Range](/en-US/docs/Web/API/Range)
- [AbstractRange](/en-US/docs/Web/API/AbstractRange), the abstract interface from which all ranges are derived

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 27, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/StaticRange/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/staticrange/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStaticRange&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fstaticrange%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStaticRange%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fstaticrange%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a9aa33c8071362dec1426e7e45b587bd472d559%0A*+Document+last+modified%3A+2023-12-27T20%3A32%3A42.000Z%0A%0A%3C%2Fdetails%3E)
