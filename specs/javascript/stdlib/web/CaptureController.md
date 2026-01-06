# CaptureController

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCaptureController&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `CaptureController` interface provides methods that can be used to further manipulate a captured display surface (captured via [MediaDevices.getDisplayMedia()](/en-US/docs/Web/API/MediaDevices/getDisplayMedia))

A `CaptureController` object is associated with a captured display surface by passing it into a `getDisplayMedia()` call as the value of the options object's `controller` property.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[CaptureController()](/en-US/docs/Web/API/CaptureController/CaptureController)Experimental

Creates a new `CaptureController` object instance.

## [Instance properties](#instance_properties)

[zoomLevel](/en-US/docs/Web/API/CaptureController/zoomLevel)Experimental

The captured display surface's current zoom level.

## [Instance methods](#instance_methods)

[decreaseZoomLevel()](/en-US/docs/Web/API/CaptureController/decreaseZoomLevel)Experimental

Decreases the captured display surface's zoom level by one increment.

[forwardWheel()](/en-US/docs/Web/API/CaptureController/forwardWheel)Experimental

Starts forwarding [wheel](/en-US/docs/Web/API/Element/wheel_event) events fired on the referenced element to the viewport of an associated captured display surface.

[getSupportedZoomLevels()](/en-US/docs/Web/API/CaptureController/getSupportedZoomLevels)Experimental

Returns the different zoom levels supported by the captured display surface.

[increaseZoomLevel()](/en-US/docs/Web/API/CaptureController/increaseZoomLevel)Experimental

Increases the captured display surface's zoom level by one increment.

[resetZoomLevel()](/en-US/docs/Web/API/CaptureController/resetZoomLevel)Experimental

Resets the captured display surface's zoom to its initial level, which is `100`.

[setFocusBehavior()](/en-US/docs/Web/API/CaptureController/setFocusBehavior)Experimental

Controls whether the captured tab or window will be focused or whether the focus will remain with the tab containing the capturing app.

## [Events](#events)

[zoomlevelchange](/en-US/docs/Web/API/CaptureController/zoomlevelchange_event)Experimental

Fires when the captured display surface's zoom level changes.

## [Examples](#examples)

js

```
// Create a new CaptureController instance
const controller = new CaptureController();

// Prompt the user to share a tab, window, or screen.
const stream = await navigator.mediaDevices.getDisplayMedia({ controller });

// Query the displaySurface value of the captured video track
const [track] = stream.getVideoTracks();
const displaySurface = track.getSettings().displaySurface;

if (displaySurface === "browser") {
  // Focus the captured tab.
  controller.setFocusBehavior("focus-captured-surface");
} else if (displaySurface === "window") {
  // Do not move focus to the captured window.
  // Keep the capturing page focused.
  controller.setFocusBehavior("no-focus-change");
}
```

## [Specifications](#specifications)

Specification
[Screen Capture# dom-capturecontroller](https://w3c.github.io/mediacapture-screen-share/#dom-capturecontroller)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Screen Capture API](/en-US/docs/Web/API/Screen_Capture_API)
- [MediaDevices.getDisplayMedia()](/en-US/docs/Web/API/MediaDevices/getDisplayMedia)
- [Using the Element Capture and Region Capture APIs](/en-US/docs/Web/API/Screen_Capture_API/Element_Region_Capture)
- [Using the Captured Surface Control API](/en-US/docs/Web/API/Screen_Capture_API/Captured_Surface_Control)
- [Better screen sharing with Conditional Focus](https://developer.chrome.com/docs/web-platform/conditional-focus/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 14, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CaptureController/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/capturecontroller/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCaptureController&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcapturecontroller%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCaptureController%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcapturecontroller%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F83a92f1eaf27dabf71beec6c548afb03171aa194%0A*+Document+last+modified%3A+2025-07-14T12%3A34%3A28.000Z%0A%0A%3C%2Fdetails%3E)
