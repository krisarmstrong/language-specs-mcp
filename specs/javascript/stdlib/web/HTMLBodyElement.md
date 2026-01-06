# HTMLBodyElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLBodyElement&level=high)

The `HTMLBodyElement` interface provides special properties (beyond those inherited from the regular [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface) for manipulating [<body>](/en-US/docs/Web/HTML/Reference/Elements/body) elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Event handlers](#event_handlers)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

`HTMLBodyElement.aLink`Deprecated

A string that represents the color of active hyperlinks.

`HTMLBodyElement.background`Deprecated

A string that represents the description of the location of the background image resource. Note that this is not a URI, though some older version of some browsers do expect it.

`HTMLBodyElement.bgColor`Deprecated

A string that represents the background color for the document.

`HTMLBodyElement.link`Deprecated

A string that represents the color of unvisited links.

`HTMLBodyElement.text`Deprecated

A string that represents the foreground color of text.

`HTMLBodyElement.vLink`Deprecated

A string that represents the color of visited links.

## [Instance methods](#instance_methods)

No specific methods; inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Event handlers](#event_handlers)

The [HTMLElement](/en-US/docs/Web/API/HTMLElement) events are inherited.

The following [Window](/en-US/docs/Web/API/Window)`onXYZ` event handler properties are also available as aliases targeting the `window` object. However, it is advised to listen to them on the `window` object directly rather than on `HTMLBodyElement`.

Note: Using `addEventListener()` on `HTMLBodyElement` will not work for the `onXYZ` event handlers listed below. Listen to the events on the [window](/en-US/docs/Web/API/Window) object instead.

[HTMLBodyElement.onafterprint](/en-US/docs/Web/API/Window/afterprint_event)

Fired after the associated document has started printing or the print preview has been closed.

[HTMLBodyElement.onbeforeprint](/en-US/docs/Web/API/Window/beforeprint_event)

Fired when the associated document is about to be printed or previewed for printing.

[HTMLBodyElement.onbeforeunload](/en-US/docs/Web/API/Window/beforeunload_event)

Fired when the window, the document and its resources are about to be unloaded.

[HTMLBodyElement.onblur](/en-US/docs/Web/API/Window/blur_event)

Fired when the window loses focus.

[HTMLBodyElement.onerror](/en-US/docs/Web/API/Window/error_event)

Fired when an error occurs and bubbles up to the window.

[HTMLBodyElement.onfocus](/en-US/docs/Web/API/Window/focus_event)

Fired when the window gains focus.

[HTMLBodyElement.ongamepadconnected](/en-US/docs/Web/API/Window/gamepadconnected_event)

Fired when the browser detects that a gamepad has been connected or the first time a button/axis of the gamepad is used.

[HTMLBodyElement.ongamepaddisconnected](/en-US/docs/Web/API/Window/gamepaddisconnected_event)

Fired when the browser detects that a gamepad has been disconnected.

[HTMLBodyElement.onhashchange](/en-US/docs/Web/API/Window/hashchange_event)

Fired when the fragment identifier of the URL has changed (the part of the URL beginning with and following the `#` symbol).

[HTMLBodyElement.onlanguagechange](/en-US/docs/Web/API/Window/languagechange_event)

Fired when the user's preferred language changes.

[HTMLBodyElement.onload](/en-US/docs/Web/API/Window/load_event)

Fired when the document has finished loading.

[HTMLBodyElement.onmessage](/en-US/docs/Web/API/Window/message_event)

Fired when the window receives a message, for example from a call to [Window.postMessage()](/en-US/docs/Web/API/Window/postMessage) from another browsing context.

[HTMLBodyElement.onmessageerror](/en-US/docs/Web/API/Window/messageerror_event)

Fired when the window receives a message that can't be deserialized.

[HTMLBodyElement.onoffline](/en-US/docs/Web/API/Window/offline_event)

Fired when the browser has lost access to the network and the value of [Navigator.onLine](/en-US/docs/Web/API/Navigator/onLine) switches to `false`.

[HTMLBodyElement.ononline](/en-US/docs/Web/API/Window/online_event)

Fired when the browser has gained access to the network and the value of [Navigator.onLine](/en-US/docs/Web/API/Navigator/onLine) switches to `true`.

[HTMLBodyElement.onpagehide](/en-US/docs/Web/API/Window/pagehide_event)

Fired when the browser hides the current page in the process of presenting a different page from the session's history.

[HTMLBodyElement.onpageshow](/en-US/docs/Web/API/Window/pageshow_event)

Fired when the browser displays the window's document due to navigation.

[HTMLBodyElement.onpopstate](/en-US/docs/Web/API/Window/popstate_event)

Fired when the active history entry changes while the user navigates the session history.

[HTMLBodyElement.onrejectionhandled](/en-US/docs/Web/API/Window/rejectionhandled_event)

Fired whenever a JavaScript [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) is rejected and the rejection has been handled.

[HTMLBodyElement.onresize](/en-US/docs/Web/API/Window/resize_event)

Fired when the document view has been resized.

`HTMLBodyElement.onscroll`

Fired when the document view or an element has been scrolled.

[HTMLBodyElement.onstorage](/en-US/docs/Web/API/Window/storage_event)

Fired when a storage area (`localStorage`) has been modified in the context of another document.

[HTMLBodyElement.onunhandledrejection](/en-US/docs/Web/API/Window/unhandledrejection_event)

Fired whenever a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) is rejected but the rejection was not handled.

[HTMLBodyElement.onunload](/en-US/docs/Web/API/Window/unload_event)

Fired when the document is being unloaded.

Note that while `onblur`, `onerror`, `onfocus`, `onload`, `onresize`, and `onscroll` are available on any element, their meanings on the `<body>` element are not the same as on other elements. They listen for events on the `window` object instead.

## [Specifications](#specifications)

Specification
[HTML# htmlbodyelement](https://html.spec.whatwg.org/multipage/sections.html#htmlbodyelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- HTML element implementing this interface: [<body>](/en-US/docs/Web/HTML/Reference/Elements/body)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLBodyElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlbodyelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLBodyElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlbodyelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLBodyElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlbodyelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
