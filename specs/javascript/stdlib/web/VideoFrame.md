# VideoFrame

 Baseline  2024  * Newly available

 Since ⁨September 2024⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoFrame&level=low)

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `VideoFrame` interface of the [Web Codecs API](/en-US/docs/Web/API/WebCodecs_API) represents a frame of a video.

`VideoFrame` is a [transferable object](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects).

## In this article

- [Description](#description)
- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Description](#description)

A `VideoFrame` object can be created or accessed in a number of ways. The [MediaStreamTrackProcessor](/en-US/docs/Web/API/MediaStreamTrackProcessor) breaks a media track into individual `VideoFrame` objects.

A `VideoFrame` is an image source and has a constructor that accepts any other canvas source ( an [SVGImageElement](/en-US/docs/Web/API/SVGImageElement), an [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement), an [HTMLCanvasElement](/en-US/docs/Web/API/HTMLCanvasElement), an [ImageBitmap](/en-US/docs/Web/API/ImageBitmap), an [OffscreenCanvas](/en-US/docs/Web/API/OffscreenCanvas), or another `VideoFrame`). This means that a frame can be created from an image or video element.

A second constructor enables the creation of a `VideoFrame` from its binary pixel representation in an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), a [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray), or a [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView).

Created frames may then turned into a media track, for example with the [MediaStreamTrackGenerator](/en-US/docs/Web/API/MediaStreamTrackGenerator) interface that creates a media track from a stream of frames.

## [Constructor](#constructor)

[VideoFrame()](/en-US/docs/Web/API/VideoFrame/VideoFrame)

Creates a new `VideoFrame` object.

## [Instance properties](#instance_properties)

[VideoFrame.format](/en-US/docs/Web/API/VideoFrame/format)Read only

Returns the pixel format of the `VideoFrame`.

[VideoFrame.codedWidth](/en-US/docs/Web/API/VideoFrame/codedWidth)Read only

Returns the width of the `VideoFrame` in pixels, potentially including non-visible padding, and prior to considering potential ratio adjustments.

[VideoFrame.codedHeight](/en-US/docs/Web/API/VideoFrame/codedHeight)Read only

Returns the height of the `VideoFrame` in pixels, potentially including non-visible padding, and prior to considering potential ratio adjustments.

[VideoFrame.codedRect](/en-US/docs/Web/API/VideoFrame/codedRect)Read only

Returns a [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly) with the width and height matching `codedWidth` and `codedHeight`.

[VideoFrame.visibleRect](/en-US/docs/Web/API/VideoFrame/visibleRect)Read only

Returns a [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly) describing the visible rectangle of pixels for this `VideoFrame`.

[VideoFrame.displayWidth](/en-US/docs/Web/API/VideoFrame/displayWidth)Read only

Returns the width of the `VideoFrame` when displayed after applying [aspect ratio](/en-US/docs/Glossary/Aspect_ratio) adjustments.

[VideoFrame.displayHeight](/en-US/docs/Web/API/VideoFrame/displayHeight)Read only

Returns the height of the `VideoFrame` when displayed after applying aspect ratio adjustments.

[VideoFrame.duration](/en-US/docs/Web/API/VideoFrame/duration)Read only

Returns an integer indicating the duration of the video in microseconds.

[VideoFrame.timestamp](/en-US/docs/Web/API/VideoFrame/timestamp)Read only

Returns an integer indicating the timestamp of the video in microseconds.

[VideoFrame.colorSpace](/en-US/docs/Web/API/VideoFrame/colorSpace)Read only

Returns a [VideoColorSpace](/en-US/docs/Web/API/VideoColorSpace) object.

[VideoFrame.flip](/en-US/docs/Web/API/VideoFrame/flip)Read onlyExperimental

Returns whether the `VideoFrame` is horizontally mirrored.

[VideoFrame.rotation](/en-US/docs/Web/API/VideoFrame/rotation)Read onlyExperimental

Returns the rotation (0, 90, 180, or 270) in degrees clockwise applied to the `VideoFrame`. Arbitrary numbers (including negatives) are rounded to the next quarter turn.

## [Instance methods](#instance_methods)

[VideoFrame.allocationSize()](/en-US/docs/Web/API/VideoFrame/allocationSize)

Returns the number of bytes required to hold the `VideoFrame` as filtered by options passed into the method.

[VideoFrame.copyTo()](/en-US/docs/Web/API/VideoFrame/copyTo)

Copies the contents of the `VideoFrame` to an `ArrayBuffer`.

[VideoFrame.clone()](/en-US/docs/Web/API/VideoFrame/clone)

Creates a new `VideoFrame` object with reference to the same media resource as the original.

[VideoFrame.close()](/en-US/docs/Web/API/VideoFrame/close)

Clears all states and releases the reference to the media resource.

## [Examples](#examples)

In the following example frames are returned from a [MediaStreamTrackProcessor](/en-US/docs/Web/API/MediaStreamTrackProcessor), then encoded. See the full example and read more about it in the article [Video processing with WebCodecs](https://developer.chrome.com/docs/web-platform/best-practices/webcodecs).

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

## [Specifications](#specifications)

Specification
[WebCodecs# videoframe-interface](https://w3c.github.io/webcodecs/#videoframe-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Video processing with WebCodecs](https://developer.chrome.com/docs/web-platform/best-practices/webcodecs)
- [WebCodecs examples](https://w3c.github.io/webcodecs/samples/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/VideoFrame/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/videoframe/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoFrame&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvideoframe%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoFrame%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvideoframe%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff336c5b6795a562c64fe859aa9ee2becf223ad8a%0A*+Document+last+modified%3A+2025-11-03T18%3A29%3A25.000Z%0A%0A%3C%2Fdetails%3E)
