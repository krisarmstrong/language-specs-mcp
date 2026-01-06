# Gamepad

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2017⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepad&level=high)

The `Gamepad` interface of the [Gamepad API](/en-US/docs/Web/API/Gamepad_API) defines an individual gamepad or other controller, allowing access to information such as button presses, axis positions, and id.

A Gamepad object can be returned in one of two ways: via the `gamepad` property of the [gamepadconnected](/en-US/docs/Web/API/Window/gamepadconnected_event) and [gamepaddisconnected](/en-US/docs/Web/API/Window/gamepaddisconnected_event) events, or by grabbing any position in the array returned by the [Navigator.getGamepads()](/en-US/docs/Web/API/Navigator/getGamepads) method.

Note: The support of gamepad features varies across different combinations of platforms and controllers. Even if the controller supports a certain feature (for example, haptic feedback), the platform may not support it for that controller.

## In this article

- [Instance properties](#instance_properties)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[Gamepad.axes](/en-US/docs/Web/API/Gamepad/axes)Read only

An array representing the controls with axes present on the device (e.g., analog thumb sticks).

[Gamepad.buttons](/en-US/docs/Web/API/Gamepad/buttons)Read only

An array of [gamepadButton](/en-US/docs/Web/API/GamepadButton) objects representing the buttons present on the device.

[Gamepad.connected](/en-US/docs/Web/API/Gamepad/connected)Read only

A boolean indicating whether the gamepad is still connected to the system.

[Gamepad.displayId](/en-US/docs/Web/API/Gamepad/displayId)Read onlyDeprecatedNon-standard

Returns the [VRDisplay.displayId](/en-US/docs/Web/API/VRDisplay/displayId) of an associated [VRDisplay](/en-US/docs/Web/API/VRDisplay) (if relevant) — the `VRDisplay` that the gamepad is controlling the displayed scene of.

[Gamepad.hand](/en-US/docs/Web/API/Gamepad/hand)Read onlyExperimental

An enum defining what hand the controller is being held in, or is most likely to be held in.

[Gamepad.hapticActuators](/en-US/docs/Web/API/Gamepad/hapticActuators)Read onlyExperimental

An array containing [GamepadHapticActuator](/en-US/docs/Web/API/GamepadHapticActuator) objects, each of which represents haptic feedback hardware available on the controller.

[Gamepad.vibrationActuator](/en-US/docs/Web/API/Gamepad/vibrationActuator)Read only

A [GamepadHapticActuator](/en-US/docs/Web/API/GamepadHapticActuator) object, which represents haptic feedback hardware available on the controller.

[Gamepad.id](/en-US/docs/Web/API/Gamepad/id)Read only

A string containing identifying information about the controller.

[Gamepad.index](/en-US/docs/Web/API/Gamepad/index)Read only

An integer that is auto-incremented to be unique for each device currently connected to the system.

[Gamepad.mapping](/en-US/docs/Web/API/Gamepad/mapping)Read only

A string indicating whether the browser has remapped the controls on the device to a known layout.

[Gamepad.pose](/en-US/docs/Web/API/Gamepad/pose)Read onlyExperimental

A [GamepadPose](/en-US/docs/Web/API/GamepadPose) object representing the pose information associated with a WebVR controller (e.g., its position and orientation in 3D space).

[Gamepad.timestamp](/en-US/docs/Web/API/Gamepad/timestamp)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the last time the data for this gamepad was updated.

## [Example](#example)

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

## [Specifications](#specifications)

Specification
[Gamepad# gamepad-interface](https://w3c.github.io/gamepad/#gamepad-interface)
[Gamepad Extensions# partial-gamepad-interface](https://w3c.github.io/gamepad/extensions.html#partial-gamepad-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Gamepad API](/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API)
- [Gamepad API](/en-US/docs/Web/API/Gamepad_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Gamepad/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gamepad/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepad&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgamepad%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepad%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgamepad%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3020adac456187cf18edeb20613482fb73b38c1e%0A*+Document+last+modified%3A+2025-12-27T03%3A36%3A31.000Z%0A%0A%3C%2Fdetails%3E)
