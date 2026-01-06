# XRWebGLBinding

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRWebGLBinding&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRWebGLBinding` interface is used to create layers that have a GPU backend.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[XRWebGLBinding()](/en-US/docs/Web/API/XRWebGLBinding/XRWebGLBinding)Experimental

Creates a new `XRWebGLBinding` object for the specified XR session and WebGL rendering context.

## [Instance properties](#instance_properties)

[XRWebGLBinding.nativeProjectionScaleFactor](/en-US/docs/Web/API/XRWebGLBinding/nativeProjectionScaleFactor)Read onlyExperimental

The `scaleFactor` that was passed in during the construction of the projection layer. The native buffer size is scaled by this number.

## [Instance methods](#instance_methods)

[XRWebGLBinding.createCubeLayer()](/en-US/docs/Web/API/XRWebGLBinding/createCubeLayer)Experimental

Returns an [XRCubeLayer](/en-US/docs/Web/API/XRCubeLayer) object, which is a layer that renders directly from a [cubemap](https://en.wikipedia.org/wiki/Cube_mapping), and projects it onto the inside faces of a cube.

[XRWebGLBinding.createCylinderLayer()](/en-US/docs/Web/API/XRWebGLBinding/createCylinderLayer)Experimental

Returns an [XRCylinderLayer](/en-US/docs/Web/API/XRCylinderLayer) object which is a layer that takes up a curved rectangular space in the virtual environment.

[XRWebGLBinding.createEquirectLayer()](/en-US/docs/Web/API/XRWebGLBinding/createEquirectLayer)Experimental

Returns an [XREquirectLayer](/en-US/docs/Web/API/XREquirectLayer) object which is a layer that maps [equirectangular](https://en.wikipedia.org/wiki/Equirectangular_projection) coded data onto the inside of a sphere.

[XRWebGLBinding.createProjectionLayer()](/en-US/docs/Web/API/XRWebGLBinding/createProjectionLayer)Experimental

Returns an [XRProjectionLayer](/en-US/docs/Web/API/XRProjectionLayer) object which is a layer that fills the entire view of the observer and is refreshed close to the device's native frame rate.

[XRWebGLBinding.createQuadLayer()](/en-US/docs/Web/API/XRWebGLBinding/createQuadLayer)Experimental

Returns an [XRQuadLayer](/en-US/docs/Web/API/XRQuadLayer) object which is a two-dimensional object positioned and oriented in 3D space.

[XRWebGLBinding.getDepthInformation()](/en-US/docs/Web/API/XRWebGLBinding/getDepthInformation)Experimental

Returns an [XRWebGLDepthInformation](/en-US/docs/Web/API/XRWebGLDepthInformation) object containing WebGL depth information.

[XRWebGLBinding.getReflectionCubeMap()](/en-US/docs/Web/API/XRWebGLBinding/getReflectionCubeMap)Experimental

Returns a [WebGLTexture](/en-US/docs/Web/API/WebGLTexture) object containing a reflection cube map texture.

[XRWebGLBinding.getSubImage()](/en-US/docs/Web/API/XRWebGLBinding/getSubImage)Experimental

Returns an [XRWebGLSubImage](/en-US/docs/Web/API/XRWebGLSubImage) object representing the WebGL texture to render.

[XRWebGLBinding.getViewSubImage()](/en-US/docs/Web/API/XRWebGLBinding/getViewSubImage)Experimental

Returns an [XRWebGLSubImage](/en-US/docs/Web/API/XRWebGLSubImage) object representing the WebGL texture to render for an [XRView](/en-US/docs/Web/API/XRView).

## [Specifications](#specifications)

Specification
[WebXR Layers API Level 1# XRWebGLBindingtype](https://immersive-web.github.io/layers/#XRWebGLBindingtype)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRWebGLLayer](/en-US/docs/Web/API/XRWebGLLayer)
- [WebGLRenderingContext](/en-US/docs/Web/API/WebGLRenderingContext) and [WebGL2RenderingContext](/en-US/docs/Web/API/WebGL2RenderingContext)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 18, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRWebGLBinding/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrwebglbinding/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRWebGLBinding&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrwebglbinding%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRWebGLBinding%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrwebglbinding%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff8553485fe1d9ab48b9f4816385b43bcbb388c0e%0A*+Document+last+modified%3A+2023-02-18T07%3A03%3A23.000Z%0A%0A%3C%2Fdetails%3E)
