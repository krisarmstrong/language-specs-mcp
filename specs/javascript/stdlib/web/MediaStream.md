# MediaStream

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2017⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStream&level=high)

The `MediaStream` interface of the [Media Capture and Streams API](/en-US/docs/Web/API/Media_Capture_and_Streams_API) represents a stream of media content. A stream consists of several tracks, such as video or audio tracks. Each track is specified as an instance of [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack).

You can obtain a `MediaStream` object either by using the constructor or by calling functions such as [MediaDevices.getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia), [MediaDevices.getDisplayMedia()](/en-US/docs/Web/API/MediaDevices/getDisplayMedia), or [HTMLCanvasElement.captureStream()](/en-US/docs/Web/API/HTMLCanvasElement/captureStream) and [HTMLMediaElement.captureStream()](/en-US/docs/Web/API/HTMLMediaElement/captureStream).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[MediaStream()](/en-US/docs/Web/API/MediaStream/MediaStream)

Creates and returns a new `MediaStream` object. You can create an empty stream, a stream which is based upon an existing stream, or a stream that contains a specified list of tracks (specified as an array of [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) objects).

## [Instance properties](#instance_properties)

This interface inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[MediaStream.active](/en-US/docs/Web/API/MediaStream/active)Read only

A Boolean value that returns `true` if the `MediaStream` is active, or `false` otherwise.

[MediaStream.id](/en-US/docs/Web/API/MediaStream/id)Read only

A string containing a 36-character universally unique identifier ([UUID](/en-US/docs/Glossary/UUID)) for the object.

## [Instance methods](#instance_methods)

This interface inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[MediaStream.addTrack()](/en-US/docs/Web/API/MediaStream/addTrack)

Stores a copy of the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) given as argument. If the track has already been added to the `MediaStream` object, nothing happens.

[MediaStream.clone()](/en-US/docs/Web/API/MediaStream/clone)

Returns a clone of the `MediaStream` object. The clone will, however, have a unique value for [id](/en-US/docs/Web/API/MediaStream/id).

[MediaStream.getAudioTracks()](/en-US/docs/Web/API/MediaStream/getAudioTracks)

Returns a list of the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) objects stored in the `MediaStream` object that have their `kind` attribute set to `audio`. The order is not defined, and may not only vary from one browser to another, but also from one call to another.

[MediaStream.getTrackById()](/en-US/docs/Web/API/MediaStream/getTrackById)

Returns the track whose ID corresponds to the one given in parameters, `trackId`. If no parameter is given, or if no track with that ID does exist, it returns `null`. If several tracks have the same ID, it returns the first one.

[MediaStream.getTracks()](/en-US/docs/Web/API/MediaStream/getTracks)

Returns a list of all [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) objects stored in the `MediaStream` object, regardless of the value of the `kind` attribute. The order is not defined, and may not only vary from one browser to another, but also from one call to another.

[MediaStream.getVideoTracks()](/en-US/docs/Web/API/MediaStream/getVideoTracks)

Returns a list of the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) objects stored in the `MediaStream` object that have their `kind` attribute set to `"video"`. The order is not defined, and may not only vary from one browser to another, but also from one call to another.

[MediaStream.removeTrack()](/en-US/docs/Web/API/MediaStream/removeTrack)

Removes the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) given as argument. If the track is not part of the `MediaStream` object, nothing happens.

## [Events](#events)

[addtrack](/en-US/docs/Web/API/MediaStream/addtrack_event)

Fired when a new [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) object is added.

[removetrack](/en-US/docs/Web/API/MediaStream/removetrack_event)

Fired when a [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) object has been removed.

`active`Non-standard

Fired when the MediaStream is activated.

`inactive`Non-standard

Fired when the MediaStream is inactivated.

## [Specifications](#specifications)

Specification
[Media Capture and Streams# mediastream](https://w3c.github.io/mediacapture-main/#mediastream)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the MediaStream Recording API](/en-US/docs/Web/API/MediaStream_Recording_API/Using_the_MediaStream_Recording_API)
- [WebRTC API](/en-US/docs/Web/API/WebRTC_API)
- [Web Audio API](/en-US/docs/Web/API/Web_Audio_API)
- [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 27, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaStream/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediastream/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStream&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediastream%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStream%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediastream%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbff3a6a2e6b3c13dd8bb0c80a1eb9da08cce5dc6%0A*+Document+last+modified%3A+2024-10-27T23%3A53%3A01.000Z%0A%0A%3C%2Fdetails%3E)
