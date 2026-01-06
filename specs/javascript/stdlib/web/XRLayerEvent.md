# XRLayerEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRLayerEvent&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRLayerEvent` interface of the [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API) is the event type for events related to a change of state of an [XRLayer](/en-US/docs/Web/API/XRLayer) object. These events occur, for example, when the layer needs to be redrawn.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Event types](#event_types)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[XRLayerEvent()](/en-US/docs/Web/API/XRLayerEvent/XRLayerEvent)Experimental

Creates and returns a new `XRLayerEvent` object.

## [Instance properties](#instance_properties)

In addition to properties inherited from its parent interface, [Event](/en-US/docs/Web/API/Event), `XRLayerEvent` provides the following:

[layer](/en-US/docs/Web/API/XRLayerEvent/layer)Read onlyExperimental

The [XRLayer](/en-US/docs/Web/API/XRLayer) which generated the event.

## [Instance methods](#instance_methods)

While `XRSessionEvent` defines no methods, it inherits methods from its parent interface, [Event](/en-US/docs/Web/API/Event).

## [Event types](#event_types)

The following events are represented using the `XRLayerEvent` interface, and are permitted values for its `type` parameter.

### [redraw event](#redraw_event)

The `redraw` event is tent to the layer object when the underlying resources of the layer are lost or when the XR Compositor can no longer reproject the layer. If this event is sent, authors should redraw the content of the layer in the next XR animation frame. It is available on the following layer objects:

- [XRQuadLayer](/en-US/docs/Web/API/XRQuadLayer): [redraw](/en-US/docs/Web/API/XRQuadLayer/redraw_event)
- [XRCylinderLayer](/en-US/docs/Web/API/XRCylinderLayer): [redraw](/en-US/docs/Web/API/XRCylinderLayer/redraw_event)
- [XREquirectLayer](/en-US/docs/Web/API/XREquirectLayer): [redraw](/en-US/docs/Web/API/XREquirectLayer/redraw_event)
- [XRCubeLayer](/en-US/docs/Web/API/XRCubeLayer): [redraw](/en-US/docs/Web/API/XRCubeLayer/redraw_event)

## [Specifications](#specifications)

Specification
[WebXR Layers API Level 1# xrlayerevent-interface](https://immersive-web.github.io/layers/#xrlayerevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRCompositionLayer.needsRedraw](/en-US/docs/Web/API/XRCompositionLayer/needsRedraw)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 18, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRLayerEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrlayerevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRLayerEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrlayerevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRLayerEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrlayerevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5b33acd44e7bb9c7be2efc75ba9a04b8bf8b2b2%0A*+Document+last+modified%3A+2023-02-18T09%3A00%3A03.000Z%0A%0A%3C%2Fdetails%3E)
