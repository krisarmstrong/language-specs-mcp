# XRMediaBinding

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRMediaBinding&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRMediaBinding` interface is used to create layers that display the content of an [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement).

Note: Only the video frames will be displayed in the layer. Video controls need to be implemented separately and must be drawn in another layer.

## In this article

- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[XRMediaBinding()](/en-US/docs/Web/API/XRMediaBinding/XRMediaBinding)Experimental

Creates a new `XRMediaBinding` object for the specified [XRSession](/en-US/docs/Web/API/XRSession).

## [Instance methods](#instance_methods)

[XRMediaBinding.createCylinderLayer()](/en-US/docs/Web/API/XRMediaBinding/createCylinderLayer)Experimental

Returns an [XRCylinderLayer](/en-US/docs/Web/API/XRCylinderLayer) object bound to an [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement).

[XRMediaBinding.createEquirectLayer()](/en-US/docs/Web/API/XRMediaBinding/createEquirectLayer)Experimental

Returns an [XREquirectLayer](/en-US/docs/Web/API/XREquirectLayer) object bound to an [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement).

[XRMediaBinding.createQuadLayer()](/en-US/docs/Web/API/XRMediaBinding/createQuadLayer)Experimental

Returns an [XRQuadLayer](/en-US/docs/Web/API/XRQuadLayer) object bound to an [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement).

## [Specifications](#specifications)

Specification
[WebXR Layers API Level 1# XRWebGLBindingtype](https://immersive-web.github.io/layers/#XRWebGLBindingtype)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement)
- [XRCylinderLayer](/en-US/docs/Web/API/XRCylinderLayer), [XREquirectLayer](/en-US/docs/Web/API/XREquirectLayer), [XRQuadLayer](/en-US/docs/Web/API/XRQuadLayer)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/XRMediaBinding/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrmediabinding/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRMediaBinding&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrmediabinding%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRMediaBinding%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrmediabinding%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe561fa67af347b9770b359ba93e8579d2a540682%0A*+Document+last+modified%3A+2024-07-26T15%3A42%3A59.000Z%0A%0A%3C%2Fdetails%3E)
