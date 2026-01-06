# XRHitTestResult

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRHitTestResult&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRHitTestResult` interface of the [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API) contains a single result of a hit test. You can get an array of `XRHitTestResult` objects for a frame by calling [XRFrame.getHitTestResults()](/en-US/docs/Web/API/XRFrame/getHitTestResults).

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

[XRHitTestResult.createAnchor()](/en-US/docs/Web/API/XRHitTestResult/createAnchor)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with an [XRAnchor](/en-US/docs/Web/API/XRAnchor) created from the hit test result.

[XRHitTestResult.getPose()](/en-US/docs/Web/API/XRHitTestResult/getPose)Experimental

Returns the [XRPose](/en-US/docs/Web/API/XRPose) of the hit test result relative to the given base space.

## [Examples](#examples)

### [Getting XRHitTestResult objects within the frame loop](#getting_xrhittestresult_objects_within_the_frame_loop)

In addition to showing `XRHitTestResult` within a frame loop, this example demonstrates a few things you must do before requesting this object. While setting up the session, specify `"hit-test"` as one of the `requiredFeatures`. Next, call [XRSession.requestHitTestSource()](/en-US/docs/Web/API/XRSession/requestHitTestSource) with the desired references. (Obtain this by calling [XRSession.requestReferenceSpace()](/en-US/docs/Web/API/XRSession/requestReferenceSpace).) This returns a [XRHitTestSource](/en-US/docs/Web/API/XRHitTestSource). That you will use in the frame loop to get `XRHitTestResult` objects.

js

```
const xrSession = navigator.xr.requestSession("immersive-ar", {
  requiredFeatures: ["local", "hit-test"],
});

let hitTestSource = null;

xrSession
  .requestHitTestSource({
    space: viewerSpace, // obtained from xrSession.requestReferenceSpace("viewer");
    offsetRay: new XRRay({ y: 0.5 }),
  })
  .then((viewerHitTestSource) => {
    hitTestSource = viewerHitTestSource;
  });

// frame loop
function onXRFrame(time, xrFrame) {
  let hitTestResults = xrFrame.getHitTestResults(hitTestSource);

  // do things with the hit test results
}
```

### [Getting the hit test result's pose](#getting_the_hit_test_results_pose)

Use [getPose()](/en-US/docs/Web/API/XRHitTestResult/getPose) to query the result's pose.

js

```
let hitTestResults = xrFrame.getHitTestResults(hitTestSource);

if (hitTestResults.length > 0) {
  let pose = hitTestResults[0].getPose(referenceSpace);
}
```

### [Creating an anchor from a hit test result](#creating_an_anchor_from_a_hit_test_result)

Once you find intersections on real-world surfaces using hit testing, you can create an [XRAnchor](/en-US/docs/Web/API/XRAnchor) to attach a virtual object to that location.

js

```
hitTestResult.createAnchor().then(
  (anchor) => {
    // add anchored objects to the scene
  },
  (error) => {
    console.error(`Could not create anchor: ${error}`);
  },
);
```

## [Specifications](#specifications)

Specification
[WebXR Hit Test Module# xr-hit-test-result-interface](https://immersive-web.github.io/hit-test/#xr-hit-test-result-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRTransientInputHitTestResult](/en-US/docs/Web/API/XRTransientInputHitTestResult)
- [XRPose](/en-US/docs/Web/API/XRPose)
- [XRAnchor](/en-US/docs/Web/API/XRAnchor)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 7, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRHitTestResult/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrhittestresult/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRHitTestResult&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrhittestresult%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRHitTestResult%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrhittestresult%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Facfe8c9f1f4145f77653a2bc64a9744b001358dc%0A*+Document+last+modified%3A+2023-07-07T07%3A19%3A19.000Z%0A%0A%3C%2Fdetails%3E)
