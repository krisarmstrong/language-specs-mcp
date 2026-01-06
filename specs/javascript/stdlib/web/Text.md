# Text

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FText&level=high)

The `Text` interface represents a text [node](/en-US/docs/Web/API/Node) in a DOM tree.

To understand what a text node is, consider the following document:

html

```
<html lang="en" class="e">
  <head>
    <title>Aliens?</title>
  </head>
  <body>
    Why yes.
  </body>
</html>
```

In that document, there are five text nodes, with the following contents:

- `"\n    "` (after the `<head>` start tag, a newline followed by four spaces)
- `"Aliens?"` (the contents of the `title` element)
- `"\n  "` (after the `</head>` end tag, a newline followed by two spaces)
- `"\n  "` (after the `<body>` start tag, a newline followed by two spaces)
- `"\n Why yes.\n \n\n"` (the contents of the `body` element)

Each of those text nodes is an object that has the properties and methods documented in this article.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[Text()](/en-US/docs/Web/API/Text/Text)

Returns a new `Text` node with the parameter as its textual content.

## [Instance properties](#instance_properties)

Inherits properties from its parents, [CharacterData](/en-US/docs/Web/API/CharacterData), [Node](/en-US/docs/Web/API/Node), and [EventTarget](/en-US/docs/Web/API/EventTarget).

[Text.assignedSlot](/en-US/docs/Web/API/Text/assignedSlot)Read only

Returns a [HTMLSlotElement](/en-US/docs/Web/API/HTMLSlotElement) representing the [<slot>](/en-US/docs/Web/HTML/Reference/Elements/slot) the node is inserted in.

[Text.wholeText](/en-US/docs/Web/API/Text/wholeText)Read only

Returns a string containing the text of all `Text` nodes logically adjacent to this [Node](/en-US/docs/Web/API/Node), concatenated in document order.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [CharacterData](/en-US/docs/Web/API/CharacterData), [Node](/en-US/docs/Web/API/Node), and [EventTarget](/en-US/docs/Web/API/EventTarget).

[Text.splitText](/en-US/docs/Web/API/Text/splitText)

Breaks the node into two nodes at a specified offset.

## [Specifications](#specifications)

Specification
[DOM# interface-text](https://dom.spec.whatwg.org/#interface-text)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [The DOM API](/en-US/docs/Web/API/Document_Object_Model)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 19, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/Text/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/text/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FText&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftext%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FText%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftext%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd414c502f3cc1c08d2fb043e98cda4a65621ff08%0A*+Document+last+modified%3A+2023-02-19T08%3A44%3A56.000Z%0A%0A%3C%2Fdetails%3E)
