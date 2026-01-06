# HTMLOptionsCollection

The `HTMLOptionsCollection` interface represents a collection of [<option>](/en-US/docs/Web/HTML/Reference/Elements/option) HTML elements (in document order) and offers methods and properties for selecting from the list as well as optionally altering its items. This object is returned only by the `options` property of [select](/en-US/docs/Web/API/HTMLSelectElement).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[HTMLOptionsCollection.length](/en-US/docs/Web/API/HTMLOptionsCollection/length)

Returns or sets the number of options in the collection.

[HTMLOptionsCollection.selectedIndex](/en-US/docs/Web/API/HTMLOptionsCollection/selectedIndex)

The index number of the first selected [<option>](/en-US/docs/Web/HTML/Reference/Elements/option) element. The value `-1` indicates no element is selected.

## [Instance methods](#instance_methods)

This interface inherits the methods of its parent, [HTMLCollection](/en-US/docs/Web/API/HTMLCollection).

[HTMLOptionsCollection.add()](/en-US/docs/Web/API/HTMLOptionsCollection/add)

Appends an [HTMLOptionElement](/en-US/docs/Web/API/HTMLOptionElement) or [HTMLOptGroupElement](/en-US/docs/Web/API/HTMLOptGroupElement) element to the collection of `option` elements or adds it before a specified option.

[HTMLOptionsCollection.remove()](/en-US/docs/Web/API/HTMLOptionsCollection/remove)

Removes the element at the specified index from the options collection.

## [Specifications](#specifications)

Specification
[HTML# the-htmloptionscollection-interface](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#the-htmloptionscollection-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [HTMLOptionElement](/en-US/docs/Web/API/HTMLOptionElement)
- [HTMLCollection](/en-US/docs/Web/API/HTMLCollection)
- [HTMLOptGroupElement](/en-US/docs/Web/API/HTMLOptGroupElement)
- [HTMLSelectElement](/en-US/docs/Web/API/HTMLSelectElement)
- [Indexed collections guide](/en-US/docs/Web/JavaScript/Guide/Indexed_collections)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLOptionsCollection/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmloptionscollection/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLOptionsCollection&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmloptionscollection%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLOptionsCollection%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmloptionscollection%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9b6cd1b7fa8612257b72b2a85a96dd7d45c0200%0A*+Document+last+modified%3A+2025-04-10T14%3A56%3A07.000Z%0A%0A%3C%2Fdetails%3E)
