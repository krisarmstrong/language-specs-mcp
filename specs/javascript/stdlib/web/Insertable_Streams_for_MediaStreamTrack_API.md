# Insertable Streams for MediaStreamTrack API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInsertable_Streams_for_MediaStreamTrack_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is only available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The Insertable Streams for MediaStreamTrack API provides a way to process the video frames of a [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) as they are consumed.

## In this article

- [Concepts and Usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Concepts and Usage](#concepts_and_usage)

When processing real-time video, you sometimes want to insert visual elements or otherwise process the stream of video frames. For example, an application might include two tracks that need to be combined, such as a weather map and video of a presenter explaining the map. Or, you may want to do processing on a track to blur backgrounds, or introduce other elements (such as adding funny hats to people, and so on). The APIs described here provide direct access to the video stream, allowing you to manipulate it in real time.

To ensure optimal performance, the APIs are only available in [dedicated workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope) (unless otherwise stated).

## [Interfaces](#interfaces)

[MediaStreamTrackProcessor](/en-US/docs/Web/API/MediaStreamTrackProcessor)Experimental

Consumes a [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) object's source and produces a stream of video frames.

[VideoTrackGenerator](/en-US/docs/Web/API/VideoTrackGenerator)Experimental

Creates a [WritableStream](/en-US/docs/Web/API/WritableStream) that acts as a [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) video source.

[MediaStreamTrackGenerator](/en-US/docs/Web/API/MediaStreamTrackGenerator)ExperimentalNon-standard

Creates a [WritableStream](/en-US/docs/Web/API/WritableStream) that acts as a [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) source for either video or audio. Only available on the [main thread](/en-US/docs/Glossary/Main_thread).

## [Examples](#examples)

The following example is from the article [Unbundling MediaStreamTrackProcessor and VideoTrackGenerator](https://blog.mozilla.org/webrtc/unbundling-mediastreamtrackprocessor-and-videotrackgenerator/). It [transfers](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects) a camera [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) to a worker for processing. The worker creates a pipeline that applies a sepia tone filter to the video frames and mirrors them. The pipeline culminates in a [VideoTrackGenerator](/en-US/docs/Web/API/VideoTrackGenerator) whose [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) is transferred back and played. The media now flows in real time through the transform off the [main thread](/en-US/docs/Glossary/Main_thread).

js

```
const stream = await navigator.mediaDevices.getUserMedia({ video: true });
const [track] = stream.getVideoTracks();
const worker = new Worker("worker.js");
worker.postMessage({ track }, [track]);
const { data } = await new Promise((r) => (worker.onmessage = r));
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

Specification[MediaStreamTrack Insertable Media Processing using Streams](https://w3c.github.io/mediacapture-transform/)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 14, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Insertable_Streams_for_MediaStreamTrack_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/insertable_streams_for_mediastreamtrack_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInsertable_Streams_for_MediaStreamTrack_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Finsertable_streams_for_mediastreamtrack_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInsertable_Streams_for_MediaStreamTrack_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Finsertable_streams_for_mediastreamtrack_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0d0ccc861fa024fa10836fbf0cc2c3813cd74745%0A*+Document+last+modified%3A+2025-07-14T15%3A01%3A33.000Z%0A%0A%3C%2Fdetails%3E)
