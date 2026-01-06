# DOMStringList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMStringList&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `DOMStringList` interface is a legacy type returned by some APIs and represents a non-modifiable list of strings (`DOMString`).

This interface was an [attempt to create an unmodifiable list](https://stackoverflow.com/questions/74630989/why-use-domstringlist-rather-than-an-array/74641156#74641156) and only continues to be supported to not break code that's already using it. Modern APIs represent list structures using types based on JavaScript [arrays](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), thus making many array methods available, and at the same time imposing additional semantics on their usage (such as making their items read-only).

These historical reasons do not mean that you as a developer should avoid `DOMStringList`. You don't create `DOMStringList` objects yourself, but you get them from APIs such as `Location.ancestorOrigins`, and these APIs are not deprecated. However, be careful of the semantic differences from a real array.

This interface is used in [IndexedDB](/en-US/docs/Web/API/IndexedDB_API) and in the [Location](/en-US/docs/Web/API/Location) API:

- [IDBDatabase.objectStoreNames](/en-US/docs/Web/API/IDBDatabase/objectStoreNames)
- [IDBObjectStore.indexNames](/en-US/docs/Web/API/IDBObjectStore/indexNames)
- [Location.ancestorOrigins](/en-US/docs/Web/API/Location/ancestorOrigins)

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[DOMStringList.length](/en-US/docs/Web/API/DOMStringList/length)Read only

Returns the size of the list.

## [Instance methods](#instance_methods)

[DOMStringList.item()](/en-US/docs/Web/API/DOMStringList/item)

Returns a string from the list with the given index.

[DOMStringList.contains()](/en-US/docs/Web/API/DOMStringList/contains)

Returns a boolean indicating whether the given string is in the list.

## [Specifications](#specifications)

Specification
[HTML# the-domstringlist-interface](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#the-domstringlist-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/DOMStringList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/domstringlist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMStringList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdomstringlist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMStringList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdomstringlist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3652cfa9c036cf3ceebb1384bdc7edfd549251f3%0A*+Document+last+modified%3A+2024-10-08T19%3A28%3A25.000Z%0A%0A%3C%2Fdetails%3E)
