# GamepadEvent

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2017⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepadEvent&level=high)

The GamepadEvent interface of the Gamepad API contains references to gamepads connected to the system, which is what the gamepad events [gamepadconnected](/en-US/docs/Web/API/Window/gamepadconnected_event) and [gamepaddisconnected](/en-US/docs/Web/API/Window/gamepaddisconnected_event) are fired in response to.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[GamepadEvent()](/en-US/docs/Web/API/GamepadEvent/GamepadEvent)

Returns a new `GamepadEvent` object.

## [Instance properties](#instance_properties)

[GamepadEvent.gamepad](/en-US/docs/Web/API/GamepadEvent/gamepad)Read only

Returns a [Gamepad](/en-US/docs/Web/API/Gamepad) object, providing access to the associated gamepad data for the event fired.

## [Examples](#examples)

The gamepad property being called on a fired [gamepadconnected](/en-US/docs/Web/API/Window/gamepadconnected_event) event.

js

```
window.addEventListener("gamepadconnected", (e) => {
  console.log(
    "Gamepad connected at index %d: %s. %d buttons, %d axes.",
    e.gamepad.index,
    e.gamepad.id,
    e.gamepad.buttons.length,
    e.gamepad.axes.length,
  );
});
```

And on a [gamepaddisconnected](/en-US/docs/Web/API/Window/gamepaddisconnected_event) event.

js

```
window.addEventListener("gamepaddisconnected", (e) => {
  console.log(
    "Gamepad disconnected from index %d: %s",
    e.gamepad.index,
    e.gamepad.id,
  );
});
```

## [Specifications](#specifications)

Specification
[Gamepad# gamepadevent-interface](https://w3c.github.io/gamepad/#gamepadevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

[Using the Gamepad API](/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GamepadEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gamepadevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepadEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgamepadevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepadEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgamepadevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3020adac456187cf18edeb20613482fb73b38c1e%0A*+Document+last+modified%3A+2025-12-27T03%3A36%3A31.000Z%0A%0A%3C%2Fdetails%3E)
