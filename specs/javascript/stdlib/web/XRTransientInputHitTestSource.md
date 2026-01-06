# XRTransientInputHitTestSource

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRTransientInputHitTestSource&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRTransientInputHitTestSource` interface of the [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API) handles transient input hit test subscriptions. You can get an `XRTransientInputHitTestSource` object by calling the [XRSession.requestHitTestSourceForTransientInput()](/en-US/docs/Web/API/XRSession/requestHitTestSourceForTransientInput).

This object doesn't itself contain transient input hit test results, but it is used to compute hit tests for each [XRFrame](/en-US/docs/Web/API/XRFrame) by calling [XRFrame.getHitTestResultsForTransientInput()](/en-US/docs/Web/API/XRFrame/getHitTestResultsForTransientInput), which returns [XRTransientInputHitTestResult](/en-US/docs/Web/API/XRTransientInputHitTestResult) objects.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

None.

## [Instance methods](#instance_methods)

[XRTransientInputHitTestSource.cancel()](/en-US/docs/Web/API/XRTransientInputHitTestSource/cancel)Experimental

Unsubscribes from the transient input hit test.

## [Examples](#examples)

### [Getting an XRTransientInputHitTestSource object for a session](#getting_an_xrtransientinputhittestsource_object_for_a_session)

Use the [XRSession.requestHitTestSourceForTransientInput()](/en-US/docs/Web/API/XRSession/requestHitTestSourceForTransientInput) method to get a transient input hit test source.

js

```
const xrSession = navigator.xr.requestSession("immersive-ar", {
  requiredFeatures: ["local", "hit-test"],
});

let transientHitTestSource = null;

xrSession
  .requestHitTestSourceForTransientInput({
    profile: "generic-touchscreen",
    offsetRay: new XRRay(),
  })
  .then((touchScreenHitTestSource) => {
    transientHitTestSource = touchScreenHitTestSource;
  });

// frame loop
function onXRFrame(time, xrFrame) {
  let hitTestResults = xrFrame.getHitTestResultsForTransientInput(
    transientHitTestSource,
  );

  // do things with the transient hit test results
}
```

### [Unsubscribe from a transient input hit test](#unsubscribe_from_a_transient_input_hit_test)

To unsubscribe from a transient input hit test source, use the [XRTransientInputHitTestSource.cancel()](/en-US/docs/Web/API/XRTransientInputHitTestSource/cancel) method. Since the object will no longer be usable, you can clean up and set the `XRTransientInputHitTestSource` object to [null](/en-US/docs/Web/JavaScript/Reference/Operators/null).

js

```
transientHitTestSource.cancel();
transientHitTestSource = null;
```

## [Specifications](#specifications)

Specification
[WebXR Hit Test Module# transient-input-hit-test-source-interface](https://immersive-web.github.io/hit-test/#transient-input-hit-test-source-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRTransientInputHitTestResult](/en-US/docs/Web/API/XRTransientInputHitTestResult)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 7, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRTransientInputHitTestSource/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrtransientinputhittestsource/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRTransientInputHitTestSource&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrtransientinputhittestsource%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRTransientInputHitTestSource%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrtransientinputhittestsource%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Facfe8c9f1f4145f77653a2bc64a9744b001358dc%0A*+Document+last+modified%3A+2023-07-07T07%3A19%3A19.000Z%0A%0A%3C%2Fdetails%3E)
