# XRBoundedReferenceSpace

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRBoundedReferenceSpace&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API)'s `XRBoundedReferenceSpace` interface describes a virtual world [reference space](/en-US/docs/Web/API/WebXR_Device_API/Geometry) which has preset boundaries. This extends [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace), which describes an essentially unrestricted space around the viewer's position. These bounds are defined using an array of points, each of which defines a vertex in a polygon inside which the user is allowed to move.

This is typically used when the XR system is capable of tracking the user's physical movement within a limited distance of their starting position. The specified bounds may, in fact, describe the shape and size of the room the user is located in, in order to let the WebXR site or application prevent the user from colliding with the walls or other obstacles in the real world. At a minimum, the boundaries indicate the area in which the XR device is capable of tracking the user's movement. See the article [Using bounded reference spaces](/en-US/docs/Web/API/WebXR_Device_API/Bounded_reference_spaces) for details on how bounded spaces work and why they're useful.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

In addition to the properties of [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace), `XRBoundedReferenceSpace` includes the following:

[boundsGeometry](/en-US/docs/Web/API/XRBoundedReferenceSpace/boundsGeometry)Read onlyExperimental

An array of [DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly) objects, each of which defines a vertex in the polygon defining the boundaries within which the user will be required to remain. These vertices must be sorted such that they move clockwise around the viewer's position.

## [Instance methods](#instance_methods)

`XRBoundedReferenceSpace` inherits the methods of its parent interface, [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace). It has no further methods.

## [Specifications](#specifications)

Specification
[WebXR Device API# xrboundedreferencespace-interface](https://immersive-web.github.io/webxr/#xrboundedreferencespace-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API)
- [Geometry and reference spaces in WebXR](/en-US/docs/Web/API/WebXR_Device_API/Geometry)
- [Viewpoints and viewers: simulating cameras in WebXR](/en-US/docs/Web/API/WebXR_Device_API/Cameras)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 18, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRBoundedReferenceSpace/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrboundedreferencespace/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRBoundedReferenceSpace&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrboundedreferencespace%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRBoundedReferenceSpace%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrboundedreferencespace%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5b33acd44e7bb9c7be2efc75ba9a04b8bf8b2b2%0A*+Document+last+modified%3A+2023-02-18T09%3A00%3A03.000Z%0A%0A%3C%2Fdetails%3E)
