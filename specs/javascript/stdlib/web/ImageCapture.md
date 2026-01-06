# ImageCapture

The `ImageCapture` interface of the [MediaStream Image Capture API](/en-US/docs/Web/API/MediaStream_Image_Capture_API) provides methods to enable the capture of images or photos from a camera or other photographic device. It provides an interface for capturing images from a photographic device referenced through a valid [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[ImageCapture()](/en-US/docs/Web/API/ImageCapture/ImageCapture)

Creates a new `ImageCapture` object which can be used to capture still frames (photos) from a given [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) which represents a video stream.

## [Instance properties](#instance_properties)

[ImageCapture.track](/en-US/docs/Web/API/ImageCapture/track)Read only

Returns a reference to the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) passed to the constructor.

## [Instance methods](#instance_methods)

[ImageCapture.takePhoto()](/en-US/docs/Web/API/ImageCapture/takePhoto)

Takes a single exposure using the video capture device sourcing a [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a [Blob](/en-US/docs/Web/API/Blob) containing the data.

[ImageCapture.getPhotoCapabilities()](/en-US/docs/Web/API/ImageCapture/getPhotoCapabilities)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with an object containing the ranges of available configuration options.

[ImageCapture.getPhotoSettings()](/en-US/docs/Web/API/ImageCapture/getPhotoSettings)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with an object containing the current photo configuration settings.

[ImageCapture.grabFrame()](/en-US/docs/Web/API/ImageCapture/grabFrame)

Takes a snapshot of the live video in a [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack), returning an [ImageBitmap](/en-US/docs/Web/API/ImageBitmap), if successful.

## [Example](#example)

The following code is taken from [Chrome's Grab Frame - Take Photo Sample](https://googlechrome.github.io/samples/image-capture/grab-frame-take-photo.html). Since `ImageCapture` requires some place to capture an image from, the example below starts with a device's media device (in other words a camera).

This example shows, roughly, a [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) extracted from a device's [MediaStream](/en-US/docs/Web/API/MediaStream). The track is then used to create an `ImageCapture` object so that `takePhoto()` and `grabFrame()` can be called. Finally, it shows how to apply the results of these calls to a canvas object.

js

```
let imageCapture;

function onGetUserMediaButtonClick() {
  navigator.mediaDevices
    .getUserMedia({ video: true })
    .then((mediaStream) => {
      document.querySelector("video").srcObject = mediaStream;

      const track = mediaStream.getVideoTracks()[0];
      imageCapture = new ImageCapture(track);
    })
    .catch((error) => console.error(error));
}

function onGrabFrameButtonClick() {
  imageCapture
    .grabFrame()
    .then((imageBitmap) => {
      const canvas = document.querySelector("#grabFrameCanvas");
      drawCanvas(canvas, imageBitmap);
    })
    .catch((error) => console.error(error));
}

function onTakePhotoButtonClick() {
  imageCapture
    .takePhoto()
    .then((blob) => createImageBitmap(blob))
    .then((imageBitmap) => {
      const canvas = document.querySelector("#takePhotoCanvas");
      drawCanvas(canvas, imageBitmap);
    })
    .catch((error) => console.error(error));
}

/* Utils */

function drawCanvas(canvas, img) {
  canvas.width = getComputedStyle(canvas).width.split("px")[0];
  canvas.height = getComputedStyle(canvas).height.split("px")[0];
  let ratio = Math.min(canvas.width / img.width, canvas.height / img.height);
  let x = (canvas.width - img.width * ratio) / 2;
  let y = (canvas.height - img.height * ratio) / 2;
  canvas.getContext("2d").clearRect(0, 0, canvas.width, canvas.height);
  canvas
    .getContext("2d")
    .drawImage(
      img,
      0,
      0,
      img.width,
      img.height,
      x,
      y,
      img.width * ratio,
      img.height * ratio,
    );
}

document.querySelector("video").addEventListener("play", () => {
  document.querySelector("#grabFrameButton").disabled = false;
  document.querySelector("#takePhotoButton").disabled = false;
});
```

## [Specifications](#specifications)

Specification
[MediaStream Image Capture# imagecaptureapi](https://w3c.github.io/mediacapture-image/#imagecaptureapi)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ImageCapture/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/imagecapture/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FImageCapture&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fimagecapture%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FImageCapture%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fimagecapture%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f226b6f08c5cff7f96b7cc49a164fdc43d11a0c%0A*+Document+last+modified%3A+2025-06-18T11%3A40%3A13.000Z%0A%0A%3C%2Fdetails%3E)
