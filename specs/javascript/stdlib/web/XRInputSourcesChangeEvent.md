# XRInputSourcesChangeEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRInputSourcesChangeEvent&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The WebXR Device API interface `XRInputSourcesChangeEvent` is used to represent the [inputsourceschange](/en-US/docs/Web/API/XRSession/inputsourceschange_event) event sent to an [XRSession](/en-US/docs/Web/API/XRSession) when the set of available WebXR input controllers changes.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Event types](#event_types)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[XRInputSourcesChangeEvent()](/en-US/docs/Web/API/XRInputSourcesChangeEvent/XRInputSourcesChangeEvent)

Creates and returns a new `XRInputSourcesChangeEvent` object. The specified type must be `inputsourceschange`, which is the only event that uses this interface.

## [Instance properties](#instance_properties)

[added](/en-US/docs/Web/API/XRInputSourcesChangeEvent/added)Read only

An array of zero or more [XRInputSource](/en-US/docs/Web/API/XRInputSource) objects, each representing an input device which has been newly connected or enabled for use.

[removed](/en-US/docs/Web/API/XRInputSourcesChangeEvent/removed)Read only

An array of zero or more [XRInputSource](/en-US/docs/Web/API/XRInputSource) objects representing the input devices newly connected or enabled for use.

[session](/en-US/docs/Web/API/XRInputSourcesChangeEvent/session)Read only

The [XRSession](/en-US/docs/Web/API/XRSession) to which this input source change event is being directed.

## [Instance methods](#instance_methods)

While `XRInputSourcesChangeEvent` defines no methods of its own, it inherits methods from its parent interface, [Event](/en-US/docs/Web/API/Event).

## [Event types](#event_types)

[inputsourceschange](/en-US/docs/Web/API/XRSession/inputsourceschange_event)

Delivered to the [XRSession](/en-US/docs/Web/API/XRSession) when the set of input devices available to it changes.

## [Examples](#examples)

The following example shows how to set up an event handler which uses `inputsourceschange` events to detect newly-available pointing devices and to load their models in preparation to display them in the next animation frame.

js

```
xrSession.addEventListener("inputsourceschange", onInputSourcesChange);

function onInputSourcesChange(event) {
  for (const input of event.added) {
    if (input.targetRayMode === "tracked-pointer") {
      loadControllerMesh(input);
    }
  }
}
```

You can also add a handler for `inputsourceschange` events by setting the `oninputsourceschange` event handler:

js

```
xrSession.oninputsourceschange = onInputSourcesChange;
```

## [Specifications](#specifications)

Specification
[WebXR Device API# xrinputsourceschangeevent-interface](https://immersive-web.github.io/webxr/#xrinputsourceschangeevent-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 17, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/XRInputSourcesChangeEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrinputsourceschangeevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRInputSourcesChangeEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrinputsourceschangeevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRInputSourcesChangeEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrinputsourceschangeevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6c592023efa1f762eaa1eb1f36241750626be51c%0A*+Document+last+modified%3A+2024-07-17T23%3A29%3A22.000Z%0A%0A%3C%2Fdetails%3E)
