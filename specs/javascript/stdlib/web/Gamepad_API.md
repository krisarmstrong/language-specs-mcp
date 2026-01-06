# Gamepad API

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2017⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepad_API&level=high)

The Gamepad API is a way for developers to access and respond to signals from gamepads and other game controllers in a simple, consistent way. It contains three interfaces, two events and one specialist function, to respond to gamepads being connected and disconnected, and to access other information about the gamepads themselves, and what buttons and other controls are currently being pressed.

## In this article

- [Interfaces](#interfaces)
- [Tutorials and guides](#tutorials_and_guides)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces](#interfaces)

[Gamepad](/en-US/docs/Web/API/Gamepad)

Represents a gamepad/controller connected to the computer.

[GamepadButton](/en-US/docs/Web/API/GamepadButton)

Represents a button on one of the connected controllers.

[GamepadEvent](/en-US/docs/Web/API/GamepadEvent)

The event object representing events fired that are related to gamepads.

### [Experimental Gamepad extensions](#experimental_gamepad_extensions)

[GamepadHapticActuator](/en-US/docs/Web/API/GamepadHapticActuator)

Represents hardware in the controller designed to provide haptic feedback to the user (if available), most commonly vibration hardware.

[GamepadPose](/en-US/docs/Web/API/GamepadPose)

Represents the pose of a controller (e.g., position and orientation in 3D space) in the case of a [WebVR](/en-US/docs/Web/API/WebVR_API) controller. This is not used by the newer [WebXR](/en-US/docs/Web/API/WebXR_Device_API) standard.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

#### Navigator

[Navigator.getGamepads()](/en-US/docs/Web/API/Navigator/getGamepads)

An extension to the [Navigator](/en-US/docs/Web/API/Navigator) object that returns an array of [Gamepad](/en-US/docs/Web/API/Gamepad) objects, one for each connected gamepad.

#### Window events

[gamepadconnected](/en-US/docs/Web/API/Window/gamepadconnected_event)

An event that will fire when a gamepad is connected.

[gamepaddisconnected](/en-US/docs/Web/API/Window/gamepaddisconnected_event)

An event that will fire when a gamepad is disconnected.

## [Tutorials and guides](#tutorials_and_guides)

- [Using the Gamepad API](/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API)
- [Implementing controls using the Gamepad API](/en-US/docs/Games/Techniques/Controls_Gamepad_API)

## [Specifications](#specifications)

Specification
[Gamepad# gamepad-interface](https://w3c.github.io/gamepad/#gamepad-interface)
[Gamepad Extensions# partial-gamepad-interface](https://w3c.github.io/gamepad/extensions.html#partial-gamepad-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [The Gamepad API](https://hacks.mozilla.org/2013/12/the-gamepad-api/) by Ted Mielczarek and Robert Nyman
- [Simple API demo page](https://luser.github.io/gamepadtest/) ([source](https://github.com/luser/gamepadtest))

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Gamepad_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gamepad_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepad_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgamepad_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepad_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgamepad_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3020adac456187cf18edeb20613482fb73b38c1e%0A*+Document+last+modified%3A+2025-12-27T03%3A36%3A31.000Z%0A%0A%3C%2Fdetails%3E)
