# TextTrackCueList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextTrackCueList&level=high)

The `TextTrackCueList` interface of the [WebVTT API](/en-US/docs/Web/API/WebVTT_API) is an array-like object that represents a dynamically updating list of [TextTrackCue](/en-US/docs/Web/API/TextTrackCue) objects.

An instance of this type is obtained from [TextTrack.cues](/en-US/docs/Web/API/TextTrack/cues) in order to get all the cues in the [TextTrack](/en-US/docs/Web/API/TextTrack) object. This interface has no constructor.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[TextTrackCueList.length](/en-US/docs/Web/API/TextTrackCueList/length)Read only

An `unsigned long` that is the number of cues in the list.

## [Instance methods](#instance_methods)

[TextTrackCueList.getCueById()](/en-US/docs/Web/API/TextTrackCueList/getCueById)

Returns the first [TextTrackCue](/en-US/docs/Web/API/TextTrackCue) object with the identifier passed to it.

## [Examples](#examples)

The [HTMLMediaElement.textTracks](/en-US/docs/Web/API/HTMLMediaElement/textTracks) property returns a [TextTrackList](/en-US/docs/Web/API/TextTrackList) object listing all of the [TextTrack](/en-US/docs/Web/API/TextTrack) objects, one for each text track linked to the media. The [TextTrack.cues](/en-US/docs/Web/API/TextTrack/cues) property then returns a `TextTrackCueList` containing the cues for that particular track.

js

```
const video = document.getElementById("video");
video.onplay = () => {
  console.log(video.textTracks[0].cues);
};
```

## [Specifications](#specifications)

Specification
[HTML# texttrackcuelist](https://html.spec.whatwg.org/multipage/media.html#texttrackcuelist)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 12, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/TextTrackCueList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/texttrackcuelist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextTrackCueList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftexttrackcuelist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextTrackCueList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftexttrackcuelist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3975bcf6caa09c9c5f7fddf2eef2be6c021d00f6%0A*+Document+last+modified%3A+2024-07-12T06%3A45%3A00.000Z%0A%0A%3C%2Fdetails%3E)
