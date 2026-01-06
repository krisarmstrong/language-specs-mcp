# HTMLAllCollection

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `HTMLAllCollection` interface represents a collection of all of the document's elements, accessible by index (like an array) and by the element's [id](/en-US/docs/Web/HTML/Reference/Global_attributes/id). It is returned by the [document.all](/en-US/docs/Web/API/Document/all) property.

`HTMLAllCollection` has a very similar shape to [HTMLCollection](/en-US/docs/Web/API/HTMLCollection), but there are many subtle behavior differences — for example, `HTMLAllCollection` can be called as a function, and its `item()` method can be called with a string representing an element's `id` or `name` attribute.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Usage in JavaScript](#usage_in_javascript)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[HTMLAllCollection.length](/en-US/docs/Web/API/HTMLAllCollection/length)Read only

Returns the number of items in the collection.

## [Instance methods](#instance_methods)

[HTMLAllCollection.item()](/en-US/docs/Web/API/HTMLAllCollection/item)

Returns the element located at the specified offset into the collection, or the element with the specified value for its `id` or `name` attribute. Returns `null` if no element is found.

[HTMLAllCollection.namedItem()](/en-US/docs/Web/API/HTMLAllCollection/namedItem)

Returns the first [element](/en-US/docs/Web/API/Element) in the collection whose [id](/en-US/docs/Web/HTML/Reference/Global_attributes/id) or `name` attribute match the given string name, or `null` if no element matches.

## [Usage in JavaScript](#usage_in_javascript)

### [Indexed access](#indexed_access)

In addition to the methods above, elements in an `HTMLAllCollection` can be accessed by integer indices and string property names. The HTML `id` attribute may contain `:` and `.` as valid characters, which would necessitate using bracket notation for property access. `collection[i]` is equivalent to `collection.item(i)`, where `i` can be an integer, a string containing an integer, or a string representing an `id`.

### [Calling as a function](#calling_as_a_function)

An `HTMLAllCollection` object is callable. When it's called with no arguments or with `undefined`, it returns `null`. Otherwise, it returns the same value as the [item()](/en-US/docs/Web/API/HTMLAllCollection/item) method when given the same arguments.

### [Special type conversion behavior](#special_type_conversion_behavior)

For historical reasons, `document.all` is an object that in the following ways behaves like `undefined`:

- It is [loosely equal](/en-US/docs/Web/JavaScript/Reference/Operators/Equality) to `undefined` and `null`.
- It is [falsy](/en-US/docs/Glossary/Falsy) in boolean contexts.
- Its [typeof](/en-US/docs/Web/JavaScript/Reference/Operators/typeof) is `"undefined"`.

These special behaviors ensure that code like:

js

```
if (document.all) {
  // Assume that we are in IE; provide special logic
}
// Assume that we are in a modern browser
```

Will continue to provide modern behavior even if the code is run in a browser that implements `document.all` for compatibility reasons.

However, in all other contexts, `document.all` remains an object. For example:

- It is not [strictly equal](/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality) to either `undefined` or `null`.
- When used on the left-hand side of the [nullish coalescing operator](/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing) (`??`) or the [optional chaining operator](/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining) (`?.`), it will not cause the expression to short-circuit.

## [Specifications](#specifications)

Specification
[HTML# the-htmlallcollection-interface](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#the-htmlallcollection-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [HTMLCollection](/en-US/docs/Web/API/HTMLCollection)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLAllCollection/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlallcollection/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLAllCollection&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlallcollection%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLAllCollection%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlallcollection%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9b6cd1b7fa8612257b72b2a85a96dd7d45c0200%0A*+Document+last+modified%3A+2025-04-10T14%3A56%3A07.000Z%0A%0A%3C%2Fdetails%3E)
