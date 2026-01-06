# Picture-in-Picture API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPicture-in-Picture_API&level=not)

The Picture-in-Picture API allow websites to create a floating, always-on-top video window. This allows users to continue consuming media while they interact with other sites or applications on their device.

Note: The [Document Picture-in-Picture API](/en-US/docs/Web/API/Document_Picture-in-Picture_API) extends the Picture-in-Picture API to allow the always-on-top window to be populated with any arbitrary HTML content, not just a video.

## In this article

- [Interfaces](#interfaces)
- [Instance methods](#instance_methods)
- [Instance properties](#instance_properties)
- [Events](#events)
- [Adding Controls](#adding_controls)
- [Controlling styling](#controlling_styling)
- [Controlling access](#controlling_access)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces](#interfaces)

[PictureInPictureWindow](/en-US/docs/Web/API/PictureInPictureWindow)

Represents the floating video window; contains [width](/en-US/docs/Web/API/PictureInPictureWindow/width) and [height](/en-US/docs/Web/API/PictureInPictureWindow/height) properties, and an [onresize](/en-US/docs/Web/API/PictureInPictureWindow/resize_event) event handler property.

[PictureInPictureEvent](/en-US/docs/Web/API/PictureInPictureEvent)

Represents picture-in-picture-related events, including [enterpictureinpicture](/en-US/docs/Web/API/HTMLVideoElement/enterpictureinpicture_event), [leavepictureinpicture](/en-US/docs/Web/API/HTMLVideoElement/leavepictureinpicture_event) and [resize](/en-US/docs/Web/API/PictureInPictureWindow/resize_event).

## [Instance methods](#instance_methods)

The Picture-in-Picture API adds methods to the [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement) and [Document](/en-US/docs/Web/API/Document) interfaces to allow toggling of the floating video window.

### [Instance methods on the HTMLVideoElement interface](#instance_methods_on_the_htmlvideoelement_interface)

[HTMLVideoElement.requestPictureInPicture()](/en-US/docs/Web/API/HTMLVideoElement/requestPictureInPicture)

Requests that the user agent enters the video into picture-in-picture mode

### [Instance methods on the Document interface](#instance_methods_on_the_document_interface)

[Document.exitPictureInPicture()](/en-US/docs/Web/API/Document/exitPictureInPicture)

Requests that the user agent returns the element in picture-in-picture mode back into its original box.

## [Instance properties](#instance_properties)

The Picture-in-Picture API augments the [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement), [Document](/en-US/docs/Web/API/Document), and [ShadowRoot](/en-US/docs/Web/API/ShadowRoot) interfaces with properties that can be used to determine if the floating video window mode is supported and available, if picture-in-picture mode is currently active, and which video is floating.

### [Instance properties on the HTMLVideoElement interface](#instance_properties_on_the_htmlvideoelement_interface)

[HTMLVideoElement.disablePictureInPicture](/en-US/docs/Web/API/HTMLVideoElement/disablePictureInPicture)

The `disablePictureInPicture` property will provide a hint to the user agent to not suggest the picture-in-picture to users or to request it automatically.

### [Instance properties on the Document interface](#instance_properties_on_the_document_interface)

[Document.pictureInPictureEnabled](/en-US/docs/Web/API/Document/pictureInPictureEnabled)

The `pictureInPictureEnabled` property tells you whether or not it is possible to engage picture-in-picture mode. This is `false` if picture-in-picture mode is not available for any reason (e.g., the ["picture-in-picture" feature](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/picture-in-picture) has been disallowed, or picture-in-picture mode is not supported).

### [Instance properties on the Document or ShadowRoot interfaces](#instance_properties_on_the_document_or_shadowroot_interfaces)

[Document.pictureInPictureElement](/en-US/docs/Web/API/Document/pictureInPictureElement) / [ShadowRoot.pictureInPictureElement](/en-US/docs/Web/API/ShadowRoot/pictureInPictureElement)

The `pictureInPictureElement` property tells you which [Element](/en-US/docs/Web/API/Element) is currently being displayed in the floating window (or in the shadow DOM). If this is `null`, the document (or shadow DOM) has no node currently in picture-in-picture mode.

## [Events](#events)

The Picture-in-Picture API defines three events, which can be used to detect when picture-in-picture mode is toggled and when the floating video window is resized.

[enterpictureinpicture](/en-US/docs/Web/API/HTMLVideoElement/enterpictureinpicture_event)

Sent to a [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement) when it enters picture-in-picture mode.

[leavepictureinpicture](/en-US/docs/Web/API/HTMLVideoElement/leavepictureinpicture_event)

Sent to a [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement) when it leaves picture-in-picture mode.

[resize](/en-US/docs/Web/API/PictureInPictureWindow/resize_event)

Sent to a [PictureInPictureWindow](/en-US/docs/Web/API/PictureInPictureWindow) when it changes size.

## [Adding Controls](#adding_controls)

If media action handlers have been set via the [Media Session API](/en-US/docs/Web/API/Media_Session_API), then appropriate controls for those actions will be added by the browser to the picture-in-picture overlay. For example, if a `"nexttrack"` action has been set, then a skip button might be displayed in the picture-in-picture view. There is no support for adding custom HTML buttons or controls.

## [Controlling styling](#controlling_styling)

The [:picture-in-picture](/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture)[CSS](/en-US/docs/Web/CSS)[pseudo-class](/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes) matches the video element currently in picture-in-picture mode, allowing you to configure your stylesheets to automatically adjust the size, style, or layout of content when a video switches back and forth between picture-in-picture and traditional presentation modes.

## [Controlling access](#controlling_access)

The availability of picture-in-picture mode can be controlled using [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy). The picture-in-picture mode feature is identified by the string `"picture-in-picture"`, with a default allowlist value of `*`, meaning that picture-in-picture mode is permitted in top-level document contexts, as well as to nested browsing contexts loaded from the same origin as the top-most document.

## [Examples](#examples)

### [Toggling picture-in-picture mode](#toggling_picture-in-picture_mode)

In this example, we have a [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element in a web page, a [<button>](/en-US/docs/Web/HTML/Reference/Elements/button) to toggle picture-in-picture, and an element to log information relevant for the example. The [<button>](/en-US/docs/Web/HTML/Reference/Elements/button) element is `disabled` initially until we've determined browser support.

html

```
<video
  src="/shared-assets/videos/friday.mp4"
  id="video"
  muted
  controls
  loop
  width="300"></video>

<button id="pip-button" disabled>Toggle PiP</button>
<pre id="log"></pre>
```

```
body {
  font:
    14px "Open Sans",
    sans-serif;
  padding: 0.5em;
}

button {
  display: block;
  margin-block: 1rem;
}
```

We first check if the browser supports PiP with `document.pictureInPictureEnabled`, and if it's not supported, we log that information to the `<pre>` element. If it is available in the browser, we can enable the toggle to enter and exit PiP.

For the controls, an event listener on the [<button>](/en-US/docs/Web/HTML/Reference/Elements/button) element calls a `togglePictureInPicture()` function that we've defined. In `togglePictureInPicture()`, an `if` statement checks the value of the [document](/en-US/docs/Web/API/Document)'s `pictureInPictureElement` attribute.

- If the value is `null`, no video is in a floating window, so we can request the video to enter picture-in-picture mode. We do that by calling [HTMLVideoElement.requestPictureInPicture()](/en-US/docs/Web/API/HTMLVideoElement/requestPictureInPicture) on the [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element.
- If the value is not `null`, an element is currently in picture-in-picture mode. We can then call [document.exitPictureInPicture()](/en-US/docs/Web/API/Document/exitPictureInPicture) to bring the video back into its initial box, exiting picture-in-picture mode.

js

```
const video = document.getElementById("video");
const pipButton = document.getElementById("pip-button");
const log = document.getElementById("log");

if (document.pictureInPictureEnabled) {
  pipButton.removeAttribute("disabled");
} else {
  log.innerText = "PiP not supported. Check browser compatibility for details.";
}

function togglePictureInPicture() {
  if (document.pictureInPictureElement) {
    document.exitPictureInPicture();
  } else {
    video.requestPictureInPicture();
  }
}

pipButton.addEventListener("click", togglePictureInPicture);
```

css

```
:picture-in-picture {
  outline: 5px dashed green;
}
```

Clicking the "Toggle PiP" button lets the user toggle between playing the video in the page and in a floating window:

## [Specifications](#specifications)

Specification
[Picture-in-Picture# interface-picture-in-picture-window](https://w3c.github.io/picture-in-picture/#interface-picture-in-picture-window)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [HTMLVideoElement.requestPictureInPicture()](/en-US/docs/Web/API/HTMLVideoElement/requestPictureInPicture)
- [HTMLVideoElement.disablePictureInPicture](/en-US/docs/Web/API/HTMLVideoElement/disablePictureInPicture)
- [Document.pictureInPictureEnabled](/en-US/docs/Web/API/Document/pictureInPictureEnabled)
- [Document.exitPictureInPicture()](/en-US/docs/Web/API/Document/exitPictureInPicture)
- [Document.pictureInPictureElement](/en-US/docs/Web/API/Document/pictureInPictureElement)
- [:picture-in-picture](/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture)
- The [Document Picture-in-Picture API](/en-US/docs/Web/API/Document_Picture-in-Picture_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Picture-in-Picture_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/picture-in-picture_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPicture-in-Picture_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpicture-in-picture_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPicture-in-Picture_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpicture-in-picture_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0c13af55e869cbc54830fd1a601fd05f60717375%0A*+Document+last+modified%3A+2025-12-17T16%3A01%3A14.000Z%0A%0A%3C%2Fdetails%3E)
