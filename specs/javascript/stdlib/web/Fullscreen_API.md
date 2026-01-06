# Fullscreen API

The Fullscreen API adds methods to present a specific [Element](/en-US/docs/Web/API/Element) (and its descendants) in fullscreen mode, and to exit fullscreen mode once it is no longer needed. This makes it possible to present desired content—such as an online game—using the user's entire screen, removing all browser user interface elements and other applications from the screen until fullscreen mode is shut off.

See the article [Guide to the Fullscreen API](/en-US/docs/Web/API/Fullscreen_API/Guide) for details on how to use the API.

## In this article

- [Interfaces](#interfaces)
- [Instance methods](#instance_methods)
- [Instance properties](#instance_properties)
- [Events](#events)
- [Controlling access](#controlling_access)
- [Usage notes](#usage_notes)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces](#interfaces)

The Fullscreen API has no interfaces of its own. Instead, it augments several other interfaces to add the methods, properties, and event handlers needed to provide fullscreen functionality. These are listed in the following sections.

## [Instance methods](#instance_methods)

The Fullscreen API adds methods to the [Document](/en-US/docs/Web/API/Document) and [Element](/en-US/docs/Web/API/Element) interfaces to allow turning off and on fullscreen mode.

### [Instance methods on the Document interface](#instance_methods_on_the_document_interface)

[Document.exitFullscreen()](/en-US/docs/Web/API/Document/exitFullscreen)

Requests that the [user agent](/en-US/docs/Glossary/User_agent) switch from fullscreen mode back to windowed mode. Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which is resolved once fullscreen mode has been completely shut off.

### [Instance methods on the Element interface](#instance_methods_on_the_element_interface)

[Element.requestFullscreen()](/en-US/docs/Web/API/Element/requestFullscreen)

Asks the user agent to place the specified element (and, by extension, its descendants) into fullscreen mode, removing all of the browser's UI elements as well as all other applications from the screen. Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which is resolved once fullscreen mode has been activated.

## [Instance properties](#instance_properties)

[Document.fullscreenElement](/en-US/docs/Web/API/Document/fullscreenElement) / [ShadowRoot.fullscreenElement](/en-US/docs/Web/API/ShadowRoot/fullscreenElement)

The `fullscreenElement` property tells you the [Element](/en-US/docs/Web/API/Element) that's currently being displayed in fullscreen mode on the DOM (or shadow DOM). If this is `null`, the document (or shadow DOM) is not in fullscreen mode.

[Document.fullscreenEnabled](/en-US/docs/Web/API/Document/fullscreenEnabled)

The `fullscreenEnabled` property tells you whether or not it is possible to engage fullscreen mode. This is `false` if fullscreen mode is not available for any reason (such as the `"fullscreen"` feature not being allowed, or fullscreen mode not being supported).

### [Obsolete properties](#obsolete_properties)

[Document.fullscreen](/en-US/docs/Web/API/Document/fullscreen)Deprecated

A Boolean value which is `true` if the document has an element currently being displayed in fullscreen mode; otherwise, this returns `false`.

Note: Use the [fullscreenElement](/en-US/docs/Web/API/Document/fullscreenElement) property on the [Document](/en-US/docs/Web/API/Document) or [ShadowRoot](/en-US/docs/Web/API/ShadowRoot) instead; if it's not `null`, then it's an [Element](/en-US/docs/Web/API/Element) currently being displayed in fullscreen mode.

## [Events](#events)

[fullscreenchange](/en-US/docs/Web/API/Element/fullscreenchange_event)

Sent to an [Element](/en-US/docs/Web/API/Element) when it transitions into or out of fullscreen mode.

[fullscreenerror](/en-US/docs/Web/API/Element/fullscreenerror_event)

Sent to an `Element` if an error occurs while attempting to switch it into or out of fullscreen mode.

## [Controlling access](#controlling_access)

The availability of fullscreen mode can be controlled using a [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy). The fullscreen mode feature is identified by the string `"fullscreen"`, with a default allowlist value of `"self"`, meaning that fullscreen mode is permitted in top-level document contexts, as well as to nested browsing contexts loaded from the same origin as the top-most document.

## [Usage notes](#usage_notes)

Users can choose to exit fullscreen mode by pressing the ESC (or F11) key, rather than waiting for the site or app to programmatically do so. Make sure you provide, somewhere in your user interface, appropriate user interface elements that inform the user that this option is available to them.

Note: Navigating to another page, changing tabs, or switching to another application using any application switcher (or Alt-Tab) will likewise exit fullscreen mode.

## [Examples](#examples)

### [Simple fullscreen usage](#simple_fullscreen_usage)

In this example, a video is presented in a web page. Pressing the Enter key lets the user toggle between windowed and fullscreen presentation of the video.

[View Live Example](https://mdn.github.io/dom-examples/fullscreen-api/index.html)

#### Watching for the Enter key

When the page is loaded, this code is run to set up an event listener to watch for the Enter key.

js

```
const video = document.getElementById("video");

// On pressing ENTER call toggleFullScreen method
document.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    toggleFullScreen(video);
  }
});
```

#### Toggling fullscreen mode

This code is called by the event handler above when the user hits the Enter key.

js

```
function toggleFullScreen(video) {
  if (!document.fullscreenElement) {
    // If the document is not in full screen mode
    // make the video full screen
    video.requestFullscreen();
  } else {
    // Otherwise exit the full screen
    document.exitFullscreen?.();
  }
}
```

This starts by looking at the value of the [document](/en-US/docs/Web/API/Document)'s `fullscreenElement` attribute. If the value is `null`, the document is currently in windowed mode, so we need to switch to fullscreen mode; otherwise, it's the element that's currently in fullscreen mode. Switching to fullscreen mode is done by calling [Element.requestFullscreen()](/en-US/docs/Web/API/Element/requestFullscreen) on the [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element.

If fullscreen mode is already active (`fullscreenElement` is not `null`), we call [exitFullscreen()](/en-US/docs/Web/API/Document/exitFullscreen) on the `document` to shut off fullscreen mode.

## [Specifications](#specifications)

Specification
[Fullscreen API# ref-for-dom-document-fullscreenelement①](https://fullscreen.spec.whatwg.org/#ref-for-dom-document-fullscreenelement①)
[Fullscreen API# ref-for-dom-document-fullscreenenabled①](https://fullscreen.spec.whatwg.org/#ref-for-dom-document-fullscreenenabled①)
[Fullscreen API# ref-for-dom-document-exitfullscreen①](https://fullscreen.spec.whatwg.org/#ref-for-dom-document-exitfullscreen①)
[Fullscreen API# ref-for-dom-element-requestfullscreen①](https://fullscreen.spec.whatwg.org/#ref-for-dom-element-requestfullscreen①)
[Fullscreen API# dom-document-fullscreen](https://fullscreen.spec.whatwg.org/#dom-document-fullscreen)

## [Browser compatibility](#browser_compatibility)

### [api.Document.fullscreenElement](#api.Document.fullscreenElement)

### [api.Document.fullscreenEnabled](#api.Document.fullscreenEnabled)

### [api.Document.exitFullscreen](#api.Document.exitFullscreen)

### [api.Element.requestFullscreen](#api.Element.requestFullscreen)

### [api.Document.fullscreen](#api.Document.fullscreen)

## [See also](#see_also)

- [Element.requestFullscreen()](/en-US/docs/Web/API/Element/requestFullscreen)
- [Document.exitFullscreen()](/en-US/docs/Web/API/Document/exitFullscreen)
- [Document.fullscreen](/en-US/docs/Web/API/Document/fullscreen)
- [Document.fullscreenElement](/en-US/docs/Web/API/Document/fullscreenElement)
- [:fullscreen](/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen), [::backdrop](/en-US/docs/Web/CSS/Reference/Selectors/::backdrop)
- [allowfullscreen](/en-US/docs/Web/HTML/Reference/Elements/iframe#allowfullscreen)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Fullscreen_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fullscreen_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFullscreen_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffullscreen_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFullscreen_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffullscreen_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
