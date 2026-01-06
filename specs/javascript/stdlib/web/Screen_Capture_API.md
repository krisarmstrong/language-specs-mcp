# Screen Capture API

The Screen Capture API introduces additions to the existing Media Capture and Streams API to let the user select a screen or portion of a screen (such as a window) to capture as a media stream. This stream can then be recorded or shared with others over the network.

## In this article

- [Screen Capture API concepts and usage](#screen_capture_api_concepts_and_usage)
- [Interfaces](#interfaces)
- [Additions to the MediaDevices interface](#additions_to_the_mediadevices_interface)
- [Additions to existing dictionaries](#additions_to_existing_dictionaries)
- [Security considerations](#security_considerations)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Screen Capture API concepts and usage](#screen_capture_api_concepts_and_usage)

The Screen Capture API is relatively simple to use. Its main method is [MediaDevices.getDisplayMedia()](/en-US/docs/Web/API/MediaDevices/getDisplayMedia), whose job is to ask the user to select a screen or portion of a screen to capture in the form of a [MediaStream](/en-US/docs/Web/API/MediaStream).

To start capturing video from the screen, you call `getDisplayMedia()` on `navigator.mediaDevices`:

js

```
captureStream =
  await navigator.mediaDevices.getDisplayMedia(displayMediaOptions);
```

The [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) returned by `getDisplayMedia()` resolves to a [MediaStream](/en-US/docs/Web/API/MediaStream) which streams the captured display surface.

See the article [Using the Screen Capture API](/en-US/docs/Web/API/Screen_Capture_API/Using_Screen_Capture) for a more in-depth look at how to use the API to capture screen contents as a stream.

### [Screen capture extensions](#screen_capture_extensions)

The Screen Capture API has additional features that extend its capabilities:

#### Limiting the screen area captured in the stream

- The Element Capture API restricts the captured region to a specified rendered DOM element and its descendants.
- The Region Capture API crops the captured region to the area of the screen in which a specified DOM element is rendered.

See [Using the Element Capture and Region Capture APIs](/en-US/docs/Web/API/Screen_Capture_API/Element_Region_Capture) to learn more.

#### Controlling the captured screen area

The Captured Surface Control API allows the capturing application to provide limited control over the captured display surface, for example zooming and scrolling its contents.

See [Using the Captured Surface Control API](/en-US/docs/Web/API/Screen_Capture_API/Captured_Surface_Control) to learn more.

## [Interfaces](#interfaces)

[BrowserCaptureMediaStreamTrack](/en-US/docs/Web/API/BrowserCaptureMediaStreamTrack)

Represents a single video track; extends the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) class with methods to limit the part of a self-capture stream (for example, a user's screen or window) that is captured.

[CaptureController](/en-US/docs/Web/API/CaptureController)

Provides methods that can be used to further manipulate a captured display surface (captured via [MediaDevices.getDisplayMedia()](/en-US/docs/Web/API/MediaDevices/getDisplayMedia)). A `CaptureController` object is associated with a captured display surface by passing it into a `getDisplayMedia()` call as the value of the options object's `controller` property.

[CropTarget](/en-US/docs/Web/API/CropTarget)

Provides a static method, [fromElement()](/en-US/docs/Web/API/CropTarget/fromElement_static), which returns a [CropTarget](/en-US/docs/Web/API/CropTarget) instance that can be used to crop a captured video track to the area in which a specified element is rendered.

[RestrictionTarget](/en-US/docs/Web/API/RestrictionTarget)

Provides a static method, [fromElement()](/en-US/docs/Web/API/RestrictionTarget/fromElement_static), which returns a [RestrictionTarget](/en-US/docs/Web/API/RestrictionTarget) instance that can be used to restrict a captured video track to a specified DOM element.

## [Additions to the MediaDevices interface](#additions_to_the_mediadevices_interface)

[MediaDevices.getDisplayMedia()](/en-US/docs/Web/API/MediaDevices/getDisplayMedia)

The `getDisplayMedia()` method is added to the `MediaDevices` interface. Similar to [getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia), this method creates a promise that resolves with a [MediaStream](/en-US/docs/Web/API/MediaStream) containing the display area selected by the user, in a format that matches the specified options.

## [Additions to existing dictionaries](#additions_to_existing_dictionaries)

The Screen Capture API adds properties to the following dictionaries defined by other specifications.

### [MediaTrackConstraints](#mediatrackconstraints)

[MediaTrackConstraints.displaySurface](/en-US/docs/Web/API/MediaTrackConstraints/displaySurface)

A [ConstrainDOMString](/en-US/docs/Web/API/MediaTrackConstraints#constraindomstring) indicating what type of display surface is to be captured. The value is one of `browser`, `monitor`, or `window`.

[MediaTrackConstraints.logicalSurface](/en-US/docs/Web/API/MediaTrackConstraints/logicalSurface)

Indicates whether or not the video in the stream represents a logical display surface (that is, one which may not be entirely visible onscreen, or may be completely offscreen). A value of `true` indicates a logical display surface is to be captured.

[MediaTrackConstraints.suppressLocalAudioPlayback](/en-US/docs/Web/API/MediaTrackConstraints/suppressLocalAudioPlayback)

Controls whether the audio playing in a tab will continue to be played out of a user's local speakers when the tab is captured, or whether it will be suppressed. A value of `true` indicates that it will be suppressed.

### [MediaTrackSettings](#mediatracksettings)

[MediaTrackSettings.cursor](/en-US/docs/Web/API/MediaTrackSettings/cursor)

A string which indicates whether or not the display surface currently being captured includes the mouse cursor, and if so, whether it's only visible while the mouse is in motion or if it's always visible. The value is one of `always`, `motion`, or `never`.

[MediaTrackSettings.displaySurface](/en-US/docs/Web/API/MediaTrackSettings/displaySurface)

A string indicating what type of display surface is currently being captured. The value is one of `browser`, `monitor`, or `window`.

[MediaTrackSettings.logicalSurface](/en-US/docs/Web/API/MediaTrackSettings/logicalSurface)

A boolean value, which is `true` if the video being captured doesn't directly correspond to a single onscreen display area.

[MediaTrackSettings.suppressLocalAudioPlayback](/en-US/docs/Web/API/MediaTrackSettings/suppressLocalAudioPlayback)

A boolean value, which is `true` if the audio being captured is not played out of the user's local speakers.

[MediaTrackSettings.screenPixelRatio](/en-US/docs/Web/API/MediaTrackSettings/screenPixelRatio)

A number representing the ratio of the physical size of a pixel on the captured display surface (displayed at its physical resolution) to the logical size of a CSS pixel on the capturing screen (displayed at its logical resolution). It cannot be used as a constraint or capability.

### [MediaTrackSupportedConstraints](#mediatracksupportedconstraints)

[MediaTrackSupportedConstraints.displaySurface](/en-US/docs/Web/API/MediaTrackSupportedConstraints/displaySurface)

A boolean, which is `true` if the current environment supports the [MediaTrackConstraints.displaySurface](/en-US/docs/Web/API/MediaTrackConstraints/displaySurface) constraint.

[MediaTrackSupportedConstraints.logicalSurface](/en-US/docs/Web/API/MediaTrackSupportedConstraints/logicalSurface)

A boolean, which is `true` if the current environment supports the constraint [MediaTrackConstraints.logicalSurface](/en-US/docs/Web/API/MediaTrackConstraints/logicalSurface).

[MediaTrackSupportedConstraints.suppressLocalAudioPlayback](/en-US/docs/Web/API/MediaTrackSupportedConstraints/suppressLocalAudioPlayback)

A boolean, which is `true` if the current environment supports the constraint [MediaTrackConstraints.suppressLocalAudioPlayback](/en-US/docs/Web/API/MediaTrackConstraints/suppressLocalAudioPlayback).

## [Security considerations](#security_considerations)

Websites that support [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) (either using the HTTP [Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy) header or the [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe) attribute [allow](/en-US/docs/Web/HTML/Reference/Elements/iframe#allow)) can specify a desire to use the Screen Capture API using the directive [display-capture](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/display-capture):

html

```
<iframe allow="display-capture" src="/some-other-document.html">…</iframe>
```

A site can also specify a desire to use the [Captured Surface Control API](/en-US/docs/Web/API/Screen_Capture_API/Captured_Surface_Control) via the [captured-surface-control](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/captured-surface-control) directive. Specifically, the [forwardWheel()](/en-US/docs/Web/API/CaptureController/forwardWheel), [increaseZoomLevel()](/en-US/docs/Web/API/CaptureController/increaseZoomLevel), [decreaseZoomLevel()](/en-US/docs/Web/API/CaptureController/decreaseZoomLevel), and [resetZoomLevel()](/en-US/docs/Web/API/CaptureController/resetZoomLevel) methods are controlled by this directive.

The default allowlist for both directives is `self`, which permits any content within the same origin use Screen Capture.

These methods are considered [powerful features](/en-US/docs/Web/Security#secure_contexts_and_feature_permissions), which means that even if permission is allowed via a `Permissions-Policy`, the user will still be prompted for permission to use them. The [Permissions API](/en-US/docs/Web/API/Permissions_API) can be used to query the aggregate permission (from both the website and the user) for using the listed features.

In addition, the specification requires that a user has recently interacted with the page to use these features — this means that [transient activation](/en-US/docs/Glossary/Transient_activation) is required. See the individual method pages for more details.

## [Specifications](#specifications)

Specification[Screen Capture](https://w3c.github.io/mediacapture-screen-share/)[Element Capture](https://screen-share.github.io/element-capture/)[Region Capture](https://w3c.github.io/mediacapture-region/)[Captured Surface Control](https://w3c.github.io/mediacapture-surface-control/)

## [Browser compatibility](#browser_compatibility)

### [api.MediaDevices.getDisplayMedia](#api.MediaDevices.getDisplayMedia)

### [api.CropTarget](#api.CropTarget)

### [api.RestrictionTarget](#api.RestrictionTarget)

## [See also](#see_also)

- [Using the Screen Capture API](/en-US/docs/Web/API/Screen_Capture_API/Using_Screen_Capture)
- [Using the Element Capture and Region Capture APIs](/en-US/docs/Web/API/Screen_Capture_API/Element_Region_Capture)
- [Using the Captured Surface Control API](/en-US/docs/Web/API/Screen_Capture_API/Captured_Surface_Control)
- [MediaDevices.getDisplayMedia()](/en-US/docs/Web/API/MediaDevices/getDisplayMedia)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 14, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Screen_Capture_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/screen_capture_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreen_Capture_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fscreen_capture_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreen_Capture_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fscreen_capture_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F83a92f1eaf27dabf71beec6c548afb03171aa194%0A*+Document+last+modified%3A+2025-07-14T12%3A34%3A28.000Z%0A%0A%3C%2Fdetails%3E)
