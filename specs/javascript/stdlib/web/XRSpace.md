# XRSpace

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRSpace&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `XRSpace` interface of the [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API) is an abstract interface providing a common basis for every class which represents a virtual coordinate system within the virtual world, in which its origin corresponds to a physical location. Spatial data in WebXR is always expressed relative to an object based upon one of the descendant interfaces of `XRSpace`, at the time at which a given [XRFrame](/en-US/docs/Web/API/XRFrame) takes place.

Numeric values such as pose positions are thus coordinates in the corresponding `XRSpace`, relative to that space's origin.

Note: The `XRSpace` interface is never used directly; instead, all spaces are created using one of the interfaces based on `XRSpace`. At this time, those are [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace), [XRBoundedReferenceSpace](/en-US/docs/Web/API/XRBoundedReferenceSpace), and [XRJointSpace](/en-US/docs/Web/API/XRJointSpace).

## In this article

- [Interfaces based on XRSpace](#interfaces_based_on_xrspace)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Interfaces based on XRSpace](#interfaces_based_on_xrspace)

Below is a list of interfaces based on the `XRSpace` interface.

[XRBoundedReferenceSpace](/en-US/docs/Web/API/XRBoundedReferenceSpace)

Represents a reference space which may move within a region of space whose borders are defined by an array of points laid out in clockwise order along the floor to define the passable region of the space. The origin of an `XRBoundedReferenceSpace` is always at floor level, with its X and Z coordinates typically defaulting to a location near the room's center.

[XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace)

Represents a reference space which is typically expected to remain static for the duration of the [XRSession](/en-US/docs/Web/API/XRSession). While objects may move within the space, the space itself remains fixed in place. There are exceptions to this static nature; most commonly, an `XRReferenceSpace` may move in order to adjust based on reconfiguration of the user's headset or other motion-sensitive device.

[XRJointSpace](/en-US/docs/Web/API/XRJointSpace)

Represents the space of an [XRHand](/en-US/docs/Web/API/XRHand) joint.

## [Instance properties](#instance_properties)

The `XRSpace` interface defines no properties of its own; however, it does inherit the properties of its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Instance methods](#instance_methods)

The `XRSpace` interface provides no methods of its own. However, it inherits the methods of [EventTarget](/en-US/docs/Web/API/EventTarget), its parent interface.

## [Specifications](#specifications)

Specification
[WebXR Device API# xrspace-interface](https://immersive-web.github.io/webxr/#xrspace-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/XRSpace/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrspace/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRSpace&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrspace%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRSpace%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrspace%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe561fa67af347b9770b359ba93e8579d2a540682%0A*+Document+last+modified%3A+2024-07-26T15%3A42%3A59.000Z%0A%0A%3C%2Fdetails%3E)
