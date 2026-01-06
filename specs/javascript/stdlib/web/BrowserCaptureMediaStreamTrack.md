# BrowserCaptureMediaStreamTrack

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBrowserCaptureMediaStreamTrack&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `BrowserCaptureMediaStreamTrack` interface of the [Screen Capture API](/en-US/docs/Web/API/Screen_Capture_API) represents a single video track. It extends the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) class with methods to limit the part of a self-capture stream (for example, a user's screen or window) that is captured.

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[clone()](/en-US/docs/Web/API/BrowserCaptureMediaStreamTrack/clone)Experimental

Returns an uncropped, unrestricted clone of the original `BrowserCaptureMediaStreamTrack`.

[cropTo()](/en-US/docs/Web/API/BrowserCaptureMediaStreamTrack/cropTo)Experimental

Crops a self-capture stream to the area in which a specified DOM element is rendered.

[restrictTo()](/en-US/docs/Web/API/BrowserCaptureMediaStreamTrack/restrictTo)Experimental

Restricts a self-capture stream to a specific DOM element.

## [Examples](#examples)

See [Using the Element Capture and Region Capture APIs](/en-US/docs/Web/API/Screen_Capture_API/Element_Region_Capture) for in-context example code.

## [Specifications](#specifications)

Specification
[Region Capture# browser-capture-media-stream-track](https://w3c.github.io/mediacapture-region/#browser-capture-media-stream-track)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Screen Capture API](/en-US/docs/Web/API/Screen_Capture_API)
- [Using the Element Capture and Region Capture APIs](/en-US/docs/Web/API/Screen_Capture_API/Element_Region_Capture)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/BrowserCaptureMediaStreamTrack/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/browsercapturemediastreamtrack/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBrowserCaptureMediaStreamTrack&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbrowsercapturemediastreamtrack%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBrowserCaptureMediaStreamTrack%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbrowsercapturemediastreamtrack%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd9879ec9fe29b627ea1bde790d981dd13d602794%0A*+Document+last+modified%3A+2025-02-07T11%3A15%3A27.000Z%0A%0A%3C%2Fdetails%3E)
