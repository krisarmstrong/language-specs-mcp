# XRSystem

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRSystem&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API) interface `XRSystem` provides methods which let you get access to an [XRSession](/en-US/docs/Web/API/XRSession) object representing a WebXR session. With that `XRSession` in hand, you can use it to interact with the Augmented Reality (AR) or Virtual Reality (VR) device.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Usage notes](#usage_notes)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

While `XRSystem` directly offers no properties, it does inherit properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Instance methods](#instance_methods)

In addition to inheriting methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget), the `XRSystem` interface includes the following methods:

[isSessionSupported()](/en-US/docs/Web/API/XRSystem/isSessionSupported)Experimental

Returns a promise which resolves to `true` if the browser supports the given session mode. Resolves to `false` if the specified mode isn't supported.

[requestSession()](/en-US/docs/Web/API/XRSystem/requestSession)Experimental

Returns a promise that resolves to a new [XRSession](/en-US/docs/Web/API/XRSession) with the specified session mode.

## [Events](#events)

[devicechange](/en-US/docs/Web/API/XRSystem/devicechange_event)Experimental

Sent when the set of available XR devices has changed. Also available using the `ondevicechange` event handler.

## [Usage notes](#usage_notes)

This interface was previously known as `XR` in earlier versions of the specification; if you see references to `XR` in code or documentation, replace that with `XRSystem`.

## [Examples](#examples)

The following example shows how to use both [isSessionSupported()](/en-US/docs/Web/API/XRSystem/isSessionSupported) and [requestSession()](/en-US/docs/Web/API/XRSystem/requestSession).

js

```
if (navigator.xr) {
  immersiveButton.addEventListener("click", onButtonClicked);
  navigator.xr.isSessionSupported("immersive-vr").then((isSupported) => {
    immersiveButton.disabled = !isSupported;
  });
}

function onButtonClicked() {
  if (!xrSession) {
    navigator.xr.requestSession("immersive-vr").then((session) => {
      // onSessionStarted() not shown for reasons of brevity and clarity.
      onSessionStarted(session);
    });
  } else {
    // Shut down the already running XRSession
    xrSession.end().then(() => {
      // Since there are cases where the end event is not sent, call the handler here as well.
      onSessionEnded();
    });
  }
}
```

This code starts by checking to see if WebXR is available by looking for the [navigator.xr](/en-US/docs/Web/API/Navigator/xr) property. If it's found, we know WebXR is present, so we proceed by establishing a handler for the button which the user can click to toggle immersive VR mode on and off.

However, we don't yet know if the desired immersive mode is available. To determine this, we call `isSessionSupported()`, passing it the desired session option before enabling the button, `immersiveButton`, which the user can then use to switch to immersive mode only if immersive VR mode is available. If immersive VR isn't available, the button is disabled to prevent its use.

The `onButtonClicked()` function checks to see if there's already a session running. If there isn't, we use `requestSession()` to start one and, once the returned promise resolves, we call a function `onSessionStarted()` to set up our session for rendering and so forth.

If, on the other hand, there is already an ongoing XR session, we instead call [end()](/en-US/docs/Web/API/XRSession/end) to end the current session. When the current session ends, the [end](/en-US/docs/Web/API/XRSession/end_event) event is sent, so set `xrSession` to `null` in its handler to record the fact that we no longer have an ongoing session. That way, if the user clicks the button again, a new session will start.

## [Specifications](#specifications)

Specification
[WebXR Device API# xrsystem-interface](https://immersive-web.github.io/webxr/#xrsystem-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 10, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRSystem/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrsystem/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRSystem&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrsystem%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRSystem%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrsystem%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F76637f9517e4b0a57a3096a36f66b5e33a3f1051%0A*+Document+last+modified%3A+2023-05-10T11%3A15%3A43.000Z%0A%0A%3C%2Fdetails%3E)
