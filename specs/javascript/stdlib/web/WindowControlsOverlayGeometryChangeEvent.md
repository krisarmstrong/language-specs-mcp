# WindowControlsOverlayGeometryChangeEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindowControlsOverlayGeometryChangeEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `WindowControlsOverlayGeometryChangeEvent` interface of the [Window Controls Overlay API](/en-US/docs/Web/API/Window_Controls_Overlay_API) is passed to [geometrychange](/en-US/docs/Web/API/WindowControlsOverlay/geometrychange_event) when the size or visibility of a desktop Progress Web App's title bar region changes.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[WindowControlsOverlayGeometryChangeEvent()](/en-US/docs/Web/API/WindowControlsOverlayGeometryChangeEvent/WindowControlsOverlayGeometryChangeEvent)Experimental

Creates a `WindowControlsOverlayGeometryChangeEvent` event with the given parameters.

## [Instance properties](#instance_properties)

Also inherits properties from its parent [Event](/en-US/docs/Web/API/Event).

[WindowControlsOverlayGeometryChangeEvent.titlebarAreaRect](/en-US/docs/Web/API/WindowControlsOverlayGeometryChangeEvent/titlebarAreaRect)Read onlyExperimental

A [DOMRect](/en-US/docs/Web/API/DOMRect) representing the position and size of the title bar region.

[WindowControlsOverlayGeometryChangeEvent.visible](/en-US/docs/Web/API/WindowControlsOverlayGeometryChangeEvent/visible)Read onlyExperimental

A [Boolean](/en-US/docs/Glossary/Boolean) that indicates whether the window controls overlay is visible or not.

## [Examples](#examples)

The following example shows how to use a `WindowControlsOverlayGeometryChangeEvent` instance by adding an event handler on the [Navigator.windowControlsOverlay](/en-US/docs/Web/API/Navigator/windowControlsOverlay) property, to listen to geometry changes of a PWA's title bar region.

js

```
if ("windowControlsOverlay" in navigator) {
  navigator.windowControlsOverlay.addEventListener(
    "geometrychange",
    (event) => {
      if (event.visible) {
        const rect = event.titlebarAreaRect;
        // Do something with the coordinates of the title bar area.
      }
    },
  );
}
```

## [Specifications](#specifications)

Specification
[Window Controls Overlay# windowcontrolsoverlay-interface](https://wicg.github.io/window-controls-overlay/#windowcontrolsoverlay-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [Window Controls Overlay API](/en-US/docs/Web/API/Window_Controls_Overlay_API).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 10, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/WindowControlsOverlayGeometryChangeEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/windowcontrolsoverlaygeometrychangeevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindowControlsOverlayGeometryChangeEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwindowcontrolsoverlaygeometrychangeevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindowControlsOverlayGeometryChangeEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwindowcontrolsoverlaygeometrychangeevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F195edecd7c4a1205562d2a984bea9e2f8895c479%0A*+Document+last+modified%3A+2023-12-10T07%3A36%3A55.000Z%0A%0A%3C%2Fdetails%3E)
