# VideoTrackList

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoTrackList&level=not)

The `VideoTrackList` interface is used to represent a list of the video tracks contained within a [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element, with each track represented by a separate [VideoTrack](/en-US/docs/Web/API/VideoTrack) object in the list.

Retrieve an instance of this object with [HTMLMediaElement.videoTracks](/en-US/docs/Web/API/HTMLMediaElement/videoTracks). The individual tracks can be accessed using array syntax or functions such as [forEach()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach) for example.

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

[length](/en-US/docs/Web/API/VideoTrackList/length)Read only

The number of tracks in the list.

[selectedIndex](/en-US/docs/Web/API/VideoTrackList/selectedIndex)Read only

The index of the currently selected track, if any, or `−1` otherwise.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[getTrackById()](/en-US/docs/Web/API/VideoTrackList/getTrackById)

Returns the [VideoTrack](/en-US/docs/Web/API/VideoTrack) found within the `VideoTrackList` whose [id](/en-US/docs/Web/API/VideoTrack/id) matches the specified string. If no match is found, `null` is returned.

## [Events](#events)

[addtrack](/en-US/docs/Web/API/VideoTrackList/addtrack_event)

Fired when a new video track has been added to the media element. Also available via the `onaddtrack` property.

[change](/en-US/docs/Web/API/VideoTrackList/change_event)

Fired when a video track has been made active or inactive. Also available via the `onchange` property.

[removetrack](/en-US/docs/Web/API/VideoTrackList/removetrack_event)

Fired when a new video track has been removed from the media element. Also available via the `onremovetrack` property.

## [Usage notes](#usage_notes)

In addition to being able to obtain direct access to the video tracks present on a media element, `VideoTrackList` lets you set event handlers on the [addtrack](/en-US/docs/Web/API/VideoTrackList/addtrack_event) and [removetrack](/en-US/docs/Web/API/VideoTrackList/removetrack_event) events, so that you can detect when tracks are added to or removed from the media element's stream.

## [Examples](#examples)

### [Getting a media element's video track list](#getting_a_media_elements_video_track_list)

To get a media element's `VideoTrackList`, use its [videoTracks](/en-US/docs/Web/API/HTMLMediaElement/videoTracks) property.

js

```
const videoTracks = document.querySelector("video").videoTracks;
```

### [Monitoring track count changes](#monitoring_track_count_changes)

In this example, we have an app that displays information about the number of channels available. To keep it up to date, handlers for the [addtrack](/en-US/docs/Web/API/VideoTrackList/addtrack_event) and [removetrack](/en-US/docs/Web/API/VideoTrackList/removetrack_event) events are set up.

js

```
videoTracks.onaddtrack = updateTrackCount;
videoTracks.onremovetrack = updateTrackCount;

function updateTrackCount(event) {
  trackCount = videoTracks.length;
  drawTrackCountIndicator(trackCount);
}
```

## [Specifications](#specifications)

Specification
[HTML# audiotracklist-and-videotracklist-objects](https://html.spec.whatwg.org/multipage/media.html#audiotracklist-and-videotracklist-objects)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/VideoTrackList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/videotracklist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoTrackList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvideotracklist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoTrackList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvideotracklist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32305cc3cf274fbfdcc73a296bbd400a26f38296%0A*+Document+last+modified%3A+2024-07-24T20%3A47%3A46.000Z%0A%0A%3C%2Fdetails%3E)
