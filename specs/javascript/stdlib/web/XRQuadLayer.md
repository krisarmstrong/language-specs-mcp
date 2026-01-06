# XRQuadLayer

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRQuadLayer&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRQuadLayer` interface of the [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API) is a layer that takes up a flat rectangular space in the virtual environment. An `XRQuadLayer` has no thickness. It is a two-dimensional object positioned and oriented in 3D space. The position of a quad refers to the center of the quad. Only the front of the layer is visible.

`XRQuadLayer` requires the `layers` feature to be enabled for the [XRSession](/en-US/docs/Web/API/XRSession). You can request it in [XRSystem.requestSession()](/en-US/docs/Web/API/XRSystem/requestSession).

To create a new `XRQuadLayer`, call either:

- [XRWebGLBinding.createQuadLayer()](/en-US/docs/Web/API/XRWebGLBinding/createQuadLayer) for a WebGL opaque texture quad layer, or
- [XRMediaBinding.createQuadLayer()](/en-US/docs/Web/API/XRMediaBinding/createQuadLayer) for an HTML [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) playback quad layer.

To present layers to the XR device, add them to the `layers` render state using [XRSession.updateRenderState()](/en-US/docs/Web/API/XRSession/updateRenderState).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [XRCompositionLayer](/en-US/docs/Web/API/XRCompositionLayer).

[XRQuadLayer.height](/en-US/docs/Web/API/XRQuadLayer/height)Experimental

Represents the height of the layer in meters.

[XRQuadLayer.space](/en-US/docs/Web/API/XRQuadLayer/space)Experimental

An [XRSpace](/en-US/docs/Web/API/XRSpace) representing the layer's spatial relationship with the user's physical environment.

[XRQuadLayer.transform](/en-US/docs/Web/API/XRQuadLayer/transform)Experimental

An [XRRigidTransform](/en-US/docs/Web/API/XRRigidTransform) representing the offset and orientation relative to `space`.

[XRQuadLayer.width](/en-US/docs/Web/API/XRQuadLayer/width)Experimental

Represents the width of the layer in meters.

## [Instance methods](#instance_methods)

Inherits methods from its parents, [XRCompositionLayer](/en-US/docs/Web/API/XRCompositionLayer) and [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Events](#events)

[redraw](/en-US/docs/Web/API/XRQuadLayer/redraw_event)Experimental

Sent to the `XRQuadLayer` object when the underlying resources of the layer are lost or when the XR Compositor can no longer reproject the layer. If this event is sent, authors should redraw the content of the layer in the next XR animation frame.

## [Specifications](#specifications)

Specification
[WebXR Layers API Level 1# xrquadlayertype](https://immersive-web.github.io/layers/#xrquadlayertype)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRLayer](/en-US/docs/Web/API/XRLayer)
- [EventTarget](/en-US/docs/Web/API/EventTarget)
- [XRCompositionLayer](/en-US/docs/Web/API/XRCompositionLayer)
- [XREquirectLayer](/en-US/docs/Web/API/XREquirectLayer)
- [XRCubeLayer](/en-US/docs/Web/API/XRCubeLayer)
- [XRCylinderLayer](/en-US/docs/Web/API/XRCylinderLayer)
- [XRProjectionLayer](/en-US/docs/Web/API/XRProjectionLayer)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 18, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRQuadLayer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrquadlayer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRQuadLayer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrquadlayer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRQuadLayer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrquadlayer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5b33acd44e7bb9c7be2efc75ba9a04b8bf8b2b2%0A*+Document+last+modified%3A+2023-02-18T09%3A00%3A03.000Z%0A%0A%3C%2Fdetails%3E)
