# XRLightEstimate

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRLightEstimate&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRLightEstimate` interface of the [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API) provides the estimated lighting values for an [XRLightProbe](/en-US/docs/Web/API/XRLightProbe) at the time represented by an [XRFrame](/en-US/docs/Web/API/XRFrame).

To get an `XRLightEstimate` object, call the [XRFrame.getLightEstimate()](/en-US/docs/Web/API/XRFrame/getLightEstimate) method.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[XRLightEstimate.primaryLightDirection](/en-US/docs/Web/API/XRLightEstimate/primaryLightDirection)Read onlyExperimental

A [DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly) representing the direction to the primary light source from the `probeSpace` of an [XRLightProbe](/en-US/docs/Web/API/XRLightProbe).

[XRLightEstimate.primaryLightIntensity](/en-US/docs/Web/API/XRLightEstimate/primaryLightIntensity)Read onlyExperimental

A [DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly) (with the `x`, `y`, `z` values mapped to RGB) representing the intensity of the primary light source from the `probeSpace` of an [XRLightProbe](/en-US/docs/Web/API/XRLightProbe).

[XRLightEstimate.sphericalHarmonicsCoefficients](/en-US/docs/Web/API/XRLightEstimate/sphericalHarmonicsCoefficients)Read onlyExperimental

A [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) containing 9 spherical harmonics coefficients.

## [Instance methods](#instance_methods)

None.

## [Examples](#examples)

### [Getting an XRLightProbe object](#getting_an_xrlightprobe_object)

First, use the [XRSession.requestLightProbe()](/en-US/docs/Web/API/XRSession/requestLightProbe) method to get a light probe from a session. Then, within an [XRFrame](/en-US/docs/Web/API/XRFrame) loop, the [getLightEstimate()](/en-US/docs/Web/API/XRFrame/getLightEstimate) method will return a `XRLightEstimate` object containing the lighting values for each frame.

js

```
const lightProbe = await xrSession.requestLightProbe();

// frame loop
function onXRFrame(time, xrFrame) {
  let lightEstimate = xrFrame.getLightEstimate(lightProbe);

  // Use light estimate data to light the scene

  // Available properties
  lightEstimate.sphericalHarmonicsCoefficients;
  lightEstimate.primaryLightDirection;
  lightEstimate.primaryLightIntensity;
}
```

## [Specifications](#specifications)

Specification
[WebXR Lighting Estimation API Level 1# xrlightestimate-interface](https://immersive-web.github.io/lighting-estimation/#xrlightestimate-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRFrame.getLightEstimate()](/en-US/docs/Web/API/XRFrame/getLightEstimate)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 18, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRLightEstimate/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrlightestimate/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRLightEstimate&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrlightestimate%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRLightEstimate%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrlightestimate%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5b33acd44e7bb9c7be2efc75ba9a04b8bf8b2b2%0A*+Document+last+modified%3A+2023-02-18T09%3A00%3A03.000Z%0A%0A%3C%2Fdetails%3E)
