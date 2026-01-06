# GamepadButton

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2017⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepadButton&level=high)

The `GamepadButton` interface defines an individual button of a gamepad or other controller, allowing access to the current state of different types of buttons available on the control device.

A `GamepadButton` object is returned by querying any value of the array returned by the `buttons` property of the [Gamepad](/en-US/docs/Web/API/Gamepad) interface.

## In this article

- [Instance properties](#instance_properties)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[GamepadButton.pressed](/en-US/docs/Web/API/GamepadButton/pressed)Read only

A boolean value indicating whether the button is currently pressed (`true`) or unpressed (`false`).

[GamepadButton.touched](/en-US/docs/Web/API/GamepadButton/touched)Read only

A boolean value indicating whether the button is currently touched (`true`) or not touched (`false`).

[GamepadButton.value](/en-US/docs/Web/API/GamepadButton/value)Read only

A double value used to represent the current state of analog buttons, such as the triggers on many modern gamepads. The values are normalized to the range 0.0 —1.0, with 0.0 representing a button that is not pressed, and 1.0 representing a button that is fully pressed.

## [Example](#example)

The button values in the following example are stored as an array of `GamepadButton` objects. This simple example checks to see if the [GamepadButton.value](/en-US/docs/Web/API/GamepadButton/value) of a button is greater than `0`, or if the [GamepadButton.pressed](/en-US/docs/Web/API/GamepadButton/pressed) property indicates the button has been pressed.

js

```
function gameLoop() {
  const gp = navigator.getGamepads()[0];

  if (gp.buttons[0].value > 0 || gp.buttons[0].pressed) {
    b--;
  } else if (gp.buttons[1].value > 0 || gp.buttons[1].pressed) {
    a++;
  } else if (gp.buttons[2].value > 0 || gp.buttons[2].pressed) {
    b++;
  } else if (gp.buttons[3].value > 0 || gp.buttons[3].pressed) {
    a--;
  }

  ball.style.left = `${a * 2}px`; // ball is a UI widget
  ball.style.top = `${b * 2}px`;

  requestAnimationFrame(gameLoop);
}
```

## [Specifications](#specifications)

Specification
[Gamepad# gamepadbutton-interface](https://w3c.github.io/gamepad/#gamepadbutton-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

[Using the Gamepad API](/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GamepadButton/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gamepadbutton/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepadButton&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgamepadbutton%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepadButton%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgamepadbutton%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3020adac456187cf18edeb20613482fb73b38c1e%0A*+Document+last+modified%3A+2025-12-27T03%3A36%3A31.000Z%0A%0A%3C%2Fdetails%3E)
