# XRRay

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRRay&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRRay` interface of the [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API) is a geometric ray described by an origin point and a direction vector.

`XRRay` objects can be passed to [XRSession.requestHitTestSource()](/en-US/docs/Web/API/XRSession/requestHitTestSource) or [XRSession.requestHitTestSourceForTransientInput()](/en-US/docs/Web/API/XRSession/requestHitTestSourceForTransientInput) to perform hit testing.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[XRRay()](/en-US/docs/Web/API/XRRay/XRRay)Experimental

Creates a new `XRRay` object.

## [Instance properties](#instance_properties)

[XRRay.direction](/en-US/docs/Web/API/XRRay/direction)Read onlyExperimental

A [DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly) representing the ray's 3-dimensional directional vector.

[XRRay.matrix](/en-US/docs/Web/API/XRRay/matrix)Read onlyExperimental

A transform that can be used to position objects along the `XRRay`. This is a 4 by 4 matrix given as a 16 element [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) in column major order.

[XRRay.origin](/en-US/docs/Web/API/XRRay/origin)Read onlyExperimental

A [DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly) representing the 3-dimensional point in space that the ray originates from, in meters.

## [Instance methods](#instance_methods)

None.

## [Examples](#examples)

### [Using XRRay to request a hit test source](#using_xrray_to_request_a_hit_test_source)

The [XRSession.requestHitTestSource()](/en-US/docs/Web/API/XRSession/requestHitTestSource) method takes an `XRRay` object for its `offsetRay` option. In this example, the hit test source is positioned slightly above the viewer as the application has some UI elements at the bottom while wanting to maintain the perception of a centered cursor.

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
```

## [Specifications](#specifications)

Specification
[WebXR Hit Test Module# xrray-interface](https://immersive-web.github.io/hit-test/#xrray-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRSession.requestHitTestSource()](/en-US/docs/Web/API/XRSession/requestHitTestSource)
- [XRHitTestResult](/en-US/docs/Web/API/XRHitTestResult)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 10, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRRay/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrray/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRRay&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrray%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRRay%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrray%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F76637f9517e4b0a57a3096a36f66b5e33a3f1051%0A*+Document+last+modified%3A+2023-05-10T11%3A15%3A43.000Z%0A%0A%3C%2Fdetails%3E)
