# VirtualKeyboard API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVirtualKeyboard_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The VirtualKeyboard API provides developers control over the layout of their applications when the on-screen virtual keyboard appears and disappears on devices such as tablets, mobile phones, or other devices where a hardware keyboard may not be available.

Web browsers usually deal with virtual keyboards on their own, by adjusting the viewport height and scrolling to input fields when focused.

The figure below illustrates the difference in viewport height and scroll position on a web page when the device has its on-screen virtual keyboard hidden, and when it is shown.

More complex applications or specific devices such as multi-screen mobile phones may require more control of the layout when the virtual keyboard appears.

The figure below shows what happens on a dual-screen device when the virtual keyboard appears on just one of the two screens. The viewport becomes smaller on both screens to accommodate for the virtual keyboard, leaving wasted space on the screen where the virtual keyboard is not displayed.

The VirtualKeyboard API can be used to opt out of the way the browser automatically handles the virtual keyboard, and take full control of it instead. With the VirtualKeyboard API, the keyboard still appears and disappears as necessary when form controls are focused, but the viewport does not change, and you can use JavaScript and CSS to adapt your layout.

## In this article

- [Concept](#concept)
- [Interfaces](#interfaces)
- [Extensions to other interfaces](#extensions_to_other_interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concept](#concept)

The VirtualKeyboard API consists of three parts:

- The [VirtualKeyboard](/en-US/docs/Web/API/VirtualKeyboard) interface, accessed through [navigator.virtualKeyboard](/en-US/docs/Web/API/Navigator/virtualKeyboard), is used to opt out of the automatic virtual keyboard behavior, show or hide the virtual keyboard programmatically, as well as get the current position and size of the virtual keyboard.
- The `keyboard-inset-*` CSS environment variables provide information about the virtual keyboard's position and size.
- The [virtualkeyboardpolicy](/en-US/docs/Web/HTML/Reference/Global_attributes/virtualkeyboardpolicy) attribute specifies whether the virtual keyboard should appear on `contenteditable` elements.

### [Opt out of the automatic virtual keyboard behavior](#opt_out_of_the_automatic_virtual_keyboard_behavior)

To opt out of the automatic virtual keyboard behavior of the browser, use `navigator.virtualKeyboard.overlaysContent = true`. The browser will no longer automatically resize the viewport to make space for the virtual keyboard, which will overlay your content instead.

### [Detect the virtual keyboard geometry using JavaScript](#detect_the_virtual_keyboard_geometry_using_javascript)

Once you've opted out of the default browser behavior, you can get the current geometry of the virtual keyboard using `navigator.virtualKeyboard.boundingRect`, and adapt the layout as appropriate using CSS and JavaScript. In addition, you can listen to geometry changes, such as when the keyboard is shown or hidden, by using the `geometrychange` event.

This is useful for positioning important UI elements in the area that's not covered by the virtual keyboard.

The code snippet below uses the `geometrychange` event to detect when the virtual keyboard geometry changes; it then accesses the `boundingRect` property to query the size and position of the virtual keyboard:

js

```
if ("virtualKeyboard" in navigator) {
  navigator.virtualKeyboard.overlaysContent = true;

  navigator.virtualKeyboard.addEventListener("geometrychange", (event) => {
    const { x, y, width, height } = event.target.boundingRect;
  });
}
```

### [Detect the virtual keyboard geometry using CSS environment variables](#detect_the_virtual_keyboard_geometry_using_css_environment_variables)

The VirtualKeyboard API also exposes the following [CSS environment variables](/en-US/docs/Web/CSS/Reference/Values/env): `keyboard-inset-top`, `keyboard-inset-right`, `keyboard-inset-bottom`, `keyboard-inset-left`, `keyboard-inset-width`, and `keyboard-inset-height`.

The `keyboard-inset-*` CSS environment variables are useful to adapt your layout to the virtual keyboard appearance using CSS. They define a rectangle by its top, right, bottom, and left insets from the edge of the viewport. The `width` and `height` variables are also available if needed.

The code snippet below uses the `keyboard-inset-height` CSS variable to reserve space for the virtual keyboard to appear below the list of messages and input field in a chat-like application. When the virtual keyboard is hidden, the `env()` function returns `0px` and the `keyboard` grid area is hidden. The messages and input elements can occupy the full height of the viewport. When the virtual keyboard appears, the `keyboard` grid area gets the height of the virtual keyboard.

html

```
<ul id="messages"></ul>
<input type="text" />
```

css

```
body {
  display: grid;
  margin: 0;
  height: 100vh;
  grid-template:
    "messages" 1fr
    "input" auto
    "keyboard" env(keyboard-inset-height, 0px);
}
```

js

```
if ("virtualKeyboard" in navigator) {
  navigator.virtualKeyboard.overlaysContent = true;
}
```

### [Control the virtual keyboard on contenteditable elements](#control_the_virtual_keyboard_on_contenteditable_elements)

By default, elements using the [contenteditable](/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable) attribute also trigger the virtual keyboard when tapped or clicked. In certain situations, it may be desirable to prevent this behavior and instead show the virtual keyboard after a different event.

Set the [virtualkeyboardpolicy](/en-US/docs/Web/HTML/Reference/Global_attributes/virtualkeyboardpolicy) attribute to `manual` to prevent the default handling of the virtual keyboard in the browser, and instead handle it yourself by using the [VirtualKeyboard](/en-US/docs/Web/API/VirtualKeyboard) interface's `show()` and `hide()` methods.

The code snippet below shows how to use the `virtualkeyboardpolicy` attribute and the `navigator.virtualKeyboard.show()` method to show the virtual keyboard on double-click instead:

html

```
<div contenteditable virtualkeyboardpolicy="manual" id="editor"></div>
```

js

```
if ("virtualKeyboard" in navigator) {
  navigator.virtualKeyboard.overlaysContent = true;

  const editor = document.getElementById("editor");
  editor.addEventListener("dblclick", () => {
    navigator.virtualKeyboard.show();
  });
}
```

## [Interfaces](#interfaces)

[VirtualKeyboard](/en-US/docs/Web/API/VirtualKeyboard)Experimental

Provides functions that retrieve keyboard layout maps and toggle capturing of key presses from the physical keyboard.

## [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.virtualKeyboard](/en-US/docs/Web/API/Navigator/virtualKeyboard)Read onlyExperimental

Returns a reference to the [VirtualKeyboard](/en-US/docs/Web/API/VirtualKeyboard) API, to take control of the on-screen virtual keyboard.

[HTMLElement.virtualkeyboardpolicy](/en-US/docs/Web/API/HTMLElement/virtualKeyboardPolicy)Experimental

A string indicating whether to use the browser's default policy for showing the virtual keyboard when the element is focused, or to handle showing the virtual keyboard manually.

## [Specifications](#specifications)

Specification
[VirtualKeyboard API# the-virtualkeyboard-interface](https://w3c.github.io/virtual-keyboard/#the-virtualkeyboard-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Full control with the VirtualKeyboard API](https://developer.chrome.com/docs/web-platform/virtual-keyboard/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 6, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/VirtualKeyboard_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/virtualkeyboard_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVirtualKeyboard_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvirtualkeyboard_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVirtualKeyboard_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvirtualkeyboard_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff69b6693212029ce4b9fa0c753729044577af548%0A*+Document+last+modified%3A+2025-11-06T14%3A49%3A20.000Z%0A%0A%3C%2Fdetails%3E)
