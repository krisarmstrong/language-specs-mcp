# ScreenDetailed

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreenDetailed&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `ScreenDetailed` interface of the [Window Management API](/en-US/docs/Web/API/Window_Management_API) represents detailed information about one specific screen available to the user's device.

`ScreenDetailed` objects can be accessed via the [ScreenDetails.screens](/en-US/docs/Web/API/ScreenDetails/screens) and [ScreenDetails.currentScreen](/en-US/docs/Web/API/ScreenDetails/currentScreen) properties.

## In this article

- [Instance properties](#instance_properties)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [Screen](/en-US/docs/Web/API/Screen).

[availLeft](/en-US/docs/Web/API/ScreenDetailed/availLeft)Read onlyExperimental

A number representing the x-coordinate (left-hand edge) of the available screen area.

[availTop](/en-US/docs/Web/API/ScreenDetailed/availTop)Read onlyExperimental

A number representing the y-coordinate (top edge) of the available screen area.

[devicePixelRatio](/en-US/docs/Web/API/ScreenDetailed/devicePixelRatio)Read onlyExperimental

A number representing the screen's device pixel ratio.

[isInternal](/en-US/docs/Web/API/ScreenDetailed/isInternal)Read onlyExperimental

A boolean indicating whether the screen is internal to the device or external.

[isPrimary](/en-US/docs/Web/API/ScreenDetailed/isPrimary)Read onlyExperimental

A boolean indicating whether the screen is set as the operating system (OS) primary screen or not.

[label](/en-US/docs/Web/API/ScreenDetailed/label)Read onlyExperimental

A string providing a descriptive label for the screen, for example "Built-in Retina Display".

[left](/en-US/docs/Web/API/ScreenDetailed/left)Read onlyExperimental

A number representing the x-coordinate (left-hand edge) of the total screen area.

[top](/en-US/docs/Web/API/ScreenDetailed/top)Read onlyExperimental

A number representing the y-coordinate (top edge) of the total screen area.

## [Events](#events)

Inherits events from its parent, [Screen](/en-US/docs/Web/API/Screen).

[change 
Experimental](#change)

Fired on a specific screen when any property of the screen changes — width or height, available width or available height, color depth, or orientation, screen position and available screen position, device pixel ratio, label or screen's designation.

## [Examples](#examples)

When [Window.getScreenDetails()](/en-US/docs/Web/API/Window/getScreenDetails) is invoked, the user will be asked for permission to manage windows on all their displays (the status of this permission can be checked using [Permissions.query()](/en-US/docs/Web/API/Permissions/query) to query `window-management`). Provided they grant permission, the resulting [ScreenDetails](/en-US/docs/Web/API/ScreenDetails) object contains `ScreenDetailed` objects representing all the screens available to the user's system.

The following example opens a window in the top-left corner of the OS primary screen:

js

```
// Return ScreenDetails
const allScreens = await window.getScreenDetails();

// Return the primary screen ScreenDetailed object
const primaryScreenDetailed = allScreens.screens.find(
  (screenDetailed) => screenDetailed.isPrimary,
);

// Open a window in the top-left corner of the OS primary screen
window.open(
  "https://example.com",
  "_blank",
  `left=${primaryScreenDetailed.availLeft},
   top=${primaryScreenDetailed.availTop},
   width=200,
   height=200`,
);
```

Note: See [Multi-window learning environment](https://mdn.github.io/dom-examples/window-management-api/) for a full example (see the [source code](https://github.com/mdn/dom-examples/tree/main/window-management-api) also).

## [Specifications](#specifications)

Specification
[Window Management# api-screendetailed-interface](https://w3c.github.io/window-management/#api-screendetailed-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Window Management API](/en-US/docs/Web/API/Window_Management_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/ScreenDetailed/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/screendetailed/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreenDetailed&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fscreendetailed%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreenDetailed%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fscreendetailed%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4f35a8237ee0842beb9cfef3354e05464ad7ce1a%0A*+Document+last+modified%3A+2024-07-26T03%3A46%3A04.000Z%0A%0A%3C%2Fdetails%3E)
