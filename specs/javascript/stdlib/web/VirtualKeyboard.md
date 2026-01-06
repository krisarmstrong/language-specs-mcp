# VirtualKeyboard

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVirtualKeyboard&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `VirtualKeyboard` interface of the [VirtualKeyboard API](/en-US/docs/Web/API/VirtualKeyboard_API) is useful on devices that have on-screen virtual keyboards, such as tablets, mobile phones, or other devices where a hardware keyboard may not be available.

The `VirtualKeyboard` interface makes it possible to opt out of the automatic way browsers handle on-screen virtual keyboards by reducing the height of the viewport to make room for the virtual keyboard. You can prevent the browser from changing the size of the viewport, detect the position and size of the virtual keyboard — adapting the layout of your web page as a follow-up — and programmatically show or hide the virtual keyboard.

You access the `VirtualKeyboard` interface by using [navigator.virtualKeyboard](/en-US/docs/Web/API/Navigator/virtualKeyboard).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `VirtualKeyboard` interface inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[VirtualKeyboard.boundingRect](/en-US/docs/Web/API/VirtualKeyboard/boundingRect)Read onlyExperimental

A [DOMRect](/en-US/docs/Web/API/DOMRect) that describes the geometry of the virtual keyboard.

[VirtualKeyboard.overlaysContent](/en-US/docs/Web/API/VirtualKeyboard/overlaysContent)Experimental

A [Boolean](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean) that defines whether the browser should stop handling the on-screen virtual keyboard.

## [Instance methods](#instance_methods)

The `VirtualKeyboard` interface inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[VirtualKeyboard.show()](/en-US/docs/Web/API/VirtualKeyboard/show)Experimental

Show the virtual keyboard.

[VirtualKeyboard.hide()](/en-US/docs/Web/API/VirtualKeyboard/hide)Experimental

Hide the virtual keyboard.

## [Events](#events)

[geometrychange](/en-US/docs/Web/API/VirtualKeyboard/geometrychange_event)Experimental

Fires when the geometry of the on-screen virtual keyboard changes, which happens when the virtual keyboard appears or disappears.

## [Example](#example)

The following example demonstrates how to opt out of the automatic virtual keyboard behavior, and detect the geometry of the virtual keyboard in the web page:

js

```
if ("virtualKeyboard" in navigator) {
  navigator.virtualKeyboard.overlaysContent = true;

  navigator.virtualKeyboard.addEventListener("geometrychange", (event) => {
    const { x, y, width, height } = event.target.boundingRect;
  });
}
```

## [Specifications](#specifications)

Specification
[VirtualKeyboard API# the-virtualkeyboard-interface](https://w3c.github.io/virtual-keyboard/#the-virtualkeyboard-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [The VirtualKeyboard API](/en-US/docs/Web/API/VirtualKeyboard_API)
- [Full control with the VirtualKeyboard API](https://developer.chrome.com/docs/web-platform/virtual-keyboard/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/VirtualKeyboard/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/virtualkeyboard/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVirtualKeyboard&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvirtualkeyboard%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVirtualKeyboard%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvirtualkeyboard%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5cdb341c723de0edb273769555d9124266d9c851%0A*+Document+last+modified%3A+2023-10-30T09%3A05%3A18.000Z%0A%0A%3C%2Fdetails%3E)
