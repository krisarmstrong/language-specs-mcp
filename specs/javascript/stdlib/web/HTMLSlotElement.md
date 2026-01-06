# HTMLSlotElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLSlotElement&level=high)

The `HTMLSlotElement` interface of the [Shadow DOM API](/en-US/docs/Web/API/Web_components/Using_shadow_DOM) enables access to the name and assigned nodes of an HTML [<slot>](/en-US/docs/Web/HTML/Reference/Elements/slot) element.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLSlotElement.name](/en-US/docs/Web/API/HTMLSlotElement/name)

A string used to get and set the slot's name.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLSlotElement.assign()](/en-US/docs/Web/API/HTMLSlotElement/assign)

Sets the manually assigned nodes for this slot to the given nodes.

[HTMLSlotElement.assignedNodes()](/en-US/docs/Web/API/HTMLSlotElement/assignedNodes)

Returns a sequence of the nodes assigned to this slot. If the `flatten` option is set to `true`, it returns a sequence of both the nodes assigned to this slot, and the nodes assigned to any other slots that are descendants of this slot. If no assigned nodes are found, it returns the slot's fallback content.

[HTMLSlotElement.assignedElements()](/en-US/docs/Web/API/HTMLSlotElement/assignedElements)

Returns a sequence of the elements assigned to this slot (and no other nodes). If the `flatten` option is set to `true`, it returns a sequence of both the elements assigned to this slot, and the elements assigned to any other slots that are descendants of this slot. If no assigned elements are found, it returns the slot's fallback content.

## [Events](#events)

Also inherits events from its parent interface, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[slotchange](/en-US/docs/Web/API/HTMLSlotElement/slotchange_event)

Fired on an `HTMLSlotElement` instance ([<slot>](/en-US/docs/Web/HTML/Reference/Elements/slot) element) when the node(s) contained in that slot change.

## [Examples](#examples)

The following snippet is taken from our [slotchange example](https://github.com/mdn/web-components-examples/tree/main/slotchange) ([see it live also](https://mdn.github.io/web-components-examples/slotchange/)).

js

```
let slots = this.shadowRoot.querySelectorAll("slot");
slots[1].addEventListener("slotchange", (e) => {
  let nodes = slots[1].assignedNodes();
  console.log(
    `Element in Slot "${slots[1].name}" changed to "${nodes[0].outerHTML}".`,
  );
});
```

Here we grab references to all the slots, then add a slotchange event listener to the 2nd slot in the template — which is the one that keeps having its contents changed in the example.

Every time the element inserted in the slot changes, we log a report to the console saying which slot has changed, and what the new node inside the slot is.

## [Specifications](#specifications)

Specification
[HTML# htmlslotelement](https://html.spec.whatwg.org/multipage/scripting.html#htmlslotelement)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 25, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLSlotElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlslotelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLSlotElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlslotelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLSlotElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlslotelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa7265fc3effa7c25b9997135104370c057a65293%0A*+Document+last+modified%3A+2025-09-25T16%3A11%3A52.000Z%0A%0A%3C%2Fdetails%3E)
