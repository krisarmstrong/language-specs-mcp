# Window Controls Overlay API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindow_Controls_Overlay_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Window Controls Overlay API gives Progressive Web Apps installed on desktop operating systems the ability to hide the default window title bar and display their own content over the full surface area of the app window, turning the control buttons (maximize, minimize, and close) into an overlay.

## In this article

- [Opting-in to the feature](#opting-in_to_the_feature)
- [Main concepts](#main_concepts)
- [CSS environment variables](#css_environment_variables)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Opting-in to the feature](#opting-in_to_the_feature)

Before using this feature, the following conditions must be true:

- The Web App Manifest's [display_override](/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/display_override) member must be set to `window-controls-overlay`.
- The Progressive Web App must be installed on a desktop operating system.

## [Main concepts](#main_concepts)

Progressive Web Apps installed on desktop devices can be displayed in standalone app windows, just like native apps. Here is what an application window looks like:

As seen above, the app window is made of two main areas:

- The title bar area at the top.
- The application content area at the bottom, which displays the HTML content from the PWA.

The title bar area contains the system-critical maximize, minimize, and close buttons (their position may vary across operating systems), the name of the application (which comes from the `<title>` HTML element in the page), and possibly user-agent-specific PWA buttons.

With the Window Controls Overlay feature, Progressive Web Apps can display their web content over the whole app window surface area. Because the window control buttons and user-agent-specific PWA buttons must remain visible, they get turned into an overlay displayed on top of the web content.

The part of the title bar that normally contains the application name is hidden, and the area that it normally occupies becomes available via the Window Controls Overlay API.

PWAs can use the API to position content in this area, and avoid having content hidden behind the control buttons overlay, similar to how web authors can account for the presence of notches on certain mobile devices.

## [CSS environment variables](#css_environment_variables)

Progressive Web Apps can position their web content in the area that the title bar normally occupies by using the `titlebar-area-x`, `titlebar-area-y`, `titlebar-area-width`, and `titlebar-area-height` CSS environment variables. See [Using env() to ensure content is not obscured by window control buttons in desktop PWAs](/en-US/docs/Web/CSS/Reference/Values/env#using_env_to_ensure_content_is_not_obscured_by_window_control_buttons_in_desktop_pwas).

## [Interfaces](#interfaces)

[WindowControlsOverlay](/en-US/docs/Web/API/WindowControlsOverlay)Experimental

Provides information about the visibility and geometry of the title bar and an event to know whenever it changes.

[WindowControlsOverlayGeometryChangeEvent](/en-US/docs/Web/API/WindowControlsOverlayGeometryChangeEvent)Experimental

Represents events providing information related to the desktop Progress Web App's title var region when its size or visibility changes.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.windowControlsOverlay](/en-US/docs/Web/API/Navigator/windowControlsOverlay)

Returns the [WindowControlsOverlay](/en-US/docs/Web/API/WindowControlsOverlay) interface, which exposes information about the title bar geometry in desktop Progressive Web Apps.

## [Specifications](#specifications)

Specification[Window Controls Overlay](https://wicg.github.io/window-controls-overlay/)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Customize the window controls overlay of your PWA's title bar](https://web.dev/articles/window-controls-overlay)
- [Breaking Out of the Box](https://alistapart.com/article/breaking-out-of-the-box/)
- [Display content in the title bar](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps/how-to/window-controls-overlay)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 6, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Window_Controls_Overlay_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/window_controls_overlay_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindow_Controls_Overlay_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwindow_controls_overlay_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindow_Controls_Overlay_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwindow_controls_overlay_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff69b6693212029ce4b9fa0c753729044577af548%0A*+Document+last+modified%3A+2025-11-06T14%3A49%3A20.000Z%0A%0A%3C%2Fdetails%3E)
