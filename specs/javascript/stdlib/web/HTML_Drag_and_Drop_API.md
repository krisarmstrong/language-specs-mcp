# HTML Drag and Drop API

HTML Drag and Drop interfaces enable applications to use drag-and-drop features in browsers.

The user may select draggable elements with a mouse, drag those elements to a droppable element, and drop them by releasing the mouse button. A translucent representation of the draggable elements follows the pointer during the drag operation.

You can customize which elements can become draggable, the type of feedback the draggable elements produce, and the droppable elements.

This overview of HTML Drag and Drop includes a description of the interfaces, basic steps to add drag-and-drop support to an application, and an interoperability summary of the interfaces.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Guides](#guides)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

On the surface, Drag and Drop actually has three distinct use cases: [dragging elements within a page](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Kanban_board), dragging data out of a page, and [dragging data into a page](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/File_drag_and_drop). They have subtly different requirements and implementations. However, the Drag and Drop API provides a unified model to think about all these interactions.

At its core, a drag operation involves three things:

- The [item being dragged](#draggable_items)
- The [underlying data to be transferred](#drag_data_store)
- The [drop target](#drop_target)

It's not necessarily true that all three are under your control, or you need to define them yourself:

- When dragging external data into a page, there's no draggable item to be defined (for example, it could be a file in the operating system's file explorer).
- When dragging elements within a page, you often don't need to define any transferred data; you just manipulate the dragged element.
- When dragging out of the page, there's no drop target to be defined.

We'll look at how each one can be defined and used.

### [Drag events](#drag_events)

HTML drag-and-drop uses the [DOM event model](/en-US/docs/Web/API/Event) and [drag events](/en-US/docs/Web/API/DragEvent) inherited from [mouse events](/en-US/docs/Web/API/MouseEvent). During drag operations, several event types are fired, and some events might fire many times, such as the [drag](/en-US/docs/Web/API/HTMLElement/drag_event) and [dragover](/en-US/docs/Web/API/HTMLElement/dragover_event) events.

EventFires when...[dragstart](/en-US/docs/Web/API/HTMLElement/dragstart_event)...the [draggable item](#draggable_items) starts to be dragged.[drag](/en-US/docs/Web/API/HTMLElement/drag_event)...the draggable item is being dragged, every few hundred milliseconds.[dragenter](/en-US/docs/Web/API/HTMLElement/dragenter_event)...the element has a draggable item entering it.[dragleave](/en-US/docs/Web/API/HTMLElement/dragleave_event)...the element has a draggable item leaving it.[dragover](/en-US/docs/Web/API/HTMLElement/dragover_event)...the element has a draggable item being dragged over it, every few hundred milliseconds.[drop](/en-US/docs/Web/API/HTMLElement/drop_event)...the element is a [drop target](#drop_target) and the draggable item is dropped over it.[dragend](/en-US/docs/Web/API/HTMLElement/dragend_event)...the draggable item stops being dragged.

Note: The `dragstart`, `drag`, and `dragend` events are fired on the dragged item, and therefore can't fire when dragging a file into the browser from the OS.

Similarly, the `dragenter`, `dragleave`, `dragover`, and `drop` events are fired on elements that are potential drop targets, and therefore can't fire when dragging an item out of the browser.

For more information, see [Drag operations](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Drag_operations).

### [Draggable items](#draggable_items)

In HTML, images, links, and selections are draggable by default. To make an arbitrary element draggable, set the [draggable](/en-US/docs/Web/HTML/Reference/Global_attributes/draggable) attribute to the value `"true"`.

html

```
<p id="p1" draggable="true">This element is draggable.</p>
```

At this point, the element already has the dragging appearance, although it has no behavior defined yet:

For images and links, `draggable` defaults to `true`, so you would only set it to `false` to disable dragging of these elements. For non-draggable elements, the "dragging" gesture usually selects the text instead.

Note: When an element is made draggable, text or other elements within it can no longer be selected in the normal way by clicking and dragging with the mouse. Instead, the user must hold down the Alt key to select text with the mouse, or use the keyboard.

A selection is also draggable. In this case, the source node, or the node on which various events such as `dragstart` and `dragend` are fired, is the text node that the drag started on. The selection can partially or fully contain multiple nodes, including text nodes and element nodes, which are all considered dragged simultaneously.

As aforementioned, the dragged item can also be something not on a webpage—for example, a file in the operating system's file explorer. However, only items on the webpage can cause the [dragstart](/en-US/docs/Web/API/HTMLElement/dragstart_event) and [dragend](/en-US/docs/Web/API/HTMLElement/dragend_event) events to fire.

For more information, see the [Drag operations guide](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Drag_operations).

### [Drag data store](#drag_data_store)

You can't transfer JavaScript objects directly to arbitrary webpages, and surely not to external applications, so to transfer data in and out of the webpage, the data must be serialized to a string (or as a [File](/en-US/docs/Web/API/File)). In drag and drop, this string is encapsulated in a [DataTransferItem](/en-US/docs/Web/API/DataTransferItem) object, which also defines a particular `type`—typically a MIME type such as `text/html`—that defines how the string should be interpreted.

Each drag and drop operation has an associated drag data store, which is a [DataTransfer](/en-US/docs/Web/API/DataTransfer) object accessible via the [DragEvent](/en-US/docs/Web/API/DragEvent)'s [dataTransfer](/en-US/docs/Web/API/DragEvent/dataTransfer) property. For the default-draggable items such as images, links, and selections, the drag data is already defined by the browser; for custom draggable elements defined using the `draggable` attribute, you must define the drag data yourself. The only time to make any modifications to the data store is within the [dragstart](/en-US/docs/Web/API/HTMLElement/dragstart_event) handler—for the `dataTransfer` of any other drag event, the data store is unmodifiable.

The [setData()](/en-US/docs/Web/API/DataTransfer/setData) method can be used to add an item to the drag data, as shown in the following example.

js

```
function dragstartHandler(ev) {
  // Add different types of drag data
  ev.dataTransfer.setData("text/plain", ev.target.innerText);
  ev.dataTransfer.setData("text/html", ev.target.outerHTML);
  ev.dataTransfer.setData(
    "text/uri-list",
    ev.target.ownerDocument.location.href,
  );
}

const p1 = document.getElementById("p1");
p1.addEventListener("dragstart", dragstartHandler);
```

Furthermore, the only time you can read from the data store, apart from the `dragstart` event, is during the `drop` event (allowing the drop target to retrieve the data). For all other events, the data store cannot be accessed.

For more information, read [Working with the drag data store](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Drag_data_store).

### [Drop target](#drop_target)

A drop target is an element on which a user can drop a dragged item. By default, most elements are not drop targets, and if you release the drag, a "fly-black" animation displays, indicating that the drag and drop failed. Any element can become a drop target by canceling the [dragover](/en-US/docs/Web/API/HTMLElement/dragover_event) event that fires on it with `preventDefault()`.

The [drop](/en-US/docs/Web/API/HTMLElement/drop_event) event only fires on drop targets, and it is the only time you can read the drag data store.

The following example shows a minimal valid drop target, and also combines the code from the previous examples.

html

```
<p id="target">Drop Zone</p>
```

js

```
const target = document.getElementById("target");

// Cancel dragover so that drop can fire
target.addEventListener("dragover", (ev) => {
  ev.preventDefault();
});
target.addEventListener("drop", (ev) => {
  ev.preventDefault();
  const data = ev.dataTransfer.getData("text/plain");
  ev.target.append(data);
});
```

For more information, see [Specifying drop targets](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Drag_operations#dragging_over_elements_and_specifying_drop_targets).

## [Guides](#guides)

[Drag operations](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Drag_operations)

Describes the steps that occur during a drag and drop operation, and what the application is supposed to do within each handler.

[Working with the drag data store](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Drag_data_store)

Describes how to read and write to the drag data store during a drag and drop operation.

[File drag and drop](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/File_drag_and_drop)

A hands-on guide implementing a basic interface accepting file drops.

[Kanban board with drag and drop](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Kanban_board)

A hands-on guide implementing a Kanban board involving dragging and dropping elements within a webpage.

## [Interfaces](#interfaces)

[DragEvent](/en-US/docs/Web/API/DragEvent)

The event object passed to drag event handlers.

[DataTransfer](/en-US/docs/Web/API/DataTransfer)

Holds any data transferred between contexts, consisting of text items and file items. Initially designed for drag and drop, it is now also used in other contexts such as [Clipboard API](/en-US/docs/Web/API/Clipboard_API).

[DataTransferItem](/en-US/docs/Web/API/DataTransferItem)

Represents one item in the drag data store, which can be a text item or a file item.

[DataTransferItemList](/en-US/docs/Web/API/DataTransferItemList)

Represents the list of [DataTransferItem](/en-US/docs/Web/API/DataTransferItem) objects in the drag data store.

## [Examples](#examples)

- [Copying and moving elements with the DataTransfer interface](https://mdn.github.io/dom-examples/drag-and-drop/copy-move-DataTransfer.html)
- [Copying and moving elements with the DataTransferListItem interface](https://mdn.github.io/dom-examples/drag-and-drop/copy-move-DataTransferItemList.html)

Reference pages for each interface also have individual examples.

## [Specifications](#specifications)

Specification[HTML](https://html.spec.whatwg.org/multipage/dnd.html)

## [See also](#see_also)

- [Drag Operations](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Drag_operations)
- [Working with the drag data store](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Drag_data_store)
- [HTML Living Standard: Drag and Drop](https://html.spec.whatwg.org/multipage/interaction.html#dnd)
- [Drag and Drop interoperability data from CanIUse](https://caniuse.com/#search=draganddrop)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/html_drag_and_drop_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTML_Drag_and_Drop_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtml_drag_and_drop_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTML_Drag_and_Drop_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtml_drag_and_drop_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8285d415db211ae9efe04752d9dab1b574450ee8%0A*+Document+last+modified%3A+2025-10-02T00%3A18%3A49.000Z%0A%0A%3C%2Fdetails%3E)
