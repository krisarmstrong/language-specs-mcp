# CaretPosition

 Baseline  2025 Newly available

 Since ⁨December 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCaretPosition&level=low)

The `CaretPosition` interface represents the caret position, an indicator for the text insertion point. You can get a `CaretPosition` using the [Document.caretPositionFromPoint()](/en-US/docs/Web/API/Document/caretPositionFromPoint) method.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface doesn't inherit any properties.

[CaretPosition.offsetNode](/en-US/docs/Web/API/CaretPosition/offsetNode)Read only

Returns a [Node](/en-US/docs/Web/API/Node) containing the found node at the caret's position.

[CaretPosition.offset](/en-US/docs/Web/API/CaretPosition/offset)Read only

Returns a `long` representing the offset of the selection in the caret position node. This will be the character offset in a text node or the selected child node's index in an element node.

## [Instance methods](#instance_methods)

[CaretPosition.getClientRect](/en-US/docs/Web/API/CaretPosition/getClientRect)

Returns the client rectangle for the caret range.

## [Specifications](#specifications)

Specification
[CSSOM View Module# caret-position](https://drafts.csswg.org/cssom-view/#caret-position)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Document.caretPositionFromPoint()](/en-US/docs/Web/API/Document/caretPositionFromPoint)
- [Range](/en-US/docs/Web/API/Range)
- [Node](/en-US/docs/Web/API/Node)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CaretPosition/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/caretposition/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCaretPosition&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcaretposition%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCaretPosition%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcaretposition%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F896a41d7d9832367a1e24af567fb419e9d4182f8%0A*+Document+last+modified%3A+2025-09-15T12%3A13%3A21.000Z%0A%0A%3C%2Fdetails%3E)
