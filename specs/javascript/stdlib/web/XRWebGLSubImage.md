# XRWebGLSubImage

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRWebGLSubImage&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRWebGLSubImage` interface is used during rendering of WebGL layers.

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [XRSubImage](/en-US/docs/Web/API/XRSubImage).

[XRWebGLSubImage.colorTexture](/en-US/docs/Web/API/XRWebGLSubImage/colorTexture)Read onlyExperimental

A color [WebGLTexture](/en-US/docs/Web/API/WebGLTexture) object for the [XRCompositionLayer](/en-US/docs/Web/API/XRCompositionLayer) to render.

[XRWebGLSubImage.depthStencilTexture](/en-US/docs/Web/API/XRWebGLSubImage/depthStencilTexture)Read onlyExperimental

A depth/stencil [WebGLTexture](/en-US/docs/Web/API/WebGLTexture) object for the [XRCompositionLayer](/en-US/docs/Web/API/XRCompositionLayer) to render.

[XRWebGLSubImage.imageIndex](/en-US/docs/Web/API/XRWebGLSubImage/imageIndex)Read onlyExperimental

A number representing the offset into the texture array if the layer was requested with `texture-array`; [null](/en-US/docs/Web/JavaScript/Reference/Operators/null) otherwise.

[XRWebGLSubImage.colorTextureWidth](/en-US/docs/Web/API/XRWebGLSubImage/colorTextureWidth)Read onlyExperimental

A number representing the width in pixels of the GL attachment.

[XRWebGLSubImage.colorTextureHeight](/en-US/docs/Web/API/XRWebGLSubImage/colorTextureHeight)Read onlyExperimental

A number representing the height in pixels of the GL attachment.

## [Specifications](#specifications)

Specification
[WebXR Layers API Level 1# xrwebglsubimagetype](https://immersive-web.github.io/layers/#xrwebglsubimagetype)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRLayer](/en-US/docs/Web/API/XRLayer)
- [XRWebGLBinding.getSubImage()](/en-US/docs/Web/API/XRWebGLBinding/getSubImage)
- [XRWebGLBinding.getViewSubImage()](/en-US/docs/Web/API/XRWebGLBinding/getViewSubImage)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 18, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRWebGLSubImage/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrwebglsubimage/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRWebGLSubImage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrwebglsubimage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRWebGLSubImage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrwebglsubimage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff8553485fe1d9ab48b9f4816385b43bcbb388c0e%0A*+Document+last+modified%3A+2023-02-18T07%3A03%3A23.000Z%0A%0A%3C%2Fdetails%3E)
