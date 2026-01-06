# CommandEvent

 Baseline  2025 Newly available

 Since ⁨December 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCommandEvent&level=low)

The `CommandEvent` interface represents an event notifying the user when a [button](/en-US/docs/Web/API/HTMLButtonElement) element with valid [commandForElement](/en-US/docs/Web/API/HTMLButtonElement/commandForElement) and [command](/en-US/docs/Web/API/HTMLButtonElement/command) attributes is about to invoke an interactive element.

This is the event object for the `HTMLElement`[command](/en-US/docs/Web/API/HTMLElement/command_event) event, which represents an action from an Invoker Control when it is invoked (for example when it is clicked or pressed).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[CommandEvent()](/en-US/docs/Web/API/CommandEvent/CommandEvent)

Creates a `CommandEvent` object.

## [Instance properties](#instance_properties)

This interface inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[CommandEvent.source](/en-US/docs/Web/API/CommandEvent/source)Read only

An [HTMLButtonElement](/en-US/docs/Web/API/HTMLButtonElement) representing the button that caused this invocation.

[CommandEvent.command](/en-US/docs/Web/API/CommandEvent/command)Read only

A string representing the [command](/en-US/docs/Web/API/HTMLButtonElement/command) value of the source button.

## [Examples](#examples)

### [Basic example](#basic_example)

html

```
<button commandfor="mypopover" command="show-popover">Show popover</button>

<div popover id="mypopover" role="[declare appropriate ARIA role]">
  <!-- popover content here -->
  <button commandfor="mypopover" command="hide-popover">Hide popover</button>
</div>
```

js

```
const popover = document.getElementById("mypopover");

// …

popover.addEventListener("command", (event) => {
  if (event.command === "show-popover") {
    console.log("Popover is about to be shown");
  }
});
```

### [Using custom values for commands](#using_custom_values_for_commands)

In this example three buttons have been created with [commands with custom values](/en-US/docs/Web/HTML/Reference/Elements/button#custom_values).

html

```
<div class="controls">
  <button commandfor="the-image" command="--rotate-left">Rotate Left</button>
  <button commandfor="the-image" command="--reset">Reset</button>
  <button commandfor="the-image" command="--rotate-right">Rotate Right</button>
</div>

<img
  id="the-image"
  src="/shared-assets/images/examples/dino.svg"
  alt="dinosaur head rotated 0 degrees" />
```

```
.controls {
  margin-block-end: 20px;
}
```

An event listener is attached to the image using the [command event](/en-US/docs/Web/API/HTMLElement/command_event). When one of the buttons is clicked, the listener runs code based on the custom `command` value assigned to the button, rotating the image and also updating it's `alt` text to indicate the new angle of the image.

js

```
const image = document.getElementById("the-image");

image.addEventListener("command", (event) => {
  let rotate = parseInt(event.target.style.rotate || "0", 10);
  if (event.command === "--reset") {
    rotate = 0;
    event.target.style.rotate = `${rotate}deg`;
  } else if (event.command === "--rotate-left") {
    rotate = rotate === -270 ? 0 : rotate - 90;
    event.target.style.rotate = `${rotate}deg`;
  } else if (event.command === "--rotate-right") {
    rotate = rotate === 270 ? 0 : rotate + 90;
    event.target.style.rotate = `${rotate}deg`;
  }
  event.target.alt = `dinosaur head rotated ${rotate} degrees`;
});
```

## [Specifications](#specifications)

Specification
[HTML# commandevent](https://html.spec.whatwg.org/multipage/interaction.html#commandevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Invoker Commands API](/en-US/docs/Web/API/Invoker_Commands_API)
- [HTMLButtonElement.command](/en-US/docs/Web/API/HTMLButtonElement/command)
- [HTMLButtonElement.commandForElement](/en-US/docs/Web/API/HTMLButtonElement/commandForElement)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CommandEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/commandevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCommandEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcommandevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCommandEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcommandevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
