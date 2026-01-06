# ToggleEvent

 Baseline  2023  * Newly available

 Since ⁨November 2023⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FToggleEvent&level=low)

The `ToggleEvent` interface represents an event that fires when a popover element is toggled between being shown and hidden.

This is the event object for the [beforetoggle](/en-US/docs/Web/API/HTMLElement/beforetoggle_event) and [toggle](/en-US/docs/Web/API/HTMLElement/toggle_event) events, which fire on elements as follows:

- The `beforetoggle` event fires before [popover](/en-US/docs/Web/API/Popover_API) or [<dialog>](/en-US/docs/Web/HTML/Reference/Elements/dialog) elements are shown or hidden.
- The `toggle` event fires after popover, `<dialog>`, or [<details>](/en-US/docs/Web/HTML/Reference/Elements/details) elements are shown or hidden.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ToggleEvent()](/en-US/docs/Web/API/ToggleEvent/ToggleEvent)

Creates a `ToggleEvent` object.

## [Instance properties](#instance_properties)

This interface inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[ToggleEvent.newState](/en-US/docs/Web/API/ToggleEvent/newState)Read only

A string (either `"open"` or `"closed"`), representing the state the element is transitioning to.

[ToggleEvent.oldState](/en-US/docs/Web/API/ToggleEvent/oldState)Read only

A string (either `"open"` or `"closed"`), representing the state the element is transitioning from.

[ToggleEvent.source](/en-US/docs/Web/API/ToggleEvent/source)Read only

An [Element](/en-US/docs/Web/API/Element) object instance representing the HTML control that initiated the toggle.

## [Examples](#examples)

### [Basic example](#basic_example)

js

```
const popover = document.getElementById("mypopover");

// …

popover.addEventListener("beforetoggle", (event) => {
  if (event.newState === "open") {
    console.log("Popover is being shown");
  } else {
    console.log("Popover is being hidden");
  }
});
```

## [Specifications](#specifications)

Specification
[HTML# toggleevent](https://html.spec.whatwg.org/multipage/interaction.html#toggleevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Popover API](/en-US/docs/Web/API/Popover_API)
- [beforetoggle event](/en-US/docs/Web/API/HTMLElement/beforetoggle_event)
- [toggle event](/en-US/docs/Web/API/HTMLElement/toggle_event)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ToggleEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/toggleevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FToggleEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftoggleevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FToggleEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftoggleevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2597731017bf54bd583bd533fce1a5fab064b597%0A*+Document+last+modified%3A+2025-10-27T21%3A25%3A54.000Z%0A%0A%3C%2Fdetails%3E)
