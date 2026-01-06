# XRJointPose

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRJointPose&level=not)

The `XRJointPose` interface is an [XRPose](/en-US/docs/Web/API/XRPose) with additional information about the size of the skeleton joint it represents.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[XRJointPose.radius](/en-US/docs/Web/API/XRJointPose/radius)Read only

The radius (distance from skin) for a joint.

## [Examples](#examples)

### [Using XRJointPose objects](#using_xrjointpose_objects)

Call [XRFrame.getJointPose()](/en-US/docs/Web/API/XRFrame/getJointPose) with an [XRJointSpace](/en-US/docs/Web/API/XRJointSpace) and an [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace) to get an `XRJointPose` object.

js

```
navigator.xr
  .requestSession({ optionalFeatures: ["hand-tracking"] })
  .then(/* … */);

function renderFrame(session, frame) {
  // …

  for (const inputSource of session.inputSources) {
    if (inputSource.hand) {
      const indexFingerTipJoint = inputSource.hand.get("index-finger-tip");
      frame.getJointPose(indexFingerTipJoint, referenceSpace); // XRJointPose
    }
  }
}
```

## [Specifications](#specifications)

Specification
[WebXR Hand Input Module - Level 1# xrjointpose-interface](https://immersive-web.github.io/webxr-hand-input/#xrjointpose-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRHand](/en-US/docs/Web/API/XRHand)
- [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace)
- [XRJointSpace](/en-US/docs/Web/API/XRJointSpace)
- [XRFrame.getJointPose()](/en-US/docs/Web/API/XRFrame/getJointPose)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 18, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRJointPose/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrjointpose/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRJointPose&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrjointpose%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRJointPose%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrjointpose%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5b33acd44e7bb9c7be2efc75ba9a04b8bf8b2b2%0A*+Document+last+modified%3A+2023-02-18T09%3A00%3A03.000Z%0A%0A%3C%2Fdetails%3E)
