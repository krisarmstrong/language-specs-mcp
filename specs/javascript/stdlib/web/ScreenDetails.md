# ScreenDetails

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreenDetails&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `ScreenDetails` interface of the [Window Management API](/en-US/docs/Web/API/Window_Management_API) represents the details of all the screens available to the user's device.

This information is accessed via the [Window.getScreenDetails()](/en-US/docs/Web/API/Window/getScreenDetails) method.

Note:`ScreenDetails` is a live object, meaning that it updates as the available screens change. You can therefore keep querying the same object to get updated values, rather than repeatedly calling `getScreenDetails()`.

## In this article

- [Instance properties](#instance_properties)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[currentScreen](/en-US/docs/Web/API/ScreenDetails/currentScreen)Read onlyExperimental

A single [ScreenDetailed](/en-US/docs/Web/API/ScreenDetailed) object representing detailed information about the screen that the current browser window is displayed in.

[screens](/en-US/docs/Web/API/ScreenDetails/screens)Read onlyExperimental

An array of [ScreenDetailed](/en-US/docs/Web/API/ScreenDetailed) objects, each one representing detailed information about one specific screen available to the user's device.

Note:`screens` only includes "extended" displays, not those that mirror another display.

## [Events](#events)

[currentscreenchange](/en-US/docs/Web/API/ScreenDetails/currentscreenchange_event)Experimental

Fired when the window's current screen changes in some way — for example available width or height, or orientation.

[screenschange](/en-US/docs/Web/API/ScreenDetails/screenschange_event)Experimental

Fired when screens are connected to or disconnected from the system.

## [Examples](#examples)

Note: See [Multi-window learning environment](https://mdn.github.io/dom-examples/window-management-api/) for a full example (see the [source code](https://github.com/mdn/dom-examples/tree/main/window-management-api) also).

### [Basic screen information access](#basic_screen_information_access)

When [Window.getScreenDetails()](/en-US/docs/Web/API/Window/getScreenDetails) is invoked, the user will be asked for permission to manage windows on all their displays (the status of this permission can be checked using [Permissions.query()](/en-US/docs/Web/API/Permissions/query) to query `window-management`). If the user grants permission, a `ScreenDetails` object is returned. This object contains details of all the screens available to the user's system.

The below example opens a full-size window on each available display.

js

```
const screenDetails = await window.getScreenDetails();

// Open a window on each screen of the device
for (const screen of screenDetails.screens) {
  openWindow(
    screen.availLeft,
    screen.availTop,
    screen.availWidth,
    screen.availHeight,
    url,
  );
}
```

### [Responding to changes in available screens](#responding_to_changes_in_available_screens)

You could use the `screenschange` event to detect when the available screens have changed (perhaps when a screen is plugged in or unplugged), report the change, and update window arrangements to suit the new configuration:

js

```
const screenDetails = await window.getScreenDetails();

// Return the number of screens
let noOfScreens = screenDetails.screens.length;

screenDetails.addEventListener("screenschange", () => {
  // If the new number of screens is different to the old number of screens,
  // report the difference
  if (screenDetails.screens.length !== noOfScreens) {
    console.log(
      `The screen count changed from ${noOfScreens} to ${screenDetails.screens.length}`,
    );

    // Update noOfScreens value
    noOfScreens = screenDetails.screens.length;
  }

  // Open, close, or rearrange windows as needed,
  // to fit the new screen configuration
  updateWindows();
});
```

## [Specifications](#specifications)

Specification
[Window Management# api-screendetails-interface](https://w3c.github.io/window-management/#api-screendetails-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Window Management API](/en-US/docs/Web/API/Window_Management_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ScreenDetails/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/screendetails/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreenDetails&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fscreendetails%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreenDetails%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fscreendetails%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa84b606ffd77c40a7306be6c932a74ab9ce6ab96%0A*+Document+last+modified%3A+2025-06-24T06%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
