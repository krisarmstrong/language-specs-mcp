# RTCEncodedVideoFrame

 Baseline  2023 Newly available

 Since ⁨August 2023⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCEncodedVideoFrame&level=low)

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `RTCEncodedVideoFrame` of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) represents an encoded video frame in the WebRTC receiver or sender pipeline, which may be modified using a [WebRTC Encoded Transform](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms).

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

[RTCEncodedVideoFrame()](/en-US/docs/Web/API/RTCEncodedVideoFrame/RTCEncodedVideoFrame)

Copy constructor. Creates a new and independent `RTCEncodedVideoFrame` object from another frame, optionally overwriting some of the copied metadata.

## [Instance properties](#instance_properties)

[RTCEncodedVideoFrame.type](/en-US/docs/Web/API/RTCEncodedVideoFrame/type)Read only

Returns whether the current frame is a key frame, delta frame, or empty frame.

[RTCEncodedVideoFrame.timestamp](/en-US/docs/Web/API/RTCEncodedVideoFrame/timestamp)Read onlyDeprecatedNon-standard

Returns the timestamp at which sampling of the frame started.

[RTCEncodedVideoFrame.data](/en-US/docs/Web/API/RTCEncodedVideoFrame/data)

Return a buffer containing the encoded frame data.

## [Instance methods](#instance_methods)

[RTCEncodedVideoFrame.getMetadata()](/en-US/docs/Web/API/RTCEncodedVideoFrame/getMetadata)

Returns the metadata associated with the frame.

## [Description](#description)

Raw video data is generated as a sequence of frames, where each frame is a 2 dimensional array of pixel values. Video encoders transform this raw input into a compressed representation of the original for transmission and storage. A common approach is to send "key frames" that contain enough information to reproduce a whole image at a relatively low rate, and between key frames to send many much smaller "delta frames" that just encode the changes since the previous frame.

There are many different codecs, such as H.264, VP8, and VP9, each that have a different encoding processes and configuration, which offer different trade-offs between compression efficiency and video quality.

The `RTCEncodedVideoFrame` represents a single frame encoded with a particular video encoder. The [type](/en-US/docs/Web/API/RTCEncodedVideoFrame/type) property indicates whether the frame is a "key" or "delta" frame, and you can use the [getMetadata()](/en-US/docs/Web/API/RTCEncodedVideoFrame/getMetadata) method to get other details about the encoding method. The [data](/en-US/docs/Web/API/RTCEncodedVideoFrame/data) property provides access to the encoded image data for the frame, which can then be modified ("transformed") when frames are sent or received.

## [Examples](#examples)

### [Transforming an encoded video frame](#transforming_an_encoded_video_frame)

This code snippet shows a handler for the `rtctransform` event in a [Worker](/en-US/docs/Web/API/Worker) that implements a [TransformStream](/en-US/docs/Web/API/TransformStream), and pipes encoded frames through it from the `event.transformer.readable` to `event.transformer.writable` (`event.transformer` is a [RTCRtpScriptTransformer](/en-US/docs/Web/API/RTCRtpScriptTransformer), the worker-side counterpart of [RTCRtpScriptTransform](/en-US/docs/Web/API/RTCRtpScriptTransform)).

If the transformer is inserted into a video stream, the `transform()` method is called with a `RTCEncodedVideoFrame` whenever a new frame is enqueued on `event.transformer.readable`. The `transform()` method shows how this might be read, modified by inverting the bits, and then enqueued on the controller (this ultimately pipes it through to the `event.transformer.writable`, and then back into the WebRTC pipeline).

js

```
addEventListener("rtctransform", (event) => {
  const transform = new TransformStream({
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

Note that more complete examples are provided in [Using WebRTC Encoded Transforms](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms).

## [Specifications](#specifications)

Specification
[WebRTC Encoded Transform# rtcencodedvideoframe](https://w3c.github.io/webrtc-encoded-transform/#rtcencodedvideoframe)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using WebRTC Encoded Transforms](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms)
- [TransformStream](/en-US/docs/Web/API/TransformStream)
- [RTCRtpScriptTransformer](/en-US/docs/Web/API/RTCRtpScriptTransformer)
- [RTCEncodedAudioFrame](/en-US/docs/Web/API/RTCEncodedAudioFrame)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCEncodedVideoFrame/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcencodedvideoframe/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCEncodedVideoFrame&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcencodedvideoframe%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCEncodedVideoFrame%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcencodedvideoframe%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F23398d025295ad1eaf1663a26fbe738a8fe12883%0A*+Document+last+modified%3A+2025-10-23T23%3A16%3A42.000Z%0A%0A%3C%2Fdetails%3E)
