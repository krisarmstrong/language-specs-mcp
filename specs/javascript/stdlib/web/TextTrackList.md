# TextTrackList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextTrackList&level=high)

The `TextTrackList` interface is used to represent a list of the text tracks defined for the associated video or audio element, with each track represented by a separate [TextTrack](/en-US/docs/Web/API/TextTrack) object in the list.

Text tracks can be added to a media element declaratively using the [<track>](/en-US/docs/Web/HTML/Reference/Elements/track) element or programmatically using the [HTMLMediaElement.addTextTrack()](/en-US/docs/Web/API/HTMLMediaElement/addTextTrack) method.

An instance of this object can be retrieved using the [textTracks](/en-US/docs/Web/API/HTMLMediaElement/textTracks) property of an [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) object.

For a given [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) object media, the individual tracks can be accessed using:

- `media.TextTracks[n]`, to get the n-th text track from the object's list of text tracks
- the [media.textTracks.getTrackById()](/en-US/docs/Web/API/TextTrackList/getTrackById) method

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Usage notes](#usage_notes)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[length](/en-US/docs/Web/API/TextTrackList/length)Read only

The number of tracks in the list.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[getTrackById()](/en-US/docs/Web/API/TextTrackList/getTrackById)

Returns the [TextTrack](/en-US/docs/Web/API/TextTrack) found within the `TextTrackList` whose [id](/en-US/docs/Web/API/TextTrack/id) matches the specified string. If no match is found, `null` is returned.

## [Events](#events)

[addtrack](/en-US/docs/Web/API/TextTrackList/addtrack_event)

Fired when a new text track has been added to the media element. Also available via the `onaddtrack` property.

[change](/en-US/docs/Web/API/TextTrackList/change_event)

Fired when a text track has been made active or inactive. Also available via the `onchange` property.

[removetrack](/en-US/docs/Web/API/TextTrackList/removetrack_event)

Fired when a new text track has been removed from the media element. Also available via the `onremovetrack` property.

## [Usage notes](#usage_notes)

In addition to being able to obtain direct access to the text tracks present on a media element, `TextTrackList` lets you set event handlers on the [addtrack](/en-US/docs/Web/API/TextTrackList/addtrack_event) and [removetrack](/en-US/docs/Web/API/TextTrackList/removetrack_event) events, so that you can detect when tracks are added to or removed from the media element's stream.

## [Examples](#examples)

### [Getting a video element's text track list](#getting_a_video_elements_text_track_list)

To get a media element's `TextTrackList`, use its [textTracks](/en-US/docs/Web/API/HTMLMediaElement/textTracks) property.

js

```
const textTracks = document.querySelector("video").textTracks;
```

### [Monitoring track count changes](#monitoring_track_count_changes)

In this example, we have an app that displays information about the number of channels available. To keep it up to date, handlers for the [addtrack](/en-US/docs/Web/API/TextTrackList/addtrack_event) and [removetrack](/en-US/docs/Web/API/TextTrackList/removetrack_event) events are set up.

js

```
textTracks.onaddtrack = updateTrackCount;
textTracks.onremovetrack = updateTrackCount;

function updateTrackCount(event) {
  trackCount = textTracks.length;
  drawTrackCountIndicator(trackCount);
}
```

## [Specifications](#specifications)

Specification
[HTML# text-track-api](https://html.spec.whatwg.org/multipage/media.html#text-track-api)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 9, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TextTrackList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/texttracklist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextTrackList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftexttracklist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextTrackList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftexttracklist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0eff6caa0378d6dabf24d8f5c42665a8f98c9b92%0A*+Document+last+modified%3A+2025-10-09T09%3A11%3A29.000Z%0A%0A%3C%2Fdetails%3E)
