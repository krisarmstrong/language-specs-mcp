# XRReferenceSpaceEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRReferenceSpaceEvent&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API) interface `XRReferenceSpaceEvent` represents an event sent to an [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace). Currently, the only event that uses this type is the [reset](/en-US/docs/Web/API/XRReferenceSpace/reset_event) event.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Event types](#event_types)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[XRReferenceSpaceEvent()](/en-US/docs/Web/API/XRReferenceSpaceEvent/XRReferenceSpaceEvent)

Returns a new `XRReferenceSpaceEvent` with the specified type and configuration.

## [Instance properties](#instance_properties)

In addition to inheriting the properties available on the parent interface, [Event](/en-US/docs/Web/API/Event), `XRReferenceSpaceEvent` objects include the following properties:

[referenceSpace](/en-US/docs/Web/API/XRReferenceSpaceEvent/referenceSpace)Read only

An [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace) indicating the reference space that generated the event.

[transform](/en-US/docs/Web/API/XRReferenceSpaceEvent/transform)Read only

An [XRRigidTransform](/en-US/docs/Web/API/XRRigidTransform) object indicating the position and orientation of the specified `referenceSpace`'s native origin after the event, defined relative to the coordinate system before the event.

## [Instance methods](#instance_methods)

While `XRReferenceSpaceEvent` does not define any methods, it inherits the methods of its parent interface, [Event](/en-US/docs/Web/API/Event).

## [Event types](#event_types)

[reset](/en-US/docs/Web/API/XRReferenceSpace/reset_event)

The `reset` event is sent to a reference space when its native origin is changed due to a discontinuity, recalibration, or device reset. This is an opportunity for your app to update any stored transforms, position/orientation information, or the like—or to dump any cached values based on the reference's space's origin so you can recompute them as needed.

## [Specifications](#specifications)

Specification
[WebXR Device API# xrreferencespaceevent-interface](https://immersive-web.github.io/webxr/#xrreferencespaceevent-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 17, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/XRReferenceSpaceEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrreferencespaceevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRReferenceSpaceEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrreferencespaceevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRReferenceSpaceEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrreferencespaceevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6c592023efa1f762eaa1eb1f36241750626be51c%0A*+Document+last+modified%3A+2024-07-17T23%3A29%3A22.000Z%0A%0A%3C%2Fdetails%3E)
