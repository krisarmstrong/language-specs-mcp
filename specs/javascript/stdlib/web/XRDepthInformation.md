# XRDepthInformation

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRDepthInformation&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRDepthInformation` interface contains information about the distance from the user's device to the real-world geometry in the user's environment.

This interface is the parent of:

[XRCPUDepthInformation](/en-US/docs/Web/API/XRCPUDepthInformation)

Depth information from the CPU (returned by [XRFrame.getDepthInformation()](/en-US/docs/Web/API/XRFrame/getDepthInformation)).

[XRWebGLDepthInformation](/en-US/docs/Web/API/XRWebGLDepthInformation)

Depth information from WebGL (returned by [XRWebGLBinding.getDepthInformation()](/en-US/docs/Web/API/XRWebGLBinding/getDepthInformation)).

You will usually interact with these child interfaces. However, `XRDepthInformation` provides some useful properties that are inherited:

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[XRDepthInformation.height](/en-US/docs/Web/API/XRDepthInformation/height)Read onlyExperimental

Contains the height of the depth buffer (number of rows).

[XRDepthInformation.normDepthBufferFromNormView](/en-US/docs/Web/API/XRDepthInformation/normDepthBufferFromNormView)Read onlyExperimental

An [XRRigidTransform](/en-US/docs/Web/API/XRRigidTransform) that needs to be applied when indexing into the depth buffer. The transformation that the matrix represents changes the coordinate system from normalized view coordinates to normalized depth-buffer coordinates that can then be scaled by depth buffer's `width` and `height` to obtain the absolute depth-buffer coordinates.

[XRDepthInformation.rawValueToMeters](/en-US/docs/Web/API/XRDepthInformation/rawValueToMeters)Read onlyExperimental

Contains the scale factor by which the raw depth values must be multiplied in order to get the depths in meters.

[XRDepthInformation.width](/en-US/docs/Web/API/XRDepthInformation/width)Read onlyExperimental

Contains the width of the depth buffer (number of columns).

## [Instance methods](#instance_methods)

None.

## [Examples](#examples)

See [XRCPUDepthInformation](/en-US/docs/Web/API/XRCPUDepthInformation) and [XRWebGLDepthInformation](/en-US/docs/Web/API/XRWebGLDepthInformation) for code examples.

## [Specifications](#specifications)

Specification
[WebXR Depth Sensing Module# xrdepthinformation](https://immersive-web.github.io/depth-sensing/#xrdepthinformation)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRCPUDepthInformation](/en-US/docs/Web/API/XRCPUDepthInformation)
- [XRWebGLDepthInformation](/en-US/docs/Web/API/XRWebGLDepthInformation)
- [XRFrame.getDepthInformation()](/en-US/docs/Web/API/XRFrame/getDepthInformation)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 18, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRDepthInformation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrdepthinformation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRDepthInformation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrdepthinformation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRDepthInformation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrdepthinformation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5b33acd44e7bb9c7be2efc75ba9a04b8bf8b2b2%0A*+Document+last+modified%3A+2023-02-18T09%3A00%3A03.000Z%0A%0A%3C%2Fdetails%3E)
