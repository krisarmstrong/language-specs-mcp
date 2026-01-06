# ImageDecoder

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FImageDecoder&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `ImageDecoder` interface of the [WebCodecs API](/en-US/docs/Web/API/WebCodecs_API) provides a way to unpack and decode encoded image data.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[ImageDecoder()](/en-US/docs/Web/API/ImageDecoder/ImageDecoder)

Creates a new `ImageDecoder` object.

## [Instance properties](#instance_properties)

[ImageDecoder.complete](/en-US/docs/Web/API/ImageDecoder/complete)Read only

Returns a boolean value indicating whether encoded data is completely buffered.

[ImageDecoder.completed](/en-US/docs/Web/API/ImageDecoder/completed)Read only

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves once `complete` is true.

[ImageDecoder.tracks](/en-US/docs/Web/API/ImageDecoder/tracks)Read only

Returns an [ImageTrackList](/en-US/docs/Web/API/ImageTrackList) object listing the available tracks and providing a method for selecting a track to decode.

[ImageDecoder.type](/en-US/docs/Web/API/ImageDecoder/type)Read only

Returns a string reflecting the [MIME type](/en-US/docs/Web/HTTP/Guides/MIME_types) configured during construction.

## [Static methods](#static_methods)

[ImageDecoder.isTypeSupported()](/en-US/docs/Web/API/ImageDecoder/isTypeSupported_static)

Indicates if the provided [MIME type](/en-US/docs/Web/HTTP/Guides/MIME_types) is supported for unpacking and decoding.

## [Instance methods](#instance_methods)

[ImageDecoder.close()](/en-US/docs/Web/API/ImageDecoder/close)

Ends all pending work and releases system resources.

[ImageDecoder.decode()](/en-US/docs/Web/API/ImageDecoder/decode)

Enqueues a control message to decode the frame of an image.

[ImageDecoder.reset()](/en-US/docs/Web/API/ImageDecoder/reset)

Aborts all pending `decode()` operations.

## [Examples](#examples)

Given a [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element:

html

```
<canvas></canvas>
```

the following code decodes and renders an animated image to that canvas:

js

```
let imageDecoder = null;
let imageIndex = 0;

function renderImage(result) {
  const canvas = document.querySelector("canvas");
  const canvasContext = canvas.getContext("2d");

  canvasContext.drawImage(result.image, 0, 0);

  const track = imageDecoder.tracks.selectedTrack;

  // We check complete here since `frameCount` won't be stable until all
  // data has been received. This may cause us to receive a RangeError
  // during the decode() call below which needs to be handled.
  if (imageDecoder.complete) {
    if (track.frameCount === 1) return;

    if (imageIndex + 1 >= track.frameCount) imageIndex = 0;
  }

  // Decode the next frame ahead of display so it's ready in time.
  imageDecoder
    .decode({ frameIndex: ++imageIndex })
    .then((nextResult) =>
      setTimeout(() => {
        renderImage(nextResult);
      }, result.image.duration / 1000.0),
    )
    .catch((e) => {
      // We can end up requesting an imageIndex past the end since
      // we're using a ReadableStream from fetch(), when this happens
      // just wrap around.
      if (e instanceof RangeError) {
        imageIndex = 0;
        imageDecoder.decode({ frameIndex: imageIndex }).then(renderImage);
      } else {
        throw e;
      }
    });
}

function decodeImage(imageByteStream) {
  imageDecoder = new ImageDecoder({ data: imageByteStream, type: "image/gif" });
  imageDecoder.decode({ frameIndex: imageIndex }).then(renderImage);
}

fetch("fancy.gif").then((response) => decodeImage(response.body));
```

## [Specifications](#specifications)

Specification
[WebCodecs# imagedecoder-interface](https://w3c.github.io/webcodecs/#imagedecoder-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ImageDecoder/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/imagedecoder/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FImageDecoder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fimagedecoder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FImageDecoder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fimagedecoder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d929bb0a021c7130d5a71a4bf505bcb8070378d%0A*+Document+last+modified%3A+2025-03-13T12%3A48%3A23.000Z%0A%0A%3C%2Fdetails%3E)
