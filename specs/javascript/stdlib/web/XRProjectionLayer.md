# XRProjectionLayer

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRProjectionLayer&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRProjectionLayer` interface of the [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API) is a layer that fills the entire view of the observer and is refreshed close to the device's native frame rate.

`XRProjectionLayer` is supported by all [XRSession](/en-US/docs/Web/API/XRSession) objects (no `layers` feature descriptor is needed).

To create a new `XRProjectionLayer`, call [XRWebGLBinding.createProjectionLayer()](/en-US/docs/Web/API/XRWebGLBinding/createProjectionLayer). To present layers to the XR device, add them to the `layers` render state using [XRSession.updateRenderState()](/en-US/docs/Web/API/XRSession/updateRenderState).

`XRProjectionLayer` objects don't have an associated [XRSpace](/en-US/docs/Web/API/XRSpace), because they render to the full frame.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [XRCompositionLayer](/en-US/docs/Web/API/XRCompositionLayer) and [EventTarget](/en-US/docs/Web/API/EventTarget).

[XRProjectionLayer.fixedFoveation](/en-US/docs/Web/API/XRProjectionLayer/fixedFoveation)Experimental

A number indicating the amount of foveation used by the XR compositor for the layer. Fixed Foveated Rendering (FFR) renders the edges of the eye textures at a lower resolution than the center and reduces the GPU load.

[XRProjectionLayer.ignoreDepthValues](/en-US/docs/Web/API/XRProjectionLayer/ignoreDepthValues)Read onlyExperimental

A boolean indicating that the XR compositor is not making use of depth buffer values when rendering the layer.

[XRProjectionLayer.textureArrayLength](/en-US/docs/Web/API/XRProjectionLayer/textureArrayLength)Read onlyExperimental

The layer's layer count for array textures when using `texture-array` as the `textureType`.

[XRProjectionLayer.textureHeight](/en-US/docs/Web/API/XRProjectionLayer/textureHeight)Read onlyExperimental

The height in pixels of the color textures of this layer.

[XRProjectionLayer.textureWidth](/en-US/docs/Web/API/XRProjectionLayer/textureWidth)Read onlyExperimental

The width in pixels of the color textures of this layer.

## [Instance methods](#instance_methods)

Inherits methods from its parents, [XRCompositionLayer](/en-US/docs/Web/API/XRCompositionLayer) and [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Specifications](#specifications)

Specification
[WebXR Layers API Level 1# xrprojectionlayertype](https://immersive-web.github.io/layers/#xrprojectionlayertype)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRLayer](/en-US/docs/Web/API/XRLayer)
- [EventTarget](/en-US/docs/Web/API/EventTarget)
- [XRCompositionLayer](/en-US/docs/Web/API/XRCompositionLayer)
- [XREquirectLayer](/en-US/docs/Web/API/XREquirectLayer)
- [XRCubeLayer](/en-US/docs/Web/API/XRCubeLayer)
- [XRCylinderLayer](/en-US/docs/Web/API/XRCylinderLayer)
- [XRQuadLayer](/en-US/docs/Web/API/XRQuadLayer)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 22, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRProjectionLayer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrprojectionlayer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRProjectionLayer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrprojectionlayer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRProjectionLayer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrprojectionlayer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9f24be2de6158053df593b9b466f5da96e31f928%0A*+Document+last+modified%3A+2023-11-22T06%3A41%3A52.000Z%0A%0A%3C%2Fdetails%3E)
