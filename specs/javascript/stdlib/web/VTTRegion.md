# VTTRegion

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVTTRegion&level=not)

The `VTTRegion` interface of the [WebVTT API](/en-US/docs/Web/API/WebVTT_API) describes a portion of the video to render a [VTTCue](/en-US/docs/Web/API/VTTCue) onto.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

`VTTRegion()`

Returns a newly created `VTTRegion` object.

## [Instance properties](#instance_properties)

`VTTRegion.id`

A string that identifies the region.

`VTTRegion.width`

Represents the width of the region, as a percentage of the video.

`VTTRegion.lines`

Represents the height of the region, in number of lines.

`VTTRegion.regionAnchorX`

Represents the region anchor X offset, as a percentage of the region.

`VTTRegion.regionAnchorY`

Represents the region anchor Y offset, as a percentage of the region.

`VTTRegion.viewportAnchorX`

Represents the viewport anchor X offset, as a percentage of the video.

`VTTRegion.viewportAnchorY`

Represents the viewport anchor Y offset, as a percentage of the video.

`VTTRegion.scroll`

An enum representing how adding a new cue will move existing cues.

## [Examples](#examples)

js

```
const region = new VTTRegion();
region.width = 50; // Use 50% of the video width
region.lines = 4; // Use 4 lines of height.
region.viewportAnchorX = 25; // Have the region start at 25% from the left.
const cue = new VTTCue(2, 3, "Cool text to be displayed");
cue.region = region; // This cue will be drawn only within this region.
```

## [Specifications](#specifications)

Specification
[WebVTT: The Web Video Text Tracks Format# the-vttregion-interface](https://w3c.github.io/webvtt/#the-vttregion-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 12, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/VTTRegion/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/vttregion/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVTTRegion&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvttregion%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVTTRegion%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvttregion%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3975bcf6caa09c9c5f7fddf2eef2be6c021d00f6%0A*+Document+last+modified%3A+2024-07-12T06%3A45%3A00.000Z%0A%0A%3C%2Fdetails%3E)
