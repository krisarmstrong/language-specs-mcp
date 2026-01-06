# CharacterData

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCharacterData&level=high)

The `CharacterData` abstract interface represents a [Node](/en-US/docs/Web/API/Node) object that contains characters. This is an abstract interface, meaning there aren't any objects of type `CharacterData`: it is implemented by other interfaces like [Text](/en-US/docs/Web/API/Text), [Comment](/en-US/docs/Web/API/Comment), [CDATASection](/en-US/docs/Web/API/CDATASection), or [ProcessingInstruction](/en-US/docs/Web/API/ProcessingInstruction), which aren't abstract.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parents, [Node](/en-US/docs/Web/API/Node) and [EventTarget](/en-US/docs/Web/API/EventTarget).

[CharacterData.data](/en-US/docs/Web/API/CharacterData/data)

A string representing the textual data contained in this object.

[CharacterData.length](/en-US/docs/Web/API/CharacterData/length)Read only

Returns a number representing the size of the string contained in the object.

[CharacterData.nextElementSibling](/en-US/docs/Web/API/CharacterData/nextElementSibling)Read only

Returns the first [Element](/en-US/docs/Web/API/Element) that follows this node, and is a sibling.

[CharacterData.previousElementSibling](/en-US/docs/Web/API/CharacterData/previousElementSibling)Read only

Returns the first [Element](/en-US/docs/Web/API/Element) that precedes this node, and is a sibling.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parents, [Node](/en-US/docs/Web/API/Node) and [EventTarget](/en-US/docs/Web/API/EventTarget).

[CharacterData.after()](/en-US/docs/Web/API/CharacterData/after)

Inserts a set of [Node](/en-US/docs/Web/API/Node) objects or strings in the children list of the `CharacterData`'s parent, just after the `CharacterData` object.

[CharacterData.appendData()](/en-US/docs/Web/API/CharacterData/appendData)

Appends the given string to the `CharacterData.data` string; when this method returns, `data` contains the concatenated string.

[CharacterData.before()](/en-US/docs/Web/API/CharacterData/before)

Inserts a set of [Node](/en-US/docs/Web/API/Node) objects or strings in the children list of the `CharacterData`'s parent, just before the `CharacterData` object.

[CharacterData.deleteData()](/en-US/docs/Web/API/CharacterData/deleteData)

Removes the specified amount of characters, starting at the specified offset, from the `CharacterData.data` string; when this method returns, `data` contains the shortened string.

[CharacterData.insertData()](/en-US/docs/Web/API/CharacterData/insertData)

Inserts the specified characters, at the specified offset, in the `CharacterData.data` string; when this method returns, `data` contains the modified string.

[CharacterData.remove()](/en-US/docs/Web/API/CharacterData/remove)

Removes the object from its parent children list.

[CharacterData.replaceData()](/en-US/docs/Web/API/CharacterData/replaceData)

Replaces the specified amount of characters, starting at the specified offset, with the specified string; when this method returns, `data` contains the modified string.

[CharacterData.replaceWith()](/en-US/docs/Web/API/CharacterData/replaceWith)

Replaces the characters in the children list of its parent with a set of [Node](/en-US/docs/Web/API/Node) objects or strings.

[CharacterData.substringData()](/en-US/docs/Web/API/CharacterData/substringData)

Returns a string containing the part of `CharacterData.data` of the specified length and starting at the specified offset.

## [Specifications](#specifications)

Specification
[DOM# interface-characterdata](https://dom.spec.whatwg.org/#interface-characterdata)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [The DOM overview page](/en-US/docs/Web/API/Document_Object_Model).
- The concrete interfaces implemented it: [Text](/en-US/docs/Web/API/Text), [CDATASection](/en-US/docs/Web/API/CDATASection), [ProcessingInstruction](/en-US/docs/Web/API/ProcessingInstruction), and [Comment](/en-US/docs/Web/API/Comment).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 19, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/CharacterData/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/characterdata/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCharacterData&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcharacterdata%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCharacterData%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcharacterdata%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe811fc31b67e145c5882e8e3f128d1938c627a51%0A*+Document+last+modified%3A+2023-02-19T01%3A35%3A01.000Z%0A%0A%3C%2Fdetails%3E)
