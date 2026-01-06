# GamepadPose

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepadPose&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `GamepadPose` interface of the [Gamepad API](/en-US/docs/Web/API/Gamepad_API) represents the pose of a [WebVR](/en-US/docs/Web/API/WebVR_API) controller at a given timestamp (which includes orientation, position, velocity, and acceleration information).

This interface is accessible through the [Gamepad.pose](/en-US/docs/Web/API/Gamepad/pose) property.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[GamepadPose.hasOrientation](/en-US/docs/Web/API/GamepadPose/hasOrientation)Read onlyExperimental

Returns a boolean indicating whether the gamepad is capable of returning orientation information (`true`) or not (`false`).

[GamepadPose.hasPosition](/en-US/docs/Web/API/GamepadPose/hasPosition)Read onlyExperimental

Returns a boolean indicating whether the gamepad is capable of returning position information (`true`) or not (`false`).

[GamepadPose.position](/en-US/docs/Web/API/GamepadPose/position)Read onlyExperimental

Returns the position of the [Gamepad](/en-US/docs/Web/API/Gamepad) as a 3D vector.

[GamepadPose.linearVelocity](/en-US/docs/Web/API/GamepadPose/linearVelocity)Read onlyExperimental

Returns the linear velocity of the [Gamepad](/en-US/docs/Web/API/Gamepad), in meters per second.

[GamepadPose.linearAcceleration](/en-US/docs/Web/API/GamepadPose/linearAcceleration)Read onlyExperimental

Returns the linear acceleration of the [Gamepad](/en-US/docs/Web/API/Gamepad), in meters per second per second.

[GamepadPose.orientation](/en-US/docs/Web/API/GamepadPose/orientation)Read onlyExperimental

Returns the orientation of the [Gamepad](/en-US/docs/Web/API/Gamepad), as a quaternion value.

[GamepadPose.angularVelocity](/en-US/docs/Web/API/GamepadPose/angularVelocity)Read onlyExperimental

Returns the angular velocity of the [Gamepad](/en-US/docs/Web/API/Gamepad), in radians per second.

[GamepadPose.angularAcceleration](/en-US/docs/Web/API/GamepadPose/angularAcceleration)Read onlyExperimental

Returns the angular acceleration of the [Gamepad](/en-US/docs/Web/API/Gamepad), in meters per second per second.

## [Examples](#examples)

TBD.

## [Specifications](#specifications)

Specification
[Gamepad Extensions# gamepadpose-interface](https://w3c.github.io/gamepad/extensions.html#gamepadpose-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebVR API](/en-US/docs/Web/API/WebVR_API)
- [Gamepad API](/en-US/docs/Web/API/Gamepad_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GamepadPose/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gamepadpose/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepadPose&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgamepadpose%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGamepadPose%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgamepadpose%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3020adac456187cf18edeb20613482fb73b38c1e%0A*+Document+last+modified%3A+2025-12-27T03%3A36%3A31.000Z%0A%0A%3C%2Fdetails%3E)
