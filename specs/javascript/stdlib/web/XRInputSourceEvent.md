# XRInputSourceEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRInputSourceEvent&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API)'s `XRInputSourceEvent` interface describes an event which has occurred on a WebXR user input device such as a hand controller, gaze tracking system, or motion tracking system. More specifically, they represent a change in the state of an [XRInputSource](/en-US/docs/Web/API/XRInputSource).

To learn more about handling inputs in a WebXR project, see the article [Inputs and input sources](/en-US/docs/Web/API/WebXR_Device_API/Inputs).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Event types](#event_types)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[XRInputSourceEvent()](/en-US/docs/Web/API/XRInputSourceEvent/XRInputSourceEvent)

Creates and returns a new `XRInputSourceEvent` object whose properties match those provided in the `eventInitDict` dictionary provided.

## [Instance properties](#instance_properties)

[frame](/en-US/docs/Web/API/XRInputSourceEvent/frame)Read only

An [XRFrame](/en-US/docs/Web/API/XRFrame) object providing the needed information about the event frame during which the event occurred. This frame may have been rendered in the past rather than being a current frame. Because this is an event frame, not an animation frame, you cannot call the [XRFrame](/en-US/docs/Web/API/XRFrame) method [getViewerPose()](/en-US/docs/Web/API/XRFrame/getViewerPose) on it; instead, use [getPose()](/en-US/docs/Web/API/XRFrame/getPose).

[inputSource](/en-US/docs/Web/API/XRInputSourceEvent/inputSource)Read only

An [XRInputSource](/en-US/docs/Web/API/XRInputSource) object indicating which input source generated the input event.

## [Instance methods](#instance_methods)

The `XRInputSourceEvent` interface doesn't define any methods; however, several methods are inherited from the parent interface, [Event](/en-US/docs/Web/API/Event).

## [Event types](#event_types)

[select](/en-US/docs/Web/API/XRSession/select_event)

Sent to an [XRSession](/en-US/docs/Web/API/XRSession) when the sending input source has fully completed a [primary action](/en-US/docs/Web/API/WebXR_Device_API/Inputs#primary_action).

[selectend](/en-US/docs/Web/API/XRSession/selectend_event)

Sent to an [XRSession](/en-US/docs/Web/API/XRSession) when an ongoing [primary action](/en-US/docs/Web/API/WebXR_Device_API/Inputs#primary_action) ends, or when an input source with an ongoing primary action has been disconnected from the system.

[selectstart](/en-US/docs/Web/API/XRSession/selectstart_event)

Sent to an [XRSession](/en-US/docs/Web/API/XRSession) when an input source begins its [primary action](/en-US/docs/Web/API/WebXR_Device_API/Inputs#primary_action), indicating that the user has begun a command-like input, such as pressing a trigger or button, issuing a spoken command, tapping on a touchpad, or the like.

[squeeze](/en-US/docs/Web/API/XRSession/squeeze_event)

Sent to an [XRSession](/en-US/docs/Web/API/XRSession) when the sending input source has fully completed a [primary squeeze action](/en-US/docs/Web/API/WebXR_Device_API/Inputs#primary_squeeze_action).

[squeezeend](/en-US/docs/Web/API/XRSession/squeezeend_event)

Sent to an [XRSession](/en-US/docs/Web/API/XRSession) when an ongoing [primary squeeze action](/en-US/docs/Web/API/WebXR_Device_API/Inputs#primary_squeeze_action) ends or when an input source with an ongoing primary squeeze action is disconnected.

[squeezestart](/en-US/docs/Web/API/XRSession/squeezestart_event)

Sent to an [XRSession](/en-US/docs/Web/API/XRSession) when an input source begins its [primary squeeze action](/en-US/docs/Web/API/WebXR_Device_API/Inputs#primary_squeeze_action), indicating that the user has begun to grab, squeeze, or grip the controller.

## [Examples](#examples)

The code below sets up handlers for primary action events in order to determine when the user clicks on (shoots at/pokes at/whatever) objects in the scene.

js

```
xrSession.addEventListener("select", (event) => {
  let targetRayPose = event.frame.getPose(
    event.inputSource.targetRaySpace,
    myRefSpace,
  );

  if (targetRayPose) {
    let hit = myHitTest(targetRayPose.transform);
    if (hit) {
      /* handle the hit */
    }
  }
});
```

## [Specifications](#specifications)

Specification
[WebXR Device API# xrinputsourceevent-interface](https://immersive-web.github.io/webxr/#xrinputsourceevent-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 17, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/XRInputSourceEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrinputsourceevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRInputSourceEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrinputsourceevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRInputSourceEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrinputsourceevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6c592023efa1f762eaa1eb1f36241750626be51c%0A*+Document+last+modified%3A+2024-07-17T23%3A29%3A22.000Z%0A%0A%3C%2Fdetails%3E)
