# MediaStreamTrackGenerator

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

Note: Consider using [VideoTrackGenerator](/en-US/docs/Web/API/VideoTrackGenerator) instead.

The `MediaStreamTrackGenerator` interface of the [Insertable Streams for MediaStreamTrack API](/en-US/docs/Web/API/Insertable_Streams_for_MediaStreamTrack_API) creates a [WritableStream](/en-US/docs/Web/API/WritableStream) that acts as a [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) source. The object consumes a stream of media frames as input, which can be audio or video frames.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [See also](#see_also)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[MediaStreamTrackGenerator()](/en-US/docs/Web/API/MediaStreamTrackGenerator/MediaStreamTrackGenerator)ExperimentalNon-standard

Creates a new `MediaStreamTrackGenerator` object which accepts either [VideoFrame](/en-US/docs/Web/API/VideoFrame) or [AudioData](/en-US/docs/Web/API/AudioData) objects.

## [Instance properties](#instance_properties)

This interface also inherits properties from [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack).

[MediaStreamTrackGenerator.writable](/en-US/docs/Web/API/MediaStreamTrackGenerator/writable)ExperimentalNon-standard

A [WritableStream](/en-US/docs/Web/API/WritableStream).

## [Instance methods](#instance_methods)

This interface doesn't implement any specific methods, but inherits methods from [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack).

## [Examples](#examples)

The following example is from the article [Insertable streams for MediaStreamTrack](https://developer.chrome.com/docs/capabilities/web-apis/mediastreamtrack-insertable-media-processing), and demonstrates a barcode scanner application, which process barcodes and highlights them before writing the transformed frames to the writable stream of [MediaStreamTrackGenerator.writable](/en-US/docs/Web/API/MediaStreamTrackGenerator/writable).

js

```
const stream = await getUserMedia({ video: true });
const videoTrack = stream.getVideoTracks()[0];

const trackProcessor = new MediaStreamTrackProcessor({ track: videoTrack });
const trackGenerator = new MediaStreamTrackGenerator({ kind: "video" });

const transformer = new TransformStream({
  async transform(videoFrame, controller) {
    const barcodes = await detectBarcodes(videoFrame);
    const newFrame = highlightBarcodes(videoFrame, barcodes);
    videoFrame.close();
    controller.enqueue(newFrame);
  },
});

trackProcessor.readable
  .pipeThrough(transformer)
  .pipeTo(trackGenerator.writable);
```

## [See also](#see_also)

- [VideoTrackGenerator](/en-US/docs/Web/API/VideoTrackGenerator)

## [Specifications](#specifications)

This feature does not appear to be defined in any specification.

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MediaStreamTrackGenerator/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediastreamtrackgenerator/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamTrackGenerator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediastreamtrackgenerator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamTrackGenerator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediastreamtrackgenerator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F62e6088450ab10db4697d190dd54d09dd9a0791a%0A*+Document+last+modified%3A+2025-04-17T07%3A43%3A40.000Z%0A%0A%3C%2Fdetails%3E)
