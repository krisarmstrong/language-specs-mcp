# MediaStreamTrackProcessor

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamTrackProcessor&level=not)

Note: This feature is only available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

Warning: Browsers differ on which global context they expose this interface in (e.g., only window in some browsers and only dedicated worker in others), making them incompatible. Keep this in mind when comparing support.

The `MediaStreamTrackProcessor` interface of the [Insertable Streams for MediaStreamTrack API](/en-US/docs/Web/API/Insertable_Streams_for_MediaStreamTrack_API) consumes a video [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) object's source and generates a stream of [VideoFrame](/en-US/docs/Web/API/VideoFrame) objects.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[MediaStreamTrackProcessor()](/en-US/docs/Web/API/MediaStreamTrackProcessor/MediaStreamTrackProcessor)

Creates a new `MediaStreamTrackProcessor` object.

[window.MediaStreamTrackProcessor()](/en-US/docs/Web/API/MediaStreamTrackProcessor/MediaStreamTrackProcessor)ExperimentalNon-standard

Creates a new `MediaStreamTrackProcessor` object on the [main thread](/en-US/docs/Glossary/Main_thread) that can process both video and audio.

## [Instance properties](#instance_properties)

[MediaStreamTrackProcessor.readable](/en-US/docs/Web/API/MediaStreamTrackProcessor/readable)

Returns a [ReadableStream](/en-US/docs/Web/API/ReadableStream).

## [Examples](#examples)

The following example is from the article [Unbundling MediaStreamTrackProcessor and VideoTrackGenerator](https://blog.mozilla.org/webrtc/unbundling-mediastreamtrackprocessor-and-videotrackgenerator/). It [transfers](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects) a camera [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) to a worker for processing. The worker creates a pipeline that applies a sepia tone filter to the video frames and mirrors them. The pipeline culminates in a [VideoTrackGenerator](/en-US/docs/Web/API/VideoTrackGenerator) whose [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) is transferred back and played. The media now flows in real time through the transform off the [main thread](/en-US/docs/Glossary/Main_thread).

js

```
const stream = await navigator.mediaDevices.getUserMedia({ video: true });
const [track] = stream.getVideoTracks();
const worker = new Worker("worker.js");
worker.postMessage({ track }, [track]);
const { data } = await new Promise((r) => {
  worker.onmessage = r;
});
video.srcObject = new MediaStream([data.track]);
```

worker.js:

js

```
onmessage = async ({ data: { track } }) => {
  const vtg = new VideoTrackGenerator();
  self.postMessage({ track: vtg.track }, [vtg.track]);
  const { readable } = new MediaStreamTrackProcessor({ track });
  await readable
    .pipeThrough(new TransformStream({ transform }))
    .pipeTo(vtg.writable);
};
```

## [Specifications](#specifications)

Specification
[MediaStreamTrack Insertable Media Processing using Streams# mediastreamtrackprocessor](https://w3c.github.io/mediacapture-transform/#mediastreamtrackprocessor)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [VideoTrackGenerator](/en-US/docs/Web/API/VideoTrackGenerator)
- [Insertable streams for MediaStreamTrack](https://developer.chrome.com/docs/capabilities/web-apis/mediastreamtrack-insertable-media-processing) on developer.chrome.com 

Note: This article was written before the API was restricted to workers and video. Beware its use of the non-standard version of `MediaStreamTrackProcessor` which blocks on the [main thread](/en-US/docs/Glossary/Main_thread).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MediaStreamTrackProcessor/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediastreamtrackprocessor/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamTrackProcessor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediastreamtrackprocessor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamTrackProcessor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediastreamtrackprocessor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff2dc3d5367203c860cf1a71ce0e972f018523849%0A*+Document+last+modified%3A+2025-05-23T13%3A53%3A05.000Z%0A%0A%3C%2Fdetails%3E)
