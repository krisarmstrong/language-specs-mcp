# RTCEncodedAudioFrame

 Baseline  2023 Newly available

 Since ⁨August 2023⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCEncodedAudioFrame&level=low)

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `RTCEncodedAudioFrame` of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) represents an encoded audio frame in the WebRTC receiver or sender pipeline, which may be modified using a [WebRTC Encoded Transform](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms).

The interface provides methods and properties to get metadata about the frame, allowing its format and order in the sequence of frames to be determined. The `data` property gives access to the encoded frame data as a buffer, which might be encrypted, or otherwise modified by a transform.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[RTCEncodedAudioFrame()](/en-US/docs/Web/API/RTCEncodedAudioFrame/RTCEncodedAudioFrame)

Copy constructor. Creates a new and independent `RTCEncodedAudioFrame` object from a frame, optionally overwriting some of the copied metadata.

## [Instance properties](#instance_properties)

[RTCEncodedAudioFrame.timestamp](/en-US/docs/Web/API/RTCEncodedAudioFrame/timestamp)Read onlyDeprecatedNon-standard

Returns the timestamp at which sampling of the frame started.

[RTCEncodedAudioFrame.data](/en-US/docs/Web/API/RTCEncodedAudioFrame/data)

Return a buffer containing the encoded frame data.

## [Instance methods](#instance_methods)

[RTCEncodedAudioFrame.getMetadata()](/en-US/docs/Web/API/RTCEncodedAudioFrame/getMetadata)

Returns the metadata associated with the frame.

## [Examples](#examples)

### [Transforming an encoded audio frame](#transforming_an_encoded_audio_frame)

This code snippet shows a handler for the `rtctransform` event in a [Worker](/en-US/docs/Web/API/Worker) that implements a [TransformStream](/en-US/docs/Web/API/TransformStream), and pipes encoded frames through it from the `event.transformer.readable` to `event.transformer.writable` (`event.transformer` is a [RTCRtpScriptTransformer](/en-US/docs/Web/API/RTCRtpScriptTransformer), the worker-side counterpart of [RTCRtpScriptTransform](/en-US/docs/Web/API/RTCRtpScriptTransform)).

If the transformer is inserted into an audio stream, the `transform()` method is called with a `RTCEncodedAudioFrame` whenever a new frame is enqueued on `event.transformer.readable`. The `transform()` method shows how this might be read, modified using a fictional encryption function, and then enqueued on the controller (this ultimately pipes it through to the `event.transformer.writable`, and then back into the WebRTC pipeline).

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

      // Encrypt frame bytes using the encryptFunction() method (not shown)
      for (let i = 0; i < encodedFrame.data.byteLength; ++i) {
        const encryptedByte = encryptFunction(~view.getInt8(i));
        newView.setInt8(i, encryptedByte);
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
[WebRTC Encoded Transform# rtcencodedaudioframe](https://w3c.github.io/webrtc-encoded-transform/#rtcencodedaudioframe)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using WebRTC Encoded Transforms](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms)
- [TransformStream](/en-US/docs/Web/API/TransformStream)
- [RTCRtpScriptTransformer](/en-US/docs/Web/API/RTCRtpScriptTransformer)
- [RTCEncodedVideoFrame](/en-US/docs/Web/API/RTCEncodedVideoFrame)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCEncodedAudioFrame/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcencodedaudioframe/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCEncodedAudioFrame&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcencodedaudioframe%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCEncodedAudioFrame%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcencodedaudioframe%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F23398d025295ad1eaf1663a26fbe738a8fe12883%0A*+Document+last+modified%3A+2025-10-23T23%3A16%3A42.000Z%0A%0A%3C%2Fdetails%3E)
