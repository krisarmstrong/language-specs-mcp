# KeyboardLayoutMap

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FKeyboardLayoutMap&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `KeyboardLayoutMap` interface of the [Keyboard API](/en-US/docs/Web/API/Keyboard_API) is a read-only object with functions for retrieving the string associated with specific physical keys.

A `KeyboardLayoutMap` instance is a read-only [Map-like object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#map-like_browser_apis), in which each key is a string identifying the unique physical key on the keyboard (a "key code"), and the corresponding value is the associated key attribute value (which may be affected by the keyboard layout, and so on).

A list of valid keys is found in the [UI Events KeyboardEvent code Values](https://w3c.github.io/uievents-code/) specification.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[KeyboardLayoutMap.size](/en-US/docs/Web/API/KeyboardLayoutMap/size)Read onlyExperimental

Returns the number of elements in the `KeyboardLayoutMap` object.

## [Instance methods](#instance_methods)

[KeyboardLayoutMap[Symbol.iterator]() 
Experimental](#keyboardlayoutmapsymbol.iterator)

Returns a new [Iterator](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator) object that contains the key/value pairs.

[KeyboardLayoutMap.entries()](/en-US/docs/Web/API/KeyboardLayoutMap/entries)Experimental

Returns a new [Iterator](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator) object that contains the key/value pairs.

[KeyboardLayoutMap.forEach()](/en-US/docs/Web/API/KeyboardLayoutMap/forEach)Experimental

Executes a provided function once for each element of `KeyboardLayoutMap`.

[KeyboardLayoutMap.get()](/en-US/docs/Web/API/KeyboardLayoutMap/get)Experimental

Returns the element with the given key from the `KeyboardLayoutMap` object.

[KeyboardLayoutMap.has()](/en-US/docs/Web/API/KeyboardLayoutMap/has)Experimental

Returns a boolean indicating whether the `KeyboardLayoutMap` object has an element with the specified key.

[KeyboardLayoutMap.keys()](/en-US/docs/Web/API/KeyboardLayoutMap/keys)Experimental

Returns a new [Iterator](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator) object that contains the keys for each index in the `KeyboardLayoutMap` object.

[KeyboardLayoutMap.values()](/en-US/docs/Web/API/KeyboardLayoutMap/values)Experimental

Returns a new [Iterator](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator) object that contains the values for each index in the `KeyboardLayoutMap` object.

## [Examples](#examples)

The following example demonstrates how to get the location- or layout-specific string associated with the keyboard code that corresponds to the 'W' key on an English QWERTY keyboard.

js

```
navigator.keyboard.getLayoutMap().then((keyboardLayoutMap) => {
  const upKey = keyboardLayoutMap.get("KeyW");
  window.alert(`Press ${upKey} to move up.`);
});
```

## [Specifications](#specifications)

Specification
[Keyboard Map# keyboardlayoutmap-interface](https://wicg.github.io/keyboard-map/#keyboardlayoutmap-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/KeyboardLayoutMap/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/keyboardlayoutmap/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FKeyboardLayoutMap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fkeyboardlayoutmap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FKeyboardLayoutMap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fkeyboardlayoutmap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F941ade970fd7ebad52af692b6ac27cfd96f94100%0A*+Document+last+modified%3A+2025-05-28T14%3A25%3A52.000Z%0A%0A%3C%2Fdetails%3E)
