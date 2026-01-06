# XRInputSource

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRInputSource&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The [WebXR Device API's](/en-US/docs/Web/API/WebXR_Device_API)`XRInputSource` interface describes a single source of control input which is part of the user's WebXR-compatible virtual or augmented reality system. The device is specific to the platform being used, but provides the direction in which it is being aimed and optionally may generate events if the user triggers performs actions using the device.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Usage notes](#usage_notes)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[gamepad](/en-US/docs/Web/API/XRInputSource/gamepad)Read only

A [Gamepad](/en-US/docs/Web/API/Gamepad) object describing the state of the buttons and axes on the XR input source, if it is a gamepad or comparable device. If the device isn't a gamepad-like device, this property's value is `null`.

[gripSpace](/en-US/docs/Web/API/XRInputSource/gripSpace)Read only

An [XRSpace](/en-US/docs/Web/API/XRSpace) whose origin tracks the pose which is used to render objects which should appear as if they're held in the hand indicated by `handedness`. The orientation of this space indicates the angle at which the hand is gripping the object. Read on in the main article on [gripSpace](/en-US/docs/Web/API/XRInputSource/gripSpace) for more details on how to use this space.

[hand](/en-US/docs/Web/API/XRInputSource/hand)Read only

An [XRHand](/en-US/docs/Web/API/XRHand) object providing access to the underlying hand-tracking device.

[handedness](/en-US/docs/Web/API/XRInputSource/handedness)Read only

A string that indicates which hand the device represented by this `XRInputSource` is being used in, if any. The value will be `left`, `right`, or `none`.

[profiles](/en-US/docs/Web/API/XRInputSource/profiles)Read only

An array of strings, each specifying the name of an input profile describing the preferred visual representation and behavior of this input source.

[targetRayMode](/en-US/docs/Web/API/XRInputSource/targetRayMode)Read only

A string indicating the methodology used to produce the target ray: `gaze`, `tracked-pointer`, or `screen`.

[targetRaySpace](/en-US/docs/Web/API/XRInputSource/targetRaySpace)Read only

An [XRSpace](/en-US/docs/Web/API/XRSpace) object defining the origin of the target ray and the direction in which it extends. This space is established using the method defined by `targetRayMode`.

## [Instance methods](#instance_methods)

The `XRInputSource` interface defines no methods.

## [Usage notes](#usage_notes)

### [Actions and the target ray](#actions_and_the_target_ray)

If the device provides an indication of the direction in which it is pointed, this is done using a target ray. This is a ray extending from the position of the device outward in the direction in which it is pointed.

A target ray emitted by a hand controller.

If the device includes a trigger or other squeezable input, such as a hand gesture device that recognizes when the user squeezes their fist, that action is called a primary squeeze action. A primary squeeze action should correspond to a gripping act in reality, such as taking hold of an object or pressing a trigger on a tool or weapon. When a squeeze action begins, such as by the user pressing the trigger or tightening their grip, a [squeezestart](/en-US/docs/Web/API/XRSession/squeezestart_event) event is sent to the `XRSession`. Once the action is completed and the user has released the trigger or the grip, a [squeeze](/en-US/docs/Web/API/XRSession/squeeze_event) event is sent. This is followed by a [squeezeend](/en-US/docs/Web/API/XRSession/squeezeend_event), which is also sent if the action is aborted rather than completed.

If the device has a button or other pressable input control, it is a primary input source, and this button is a primary action. A primary action may occur when the user presses a button, clicks on a touchpad or the top button of a thumb stick, or uses a hand gesture or spoken command that invokes the button-like action. When a primary action begins, a [selectstart](/en-US/docs/Web/API/XRSession/selectstart_event) event is sent to the [XRSession](/en-US/docs/Web/API/XRSession). When the action has completed (such as when the user releases the button), a [select](/en-US/docs/Web/API/XRSession/select_event) event is sent. Finally, once that is done—or if the user aborts the action—a [selectend](/en-US/docs/Web/API/XRSession/selectend_event) event is sent to the session object.

An action may be aborted either by the user in some device-specific fashion or if the input device is disconnected before the action is completed.

### [Local coordinate system](#local_coordinate_system)

Each input source has its own local coordinate system, which is described by the [gripSpace](/en-US/docs/Web/API/XRInputSource/gripSpace) property, which is an [XRSpace](/en-US/docs/Web/API/XRSpace) used to map the input's coordinate system into the world coordinate system. The grip space's coordinate system can then be used to render objects so they appear to be held in the user's hand.

For more details on the input source's coordinate system, see the article that covers the [gripSpace](/en-US/docs/Web/API/XRInputSource/gripSpace) property in detail.

## [Specifications](#specifications)

Specification
[WebXR Device API# xrinputsource-interface](https://immersive-web.github.io/webxr/#xrinputsource-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API)
- [Inputs and input sources](/en-US/docs/Web/API/WebXR_Device_API/Inputs)
- [XRInputSourceArray](/en-US/docs/Web/API/XRInputSourceArray)
- [XRSpace](/en-US/docs/Web/API/XRSpace)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 27, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/XRInputSource/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrinputsource/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRInputSource&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrinputsource%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRInputSource%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrinputsource%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0f1aecaed48d75652c6dd97f30c7febd07e5cde%0A*+Document+last+modified%3A+2024-08-27T21%3A29%3A22.000Z%0A%0A%3C%2Fdetails%3E)
