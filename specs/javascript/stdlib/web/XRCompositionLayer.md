# XRCompositionLayer

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRCompositionLayer&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRCompositionLayer` interface of the [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API) is a base class that defines a set of common properties and behaviors for WebXR layer types. It is not constructable on its own.

Several layer types inherit from `XRCompositionLayer`:

- [XREquirectLayer](/en-US/docs/Web/API/XREquirectLayer)
- [XRCubeLayer](/en-US/docs/Web/API/XRCubeLayer)
- [XRCylinderLayer](/en-US/docs/Web/API/XRCylinderLayer)
- [XRProjectionLayer](/en-US/docs/Web/API/XRProjectionLayer)
- [XRQuadLayer](/en-US/docs/Web/API/XRQuadLayer)

`XRCompositionLayer` itself inherits from the general [XRLayer](/en-US/docs/Web/API/XRLayer) class (which inherits from [EventTarget](/en-US/docs/Web/API/EventTarget)).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[XRCompositionLayer.blendTextureSourceAlpha](/en-US/docs/Web/API/XRCompositionLayer/blendTextureSourceAlpha)Experimental

A boolean enabling the layer's texture alpha channel.

[XRCompositionLayer.layout](/en-US/docs/Web/API/XRCompositionLayer/layout)Read onlyExperimental

The layout type of the layer.

[XRCompositionLayer.mipLevels](/en-US/docs/Web/API/XRCompositionLayer/mipLevels)Read onlyExperimental

The number of mip levels in the color and texture data for the layer.

[XRCompositionLayer.needsRedraw](/en-US/docs/Web/API/XRCompositionLayer/needsRedraw)Read onlyExperimental

A boolean signaling that the layer should be re-rendered in the next frame.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[XRCompositionLayer.destroy()](/en-US/docs/Web/API/XRCompositionLayer/destroy)Experimental

Deletes the underlying layer attachments.

## [Specifications](#specifications)

Specification
[WebXR Layers API Level 1# xrcompositionlayertype](https://immersive-web.github.io/layers/#xrcompositionlayertype)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRLayer](/en-US/docs/Web/API/XRLayer)
- [EventTarget](/en-US/docs/Web/API/EventTarget)
- [XREquirectLayer](/en-US/docs/Web/API/XREquirectLayer)
- [XRCubeLayer](/en-US/docs/Web/API/XRCubeLayer)
- [XRCylinderLayer](/en-US/docs/Web/API/XRCylinderLayer)
- [XRProjectionLayer](/en-US/docs/Web/API/XRProjectionLayer)
- [XRQuadLayer](/en-US/docs/Web/API/XRQuadLayer)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 18, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRCompositionLayer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrcompositionlayer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRCompositionLayer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrcompositionlayer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRCompositionLayer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrcompositionlayer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F867d4e1e8a11aed4a93b65d5c7768b225b7fbd7e%0A*+Document+last+modified%3A+2023-04-18T13%3A15%3A46.000Z%0A%0A%3C%2Fdetails%3E)
