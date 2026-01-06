# ViewTransitionTypeSet

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FViewTransitionTypeSet&level=not)

The `ViewTransitionTypeSet` interface of the [View Transition API](/en-US/docs/Web/API/View_Transition_API) is a [set-like object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set-like_browser_apis) representing the types of an active view transition. This enables the types to be queried or modified on-the-fly during a transition.

The `ViewTransitionTypeSet` object can be accessed via the [ViewTransition.types](/en-US/docs/Web/API/ViewTransition/types) property.

The property and method links below link to the JavaScript [Set](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) object documentation.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[Set.prototype.size](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/size)

Returns the number of values in the set.

## [Instance methods](#instance_methods)

[Set.prototype.add](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/add)

Inserts the specified value into this set, if it is not already present.

[Set.prototype.clear()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/clear)

Removes all values form the set.

[Set.prototype.delete()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete)

Removes the specified value from this set, if it is in the set.

[Set.prototype.entries()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/entries)

Returns a new iterator object that contains an array of `[value, value]` for each element in the set, in insertion order.

[Set.prototype.forEach()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/forEach)

Calls a callback function once for each value present in the set, in insertion order.

[Set.prototype.has()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/has)

Returns a boolean indicating whether the specified value exists in the set.

[Set.prototype.keys()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/keys)

An alias for [Set.prototype.values()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/values).

[Set.prototype.values()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/values)

Returns a new iterator object that yields the values for each element in the set, in insertion order.

[Set.prototype[Symbol.iterator]()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/Symbol.iterator)

Returns a new iterator object that yields the values for each element in the set, in insertion order.

## [Examples](#examples)

js

```
// Start a view transition
const vt = document.startViewTransition({
  update: updateTheDOMSomehow,
  types: ["slideLeft", "fadeOut", "flipVertical"],
});

// Add another type
vt.types.add("flipHorizontal");

// Delete a type
vt.types.delete("flipVertical");

// Return the number of types in the set
console.log(vt.types.size);

// Log each type to the console
vt.types.forEach((type) => console.log(type));
```

## [Specifications](#specifications)

Specification
[CSS View Transitions Module Level 2# viewtransitiontypeset](https://drafts.csswg.org/css-view-transitions-2/#viewtransitiontypeset)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [ViewTransition.types](/en-US/docs/Web/API/ViewTransition/types)
- [View Transition API](/en-US/docs/Web/API/View_Transition_API)
- [Using the View Transition API](/en-US/docs/Web/API/View_Transition_API/Using)
- [Using view transition types](/en-US/docs/Web/API/View_Transition_API/Using_types)
- [Smooth transitions with the View Transition API](https://developer.chrome.com/docs/web-platform/view-transitions/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 9, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ViewTransitionTypeSet/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/viewtransitiontypeset/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FViewTransitionTypeSet&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fviewtransitiontypeset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FViewTransitionTypeSet%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fviewtransitiontypeset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbaf0cb6bfe8bf2418122300d3f93e3aa94f72dca%0A*+Document+last+modified%3A+2025-12-09T12%3A19%3A47.000Z%0A%0A%3C%2Fdetails%3E)
