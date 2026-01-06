# DragEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDragEvent&level=high)

The `DragEvent` interface is a [DOM event](/en-US/docs/Web/API/Event) that represents a drag and drop interaction. The user initiates a drag by placing a pointer device (such as a mouse) on the touch surface and then dragging the pointer to a new location (such as another DOM element). Applications are free to interpret a drag and drop interaction in an application-specific way.

This interface inherits properties from [MouseEvent](/en-US/docs/Web/API/MouseEvent) and [Event](/en-US/docs/Web/API/Event).

## In this article

- [Instance properties](#instance_properties)
- [Constructors](#constructors)
- [Event types](#event_types)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[DragEvent.dataTransfer](/en-US/docs/Web/API/DragEvent/dataTransfer)Read only

The data that is transferred during a drag and drop interaction.

## [Constructors](#constructors)

Although this interface has a constructor, it is not possible to create a useful DataTransfer object from script, since [DataTransfer](/en-US/docs/Web/API/DataTransfer) objects have a processing and security model that is coordinated by the browser during drag-and-drops.

[DragEvent()](/en-US/docs/Web/API/DragEvent/DragEvent)

Creates a synthetic and untrusted DragEvent.

## [Event types](#event_types)

[drag](/en-US/docs/Web/API/HTMLElement/drag_event)

This event is fired when an element or text selection is being dragged.

[dragend](/en-US/docs/Web/API/HTMLElement/dragend_event)

This event is fired when a drag operation is being ended (by releasing a mouse button or hitting the escape key).

[dragenter](/en-US/docs/Web/API/HTMLElement/dragenter_event)

This event is fired when a dragged element or text selection enters a valid drop target.

[dragleave](/en-US/docs/Web/API/HTMLElement/dragleave_event)

This event is fired when a dragged element or text selection leaves a valid drop target.

[dragover](/en-US/docs/Web/API/HTMLElement/dragover_event)

This event is fired continuously when an element or text selection is being dragged and the mouse pointer is over a valid drop target (every 50 ms WHEN mouse is not moving ELSE much faster between 5 ms (slow movement) and 1ms (fast movement) approximately. This firing pattern is different than [mouseover](/en-US/docs/Web/API/Element/mouseover_event) ).

[dragstart](/en-US/docs/Web/API/HTMLElement/dragstart_event)

This event is fired when the user starts dragging an element or text selection.

[drop](/en-US/docs/Web/API/HTMLElement/drop_event)

This event is fired when an element or text selection is dropped on a valid drop target.

## [Example](#example)

An Example of each property, constructor, event type and global event handlers is included in their respective reference page.

## [Specifications](#specifications)

Specification
[HTML# the-dragevent-interface](https://html.spec.whatwg.org/multipage/dnd.html#the-dragevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Drag and drop](/en-US/docs/Web/API/HTML_Drag_and_Drop_API)
- [Drag Operations](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Drag_operations)
- [Working with the drag data store](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Drag_data_store)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DragEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/dragevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDragEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdragevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDragEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdragevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8285d415db211ae9efe04752d9dab1b574450ee8%0A*+Document+last+modified%3A+2025-10-02T00%3A18%3A49.000Z%0A%0A%3C%2Fdetails%3E)
