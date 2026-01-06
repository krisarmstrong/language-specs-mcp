# CanvasCaptureMediaStreamTrack

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCanvasCaptureMediaStreamTrack&level=not)

The `CanvasCaptureMediaStreamTrack` interface of the [Media Capture and Streams API](/en-US/docs/Web/API/Media_Capture_and_Streams_API) represents the video track contained in a [MediaStream](/en-US/docs/Web/API/MediaStream) being generated from a [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) following a call to [HTMLCanvasElement.captureStream()](/en-US/docs/Web/API/HTMLCanvasElement/captureStream).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface inherits the properties of its parent, [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack).

[CanvasCaptureMediaStreamTrack.canvas](/en-US/docs/Web/API/CanvasCaptureMediaStreamTrack/canvas)Read only

Returns the [HTMLCanvasElement](/en-US/docs/Web/API/HTMLCanvasElement) object whose surface is captured in real-time.

## [Instance methods](#instance_methods)

This interface inherits the methods of its parent, [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack).

[CanvasCaptureMediaStreamTrack.requestFrame()](/en-US/docs/Web/API/CanvasCaptureMediaStreamTrack/requestFrame)

Manually forces a frame to be captured and sent to the stream. This lets applications that wish to specify the frame capture times directly do so, if they specified a `frameRate` of 0 when calling [captureStream()](/en-US/docs/Web/API/HTMLCanvasElement/captureStream).

## [Specifications](#specifications)

Specification
[Media Capture from DOM Elements# the-canvascapturemediastreamtrack](https://w3c.github.io/mediacapture-fromelement/#the-canvascapturemediastreamtrack)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [HTMLCanvasElement.captureStream()](/en-US/docs/Web/API/HTMLCanvasElement/captureStream) to begin capturing frames from a canvas

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 16, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/CanvasCaptureMediaStreamTrack/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/canvascapturemediastreamtrack/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCanvasCaptureMediaStreamTrack&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcanvascapturemediastreamtrack%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCanvasCaptureMediaStreamTrack%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcanvascapturemediastreamtrack%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7fb6ccccf88b71712c1b603bed7092dbb622b698%0A*+Document+last+modified%3A+2023-12-16T12%3A31%3A32.000Z%0A%0A%3C%2Fdetails%3E)
