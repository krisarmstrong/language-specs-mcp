# HTMLCollection

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLCollection&level=high)

The `HTMLCollection` interface represents a generic collection (array-like object similar to [arguments](/en-US/docs/Web/JavaScript/Reference/Functions/arguments)) of elements (in document order) and offers methods and properties for selecting from the list.

An `HTMLCollection` in the HTML DOM is live; it is automatically updated when the underlying document is changed. For this reason it is a good idea to make a copy (e.g., using [Array.from](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)) to iterate over if adding, moving, or removing nodes.

This interface is called `HTMLCollection` for historical reasons, because before the modern DOM, collections implementing this interface could only have HTML elements as their items.

This interface was an [attempt to create an unmodifiable list](https://stackoverflow.com/questions/74630989/why-use-domstringlist-rather-than-an-array/74641156#74641156) and only continues to be supported to not break code that's already using it. Modern APIs represent list structures using types based on JavaScript [arrays](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), thus making many array methods available, and at the same time imposing additional semantics on their usage (such as making their items read-only).

These historical reasons do not mean that you as a developer should avoid `HTMLCollection`. You don't create `HTMLCollection` objects yourself, but you get them from APIs such as [Document.getElementsByClassName()](/en-US/docs/Web/API/Document/getElementsByClassName), and these APIs are not deprecated. However, be careful of the semantic differences from a real array.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Usage in JavaScript](#usage_in_javascript)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[HTMLCollection.length](/en-US/docs/Web/API/HTMLCollection/length)Read only

Returns the number of items in the collection.

## [Instance methods](#instance_methods)

[HTMLCollection.item()](/en-US/docs/Web/API/HTMLCollection/item)

Returns the specific element at the given zero-based `index` into the list. Returns `null` if the `index` is out of range.

An alternative to accessing `collection[i]` (which instead returns `undefined` when `i` is out-of-bounds). This is mostly useful for non-JavaScript DOM implementations.

[HTMLCollection.namedItem()](/en-US/docs/Web/API/HTMLCollection/namedItem)

Returns the specific node whose ID or, as a fallback, name matches the string specified by `name`. Matching by name is only done as a last resort, only in HTML, and only if the referenced element supports the `name` attribute. Returns `null` if no node exists by the given name.

An alternative to accessing `collection[name]` (which instead returns `undefined` when `name` does not exist). This is mostly useful for non-JavaScript DOM implementations.

## [Usage in JavaScript](#usage_in_javascript)

`HTMLCollection` also exposes its members as properties by name and index. HTML IDs may contain `:` and `.` as valid characters, which would necessitate using bracket notation for property access. Currently, an `HTMLCollection` object does not recognize purely numeric IDs, which would cause conflict with the array-style access, though HTML does permit these.

For example, assuming there is one `<form>` element in the document and its `id` is `myForm`:

js

```
let elem1, elem2;

// document.forms is an HTMLCollection

elem1 = document.forms[0];
elem2 = document.forms.item(0);

alert(elem1 === elem2); // shows: "true"

elem1 = document.forms.myForm;
elem2 = document.forms.namedItem("myForm");

alert(elem1 === elem2); // shows: "true"

elem1 = document.forms["named.item.with.periods"];
```

## [Specifications](#specifications)

Specification
[DOM# interface-htmlcollection](https://dom.spec.whatwg.org/#interface-htmlcollection)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [NodeList](/en-US/docs/Web/API/NodeList)
- [HTMLFormControlsCollection](/en-US/docs/Web/API/HTMLFormControlsCollection), [HTMLOptionsCollection](/en-US/docs/Web/API/HTMLOptionsCollection)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLCollection/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlcollection/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLCollection&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlcollection%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLCollection%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlcollection%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
