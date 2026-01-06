# RTCRtpScriptTransformer

 Baseline  2025  * Newly available

 Since ⁨October 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpScriptTransformer&level=low)

The `RTCRtpScriptTransformer` interface of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) provides a worker-side [Stream API](/en-US/docs/Web/API/Streams_API) interface that a [WebRTC Encoded Transform](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms) can use to modify encoded media frames in the incoming and outgoing WebRTC pipelines.

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/Web_Workers_API#worker_types).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Description](#description)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[RTCRtpScriptTransformer.readable](/en-US/docs/Web/API/RTCRtpScriptTransformer/readable)Read only

A [ReadableStream](/en-US/docs/Web/API/ReadableStream) on which encoded frames from the WebRTC sender or receiver pipelines may be enqueued.

[RTCRtpScriptTransformer.writable](/en-US/docs/Web/API/RTCRtpScriptTransformer/writable)Read only

A [WritableStream](/en-US/docs/Web/API/WritableStream) that encoded frames should be piped to.

[RTCRtpScriptTransformer.options](/en-US/docs/Web/API/RTCRtpScriptTransformer/options)Read only

Options passed from the [RTCRtpScriptTransform constructor](/en-US/docs/Web/API/RTCRtpScriptTransform/RTCRtpScriptTransform), which are used to configure transform code based on whether incoming or outgoing frames are being processed.

## [Instance methods](#instance_methods)

[RTCRtpScriptTransformer.generateKeyFrame()](/en-US/docs/Web/API/RTCRtpScriptTransformer/generateKeyFrame)

Requests a video encoder generate a key frame. May be called by a transformer in the sender pipeline when processing outgoing frames.

[RTCRtpScriptTransformer.sendKeyFrameRequest()](/en-US/docs/Web/API/RTCRtpScriptTransformer/sendKeyFrameRequest)

Requests the sender send a key frame. May be called by a transformer in the receiver pipeline when processing incoming encoded video frames.

## [Description](#description)

A `RTCRtpScriptTransformer` instance is created as part of construction of an associated [RTCRtpScriptTransform](/en-US/docs/Web/API/RTCRtpScriptTransform), which specifies the worker in which the transformer is created and options that will be passed to it.

The transformer is made available to a worker through the [rtctransform](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/rtctransform_event) event `transformer` property. This event is fired on construction of the associated [RTCRtpScriptTransform](/en-US/docs/Web/API/RTCRtpScriptTransform) and when an encoded frame is enqueued on the [RTCRtpScriptTransformer.readable](/en-US/docs/Web/API/RTCRtpScriptTransformer/readable) from a codec (outgoing) or from the packetizer (incoming).

The transformer exposes a [readable](/en-US/docs/Web/API/RTCRtpScriptTransformer/readable) and [writable](/en-US/docs/Web/API/RTCRtpScriptTransformer/writable) stream into the worker, along with an [options](/en-US/docs/Web/API/RTCRtpScriptTransformer/options) object provided to the [RTCRtpScriptTransform](/en-US/docs/Web/API/RTCRtpScriptTransform) on construction. When the associated `RTCRtpScriptTransform` is assigned to a [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender) or [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver), encoded media frames from the WebRTC sender or receiver pipelines are enqueued on the `readable` stream.

A WebRTC Encoded Transform must read encoded frames from `transformer.readable`, modify them as needed, and write them to `transformer.writable` in the same order, and without any duplication. The [transformer.options](/en-US/docs/Web/API/RTCRtpScriptTransformer/options) allow an appropriate transform function to be used, based on whether the encoded media frames are incoming or outgoing. The transform is usually implemented by piping frames from the `readable` through one or more [TransformStream](/en-US/docs/Web/API/TransformStream) instances to the `writable`, transforming them as needed.

The interface also provides methods for a sender to generate get a video encoder to generate a new keyframe, or for a receiver to request a new key frame from the sender's encoder (video encoders commonly send a key frame containing the full information needed to construct an image, and subsequently send delta frames containing just the information that has changed since the previous frame).

These methods are required in cases where a recipient would be unable to decode incoming frames until they receive a new key frame. For example, a new recipient joining a conference call will not be able see video until they have received a new key frame, since delta frames can only be decoded if you have the last key frame and all subsequent delta frames. Similarly, if frames are encrypted for a recipient, they will only be able to decode frames once they have received their first encrypted key frame.

## [Examples](#examples)

This example shows the code for a WebRTC Encoded Transform running in a worker.

The code uses `addEventListener()` to register a handler function for the [rtctransform](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/rtctransform_event) event, which makes the `RTCRtpScriptTransformer` available as `event.transformer`.

The handler creates a [TransformStream](/en-US/docs/Web/API/TransformStream) and pipes frames from the `event.transformer.readable` through it to `event.transformer.writable`. The transform stream `transform()` implementation is called for each encoded frame queued on the stream: it can read the data from the frame and in this case negates the bytes and then enqueues the modifiable frame on the stream.

js

```
addEventListener("rtctransform", (event) => {
  const transform = new TransformStream({
    start() {}, // Called on startup.
    flush() {}, // Called when the stream is about to be closed.
    async transform(encodedFrame, controller) {
      // Reconstruct the original frame.
      const view = new DataView(encodedFrame.data);

      // Construct a new buffer
      const newData = new ArrayBuffer(encodedFrame.data.byteLength);
      const newView = new DataView(newData);

      // Negate all bits in the incoming frame
      for (let i = 0; i < encodedFrame.data.byteLength; ++i) {
        newView.setInt8(i, ~view.getInt8(i));
      }

      encodedFrame.data = newData;
      controller.enqueue(encodedFrame);
    },
  });
  event.transformer.readable
    .pipeThrough(transform)
    .pipeTo(event.transformer.writable);
});
```

The only special things to note about the [TransformStream](/en-US/docs/Web/API/TransformStream) above are that it queues encoded media frames ([RTCEncodedVideoFrame](/en-US/docs/Web/API/RTCEncodedVideoFrame) or [RTCEncodedAudioFrame](/en-US/docs/Web/API/RTCEncodedAudioFrame)) rather than arbitrary "chunks", and that `writableStrategy` and `readableStrategy` properties are not defined (because the queuing strategy is entirely managed by the user agent).

A transform can run in either the incoming or outgoing WebRTC pipelines. This doesn't matter in the code above, because the same algorithm might be used in the sender to negate the frames, and in the receiver to revert them. If the sender and receiver pipelines need to apply a different transform algorithm then information about the current pipeline must be passed from the main thread. This is done by setting an `options` argument in the corresponding [RTCRtpScriptTransform constructor](/en-US/docs/Web/API/RTCRtpScriptTransform/RTCRtpScriptTransform#options), which is then made available to the worker in [RTCRtpScriptTransformer.options](/en-US/docs/Web/API/RTCRtpScriptTransformer/options).

Below we use the `transformer.options` to choose either a sender transform or a receiver transform. Note that the properties of the object are arbitrary (provided the values can be serialized) and it is also possible to transfer a [MessageChannel](/en-US/docs/Web/API/MessageChannel) and use it to [communicate with a transform at runtime](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms#runtime_communication_with_the_transform) in order to, for example, share encryption keys.

js

```
// Code to instantiate transform and attach them to sender/receiver pipelines.
onrtctransform = (event) => {
  let transform;
  if (event.transformer.options.name === "senderTransform")
    transform = createSenderTransform();
  // returns a TransformStream (not shown)
  else if (event.transformer.options.name === "receiverTransform")
    transform = createReceiverTransform();
  // returns a TransformStream (not shown)
  else return;
  event.transformer.readable
    .pipeThrough(transform)
    .pipeTo(event.transformer.writable);
};
```

Note that the above code is part of more complete examples provided in [Using WebRTC Encoded Transforms](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms).

## [Specifications](#specifications)

Specification
[WebRTC Encoded Transform# rtcrtpscripttransformer](https://w3c.github.io/webrtc-encoded-transform/#rtcrtpscripttransformer)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using WebRTC Encoded Transforms](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms)
- [TransformStream](/en-US/docs/Web/API/TransformStream)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCRtpScriptTransformer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcrtpscripttransformer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpScriptTransformer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcrtpscripttransformer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpScriptTransformer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcrtpscripttransformer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fffa6f5871f50856c60983a125cef7de267be7aeb%0A*+Document+last+modified%3A+2025-05-27T12%3A53%3A43.000Z%0A%0A%3C%2Fdetails%3E)
