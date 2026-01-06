# MouseEvent

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMouseEvent&level=high)

The `MouseEvent` interface represents events that occur due to the user interacting with a pointing device (such as a mouse). Common events using this interface include [click](/en-US/docs/Web/API/Element/click_event), [dblclick](/en-US/docs/Web/API/Element/dblclick_event), [mouseup](/en-US/docs/Web/API/Element/mouseup_event), [mousedown](/en-US/docs/Web/API/Element/mousedown_event).

`MouseEvent` derives from [UIEvent](/en-US/docs/Web/API/UIEvent), which in turn derives from [Event](/en-US/docs/Web/API/Event). Though the [MouseEvent.initMouseEvent()](/en-US/docs/Web/API/MouseEvent/initMouseEvent) method is kept for backward compatibility, creating of a `MouseEvent` object should be done using the [MouseEvent()](/en-US/docs/Web/API/MouseEvent/MouseEvent) constructor.

Several more specific events are based on `MouseEvent`, including [WheelEvent](/en-US/docs/Web/API/WheelEvent), [DragEvent](/en-US/docs/Web/API/DragEvent), and [PointerEvent](/en-US/docs/Web/API/PointerEvent).

## In this article

- [Constructor](#constructor)
- [Static properties](#static_properties)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[MouseEvent()](/en-US/docs/Web/API/MouseEvent/MouseEvent)

Creates a `MouseEvent` object.

## [Static properties](#static_properties)

[MouseEvent.WEBKIT_FORCE_AT_MOUSE_DOWN](/en-US/docs/Web/API/MouseEvent/WEBKIT_FORCE_AT_MOUSE_DOWN_static)Non-standardRead only

Minimum force necessary for a normal click.

[MouseEvent.WEBKIT_FORCE_AT_FORCE_MOUSE_DOWN](/en-US/docs/Web/API/MouseEvent/WEBKIT_FORCE_AT_FORCE_MOUSE_DOWN_static)Non-standardRead only

Minimum force necessary for a force click.

## [Instance properties](#instance_properties)

This interface also inherits properties of its parents, [UIEvent](/en-US/docs/Web/API/UIEvent) and [Event](/en-US/docs/Web/API/Event).

[MouseEvent.altKey](/en-US/docs/Web/API/MouseEvent/altKey)Read only

Returns `true` if the alt key was down when the mouse event was fired.

[MouseEvent.button](/en-US/docs/Web/API/MouseEvent/button)Read only

The button number that was pressed or released (if applicable) when the mouse event was fired.

[MouseEvent.buttons](/en-US/docs/Web/API/MouseEvent/buttons)Read only

The buttons being pressed (if any) when the mouse event was fired.

[MouseEvent.clientX](/en-US/docs/Web/API/MouseEvent/clientX)Read only

The X coordinate of the mouse pointer in [viewport coordinates](/en-US/docs/Web/API/CSSOM_view_API/Coordinate_systems#viewport).

[MouseEvent.clientY](/en-US/docs/Web/API/MouseEvent/clientY)Read only

The Y coordinate of the mouse pointer in [viewport coordinates](/en-US/docs/Web/API/CSSOM_view_API/Coordinate_systems#viewport).

[MouseEvent.ctrlKey](/en-US/docs/Web/API/MouseEvent/ctrlKey)Read only

Returns `true` if the control key was down when the mouse event was fired.

[MouseEvent.layerX](/en-US/docs/Web/API/MouseEvent/layerX)Non-standardRead only

Returns the horizontal coordinate of the event relative to the current layer.

[MouseEvent.layerY](/en-US/docs/Web/API/MouseEvent/layerY)Non-standardRead only

Returns the vertical coordinate of the event relative to the current layer.

[MouseEvent.metaKey](/en-US/docs/Web/API/MouseEvent/metaKey)Read only

Returns `true` if the meta key was down when the mouse event was fired.

[MouseEvent.movementX](/en-US/docs/Web/API/MouseEvent/movementX)Read only

The X coordinate of the mouse pointer relative to the position of the last [mousemove](/en-US/docs/Web/API/Element/mousemove_event) event.

[MouseEvent.movementY](/en-US/docs/Web/API/MouseEvent/movementY)Read only

The Y coordinate of the mouse pointer relative to the position of the last [mousemove](/en-US/docs/Web/API/Element/mousemove_event) event.

[MouseEvent.offsetX](/en-US/docs/Web/API/MouseEvent/offsetX)Read only

The X coordinate of the mouse pointer relative to the position of the padding edge of the target node.

[MouseEvent.offsetY](/en-US/docs/Web/API/MouseEvent/offsetY)Read only

The Y coordinate of the mouse pointer relative to the position of the padding edge of the target node.

[MouseEvent.pageX](/en-US/docs/Web/API/MouseEvent/pageX)Read only

The X coordinate of the mouse pointer relative to the whole document.

[MouseEvent.pageY](/en-US/docs/Web/API/MouseEvent/pageY)Read only

The Y coordinate of the mouse pointer relative to the whole document.

[MouseEvent.relatedTarget](/en-US/docs/Web/API/MouseEvent/relatedTarget)Read only

The secondary target for the event, if there is one.

[MouseEvent.screenX](/en-US/docs/Web/API/MouseEvent/screenX)Read only

The X coordinate of the mouse pointer in [screen coordinates](/en-US/docs/Web/API/CSSOM_view_API/Coordinate_systems#screen).

[MouseEvent.screenY](/en-US/docs/Web/API/MouseEvent/screenY)Read only

The Y coordinate of the mouse pointer in [screen coordinates](/en-US/docs/Web/API/CSSOM_view_API/Coordinate_systems#screen).

[MouseEvent.shiftKey](/en-US/docs/Web/API/MouseEvent/shiftKey)Read only

Returns `true` if the shift key was down when the mouse event was fired.

[MouseEvent.mozInputSource](/en-US/docs/Web/API/MouseEvent/mozInputSource)Non-standardRead only

The type of device that generated the event (one of the `MOZ_SOURCE_*` constants). This lets you, for example, determine whether a mouse event was generated by an actual mouse or by a touch event (which might affect the degree of accuracy with which you interpret the coordinates associated with the event).

[MouseEvent.webkitForce](/en-US/docs/Web/API/MouseEvent/webkitForce)Non-standardRead only

The amount of pressure applied when clicking.

[MouseEvent.x](/en-US/docs/Web/API/MouseEvent/x)Read only

Alias for [MouseEvent.clientX](/en-US/docs/Web/API/MouseEvent/clientX).

[MouseEvent.y](/en-US/docs/Web/API/MouseEvent/y)Read only

Alias for [MouseEvent.clientY](/en-US/docs/Web/API/MouseEvent/clientY).

## [Instance methods](#instance_methods)

This interface also inherits methods of its parents, [UIEvent](/en-US/docs/Web/API/UIEvent) and [Event](/en-US/docs/Web/API/Event).

[MouseEvent.getModifierState()](/en-US/docs/Web/API/MouseEvent/getModifierState)

Returns the current state of the specified modifier key. See [KeyboardEvent.getModifierState()](/en-US/docs/Web/API/KeyboardEvent/getModifierState) for details.

[MouseEvent.initMouseEvent()](/en-US/docs/Web/API/MouseEvent/initMouseEvent)Deprecated

Initializes the value of a `MouseEvent` created. If the event has already been dispatched, this method does nothing.

## [Example](#example)

This example demonstrates simulating a click (programmatically generating a click event) on a checkbox using DOM methods. Event state (canceled or not) is then determined with the return value of method [EventTarget.dispatchEvent()](/en-US/docs/Web/API/EventTarget/dispatchEvent).

### [HTML](#html)

html

```
<p>
  <label><input type="checkbox" id="checkbox" /> Checked</label>
</p>
<p>
  <button id="button">Click me to send a MouseEvent to the checkbox</button>
</p>
```

### [JavaScript](#javascript)

js

```
function simulateClick() {
  // Get the element to send a click event
  const cb = document.getElementById("checkbox");

  // Create a synthetic click MouseEvent
  let evt = new MouseEvent("click", {
    bubbles: true,
    cancelable: true,
    view: window,
  });

  // Send the event to the checkbox element
  cb.dispatchEvent(evt);
}
document.getElementById("button").addEventListener("click", simulateClick);
```

### [Result](#result)

## [Specifications](#specifications)

Specification
[UI Events# interface-mouseevent](https://w3c.github.io/uievents/#interface-mouseevent)
[CSSOM View Module# extensions-to-the-mouseevent-interface](https://drafts.csswg.org/cssom-view/#extensions-to-the-mouseevent-interface)
[Pointer Lock 2.0# extensions-to-the-mouseevent-interface](https://w3c.github.io/pointerlock/#extensions-to-the-mouseevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- Its direct parent, [UIEvent](/en-US/docs/Web/API/UIEvent)
- [PointerEvent](/en-US/docs/Web/API/PointerEvent): For advanced pointer events, including multi-touch

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MouseEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mouseevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMouseEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmouseevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMouseEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmouseevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F896a41d7d9832367a1e24af567fb419e9d4182f8%0A*+Document+last+modified%3A+2025-09-15T12%3A13%3A21.000Z%0A%0A%3C%2Fdetails%3E)
