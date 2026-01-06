# UI Events

## [Concepts and Usage](#concepts_and_usage)

The UI Events API defines a system for handling user interactions such as mouse and keyboard input. This includes:

- events that are fired on specific user actions such key presses or mouse clicks. Most of these events fire on the [Element](/en-US/docs/Web/API/Element) interface, but the events relating to loading and unloading resources fire on the [Window](/en-US/docs/Web/API/Window) interface.
- event interfaces, which are passed into handlers for these events. These interfaces inherit from [Event](/en-US/docs/Web/API/Event) and provide extra information specific to the type of user interaction: for example, the [KeyboardEvent](/en-US/docs/Web/API/KeyboardEvent) is passed into a [keydown](/en-US/docs/Web/API/Element/keydown_event) event handler and provides information about the key that was pressed.

## In this article

- [Concepts and Usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [See also](#see_also)

## [Interfaces](#interfaces)

[CompositionEvent](/en-US/docs/Web/API/CompositionEvent)

Passed into handlers for composition events. Composition events enable a user to enter characters that might not be available on the physical keyboard.

[FocusEvent](/en-US/docs/Web/API/FocusEvent)

Passed into handlers for focus events, which are associated with elements receiving or losing focus.

[InputEvent](/en-US/docs/Web/API/InputEvent)

Passed into handlers for input events, which are associated with the user entering some input; for example, using an [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) element.

[KeyboardEvent](/en-US/docs/Web/API/KeyboardEvent)

Passed into handlers for keyboard up/down events.

[MouseEvent](/en-US/docs/Web/API/MouseEvent)

Passed into event handlers for mouse events, including mouse move, mousing over and out, and mouse button up or down. Note that [auxclick](/en-US/docs/Web/API/Element/auxclick_event), [click](/en-US/docs/Web/API/Element/click_event), and [dblclick](/en-US/docs/Web/API/Element/dblclick_event) events are passed [PointerEvent](/en-US/docs/Web/API/PointerEvent) objects.

[MouseScrollEvent](/en-US/docs/Web/API/MouseScrollEvent)Deprecated

Deprecated, Firefox-only, non-standard interface for scroll events. Use [WheelEvent](/en-US/docs/Web/API/WheelEvent) instead.

[MutationEvent](/en-US/docs/Web/API/MutationEvent)Deprecated

Passed into mutation event handlers, which were designed to allow notifications of changes to the DOM. Now deprecated: use [MutationObserver](/en-US/docs/Web/API/MutationObserver) instead.

[UIEvent](/en-US/docs/Web/API/UIEvent)

A base from which other UI events inherit, and also the event interface passed into some events such as [load](/en-US/docs/Web/API/Window/load_event) and [unload](/en-US/docs/Web/API/Window/unload_event).

[WheelEvent](/en-US/docs/Web/API/WheelEvent)

Passed into the handler for the [wheel](/en-US/docs/Web/API/Element/wheel_event) event, which fires when the user rotates a mouse wheel or similar user interface component such as a touchpad.

## [Events](#events)

`abort`

Fired when loading a resource has been aborted (for example, because the user canceled it).

[auxclick](/en-US/docs/Web/API/Element/auxclick_event)

Fired when the user clicks the non-primary pointer button.

[beforeinput](/en-US/docs/Web/API/Element/beforeinput_event)

Fired just before the DOM is about to be updated with some user input.

[blur](/en-US/docs/Web/API/Element/blur_event)

Fired when an element has lost focus.

[click](/en-US/docs/Web/API/Element/click_event)

Fired when the user clicks the primary pointer button.

[compositionend](/en-US/docs/Web/API/Element/compositionend_event)

Fired when a text composition system (such as a speech-to-text processor) has finished its session; for example, because the user has closed it.

[compositionstart](/en-US/docs/Web/API/Element/compositionstart_event)

Fired when the user has started a new session with a text composition system.

[compositionupdate](/en-US/docs/Web/API/Element/compositionupdate_event)

Fired when a text composition system updates its text with a new character, reflected in an update to the `data` property of the [CompositionEvent](/en-US/docs/Web/API/CompositionEvent).

[contextmenu](/en-US/docs/Web/API/Element/contextmenu_event)

Fired just before a context menu is invoked.

[dblclick](/en-US/docs/Web/API/Element/dblclick_event)

Fired when the user double-clicks the primary pointer button.

[error](/en-US/docs/Web/API/HTMLElement/error_event)

Fired when a resource fails to load or can't be processed (for example, if an image is invalid or a script has an error).

[focus](/en-US/docs/Web/API/Element/focus_event)

Fired when an element has received focus.

[focusin](/en-US/docs/Web/API/Element/focusin_event)

Fired when an element is just about to receive focus.

[focusout](/en-US/docs/Web/API/Element/focusout_event)

Fired when an element is just about to lose focus.

[input](/en-US/docs/Web/API/Element/input_event)

Fired just after the DOM has been updated with some user input (for example, some text input).

[keydown](/en-US/docs/Web/API/Element/keydown_event)

Fired when the user has pressed a key.

[keypress](/en-US/docs/Web/API/Element/keypress_event)Deprecated

Fired when the user has pressed a key, only if the key produces a character value. Use [keydown](/en-US/docs/Web/API/Element/keydown_event) instead.

[keyup](/en-US/docs/Web/API/Element/keyup_event)

Fired when the user has released a key.

[load](/en-US/docs/Web/API/Window/load_event)

Fired when the whole page has loaded, including all dependent resources such as stylesheets and images.

[mousedown](/en-US/docs/Web/API/Element/mousedown_event)

Fired when the user presses a button on a mouse or other pointing device, while the pointer is over the element.

[mouseenter](/en-US/docs/Web/API/Element/mouseenter_event)

Fired when a mouse or other pointing device is moved inside the boundary of the element or one of its descendants.

[mouseleave](/en-US/docs/Web/API/Element/mouseleave_event)

Fired when a mouse or other pointing device is moved outside the boundary of the element and all of its descendants.

[mousemove](/en-US/docs/Web/API/Element/mousemove_event)

Fired when a mouse or other pointing device is moved while over an element.

[mouseout](/en-US/docs/Web/API/Element/mouseout_event)

Fired when a mouse or other pointing device is moved outside the boundary of the element.

[mouseover](/en-US/docs/Web/API/Element/mouseover_event)

Fired when a mouse or other pointing device is moved over an element.

[mouseup](/en-US/docs/Web/API/Element/mouseup_event)

Fired when the user releases a button on a mouse or other pointing device, while the pointer is over the element.

[unload](/en-US/docs/Web/API/Window/unload_event)

Fired when the document or a child resource are being unloaded.

[wheel](/en-US/docs/Web/API/Element/wheel_event)

Fired when the user rotates a mouse wheel or similar user interface component such as a touchpad.

## [Examples](#examples)

### [Mouse events](#mouse_events)

This example logs mouse events along with the X and Y coordinates at which the event was generated. Try moving the mouse into the yellow and red squares, and clicking or double-clicking.

#### HTML

html

```
<div id="outer">
  <div id="inner"></div>
</div>

<div id="log">
  <pre id="contents"></pre>
  <button id="clear">Clear log</button>
</div>
```

#### CSS

css

```
body {
  display: flex;
  gap: 1rem;
}

#outer {
  height: 200px;
  width: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: yellow;
}

#inner {
  height: 100px;
  width: 100px;
  background-color: red;
}

#contents {
  height: 150px;
  width: 250px;
  border: 1px solid black;
  padding: 0.5rem;
  overflow: scroll;
}
```

#### JavaScript

js

```
const outer = document.querySelector("#outer");
const inner = document.querySelector("#inner");
const contents = document.querySelector("#contents");
const clear = document.querySelector("#clear");
let lines = 0;

outer.addEventListener("click", (event) => {
  log(event);
});

outer.addEventListener("dblclick", (event) => {
  log(event);
});

outer.addEventListener("mouseover", (event) => {
  log(event);
});

outer.addEventListener("mouseout", (event) => {
  log(event);
});

outer.addEventListener("mouseenter", (event) => {
  log(event);
});

outer.addEventListener("mouseleave", (event) => {
  log(event);
});

function log(event) {
  const prefix = `${String(lines++).padStart(3, "0")}: `;
  const line = `${event.type}(${event.clientX}, ${event.clientY})`;
  contents.textContent = `${contents.textContent}${prefix}${line}\n`;
  contents.scrollTop = contents.scrollHeight;
}

clear.addEventListener("click", () => {
  contents.textContent = "";
  lines = 0;
});
```

#### Result

### [Keyboard and input events](#keyboard_and_input_events)

This example logs [keydown](/en-US/docs/Web/API/Element/keydown_event), [beforeinput](/en-US/docs/Web/API/Element/beforeinput_event) and, [input](/en-US/docs/Web/API/Element/input_event) events. Try typing into the text area. Note that keys like Shift produce `keydown` events but not `input` events.

#### HTML

html

```
<textarea id="story" rows="5" cols="33"></textarea>

<div id="log">
  <pre id="contents"></pre>
  <button id="clear">Clear log</button>
</div>
```

#### CSS

css

```
body {
  display: flex;
  gap: 1rem;
}

#story {
  padding: 0.5rem;
}

#contents {
  height: 150px;
  width: 250px;
  border: 1px solid black;
  padding: 0.5rem;
  overflow: scroll;
}
```

#### JavaScript

js

```
const story = document.querySelector("#story");
const contents = document.querySelector("#contents");
const clear = document.querySelector("#clear");
let lines = 0;

story.addEventListener("keydown", (event) => {
  log(`${event.type}(${event.key})`);
});

story.addEventListener("beforeinput", (event) => {
  log(`${event.type}(${event.data})`);
});

story.addEventListener("input", (event) => {
  log(`${event.type}(${event.data})`);
});

function log(line) {
  const prefix = `${String(lines++).padStart(3, "0")}: `;
  contents.textContent = `${contents.textContent}${prefix}${line}\n`;
  contents.scrollTop = contents.scrollHeight;
}

clear.addEventListener("click", () => {
  contents.textContent = "";
  lines = 0;
});
```

#### Result

## [Specifications](#specifications)

Specification[UI Events](https://w3c.github.io/uievents/)

## [See also](#see_also)

- [Pointer Events API](/en-US/docs/Web/API/Pointer_events)
- [Touch Events](/en-US/docs/Web/API/Touch_events)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/UI_Events/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/ui_events/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUI_Events&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fui_events%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUI_Events%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fui_events%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbe1922d62a0d31e4e3441db0e943aed8df736481%0A*+Document+last+modified%3A+2025-04-28T14%3A28%3A26.000Z%0A%0A%3C%2Fdetails%3E)
