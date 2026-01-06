# TrackEvent

The `TrackEvent` interface of the [HTML DOM API](/en-US/docs/Web/API/HTML_DOM_API) is used for events which represent changes to a set of available tracks on an HTML media element; these events are `addtrack` and `removetrack`.

It's important not to confuse `TrackEvent` with the [RTCTrackEvent](/en-US/docs/Web/API/RTCTrackEvent) interface, which is used for tracks which are part of an [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection).

Events based on `TrackEvent` are always sent to one of the media track list types:

- Events involving video tracks are always sent to the [VideoTrackList](/en-US/docs/Web/API/VideoTrackList) found in [HTMLMediaElement.videoTracks](/en-US/docs/Web/API/HTMLMediaElement/videoTracks)
- Events involving audio tracks are always sent to the [AudioTrackList](/en-US/docs/Web/API/AudioTrackList) specified in [HTMLMediaElement.audioTracks](/en-US/docs/Web/API/HTMLMediaElement/audioTracks)
- Events affecting text tracks are sent to the [TextTrackList](/en-US/docs/Web/API/TextTrackList) object indicated by [HTMLMediaElement.textTracks](/en-US/docs/Web/API/HTMLMediaElement/textTracks).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[TrackEvent()](/en-US/docs/Web/API/TrackEvent/TrackEvent)

Creates and initializes a new `TrackEvent` object with the event type specified, as well as optional additional properties.

## [Instance properties](#instance_properties)

`TrackEvent` is based on [Event](/en-US/docs/Web/API/Event), so properties of `Event` are also available on `TrackEvent` objects.

[track](/en-US/docs/Web/API/TrackEvent/track)Read only

The DOM track object the event is in reference to. If not `null`, this is always an object of one of the media track types: [AudioTrack](/en-US/docs/Web/API/AudioTrack), [VideoTrack](/en-US/docs/Web/API/VideoTrack), or [TextTrack](/en-US/docs/Web/API/TextTrack)).

## [Instance methods](#instance_methods)

`TrackEvent` has no methods of its own; however, it is based on [Event](/en-US/docs/Web/API/Event), so it provides the methods available on `Event` objects.

## [Example](#example)

This example sets up a function, `handleTrackEvent()`, which is called for any `addtrack` or `removetrack` event on the first [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element found in the document.

js

```
const videoElem = document.querySelector("video");

videoElem.videoTracks.addEventListener("addtrack", handleTrackEvent);
videoElem.videoTracks.addEventListener("removetrack", handleTrackEvent);
videoElem.audioTracks.addEventListener("addtrack", handleTrackEvent);
videoElem.audioTracks.addEventListener("removetrack", handleTrackEvent);
videoElem.textTracks.addEventListener("addtrack", handleTrackEvent);
videoElem.textTracks.addEventListener("removetrack", handleTrackEvent);

function handleTrackEvent(event) {
  let trackKind;

  if (event.target instanceof VideoTrackList) {
    trackKind = "video";
  } else if (event.target instanceof AudioTrackList) {
    trackKind = "audio";
  } else if (event.target instanceof TextTrackList) {
    trackKind = "text";
  } else {
    trackKind = "unknown";
  }

  switch (event.type) {
    case "addtrack":
      console.log(`Added a ${trackKind} track`);
      break;
    case "removetrack":
      console.log(`Removed a ${trackKind} track`);
      break;
  }
}
```

The event handler uses the JavaScript [instanceof](/en-US/docs/Web/JavaScript/Reference/Operators/instanceof) operator to determine which type of track the event occurred on, then outputs to console a message indicating what kind of track it is and whether it's being added to or removed from the element.

## [Specifications](#specifications)

Specification
[HTML# the-trackevent-interface](https://html.spec.whatwg.org/multipage/media.html#the-trackevent-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TrackEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/trackevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTrackEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftrackevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTrackEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftrackevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2ccbd062264d0a2a34f185a3386cb272f42c50f5%0A*+Document+last+modified%3A+2025-09-18T15%3A45%3A07.000Z%0A%0A%3C%2Fdetails%3E)
