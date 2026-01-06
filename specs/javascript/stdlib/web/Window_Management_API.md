# Window Management API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindow_Management_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Window Management API allows you to get detailed information on the displays connected to your device and more easily place windows on specific screens, paving the way towards more effective multi-screen applications.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Permissions policy integration](#permissions_policy_integration)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Concepts and usage](#concepts_and_usage)

Historically, we have used [Window.open()](/en-US/docs/Web/API/Window/open) to manage browser windows related to the current application — opening new windows, resizing and closing existing windows, etc. For example, to open a 400×300 window 50 pixels from the left and top of your screen:

js

```
const myWindow = window.open(
  "https://example.com/",
  "myWindow",
  "left=50,top=50,width=400,height=300",
);
```

You can retrieve information about your screen from the [Window.screen](/en-US/docs/Web/API/Window/screen) property, such as how much screen space you have available to place windows in.

However, the above features are limited. `Window.screen` only returns data about the primary screen, and not secondary displays available to a device. To move a window to a secondary display, you could use [Window.moveTo()](/en-US/docs/Web/API/Window/moveTo), but you'd have to guess what coordinates to use based on where it is placed in your setup relative to the primary display.

The Window Management API provides more robust, flexible window management. It allows you to query whether your display is extended with multiple screens and get information on each screen separately: windows can then be placed on each screen as desired. It also provides event handlers to allow you to respond to changes in the available screens, new fullscreen functionality to choose which screen to put into fullscreen mode (if any), and permissions functionality to control access to the API.

For details on how to use it, see [Using the Window Management API](/en-US/docs/Web/API/Window_Management_API/Using).

Note: In modern browsers, a separate user gesture event is required for each `Window.open()` call, for security purposes. This prevents sites from spamming users with lots of windows. However, this poses an issue for multi-window applications. To work around this limitation, you can design your applications to open no more than one new window at once, reuse existing windows to display different pages, or advise users on how to update their browser settings to allow multiple windows.

### [Use cases](#use_cases)

The Window Management API is useful in cases such as:

- Multi-window graphics editors and audio processors that may wish to arrange editing tools and panels across different screens.
- Virtual trading desks that want to show market trends in multiple windows and put specific windows of interest in fullscreen mode.
- Slideshow apps that want to show speaker notes on the internal primary screen and the presentation on an external projector.

## [Permissions policy integration](#permissions_policy_integration)

The [window-management](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/window-management)[Permissions-Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) can be used to control permission to use the Window Management API. Specifically:

- Usage of the [Window.getScreenDetails()](/en-US/docs/Web/API/Window/getScreenDetails) method. If blocked, its [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) will reject with a `NotAllowedError` exception.
- Querying the [Window.screen.isExtended](/en-US/docs/Web/API/Screen/isExtended) property. If blocked, it will always return `false`.

Developers can explicitly grant permission for an [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe) to use Window Management via the `allow` attribute:

html

```
<iframe src="3rd-party.example" allow="window-management"></iframe>
```

## [Interfaces](#interfaces)

[ScreenDetails](/en-US/docs/Web/API/ScreenDetails)Secure context

Represents the details of all the screens available to the user's device.

[ScreenDetailed](/en-US/docs/Web/API/ScreenDetailed)Secure context

Represents detailed information about one specific screen available to the user's device.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

The `Screen`[change](/en-US/docs/Web/API/Screen/change_event) event Secure context

Fired on a specific screen when it changes in some way — for example available width or height, or orientation.

[Screen.isExtended](/en-US/docs/Web/API/Screen/isExtended)Secure context

A boolean property that returns `true` if the user's device has multiple screens, and `false` if not.

[Element.requestFullscreen()](/en-US/docs/Web/API/Element/requestFullscreen), the `screen` option

Specifies on which screen you want to put the element in fullscreen mode.

[Window.getScreenDetails()](/en-US/docs/Web/API/Window/getScreenDetails)Secure context

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [ScreenDetails](/en-US/docs/Web/API/ScreenDetails) object instance.

## [Examples](#examples)

You can find full examples here:

- [Basic multi-window learning environment](https://mdn.github.io/dom-examples/window-management-api/) (see the [source code](https://github.com/mdn/dom-examples/tree/main/window-management-api)).
- [Multi-window Platformer Game](https://googlechromelabs.github.io/multi-window-platformer-game/) (see the [source code](https://github.com/googlechromelabs/multi-window-platformer-game)).
- [Window placement demo](https://michaelwasserman.github.io/window-placement-demo/) (see the [source code](https://github.com/michaelwasserman/window-placement-demo)).

## [Specifications](#specifications)

Specification[Window Management](https://w3c.github.io/window-management/)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Window_Management_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/window_management_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindow_Management_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwindow_management_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindow_Management_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwindow_management_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F72d51eab0cf7140e7edcca663fe24fae1a4166f8%0A*+Document+last+modified%3A+2025-07-07T15%3A18%3A12.000Z%0A%0A%3C%2Fdetails%3E)
