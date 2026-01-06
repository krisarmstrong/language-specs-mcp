# XRLightProbe

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRLightProbe&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRLightProbe` interface of the [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API) contains lighting information at a given point in the user's environment. You can get an `XRLighting` object using the [XRSession.requestLightProbe()](/en-US/docs/Web/API/XRSession/requestLightProbe) method.

This object doesn't itself contain lighting values, but it is used to collect lighting states for each [XRFrame](/en-US/docs/Web/API/XRFrame). See [XRLightEstimate](/en-US/docs/Web/API/XRLightEstimate) for the estimated lighting values for an `XRLightProbe`.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[XRLightProbe.onreflectionchange](#xrlightprobe.onreflectionchange)

Event handler property for the [reflectionchange](/en-US/docs/Web/API/XRLightProbe/reflectionchange_event) event.

[XRLightProbe.probeSpace](/en-US/docs/Web/API/XRLightProbe/probeSpace)Read onlyExperimental

An [XRSpace](/en-US/docs/Web/API/XRSpace) tracking the position and orientation the lighting estimations are relative to.

## [Instance methods](#instance_methods)

None.

## [Events](#events)

[reflectionchange](/en-US/docs/Web/API/XRLightProbe/reflectionchange_event)Experimental

Fired each time the estimated reflection cube map changes. (This happens when the user moves around and the environment's lighting changes.)

## [Examples](#examples)

### [Getting an XRLightProbe object for a session](#getting_an_xrlightprobe_object_for_a_session)

Use the [XRSession.requestLightProbe()](/en-US/docs/Web/API/XRSession/requestLightProbe) method to get a light probe.

js

```
const lightProbe = await xrSession.requestLightProbe();
```

### [Getting a probe pose within an XRFrame](#getting_a_probe_pose_within_an_xrframe)

Pass the light probe's `probeSpace` to [XRFrame.getPose()](/en-US/docs/Web/API/XRFrame/getPose) to get a light probe for a pose.

js

```
const probePose = xrFrame.getPose(lightProbe.probeSpace, xrReferenceSpace);
```

### [Using the reflectionchange event](#using_the_reflectionchange_event)

Pass `XRLightProbe` to get a reflection cube map whenever the [reflectionchange](/en-US/docs/Web/API/XRLightProbe/reflectionchange_event) event fires. See also [XRWebGLBinding.getReflectionCubeMap()](/en-US/docs/Web/API/XRWebGLBinding/getReflectionCubeMap).

js

```
const glBinding = new XRWebGLBinding(xrSession, gl);
const lightProbe = await xrSession.requestLightProbe();
let glCubeMap = glBinding.getReflectionCubeMap(lightProbe);

lightProbe.addEventListener("reflectionchange", () => {
  glCubeMap = glBinding.getReflectionCubeMap(lightProbe);
});
```

## [Specifications](#specifications)

Specification
[WebXR Lighting Estimation API Level 1# xrlightprobe-interface](https://immersive-web.github.io/lighting-estimation/#xrlightprobe-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRSession.requestLightProbe()](/en-US/docs/Web/API/XRSession/requestLightProbe)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 10, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRLightProbe/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrlightprobe/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRLightProbe&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrlightprobe%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRLightProbe%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrlightprobe%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F76637f9517e4b0a57a3096a36f66b5e33a3f1051%0A*+Document+last+modified%3A+2023-05-10T11%3A15%3A43.000Z%0A%0A%3C%2Fdetails%3E)
