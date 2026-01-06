# Screen

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreen&level=high)

The `Screen` interface represents a screen, usually the one on which the current window is being rendered, and is obtained using [window.screen](/en-US/docs/Web/API/Window/screen).

Note that browsers determine which screen to report as current by detecting which screen has the center of the browser window.

## In this article

- [Instance properties](#instance_properties)
- [Non-standard properties](#non-standard_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

Also inherits properties from its parent [EventTarget](/en-US/docs/Web/API/EventTarget).

[Screen.availHeight](/en-US/docs/Web/API/Screen/availHeight)

Specifies the height of the screen, in pixels, minus permanent or semipermanent user interface features displayed by the operating system, such as the Taskbar on Windows.

[Screen.availWidth](/en-US/docs/Web/API/Screen/availWidth)

Returns the amount of horizontal space in pixels available to the window.

[Screen.colorDepth](/en-US/docs/Web/API/Screen/colorDepth)

Returns the color depth of the screen.

[Screen.height](/en-US/docs/Web/API/Screen/height)

Returns the height of the screen in pixels.

[Screen.isExtended](/en-US/docs/Web/API/Screen/isExtended)ExperimentalSecure context

Returns `true` if the user's device has multiple screens, and `false` if not.

[Screen.orientation](/en-US/docs/Web/API/Screen/orientation)

Returns the [ScreenOrientation](/en-US/docs/Web/API/ScreenOrientation) instance associated with this screen.

[Screen.pixelDepth](/en-US/docs/Web/API/Screen/pixelDepth)

Gets the bit depth of the screen.

[Screen.width](/en-US/docs/Web/API/Screen/width)

Returns the width of the screen.

[Screen.mozEnabled](/en-US/docs/Web/API/Screen/mozEnabled)Non-standardDeprecated

Boolean. Setting to false will turn off the device's screen.

[Screen.mozBrightness](/en-US/docs/Web/API/Screen/mozBrightness)Non-standardDeprecated

Controls the brightness of a device's screen. A double between 0 and 1.0 is expected.

## [Non-standard properties](#non-standard_properties)

The following properties are specified as part of the [Window Management API](/en-US/docs/Web/API/Window_Management_API), which makes them available on the [ScreenDetailed](/en-US/docs/Web/API/ScreenDetailed) interface; this is where we have chosen to document them. However, non-standard versions of these properties are available on the `Screen` interface in browsers that don't support that API. See this page's [Browser compatibility](#browser_compatibility) table for details of the non-standard support.

[Screen.availLeft](/en-US/docs/Web/API/ScreenDetailed/availLeft)Read onlyNon-standardSecure context

A number representing the x-coordinate (left-hand edge) of the available screen area.

[Screen.availTop](/en-US/docs/Web/API/ScreenDetailed/availTop)Read onlyNon-standardSecure context

A number representing the y-coordinate (top edge) of the available screen area.

[Screen.left](/en-US/docs/Web/API/ScreenDetailed/left)Read onlyNon-standardSecure context

A number representing the x-coordinate (left-hand edge) of the total screen area.

[Screen.top](/en-US/docs/Web/API/ScreenDetailed/top)Read onlyNon-standardDeprecatedSecure context

A number representing the y-coordinate (top edge) of the total screen area.

## [Instance methods](#instance_methods)

Also inherits methods from its parent [EventTarget](/en-US/docs/Web/API/EventTarget).

[Screen.lockOrientation](/en-US/docs/Web/API/Screen/lockOrientation)Deprecated

Lock the screen orientation (only works in fullscreen or for installed apps)

[Screen.unlockOrientation](/en-US/docs/Web/API/Screen/unlockOrientation)Deprecated

Unlock the screen orientation (only works in fullscreen or for installed apps)

## [Events](#events)

[change](/en-US/docs/Web/API/Screen/change_event)ExperimentalSecure context

Fired on a specific screen when it changes in some way — width or height, available width or height, color depth, or orientation.

[orientationchange](/en-US/docs/Web/API/Screen/orientationchange_event)DeprecatedNon-standard

Fires when the screen orientation changes.

## [Examples](#examples)

js

```
if (screen.colorDepth < 8) {
  // use low-color version of page
} else {
  // use regular, colorful page
}
```

## [Specifications](#specifications)

Specification
[CSSOM View Module# the-screen-interface](https://drafts.csswg.org/cssom-view/#the-screen-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Screen/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/screen/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreen&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fscreen%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreen%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fscreen%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F896a41d7d9832367a1e24af567fb419e9d4182f8%0A*+Document+last+modified%3A+2025-09-15T12%3A13%3A21.000Z%0A%0A%3C%2Fdetails%3E)
