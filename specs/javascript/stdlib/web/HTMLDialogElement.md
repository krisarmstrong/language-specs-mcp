# HTMLDialogElement

The `HTMLDialogElement` interface provides methods to manipulate [<dialog>](/en-US/docs/Web/HTML/Reference/Elements/dialog) elements. It inherits properties and methods from the [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLDialogElement.closedBy](/en-US/docs/Web/API/HTMLDialogElement/closedBy)

A string that sets or returns the [closedby](/en-US/docs/Web/HTML/Reference/Elements/dialog#closedby) attribute value of the `<dialog>` element, which indicates the types of user actions that can be used to close the dialog.

[HTMLDialogElement.open](/en-US/docs/Web/API/HTMLDialogElement/open)

A boolean value reflecting the [open](/en-US/docs/Web/HTML/Reference/Elements/dialog#open) HTML attribute, indicating whether the dialog is available for interaction.

[HTMLDialogElement.returnValue](/en-US/docs/Web/API/HTMLDialogElement/returnValue)

A string that sets or returns the return value for the dialog.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLDialogElement.close()](/en-US/docs/Web/API/HTMLDialogElement/close)

Closes the dialog. An optional string may be passed as an argument, updating the `returnValue` of the dialog.

[HTMLDialogElement.requestClose()](/en-US/docs/Web/API/HTMLDialogElement/requestClose)

Requests to close the dialog. An optional string may be passed as an argument, updating the `returnValue` of the dialog.

[HTMLDialogElement.show()](/en-US/docs/Web/API/HTMLDialogElement/show)

Displays the dialog modelessly, i.e., still allowing interaction with content outside of the dialog.

[HTMLDialogElement.showModal()](/en-US/docs/Web/API/HTMLDialogElement/showModal)

Displays the dialog as a modal, over the top of any other dialogs that might be present. Everything outside the dialog are [inert](/en-US/docs/Web/API/HTMLElement/inert) with interactions outside the dialog being blocked.

## [Events](#events)

Also inherits events from its parent interface, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[cancel](/en-US/docs/Web/API/HTMLDialogElement/cancel_event)

Fired when the dialog is requested to close, whether with the escape key, or via the `HTMLDialogElement.requestClose()` method.

[close](/en-US/docs/Web/API/HTMLDialogElement/close_event)

Fired when the dialog is closed, whether with the escape key, the `HTMLDialogElement.close()` method, or via submitting a form within the dialog with [method="dialog"](/en-US/docs/Web/HTML/Reference/Elements/form#method).

## [Examples](#examples)

### [Opening a modal dialog](#opening_a_modal_dialog)

The following example shows a button that, when clicked, uses the [HTMLDialogElement.showModal()](/en-US/docs/Web/API/HTMLDialogElement/showModal) function to open a modal [<dialog>](/en-US/docs/Web/HTML/Reference/Elements/dialog) containing a form.

While open, everything other than the modal dialog's contents is inert. You can click the Cancel button to close the dialog (via the [HTMLDialogElement.close()](/en-US/docs/Web/API/HTMLDialogElement/close) function), or submit the form via the Confirm button.

The example demonstrates how you might use all the "state change" events that can be fired on the dialog: [cancel](/en-US/docs/Web/API/HTMLDialogElement/cancel_event) and [close](/en-US/docs/Web/API/HTMLDialogElement/close_event), and the inherited events [beforetoggle](/en-US/docs/Web/API/HTMLElement/beforetoggle_event), and [toggle](/en-US/docs/Web/API/HTMLElement/toggle_event).

#### HTML

html

```
<!-- pop-up dialog box, containing a form -->
<dialog id="favDialog">
  <form method="dialog">
    <p>
      <label for="favAnimal">Favorite animal:</label>
      <select id="favAnimal" name="favAnimal">
        <option></option>
        <option>Brine shrimp</option>
        <option>Red panda</option>
        <option>Spider monkey</option>
      </select>
    </p>
    <div>
      <button id="cancel" type="reset">Cancel</button>
      <button id="submit" type="submit">Confirm</button>
    </div>
  </form>
</dialog>

<div>
  <button id="updateDetails">Update details</button>
</div>
```

```
<pre id="log"></pre>
```

```
#log {
  height: 150px;
  overflow: scroll;
  padding: 0.5rem;
  border: 1px solid black;
}
```

```
const logElement = document.querySelector("#log");
function log(text) {
  logElement.innerText = `${logElement.innerText}${text}\n`;
  logElement.scrollTop = logElement.scrollHeight;
}
```

#### JavaScript

##### Showing the dialog

The code first gets objects for the [<button>](/en-US/docs/Web/HTML/Reference/Elements/button) elements, the [<dialog>](/en-US/docs/Web/HTML/Reference/Elements/dialog) element, and the [<select>](/en-US/docs/Web/HTML/Reference/Elements/select) element. It then adds a listener to call the [HTMLDialogElement.showModal()](/en-US/docs/Web/API/HTMLDialogElement/showModal) function when the Update button is clicked.

js

```
const updateButton = document.getElementById("updateDetails");
const confirmButton = document.getElementById("submit");
const cancelButton = document.getElementById("cancel");
const dialog = document.getElementById("favDialog");
const selectElement = document.getElementById("favAnimal");

// Update button opens a modal dialog
updateButton.addEventListener("click", () => {
  dialog.showModal();
});
```

##### Cancel and confirm buttons

Next we add listeners to the Confirm and Cancel button `click` events. The handlers call [HTMLDialogElement.close()](/en-US/docs/Web/API/HTMLDialogElement/close) with the selection value (if present) and no value, which in turn set the return value of the dialog ([HTMLDialogElement.returnValue](/en-US/docs/Web/API/HTMLDialogElement/returnValue)) to the selection value and `null`, respectively.

js

```
// Confirm button closes dialog if there is a selection.
confirmButton.addEventListener("click", () => {
  if (selectElement.value) {
    // Set dialog.returnValue to selected value
    dialog.close(selectElement.value);
  }
});

// Cancel button closes the dialog box
cancelButton.addEventListener("click", () => {
  dialog.close(); // Set dialog.returnValue to null
});
```

Calling `close()` also fires the [close](/en-US/docs/Web/API/HTMLDialogElement/close_event) event, which we implement below by logging the return value of the dialog. If the Confirm button was clicked this should be the selected value in the dialog, otherwise it should be `null`.

js

```
dialog.addEventListener("close", (event) => {
  log(`close_event: (dialog.returnValue: "${dialog.returnValue}")`);
});
```

##### Cancel event

The [cancel](/en-US/docs/Web/API/HTMLDialogElement/cancel_event) event is fired when "platform specific methods" are used to close the dialog, such as the Esc key. It is also fired when the `HTMLDialogElement.requestClose()` method is called. The event is "cancelable" which means that we could use it to prevent the dialog from closing. Here we just treat the cancel as a "close" operation, and reset the [HTMLDialogElement.returnValue](/en-US/docs/Web/API/HTMLDialogElement/returnValue) to `""` to clear any value that may have been set.

js

```
dialog.addEventListener("cancel", (event) => {
  log(`cancel_event: (dialog.returnValue: "${dialog.returnValue}")`);
  dialog.returnValue = ""; // Reset value
});
```

##### Toggle event

The [toggle event](/en-US/docs/Web/API/HTMLElement/toggle_event) (inherited from `HTMLElement`) is fired just after a dialog has opened or closed (but before the `closed` event).

Here we add a listener to log when the Dialog opens and closes.

Note: The `toggle` and `beforetoggle` events may not be fired at dialog elements on all browsers. On these browser versions you can instead check the [HTMLDialogElement.open](/en-US/docs/Web/API/HTMLDialogElement/open) property after attempting to open/close the dialog.

js

```
dialog.addEventListener("toggle", (event) => {
  log(`toggle_event: Dialog ${event.newState}`);
});
```

##### Beforetoggle event

The [beforetoggle event](/en-US/docs/Web/API/HTMLElement/beforetoggle_event) (inherited from `HTMLElement`) is a cancellable event that is fired just before a dialog is opened or closed. If needed, this can be used to prevent a dialog from showing, or to perform actions on other elements that are affected by the dialog open/close state, such as adding classes on them to trigger animations.

In this case we just log the old and new state.

js

```
dialog.addEventListener("beforetoggle", (event) => {
  log(
    `beforetoggle event: oldState: ${event.oldState}, newState: ${event.newState}`,
  );

  // Call event.preventDefault() to prevent a dialog opening
  /*
    if (shouldCancel()) {
        event.preventDefault();
    }
  */
});
```

#### Result

Try out the example below. Note that both `Confirm` and `Cancel` buttons result in the `close` event being fired, and that the result should reflect the selected dialog option.

## [Specifications](#specifications)

Specification
[HTML# htmldialogelement](https://html.spec.whatwg.org/multipage/interactive-elements.html#htmldialogelement)
[HTML# event-beforetoggle](https://html.spec.whatwg.org/multipage/indices.html#event-beforetoggle)
[HTML# event-toggle](https://html.spec.whatwg.org/multipage/indices.html#event-toggle)

## [Browser compatibility](#browser_compatibility)

### [api.HTMLDialogElement](#api.HTMLDialogElement)

### [api.HTMLElement.beforetoggle_event.dialog_elements](#api.HTMLElement.beforetoggle_event.dialog_elements)

### [api.HTMLElement.toggle_event.dialog_elements](#api.HTMLElement.toggle_event.dialog_elements)

## [See also](#see_also)

- The HTML element implementing this interface: [<dialog>](/en-US/docs/Web/HTML/Reference/Elements/dialog).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 25, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLDialogElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmldialogelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLDialogElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmldialogelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLDialogElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmldialogelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbec7ef59277e752985de0ee963c86f6e8e4b3400%0A*+Document+last+modified%3A+2025-06-25T18%3A43%3A22.000Z%0A%0A%3C%2Fdetails%3E)
