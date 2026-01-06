# XRAnchor

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRAnchor&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRAnchor` interface creates anchors which keep track of the pose that is fixed relative to the real world. With anchors, you can specify poses in the world that need to be updated to correctly reflect the evolving understanding of the world, such that the poses remain aligned with the same place in the physical world. That helps to build an illusion that the placed objects are really present in the user's environment.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[XRAnchor.anchorSpace](/en-US/docs/Web/API/XRAnchor/anchorSpace)Read onlyExperimental

Returns an [XRSpace](/en-US/docs/Web/API/XRSpace) object to locate the anchor relative to other `XRSpace` objects.

## [Instance methods](#instance_methods)

[XRAnchor.delete()](/en-US/docs/Web/API/XRAnchor/delete)Experimental

Removes the anchor.

## [Examples](#examples)

### [Requesting a session with anchors enabled](#requesting_a_session_with_anchors_enabled)

js

```
navigator.xr.requestSession("immersive-ar", {
  requireFeatures: ["anchors"],
});
```

### [Adding anchors](#adding_anchors)

You can use [XRFrame.createAnchor()](/en-US/docs/Web/API/XRFrame/createAnchor) to create an anchor.

js

```
frame.createAnchor(anchorPose, referenceSpace).then(
  (anchor) => {
    // Do stuff with the anchor (assign objects that will be relative to this anchor)
  },
  (error) => {
    console.error(`Could not create anchor: ${error}`);
  },
);
```

## [Specifications](#specifications)

Specification
[WebXR Anchors Module# xr-anchor](https://immersive-web.github.io/anchors/#xr-anchor)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRAnchorSet](/en-US/docs/Web/API/XRAnchorSet)
- [XRFrame.createAnchor()](/en-US/docs/Web/API/XRFrame/createAnchor)
- [XRFrame.trackedAnchors](/en-US/docs/Web/API/XRFrame/trackedAnchors)
- [XRHitTestResult.createAnchor()](/en-US/docs/Web/API/XRHitTestResult/createAnchor)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 7, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRAnchor/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xranchor/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRAnchor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxranchor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRAnchor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxranchor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Facfe8c9f1f4145f77653a2bc64a9744b001358dc%0A*+Document+last+modified%3A+2023-07-07T07%3A19%3A19.000Z%0A%0A%3C%2Fdetails%3E)
