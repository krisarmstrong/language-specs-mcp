# XRAnchorSet

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRAnchorSet&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `XRAnchorSet` interface exposes a collection of anchors. Its instances are returned by [XRFrame.trackedAnchors](/en-US/docs/Web/API/XRFrame/trackedAnchors) and are [Set-like objects](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set-like_browser_apis).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

See [Set](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) for details.

## [Instance methods](#instance_methods)

See [Set](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) for details.

## [Examples](#examples)

### [Handling anchor tracking loss](#handling_anchor_tracking_loss)

js

```
const trackedAnchors = frame.trackedAnchors;

for (const anchor of previousFrameAnchors) {
  if (!trackedAnchors.has(anchor)) {
    // Handle anchor tracking loss
  }
}
```

## [Specifications](#specifications)

Specification
[WebXR Anchors Module# xranchorset](https://immersive-web.github.io/anchors/#xranchorset)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRAnchor](/en-US/docs/Web/API/XRAnchor)
- [XRFrame.trackedAnchors](/en-US/docs/Web/API/XRFrame/trackedAnchors)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 5, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRAnchorSet/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xranchorset/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRAnchorSet&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxranchorset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRAnchorSet%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxranchorset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe18aa8e600733ebc25443075c563fd56361dfe98%0A*+Document+last+modified%3A+2023-09-05T23%3A54%3A58.000Z%0A%0A%3C%2Fdetails%3E)
