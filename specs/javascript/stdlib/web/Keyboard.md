# Keyboard

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FKeyboard&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `Keyboard` interface of the [Keyboard API](/en-US/docs/Web/API/Keyboard_API) provides functions that retrieve keyboard layout maps and toggle capturing of key presses from the physical keyboard.

A list of valid code values is found in the [UI Events KeyboardEvent code Values](https://w3c.github.io/uievents-code/) spec.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[Keyboard.getLayoutMap()](/en-US/docs/Web/API/Keyboard/getLayoutMap)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with an instance of [KeyboardLayoutMap](/en-US/docs/Web/API/KeyboardLayoutMap) which is a map-like object with functions for retrieving the strings associated with specific physical keys.

[Keyboard.lock()](/en-US/docs/Web/API/Keyboard/lock)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves after enabling the capture of key presses for any or all of the keys on the physical keyboard.

[Keyboard.unlock()](/en-US/docs/Web/API/Keyboard/unlock)Experimental

Unlocks all keys captured by the `lock()` method and returns synchronously.

## [Example](#example)

### [Keyboard mapping](#keyboard_mapping)

The following example demonstrates how to get the location- or layout-specific string associated with the key that corresponds to the 'W' key on an English QWERTY keyboard.

js

```
if (navigator.keyboard) {
  const keyboard = navigator.keyboard;
  keyboard.getLayoutMap().then((keyboardLayoutMap) => {
    const upKey = keyboardLayoutMap.get("KeyW");
    window.alert(`Press ${upKey} to move up.`);
  });
} else {
  // Do something else.
}
```

### [Keyboard locking](#keyboard_locking)

The following example captures the W, A, S, and D keys, call `lock()` with a list that contains the key code attribute value for each of these keys:

js

```
navigator.keyboard.lock(["KeyW", "KeyA", "KeyS", "KeyD"]);
```

This captures these keys regardless of which modifiers are used with the key press. Assuming a standard United States QWERTY layout, registering `KeyW` ensures that W, Shift+W, Control+W, Control+Shift+W, and all other key modifier combinations with W are sent to the app. The same applies to for `KeyA`, `KeyS`, and `KeyD`.

## [Specifications](#specifications)

Specification
[Keyboard Map# keyboard-interface](https://wicg.github.io/keyboard-map/#keyboard-interface)
[Keyboard Lock# keyboard-interface](https://wicg.github.io/keyboard-lock/#keyboard-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Keyboard/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/keyboard/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FKeyboard&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fkeyboard%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FKeyboard%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fkeyboard%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F941ade970fd7ebad52af692b6ac27cfd96f94100%0A*+Document+last+modified%3A+2025-05-28T14%3A25%3A52.000Z%0A%0A%3C%2Fdetails%3E)
