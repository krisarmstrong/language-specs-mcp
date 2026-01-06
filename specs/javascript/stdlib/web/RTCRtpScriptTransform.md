# RTCRtpScriptTransform

 Baseline  2025 Newly available

 Since ⁨October 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpScriptTransform&level=low)

The `RTCRtpScriptTransform` interface of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) is used to insert a [WebRTC Encoded Transform](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms) (a [TransformStream](/en-US/docs/Web/API/TransformStream) running in a worker thread) into the WebRTC sender and receiver pipelines.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Description](#description)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[RTCRtpScriptTransform()](/en-US/docs/Web/API/RTCRtpScriptTransform/RTCRtpScriptTransform)

Creates a new instance of the `RTCRtpScriptTransform` object.

## [Instance properties](#instance_properties)

None.

## [Instance methods](#instance_methods)

None.

## [Description](#description)

`RTCRtpScriptTransform` instances are constructed with a [Worker](/en-US/docs/Web/API/Worker), in which the transform stream code will run, along with an (optional) `options` object and array of [transferrable object](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects) that will be passed to the worker. They are then added into incoming and outgoing RTC pipelines by assigning them to [RTCRtpReceiver.transform](/en-US/docs/Web/API/RTCRtpReceiver/transform) and [RTCRtpSender.transform](/en-US/docs/Web/API/RTCRtpSender/transform), respectively.

On construction of this object, and whenever an encoded frame arrives, the [rtctransform](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/rtctransform_event) event is fired on the worker global object. The event's `transformer` property is a [RTCRtpScriptTransformer](/en-US/docs/Web/API/RTCRtpScriptTransformer), the worker-side counterpart to the main-thread `RTCRtpScriptTransform`. This has `readable` ([ReadableStream](/en-US/docs/Web/API/ReadableStream)) and `writable` ([WritableStream](/en-US/docs/Web/API/WritableStream)) properties that have been shared from the main thread `RTCRtpScriptTransform` — where they are not public. If the corresponding `RTCRtpScriptTransform` is used with an `RTCRtpReceiver`, then the `readable` queues incoming encoded audio or video frames from the packetizer. If it is used with `RTCRtpSender` then `readable` contains frames coming from a codec.

The worker thread [rtctransform](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/rtctransform_event) event handler defines a [pipe chain](/en-US/docs/Web/API/Streams_API/Concepts#pipe_chains). This pipes encoded frames from `event.transformer.readable`, through a [TransformStream](/en-US/docs/Web/API/TransformStream) which defines the transformation function, through to `event.transformer.writable`. The `event.transformer` also has the `options` object passed from the `RTCRtpScriptTransform` constructor (if defined) that can be used to determine the source of the event, and hence the specific [TransformStream](/en-US/docs/Web/API/TransformStream) to add to the chain.

## [Examples](#examples)

Note that these examples show how `RTCRtpScriptTransform` is defined and used. Worker thread transform code is covered as part of the more complete example in [Using WebRTC Encoded Transforms](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms).

### [Adding a transform for outgoing frames](#adding_a_transform_for_outgoing_frames)

This example shows how you might stream video from a user's webcam over WebRTC, adding a WebRTC encoded transform to modify the outgoing streams. The code assumes that there is an [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection) called `peerConnection` that is already connected to a remote peer.

First we gets a [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack), using [getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia) to get a video [MediaStream](/en-US/docs/Web/API/MediaStream) from a media device, and then the [MediaStream.getTracks()](/en-US/docs/Web/API/MediaStream/getTracks) method to get the first [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) in the stream.

The track is added to the peer connection using [addTrack()](/en-US/docs/Web/API/RTCPeerConnection/addTrack) and sent. The `addTrack()` method returns the [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender) that is being used to send the track.

js

```
// Get Video stream and MediaTrack
const stream = await navigator.mediaDevices.getUserMedia({ video: true });
const [track] = stream.getTracks();
const videoSender = peerConnection.addTrack(track, stream);
```

An `RTCRtpScriptTransform` is then constructed taking a worker script, which defines the transform, and an optional object that can be used to pass arbitrary messages to the worker (in this case we've used a `name` property with value "senderTransform" to tell the worker that this transform will be added to the outbound stream). We then add the transform to the sender by assigning it to the [RTCRtpSender.transform](/en-US/docs/Web/API/RTCRtpSender/transform) property.

js

```
// Create a worker containing a TransformStream
const worker = new Worker("worker.js");
videoSender.transform = new RTCRtpScriptTransform(worker, {
  name: "senderTransform",
});
```

Note that you can add the transform at any time. However by adding it immediately after calling `addTrack()` the transform will get the first encoded frame that is sent.

### [Adding a transform for incoming frames](#adding_a_transform_for_incoming_frames)

This example shows how you add a WebRTC encoded transform to modify an incoming stream. The code assumes that there is an [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection) called `peerConnection` that is already connected to a remote peer.

First we add an `RTCPeerConnection`[track event](/en-US/docs/Web/API/RTCPeerConnection/track_event) handler to catch the event when a new track is streamed. Within the handler we construct an `RTCRtpScriptTransform` and add it to `event.receiver.transform` (`event.receiver` is a [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver)). As in the previous example, the constructor takes an object with `name` property: but here we use `receiverTransform` as the value to tell the worker that frames are incoming from the packetizer.

js

```
peerConnection.ontrack = (event) => {
  const worker = new Worker("worker.js");
  event.receiver.transform = new RTCRtpScriptTransform(worker, {
    name: "receiverTransform",
  });
  receivedVideo.srcObject = event.streams[0];
};
```

Note again that you can add the transform stream at any time. However by adding it in the `track` event handler ensures that the transform stream will get the first encoded frame for the track.

## [Specifications](#specifications)

Specification
[WebRTC Encoded Transform# rtcrtpscripttransform](https://w3c.github.io/webrtc-encoded-transform/#rtcrtpscripttransform)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using WebRTC Encoded Transforms](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms)
- [TransformStream](/en-US/docs/Web/API/TransformStream)
- [RTCRtpScriptTransformer](/en-US/docs/Web/API/RTCRtpScriptTransformer)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCRtpScriptTransform/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcrtpscripttransform/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpScriptTransform&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcrtpscripttransform%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpScriptTransform%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcrtpscripttransform%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff336c5b6795a562c64fe859aa9ee2becf223ad8a%0A*+Document+last+modified%3A+2025-11-03T18%3A29%3A25.000Z%0A%0A%3C%2Fdetails%3E)
