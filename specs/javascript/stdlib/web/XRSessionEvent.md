# XRSessionEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRSessionEvent&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API)'s `XRSessionEvent` interface describes an event which indicates the change of the state of an [XRSession](/en-US/docs/Web/API/XRSession). These events occur, for example, when the session ends or the visibility of its context changes.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Session event types](#session_event_types)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[XRSessionEvent()](/en-US/docs/Web/API/XRSessionEvent/XRSessionEvent)

Creates and returns a new `XRSessionEvent` object.

## [Instance properties](#instance_properties)

In addition to properties inherited from its parent interface, [Event](/en-US/docs/Web/API/Event), `XRSessionEvent` provides the following:

[session](/en-US/docs/Web/API/XRSessionEvent/session)Read only

The [XRSession](/en-US/docs/Web/API/XRSession) to which the event refers.

## [Instance methods](#instance_methods)

While `XRSessionEvent` defines no methods, it inherits methods from its parent interface, [Event](/en-US/docs/Web/API/Event).

## [Session event types](#session_event_types)

The following events are represented using the `XRSessionEvent` interface, and are permitted values for its `type` property.

[end](/en-US/docs/Web/API/XRSession/end_event)

Fired at the session when it has ended, after being terminated by the application or the [user agent](/en-US/docs/Glossary/User_agent).

[visibilitychange](/en-US/docs/Web/API/XRSession/visibilitychange_event)

Fired at the session whenever its visibility state changes.

## [Examples](#examples)

This example creates a listener that watches for the visibility state of the session to change. It reacts by calling a function `mySessionVisible()` with a Boolean indicating whether or not the session is visible; this function might, for instance, spin up or reconfigure a worker that handles rendering the scene.

js

```
xrSession.addEventListener("visibilitychange", (e) => {
  switch (e.session.visibilityState) {
    case "visible":
    case "visible-blurred":
      mySessionVisible(true);
      break;
    case "hidden":
      mySessionVisible(false);
      break;
  }
});
```

## [Specifications](#specifications)

Specification
[WebXR Device API# xrsessionevent-interface](https://immersive-web.github.io/webxr/#xrsessionevent-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 28, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/XRSessionEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrsessionevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRSessionEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrsessionevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRSessionEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrsessionevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9a4005caa5cc13f5174e3b8981eeec5631ed83d1%0A*+Document+last+modified%3A+2024-10-28T12%3A46%3A03.000Z%0A%0A%3C%2Fdetails%3E)
