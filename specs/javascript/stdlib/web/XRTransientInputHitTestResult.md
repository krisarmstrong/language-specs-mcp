# XRTransientInputHitTestResult

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRTransientInputHitTestResult&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRTransientInputHitTestResult` interface of the [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API) contains an array of results of a hit test for transient input, grouped by input source.

You can get an array of `XRHitTestResult` objects for a frame by calling [XRFrame.getHitTestResultsForTransientInput()](/en-US/docs/Web/API/XRFrame/getHitTestResultsForTransientInput).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[XRTransientInputHitTestResult.inputSource](/en-US/docs/Web/API/XRTransientInputHitTestResult/inputSource)Read onlyExperimental

Represents the [XRInputSource](/en-US/docs/Web/API/XRInputSource) that was used to compute the `results` array.

[XRTransientInputHitTestResult.results](/en-US/docs/Web/API/XRTransientInputHitTestResult/results)Read onlyExperimental

Represents an array of [XRHitTestResult](/en-US/docs/Web/API/XRHitTestResult) objects containing the hit test results for the input source, ordered by the distance along the ray used to perform the hit test, with the closest result at position 0.

## [Instance methods](#instance_methods)

None.

## [Examples](#examples)

### [Accessing transient input hit test results](#accessing_transient_input_hit_test_results)

Two arrays are used to access transient input hit test results. First, you get an array of `XRTransientInputHitTestResult` objects by calling [XRFrame.getHitTestResultsForTransientInput()](/en-US/docs/Web/API/XRFrame/getHitTestResultsForTransientInput). Second, to get to the actual [XRHitTestResult](/en-US/docs/Web/API/XRHitTestResult) objects for an input source, you dereference the `results` property on one of the `XRTransientInputHitTestResult` objects.

js

```
// frame loop
function onXRFrame(time, xrFrame) {
  let hitTestResults = xrFrame.getHitTestResultsForTransientInput(
    transientHitTestSource,
  );

  hitTestResults.forEach((resultsPerInputSource) => {
    resultsPerInputSource.results.forEach((hitTest) => {
      // do something with the hit test
      hitTest.getPose(referenceSpace);
    });
  });
}
```

### [Filtering input sources](#filtering_input_sources)

The [inputSource](/en-US/docs/Web/API/XRTransientInputHitTestResult/inputSource) property allows you to filter hit test results by input source.

js

```
// frame loop
function onXRFrame(time, xrFrame) {
  let hitTestResults = xrFrame.getHitTestResultsForTransientInput(
    transientHitTestSource,
  );

  hitTestResults.forEach((resultsPerInputSource) => {
    if (resultsPerInputSource.inputSource === myPreferredInputSource) {
      // act on hit test results from the preferred input source
    }
  });
}
```

## [Specifications](#specifications)

Specification
[WebXR Hit Test Module# xr-transient-input-hit-test-result-interface](https://immersive-web.github.io/hit-test/#xr-transient-input-hit-test-result-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRHitTestResult](/en-US/docs/Web/API/XRHitTestResult)
- [XRInputSource](/en-US/docs/Web/API/XRInputSource)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 7, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRTransientInputHitTestResult/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrtransientinputhittestresult/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRTransientInputHitTestResult&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrtransientinputhittestresult%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRTransientInputHitTestResult%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrtransientinputhittestresult%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Facfe8c9f1f4145f77653a2bc64a9744b001358dc%0A*+Document+last+modified%3A+2023-07-07T07%3A19%3A19.000Z%0A%0A%3C%2Fdetails%3E)
