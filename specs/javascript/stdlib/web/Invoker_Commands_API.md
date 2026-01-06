# Invoker Commands API

The Invoker Commands API provides a way to declaratively assign behaviors to buttons, allowing control of interactive elements when the button is enacted (clicked or invoked via a keypress, such as the spacebar or return key).

## In this article

- [Concepts and usage](#concepts_and_usage)
- [HTML attributes](#html_attributes)
- [Interfaces](#interfaces)
- [Extensions to other interfaces](#extensions_to_other_interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

A common pattern on the web is to have [<button>](/en-US/docs/Web/HTML/Reference/Elements/button) elements control various aspects of the page, such as opening and closing [popovers](/en-US/docs/Web/API/Popover_API) or [<dialog>](/en-US/docs/Web/HTML/Reference/Elements/dialog) elements, formatting text, and more.

Historically creating these kinds of controls has required JavaScript event listeners added to the button which can then call the APIs on the element they control. The [commandForElement](/en-US/docs/Web/API/HTMLButtonElement/commandForElement) and [command](/en-US/docs/Web/API/HTMLButtonElement/command) properties provide a way to do this declaratively for a limited set of actions. This can be advantageous for built-in commands as the user does not have to wait for JavaScript to download and execute to make these buttons interactive.

## [HTML attributes](#html_attributes)

[commandfor](/en-US/docs/Web/HTML/Reference/Elements/button#commandfor)

Turns a [<button>](/en-US/docs/Web/HTML/Reference/Elements/button) element into a button, controlling the given interactive element; takes the ID of the element to control as its value.

[command](/en-US/docs/Web/HTML/Reference/Elements/button#command)

Specifies the action to be performed on an element being controlled by a control `<button>`, specified via the `commandfor` attribute.

## [Interfaces](#interfaces)

[CommandEvent](/en-US/docs/Web/API/CommandEvent)

Represents an event notifying the user that a command has been issued. It is the event object for the [command](/en-US/docs/Web/API/HTMLElement/command_event) event. The event fires on element referenced by [commandForElement](/en-US/docs/Web/API/HTMLButtonElement/commandForElement).

## [Extensions to other interfaces](#extensions_to_other_interfaces)

### [Instance properties](#instance_properties)

[HTMLButtonElement.commandForElement](/en-US/docs/Web/API/HTMLButtonElement/commandForElement)

Gets and sets the element being controlled by the button. The JavaScript equivalent of the [commandfor](/en-US/docs/Web/HTML/Reference/Elements/button#commandfor) HTML attribute.

[HTMLButtonElement.command](/en-US/docs/Web/API/HTMLButtonElement/command)

Gets and sets the action to be performed on the element being controlled by the button. Reflects the value of the [command](/en-US/docs/Web/HTML/Reference/Elements/button#command) HTML attribute.

### [Events](#events)

[command](/en-US/docs/Web/API/HTMLElement/command_event) event

Fired on the element referenced by the button.

## [Examples](#examples)

### [Creating declarative popovers](#creating_declarative_popovers)

html

```
<button commandfor="mypopover" command="toggle-popover">
  Toggle the popover
</button>
<div id="mypopover" popover>
  <button commandfor="mypopover" command="hide-popover">Close</button>
  Popover content
</div>
```

### [Creating declarative dialogs](#creating_declarative_dialogs)

html

```
<button commandfor="mydialog" command="show-modal">Show modal dialog</button>
<dialog id="mydialog">
  <button commandfor="mydialog" command="close">Close</button>
  Dialog Content
</dialog>
```

### [Creating custom commands](#creating_custom_commands)

html

```
<button commandfor="my-img" command="--rotate-left">Rotate left</button>
<button commandfor="my-img" command="--rotate-right">Rotate right</button>
<img id="my-img" src="photo.jpg" alt="[add appropriate alt text here]" />
```

js

```
const myImg = document.getElementById("my-img");

myImg.addEventListener("command", (event) => {
  if (event.command === "--rotate-left") {
    myImg.style.rotate = "-90deg";
  } else if (event.command === "--rotate-right") {
    myImg.style.rotate = "90deg";
  }
});
```

## [Specifications](#specifications)

Specification
[HTML# commandevent](https://html.spec.whatwg.org/multipage/interaction.html#commandevent)
[HTML# dom-button-commandforelement](https://html.spec.whatwg.org/multipage/form-elements.html#dom-button-commandforelement)
[HTML# dom-button-command](https://html.spec.whatwg.org/multipage/form-elements.html#dom-button-command)

## [Browser compatibility](#browser_compatibility)

### [api.CommandEvent](#api.CommandEvent)

### [api.HTMLButtonElement.commandForElement](#api.HTMLButtonElement.commandForElement)

### [api.HTMLButtonElement.command](#api.HTMLButtonElement.command)

## [See also](#see_also)

- [command](/en-US/docs/Web/API/HTMLButtonElement/command) property
- [commandForElement](/en-US/docs/Web/API/HTMLButtonElement/commandForElement) property
- [CommandEvent](/en-US/docs/Web/API/CommandEvent) interface

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Invoker_Commands_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/invoker_commands_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInvoker_Commands_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Finvoker_commands_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInvoker_Commands_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Finvoker_commands_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fffa6f5871f50856c60983a125cef7de267be7aeb%0A*+Document+last+modified%3A+2025-05-27T12%3A53%3A43.000Z%0A%0A%3C%2Fdetails%3E)
