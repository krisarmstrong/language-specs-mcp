# VTTCue

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVTTCue&level=high)

The `VTTCue` interface of the [WebVTT API](/en-US/docs/Web/API/WebVTT_API) represents a cue that can be added to the text track associated with a particular video (or other media).

A cue defines the text to display in a particular timeslice of a video or audio track, along with display properties such as its size, alignment, and position.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[VTTCue()](/en-US/docs/Web/API/VTTCue/VTTCue)

Returns a newly created `VTTCue` object that covers the given time range and has the given text.

## [Instance properties](#instance_properties)

This interface also inherits properties from [TextTrackCue](/en-US/docs/Web/API/TextTrackCue).

[VTTCue.region](/en-US/docs/Web/API/VTTCue/region)

A [VTTRegion](/en-US/docs/Web/API/VTTRegion) object describing the video's sub-region that the cue will be drawn onto, or `null` if none is assigned.

[VTTCue.vertical](/en-US/docs/Web/API/VTTCue/vertical)

An enum representing the cue writing direction.

[VTTCue.snapToLines](/en-US/docs/Web/API/VTTCue/snapToLines)

`true` if the [VTTCue.line](/en-US/docs/Web/API/VTTCue/line) attribute indicates an integer number of lines or `false` if it represents a percentage of the video size. This is `true` by default.

[VTTCue.line](/en-US/docs/Web/API/VTTCue/line)

Represents the line positioning of the cue. This can be the string `auto` or a number whose interpretation depends on the value of [VTTCue.snapToLines](/en-US/docs/Web/API/VTTCue/snapToLines).

[VTTCue.lineAlign](/en-US/docs/Web/API/VTTCue/lineAlign)

An enum representing the alignment of the VTT cue.

[VTTCue.position](/en-US/docs/Web/API/VTTCue/position)

Represents the indentation of the cue within the line. This can be the string `auto`, a number representing the percentage of the [VTTCue.region](/en-US/docs/Web/API/VTTCue/region), or the video size if [VTTCue.region](/en-US/docs/Web/API/VTTCue/region) is `null`.

[VTTCue.positionAlign](/en-US/docs/Web/API/VTTCue/positionAlign)

An enum representing the alignment of the cue. This is used to determine what the [VTTCue.position](/en-US/docs/Web/API/VTTCue/position) is anchored to. The default is `auto`.

[VTTCue.size](/en-US/docs/Web/API/VTTCue/size)

Represents the size of the cue, as a percentage of the video size.

[VTTCue.align](/en-US/docs/Web/API/VTTCue/align)

An enum representing the alignment of all the lines of text within the cue box.

[VTTCue.text](/en-US/docs/Web/API/VTTCue/text)

A string representing the contents of the cue.

## [Instance methods](#instance_methods)

[getCueAsHTML()](/en-US/docs/Web/API/VTTCue/getCueAsHTML)

Returns the cue text as a [DocumentFragment](/en-US/docs/Web/API/DocumentFragment).

## [Example](#example)

### [HTML](#html)

The following example adds a new [TextTrack](/en-US/docs/Web/API/TextTrack) to the video, then adds cues using the [TextTrack.addCue()](/en-US/docs/Web/API/TextTrack/addCue) method, with a `VTTCue` object as the value.

html

```
<video controls src="/shared-assets/videos/friday.mp4"></video>
```

### [CSS](#css)

css

```
video {
  width: 420px;
  height: 300px;
}
```

### [JavaScript](#javascript)

js

```
let video = document.querySelector("video");
let track = video.addTextTrack("captions", "Captions", "en");
track.mode = "showing";
track.addCue(new VTTCue(0, 0.9, "Hildy!"));
track.addCue(new VTTCue(1, 1.4, "How are you?"));
track.addCue(new VTTCue(1.5, 2.9, "Tell me, is the lord of the universe in?"));
track.addCue(new VTTCue(3, 4.2, "Yes, he's in - in a bad humor"));
track.addCue(new VTTCue(4.3, 6, "Somebody must've stolen the crown jewels"));
console.log(track.cues);
```

### [Result](#result)

## [Specifications](#specifications)

Specification
[WebVTT: The Web Video Text Tracks Format# the-vttcue-interface](https://w3c.github.io/webvtt/#the-vttcue-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/VTTCue/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/vttcue/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVTTCue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvttcue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVTTCue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvttcue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe68530dbce2b661c8860e9c6a1c70b1caca5a199%0A*+Document+last+modified%3A+2025-05-07T15%3A32%3A25.000Z%0A%0A%3C%2Fdetails%3E)
