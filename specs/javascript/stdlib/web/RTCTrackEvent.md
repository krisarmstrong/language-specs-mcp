# RTCTrackEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCTrackEvent&level=high)

The [WebRTC API](/en-US/docs/Web/API/WebRTC_API) interface `RTCTrackEvent` represents the [track](/en-US/docs/Web/API/RTCPeerConnection/track_event) event, which is sent when a new [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) is added to an [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver) which is part of the [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection).

The target is the `RTCPeerConnection` object to which the track is being added.

This event is sent by the WebRTC layer to the website or application, so you will not typically need to instantiate an `RTCTrackEvent` yourself.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Track event types](#track_event_types)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[RTCTrackEvent()](/en-US/docs/Web/API/RTCTrackEvent/RTCTrackEvent)

Creates and returns a new `RTCTrackEvent` object. You will probably not need to create new track events yourself, since they're typically created by the WebRTC infrastructure and sent to the connection's [ontrack](/en-US/docs/Web/API/RTCPeerConnection/track_event) event handler.

## [Instance properties](#instance_properties)

Since `RTCTrackEvent` is based on [Event](/en-US/docs/Web/API/Event), its properties are also available.

[receiver](/en-US/docs/Web/API/RTCTrackEvent/receiver)Read only

The [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver) used by the track that's been added to the `RTCPeerConnection`.

[streams](/en-US/docs/Web/API/RTCTrackEvent/streams)Read onlyOptional

An array of [MediaStream](/en-US/docs/Web/API/MediaStream) objects, each representing one of the media streams to which the added [track](/en-US/docs/Web/API/RTCTrackEvent/track) belongs. By default, the array is empty, indicating a streamless track.

[track](/en-US/docs/Web/API/RTCTrackEvent/track)Read only

The [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) which has been added to the connection.

[transceiver](/en-US/docs/Web/API/RTCTrackEvent/transceiver)Read only

The [RTCRtpTransceiver](/en-US/docs/Web/API/RTCRtpTransceiver) being used by the new track.

## [Track event types](#track_event_types)

There is only one type of track event.

### [track](#track)

The [track](/en-US/docs/Web/API/RTCPeerConnection/track_event) event is sent to the [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection) when a new track has been added to the connection. By the time the `track` event is delivered to the `RTCPeerConnection`'s [ontrack](/en-US/docs/Web/API/RTCPeerConnection/track_event) handler, the new media has completed its negotiation for a specific [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver) (which is specified by the event's [receiver](/en-US/docs/Web/API/RTCTrackEvent/receiver) property).

In addition, the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) specified by the receiver's [track](/en-US/docs/Web/API/RTCRtpReceiver/track) is the same one specified by the event's [track](/en-US/docs/Web/API/RTCTrackEvent/track), and the track has been added to any associated remote [MediaStream](/en-US/docs/Web/API/MediaStream) objects.

You can add a `track` event listener to be notified when the new track is available so that you can, for example, attach its media to a [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element, using either [RTCPeerConnection.addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or the `ontrack` event handler property.

Note: It may be helpful to keep in mind that you receive the `track` event when a new inbound track has been added to your connection, and you call [addTrack()](/en-US/docs/Web/API/RTCPeerConnection/addTrack) to add a track to the far end of the connection, thereby triggering a `track` event on the remote peer.

## [Example](#example)

This simple example creates an event listener for the [track](/en-US/docs/Web/API/RTCPeerConnection/track_event) event which sets the [srcObject](/en-US/docs/Web/API/HTMLMediaElement/srcObject) of the [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element with the ID `video-box` to the first stream in the list passed in the event's [streams](/en-US/docs/Web/API/RTCTrackEvent/streams) array.

js

```
peerConnection.addEventListener("track", (e) => {
  let videoElement = document.getElementById("video-box");
  videoElement.srcObject = e.streams[0];
});
```

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# dom-rtctrackevent](https://w3c.github.io/webrtc-pc/#dom-rtctrackevent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCTrackEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtctrackevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCTrackEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtctrackevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCTrackEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtctrackevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff71683f74da0078d9371c4d0c1ff9d3898fc7b59%0A*+Document+last+modified%3A+2025-09-19T15%3A38%3A24.000Z%0A%0A%3C%2Fdetails%3E)
