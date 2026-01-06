# HTMLFormControlsCollection

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLFormControlsCollection&level=high)

The `HTMLFormControlsCollection` interface represents a collection of HTML form control elements, returned by the [HTMLFormElement](/en-US/docs/Web/API/HTMLFormElement) interface's [elements](/en-US/docs/Web/API/HTMLFormElement/elements) property.

The collection returned by [HTMLFormElement.elements](/en-US/docs/Web/API/HTMLFormElement/elements) includes the form's associated listed form controls. See [HTMLFormElement.elements](/en-US/docs/Web/API/HTMLFormElement/elements) for the list of [listed form controls](/en-US/docs/Web/API/HTMLFormElement/elements#value) and an explanation of [form association](/en-US/docs/Web/API/HTMLFormElement/elements#associated_form_controls).

This interface replaces one method from [HTMLCollection](/en-US/docs/Web/API/HTMLCollection), on which it is based.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface inherits the properties of its parent, [HTMLCollection](/en-US/docs/Web/API/HTMLCollection).

## [Instance methods](#instance_methods)

This interface inherits the methods of its parent, [HTMLCollection](/en-US/docs/Web/API/HTMLCollection).

[HTMLFormControlsCollection.namedItem()](/en-US/docs/Web/API/HTMLFormControlsCollection/namedItem)

Returns the [RadioNodeList](/en-US/docs/Web/API/RadioNodeList) or the [Element](/en-US/docs/Web/API/Element) in the collection whose `name` or `id` matches the specified name, or `null` if no nodes match. Note that this version of `namedItem()` hides the one inherited from [HTMLCollection](/en-US/docs/Web/API/HTMLCollection). Like that method, using the JavaScript array bracket syntax with a [String](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String), as in `collection["value"]`, is equivalent to `collection.namedItem("value")`.

## [Specifications](#specifications)

Specification
[HTML# htmlformcontrolscollection](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#htmlformcontrolscollection)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [HTMLCollection](/en-US/docs/Web/API/HTMLCollection), [RadioNodeList](/en-US/docs/Web/API/RadioNodeList), [HTMLOptionsCollection](/en-US/docs/Web/API/HTMLOptionsCollection)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLFormControlsCollection/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlformcontrolscollection/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLFormControlsCollection&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlformcontrolscollection%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLFormControlsCollection%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlformcontrolscollection%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8626f2e444062fbbf08b8729ab4269cceaf7d1bd%0A*+Document+last+modified%3A+2025-09-13T00%3A02%3A22.000Z%0A%0A%3C%2Fdetails%3E)
