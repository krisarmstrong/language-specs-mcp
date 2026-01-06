# RadioNodeList

The `RadioNodeList` interface represents a collection of elements in a [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) returned by a call to [HTMLFormControlsCollection.namedItem()](/en-US/docs/Web/API/HTMLFormControlsCollection/namedItem).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `RadioNodeList` interface inherits the properties of[NodeList](/en-US/docs/Web/API/NodeList).

[RadioNodeList.value](/en-US/docs/Web/API/RadioNodeList/value)

If the underlying element collection contains radio buttons, the `value` property represents the checked radio button. On retrieving the `value` property, the `value` of the currently `checked` radio button is returned as a string. If the collection does not contain any radio buttons or none of the radio buttons in the collection is in `checked` state, the empty string is returned. On setting the `value` property, the first radio button input element whose `value` property is equal to the new value will be set to `checked`.

## [Instance methods](#instance_methods)

The `RadioNodeList` interface inherits the methods of[NodeList](/en-US/docs/Web/API/NodeList).

## [Specifications](#specifications)

Specification
[HTML# radionodelist](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#radionodelist)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [<form>](/en-US/docs/Web/HTML/Reference/Elements/form), [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) elements.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 21, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/RadioNodeList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/radionodelist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRadioNodeList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fradionodelist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRadioNodeList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fradionodelist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdc254715954a0224318e4d25e1de77d595fed769%0A*+Document+last+modified%3A+2024-06-21T00%3A50%3A46.000Z%0A%0A%3C%2Fdetails%3E)
