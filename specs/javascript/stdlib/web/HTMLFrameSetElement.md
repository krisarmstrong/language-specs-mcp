# HTMLFrameSetElement

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `HTMLFrameSetElement` interface provides special properties (beyond those of the regular [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface they also inherit) for manipulating [<frameset>](/en-US/docs/Web/HTML/Reference/Elements/frameset) elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Event handlers](#event_handlers)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

`HTMLFrameSetElement.cols`Deprecated

A string structured as a comma-separated list specifying the width of each column inside a frameset.

`HTMLFrameSetElement.rows`Deprecated

A string structured as a comma-separated list specifying the height of each column inside a frameset.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Event handlers](#event_handlers)

The [HTMLElement](/en-US/docs/Web/API/HTMLElement) events are inherited.

The following [Window](/en-US/docs/Web/API/Window)`onXYZ` event handler properties are also available as aliases targeting the `window` object. However, it is advised to listen to them on the `window` object directly rather than on `HTMLFrameSetElement`.

Note: Using `addEventListener()` on `HTMLFrameSetElement` will not work for the `onXYZ` event handlers listed below. Listen to the events on the [window](/en-US/docs/Web/API/Window) object instead.

[HTMLFrameSetElement.onafterprint](/en-US/docs/Web/API/Window/afterprint_event)

Fired after the associated document has started printing or the print preview has been closed.

[HTMLFrameSetElement.onbeforeprint](/en-US/docs/Web/API/Window/beforeprint_event)

Fired when the associated document is about to be printed or previewed for printing.

[HTMLFrameSetElement.onbeforeunload](/en-US/docs/Web/API/Window/beforeunload_event)

Fired when the window, the document and its resources are about to be unloaded.

[HTMLFrameSetElement.ongamepadconnected](/en-US/docs/Web/API/Window/gamepadconnected_event)

Fired when the browser detects that a gamepad has been connected or the first time a button/axis of the gamepad is used.

[HTMLFrameSetElement.ongamepaddisconnected](/en-US/docs/Web/API/Window/gamepaddisconnected_event)

Fired when the browser detects that a gamepad has been disconnected.

[HTMLFrameSetElement.onhashchange](/en-US/docs/Web/API/Window/hashchange_event)

Fired when the fragment identifier of the URL has changed (the part of the URL beginning with and following the `#` symbol).

[HTMLFrameSetElement.onlanguagechange](/en-US/docs/Web/API/Window/languagechange_event)

Fired when the user's preferred language changes.

[HTMLFrameSetElement.onmessage](/en-US/docs/Web/API/Window/message_event)

Fired when the window receives a message, for example from a call to [Window.postMessage()](/en-US/docs/Web/API/Window/postMessage) from another browsing context.

[HTMLFrameSetElement.onmessageerror](/en-US/docs/Web/API/Window/messageerror_event)

Fired when the window receives a message that can't be deserialized.

[HTMLFrameSetElement.onoffline](/en-US/docs/Web/API/Window/offline_event)

Fired when the browser has lost access to the network and the value of [Navigator.onLine](/en-US/docs/Web/API/Navigator/onLine) switches to `false`.

[HTMLFrameSetElement.ononline](/en-US/docs/Web/API/Window/online_event)

Fired when the browser has gained access to the network and the value of [Navigator.onLine](/en-US/docs/Web/API/Navigator/onLine) switches to `true`.

[HTMLFrameSetElement.onpagehide](/en-US/docs/Web/API/Window/pagehide_event)

Fired when the browser hides the current page in the process of presenting a different page from the session's history.

[HTMLFrameSetElement.onpageshow](/en-US/docs/Web/API/Window/pageshow_event)

Fired when the browser displays the window's document due to navigation.

[HTMLFrameSetElement.onpopstate](/en-US/docs/Web/API/Window/popstate_event)

Fired when the active history entry changes while the user navigates the session history.

[HTMLFrameSetElement.onrejectionhandled](/en-US/docs/Web/API/Window/rejectionhandled_event)

Fired whenever a JavaScript [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) is rejected and the rejection has been handled.

[HTMLFrameSetElement.onstorage](/en-US/docs/Web/API/Window/storage_event)

Fired when a storage area (`localStorage`) has been modified in the context of another document.

[HTMLFrameSetElement.onunhandledrejection](/en-US/docs/Web/API/Window/unhandledrejection_event)

Fired whenever a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) is rejected but the rejection was not handled.

[HTMLFrameSetElement.onunload](/en-US/docs/Web/API/Window/unload_event)

Fired when the document is being unloaded.

## [Specifications](#specifications)

Specification
[HTML# htmlframesetelement](https://html.spec.whatwg.org/multipage/obsolete.html#htmlframesetelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- HTML element implementing this interface: [<frameset>](/en-US/docs/Web/HTML/Reference/Elements/frameset)
- The equivalent of this element outside of frames: `HTMLFrameSetElement`.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 16, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLFrameSetElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlframesetelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLFrameSetElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlframesetelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLFrameSetElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlframesetelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd47348199a379f68bea876a403eb510628ec4ccb%0A*+Document+last+modified%3A+2024-10-16T00%3A20%3A59.000Z%0A%0A%3C%2Fdetails%3E)
