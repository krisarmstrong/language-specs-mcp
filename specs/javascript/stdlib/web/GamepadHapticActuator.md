# GamepadHapticActuator

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepadHapticActuator&level=not)

The `GamepadHapticActuator` interface of the [Gamepad API](/en-US/docs/Web/API/Gamepad_API) represents hardware in the controller designed to provide haptic feedback to the user (if available), most commonly vibration hardware.

This interface is accessible through the [Gamepad.hapticActuators](/en-US/docs/Web/API/Gamepad/hapticActuators) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[GamepadHapticActuator.effects](/en-US/docs/Web/API/GamepadHapticActuator/effects)Read onlyExperimental

Returns an array of enumerated values representing the different haptic effects that the actuator supports.

[GamepadHapticActuator.type](/en-US/docs/Web/API/GamepadHapticActuator/type)DeprecatedRead onlyNon-standard

Returns an enumerated value representing the type of the haptic hardware. This property is deprecated: use `GamepadHapticActuator.effects` to detect effect support.

## [Instance methods](#instance_methods)

[GamepadHapticActuator.playEffect()](/en-US/docs/Web/API/GamepadHapticActuator/playEffect)Read only

Causes the hardware to play a specific vibration effect.

[GamepadHapticActuator.pulse()](/en-US/docs/Web/API/GamepadHapticActuator/pulse)Read only

Makes the hardware pulse at a certain intensity for a specified duration.

[GamepadHapticActuator.reset()](/en-US/docs/Web/API/GamepadHapticActuator/reset)Read only

Stops the hardware from playing an active vibration effect.

## [Examples](#examples)

js

```
const gamepad = navigator.getGamepads()[0];

gamepad.hapticActuators[0].pulse(1.0, 200);

gamepad.vibrationActuator.playEffect("dual-rumble", {
  startDelay: 0,
  duration: 200,
  weakMagnitude: 1.0,
  strongMagnitude: 1.0,
});
```

## [Specifications](#specifications)

Specification
[Gamepad# gamepadhapticactuator-interface](https://w3c.github.io/gamepad/#gamepadhapticactuator-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Gamepad API](/en-US/docs/Web/API/Gamepad_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GamepadHapticActuator/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gamepadhapticactuator/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepadHapticActuator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgamepadhapticactuator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepadHapticActuator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgamepadhapticactuator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3020adac456187cf18edeb20613482fb73b38c1e%0A*+Document+last+modified%3A+2025-12-27T03%3A36%3A31.000Z%0A%0A%3C%2Fdetails%3E)
