# WebCodecs API

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The WebCodecs API gives web developers low-level access to the individual frames of a video stream and chunks of audio. It is useful for web applications that require full control over the way media is processed. For example, video or audio editors, and video conferencing.

## In this article

- [Concepts and Usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [See also](#see_also)

## [Concepts and Usage](#concepts_and_usage)

Many Web APIs use media codecs internally. For example, the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API), and the [WebRTC API](/en-US/docs/Web/API/WebRTC_API). However these APIs do not allow developers to work with individual frames of a video stream and unmixed chunks of encoded audio or video.

Web developers have typically used WebAssembly in order to get around this limitation, and to work with media codecs in the browser. However, this requires additional bandwidth to download codecs that already exist in the browser, reducing performance and power efficiency, and adding additional development overhead.

The WebCodecs API provides access to codecs that are already in the browser. It gives access to raw video frames, chunks of audio data, image decoders, audio and video encoders and decoders.

### [Processing Model](#processing_model)

The WebCodecs API uses an asynchronous [processing model](https://w3c.github.io/webcodecs/#codec-processing-model-section). Each instance of an encoder or decoder maintains an internal, independent processing queue. When queueing a substantial amount of work, it's important to keep this model in mind.

Methods named `configure()`, `encode()`, `decode()`, and `flush()` operate asynchronously by appending control messages to the end the queue, while methods named `reset()` and `close()` synchronously abort all pending work and purge the processing queue. After `reset()`, more work may be queued following a call to `configure()`, but `close()` is a permanent operation.

Methods named `flush()` can be used to wait for the completion of all work that was pending at the time `flush()` was called. However, it should generally only be called once all desired work is queued. It is not intended to force progress at regular intervals. Calling it unnecessarily will affect encoder quality and cause decoders to require the next input to be a key frame.

### [Demuxing](#demuxing)

There is currently no API for demuxing media containers. Developers working with containerized media will need to implement their own or use third party libraries. E.g., [MP4Box.js](https://github.com/gpac/mp4box.js/) or [jswebm](https://github.com/jscodec/jswebm) can be used to demux audio and video data into [EncodedAudioChunk](/en-US/docs/Web/API/EncodedAudioChunk) and [EncodedVideoChunk](/en-US/docs/Web/API/EncodedVideoChunk) objects respectively.

## [Interfaces](#interfaces)

[AudioDecoder](/en-US/docs/Web/API/AudioDecoder)

Decodes [EncodedAudioChunk](/en-US/docs/Web/API/EncodedAudioChunk) objects.

[VideoDecoder](/en-US/docs/Web/API/VideoDecoder)

Decodes [EncodedVideoChunk](/en-US/docs/Web/API/EncodedVideoChunk) objects.

[AudioEncoder](/en-US/docs/Web/API/AudioEncoder)

Encodes [AudioData](/en-US/docs/Web/API/AudioData) objects.

[VideoEncoder](/en-US/docs/Web/API/VideoEncoder)

Encodes [VideoFrame](/en-US/docs/Web/API/VideoFrame) objects.

[EncodedAudioChunk](/en-US/docs/Web/API/EncodedAudioChunk)

Represents codec-specific encoded audio bytes.

[EncodedVideoChunk](/en-US/docs/Web/API/EncodedVideoChunk)

Represents codec-specific encoded video bytes.

[AudioData](/en-US/docs/Web/API/AudioData)

Represents unencoded audio data.

[VideoFrame](/en-US/docs/Web/API/VideoFrame)

Represents a frame of unencoded video data.

[VideoColorSpace](/en-US/docs/Web/API/VideoColorSpace)

Represents the color space of a video frame.

[ImageDecoder](/en-US/docs/Web/API/ImageDecoder)

Unpacks and decodes image data, giving access to the sequence of frames in an animated image.

[ImageTrackList](/en-US/docs/Web/API/ImageTrackList)

Represents the list of tracks available in the image.

[ImageTrack](/en-US/docs/Web/API/ImageTrack)

Represents an individual image track.

## [Examples](#examples)

In the following example, frames are returned from a [MediaStreamTrackProcessor](/en-US/docs/Web/API/MediaStreamTrackProcessor), then encoded. See the full example and read more about it in the article [Video processing with WebCodecs](https://developer.chrome.com/docs/web-platform/best-practices/webcodecs).

js

```
let frameCounter = 0;
const track = stream.getVideoTracks()[0];
const mediaProcessor = new MediaStreamTrackProcessor(track);
const reader = mediaProcessor.readable.getReader();
while (true) {
  const result = await reader.read();
  if (result.done) break;
  let frame = result.value;
  if (encoder.encodeQueueSize > 2) {
    // Too many frames in flight, encoder is overwhelmed
    // let's drop this frame.
    frame.close();
  } else {
    frameCounter++;
    const insertKeyframe = frameCounter % 150 === 0;
    encoder.encode(frame, { keyFrame: insertKeyframe });
    frame.close();
  }
}
```

## [See also](#see_also)

- [Video processing with WebCodecs](https://developer.chrome.com/docs/web-platform/best-practices/webcodecs)
- [WebCodecs API Samples](https://w3c.github.io/webcodecs/samples/)
- [Real-Time Video Processing with WebCodecs and Streams: Processing Pipelines](https://webrtchacks.com/real-time-video-processing-with-webcodecs-and-streams-processing-pipelines-part-1/)
- [Video Frame Processing on the Web – WebAssembly, WebGPU, WebGL, WebCodecs, WebNN, and WebTransport](https://webrtchacks.com/video-frame-processing-on-the-web-webassembly-webgpu-webgl-webcodecs-webnn-and-webtransport/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WebCodecs_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webcodecs_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebCodecs_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebcodecs_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebCodecs_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebcodecs_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff336c5b6795a562c64fe859aa9ee2becf223ad8a%0A*+Document+last+modified%3A+2025-11-03T18%3A29%3A25.000Z%0A%0A%3C%2Fdetails%3E)
