# XRWebGLDepthInformation

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRWebGLDepthInformation&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRWebGLDepthInformation` interface contains depth information from the GPU/WebGL (returned by [XRWebGLBinding.getDepthInformation()](/en-US/docs/Web/API/XRWebGLBinding/getDepthInformation)).

This interface inherits properties from its parent, [XRDepthInformation](/en-US/docs/Web/API/XRDepthInformation).

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[XRDepthInformation.height](/en-US/docs/Web/API/XRDepthInformation/height)Read only

Contains the height of the depth buffer (number of rows).

[XRDepthInformation.normDepthBufferFromNormView](/en-US/docs/Web/API/XRDepthInformation/normDepthBufferFromNormView)Read only

An [XRRigidTransform](/en-US/docs/Web/API/XRRigidTransform) that needs to be applied when indexing into the depth buffer. The transformation that the matrix represents changes the coordinate system from normalized view coordinates to normalized depth buffer coordinates that can then be scaled by depth buffer's `width` and `height` to obtain the absolute depth buffer coordinates.

[XRDepthInformation.rawValueToMeters](/en-US/docs/Web/API/XRDepthInformation/rawValueToMeters)Read only

Contains the scale factor by which the raw depth values must be multiplied in order to get the depths in meters.

[XRWebGLDepthInformation.texture](/en-US/docs/Web/API/XRWebGLDepthInformation/texture)Read onlyExperimental

A [WebGLTexture](/en-US/docs/Web/API/WebGLTexture) containing depth buffer information as an opaque texture.

[XRDepthInformation.width](/en-US/docs/Web/API/XRDepthInformation/width)Read only

Contains the width of the depth buffer (number of columns).

## [Specifications](#specifications)

Specification
[WebXR Depth Sensing Module# xrwebgldepthinformation](https://immersive-web.github.io/depth-sensing/#xrwebgldepthinformation)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRDepthInformation](/en-US/docs/Web/API/XRDepthInformation)
- [XRCPUDepthInformation](/en-US/docs/Web/API/XRCPUDepthInformation)
- [XRWebGLBinding.getDepthInformation()](/en-US/docs/Web/API/XRWebGLBinding/getDepthInformation)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 11, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/XRWebGLDepthInformation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrwebgldepthinformation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRWebGLDepthInformation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrwebgldepthinformation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRWebGLDepthInformation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrwebgldepthinformation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd666d5ed812b56cbc9c6cba853494976da1f1dd2%0A*+Document+last+modified%3A+2025-03-11T00%3A20%3A46.000Z%0A%0A%3C%2Fdetails%3E)
