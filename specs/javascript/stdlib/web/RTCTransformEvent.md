# RTCTransformEvent

 Baseline  2025 Newly available

 Since ⁨October 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCTransformEvent&level=low)

The `RTCTransformEvent` of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) represent an event that is fired in a dedicated worker when an encoded frame has been queued for processing by a [WebRTC Encoded Transform](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms).

The interface has a [transformer](/en-US/docs/Web/API/RTCTransformEvent/transformer) property that exposes a readable stream and a writable stream. A worker should read encoded frames from `transformer.readable`, modify them as needed, and write them to `transformer.writable` in the same order and without any duplication.

At time of writing there is just one event based on `RTCTransformEvent`: [rtctransform](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/rtctransform_event).

## In this article

- [Instance properties](#instance_properties)
- [Transform event types](#transform_event_types)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

Since `RTCTransformEvent` is based on [Event](/en-US/docs/Web/API/Event), its properties are also available.

[RTCTransformEvent.transformer](/en-US/docs/Web/API/RTCTransformEvent/transformer)Read only

Returns the [RTCRtpScriptTransformer](/en-US/docs/Web/API/RTCRtpScriptTransformer) associated with the event.

## [Transform event types](#transform_event_types)

There is only one type of transform event.

### [rtctransform](#rtctransform)

The [rtctransform](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/rtctransform_event) event is fired at the worker global scope on construction of an associated [RTCRtpScriptTransform](/en-US/docs/Web/API/RTCRtpScriptTransform), and whenever a new encoded video or audio frame is enqueued for processing.

You can add a `rtctransform` event listener to be notified when the new frame is available using either [DedicatedWorkerGlobalScope.addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or the `onrtctransform` event handler property.

## [Example](#example)

This example creates an event listener for the [rtctransform](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/rtctransform_event) event.

The example assumes we have a [TransformStream](/en-US/docs/Web/API/TransformStream) with an `options` object passed from a [RTCRtpScriptTransform](/en-US/docs/Web/API/RTCRtpScriptTransform) constructor in the main-thread. The code at the end shows how the stream is piped through the transform stream from the `readable` to the `writable`.

js

```
addEventListener("rtctransform", (event) => {
  let transform;
  // Select a transform based on passed options
  if (event.transformer.options.name === "senderTransform") {
    transform = createSenderTransform(); // A TransformStream (not shown)
  } else if (event.transformer.options.name === "receiverTransform") {
    transform = createReceiverTransform(); // A TransformStream (not shown)
  }
  // Pipe frames from the readable to writeable through TransformStream
  event.transformer.readable
    .pipeThrough(transform)
    .pipeTo(event.transformer.writable);
});
```

Note that this code is part of a more complete example provided in [Using WebRTC Encoded Transforms](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms).

## [Specifications](#specifications)

Specification
[WebRTC Encoded Transform# rtctransformevent](https://w3c.github.io/webrtc-encoded-transform/#rtctransformevent)

## [Browser compatibility](#browser_compatibility)

- [Using WebRTC Encoded Transforms](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms)
- [TransformStream](/en-US/docs/Web/API/TransformStream)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCTransformEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtctransformevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCTransformEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtctransformevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCTransformEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtctransformevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fffa6f5871f50856c60983a125cef7de267be7aeb%0A*+Document+last+modified%3A+2025-05-27T12%3A53%3A43.000Z%0A%0A%3C%2Fdetails%3E)
