# MediaStream Image Capture API

The MediaStream Image Capture API is an API for capturing images or videos from a photographic device. In addition to capturing data, it also allows you to retrieve information about device capabilities such as image size, red-eye reduction and whether or not there is a flash and what they are currently set to. Conversely, the API allows the capabilities to be configured within the constraints what the device allows.

## In this article

- [MediaStream image capture concepts and usage](#mediastream_image_capture_concepts_and_usage)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [MediaStream image capture concepts and usage](#mediastream_image_capture_concepts_and_usage)

The process of retrieving an image or video stream happens as described below. The example code is adapted from [Chrome's Image Capture examples](https://googlechrome.github.io/samples/image-capture/).

First, get a reference to a device by calling [MediaDevices.getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia). The example below says give me whatever video device is available, though the `getUserMedia()` method allows more specific capabilities to be requested. This method returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a [MediaStream](/en-US/docs/Web/API/MediaStream) object.

js

```
navigator.mediaDevices.getUserMedia({ video: true }).then((mediaStream) => {
  // Do something with the stream.
});
```

Next, isolate the visual part of the media stream. Do this by calling [MediaStream.getVideoTracks()](/en-US/docs/Web/API/MediaStream/getVideoTracks). This returns an array of [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) objects. The code below assumes that the first item in the `MediaStreamTrack` array is the one to use. You can use the properties of the `MediaStreamTrack` objects to select the one you need.

js

```
const track = mediaStream.getVideoTracks()[0];
```

At this point, you might want to configure the device capabilities before capturing an image. You can do this by calling [applyConstraints()](/en-US/docs/Web/API/MediaStreamTrack/applyConstraints) on the track object before doing anything else.

js

```
let zoom = document.querySelector("#zoom");
const capabilities = track.getCapabilities();
// Check whether zoom is supported or not.
if (!capabilities.zoom) {
  return;
}
track.applyConstraints({ advanced: [{ zoom: zoom.value }] });
```

Finally, pass the `MediaStreamTrack` object to the [ImageCapture()](/en-US/docs/Web/API/ImageCapture/ImageCapture) constructor. Though a `MediaStream` holds several types of tracks and provides multiple methods for retrieving them, the ImageCapture constructor will throw a [DOMException](/en-US/docs/Web/API/DOMException) of type `NotSupportedError` if [MediaStreamTrack.kind](/en-US/docs/Web/API/MediaStreamTrack/kind) is not `"video"`.

js

```
let imageCapture = new ImageCapture(track);
```

## [Interfaces](#interfaces)

[ImageCapture](/en-US/docs/Web/API/ImageCapture)

An interface for capturing images from a photographic device referenced through a valid [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack).

## [Specifications](#specifications)

Specification
[MediaStream Image Capture# imagecaptureapi](https://w3c.github.io/mediacapture-image/#imagecaptureapi)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [MediaStream](/en-US/docs/Web/API/MediaStream)
- [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 26, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MediaStream_Image_Capture_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediastream_image_capture_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStream_Image_Capture_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediastream_image_capture_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStream_Image_Capture_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediastream_image_capture_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F624bbdcb7d9beace299a4fa0d3ddcd8f6732cd90%0A*+Document+last+modified%3A+2025-02-26T01%3A29%3A35.000Z%0A%0A%3C%2Fdetails%3E)
