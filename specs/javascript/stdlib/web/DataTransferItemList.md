# DataTransferItemList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨November 2016⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDataTransferItemList&level=high)

The `DataTransferItemList` object is a list of [DataTransferItem](/en-US/docs/Web/API/DataTransferItem) objects representing items being dragged. During a drag operation, each [DragEvent](/en-US/docs/Web/API/DragEvent) has a [dataTransfer](/en-US/docs/Web/API/DragEvent/dataTransfer) property and that property is a `DataTransferItemList`.

The individual items can be accessed using the [bracket notation](/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#bracket_notation)`[]`.

`DataTransferItemList` was primarily designed for the [HTML Drag and Drop API](/en-US/docs/Web/API/HTML_Drag_and_Drop_API), and is still specified in the HTML drag-and-drop section, but it is now also used by other APIs, such as [ClipboardEvent.clipboardData](/en-US/docs/Web/API/ClipboardEvent/clipboardData) and [InputEvent.dataTransfer](/en-US/docs/Web/API/InputEvent/dataTransfer). Documentation of `DataTransferItemList` will primarily discuss its usage in drag-and-drop operations, and you should refer to the other APIs' documentation for usage of `DataTransferItemList` in those contexts.

This interface has no constructor.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[DataTransferItemList.length](/en-US/docs/Web/API/DataTransferItemList/length)Read only

An `unsigned long` that is the number of drag items in the list.

## [Instance methods](#instance_methods)

[DataTransferItemList.add()](/en-US/docs/Web/API/DataTransferItemList/add)

Adds an item (either a [File](/en-US/docs/Web/API/File) object or a string) to the drag item list and returns a [DataTransferItem](/en-US/docs/Web/API/DataTransferItem) object for the new item.

[DataTransferItemList.remove()](/en-US/docs/Web/API/DataTransferItemList/remove)

Removes the drag item from the list at the given index.

[DataTransferItemList.clear()](/en-US/docs/Web/API/DataTransferItemList/clear)

Removes all of the drag items from the list.

## [Example](#example)

This example shows how to use drag and drop.

### [HTML](#html)

html

```
<div>
  <p id="source" draggable="true">
    Select this element, drag it to the Drop Zone and then release the selection
    to move the element.
  </p>
</div>
<div id="target">Drop Zone</div>
```

### [CSS](#css)

css

```
div {
  margin: 0em;
  padding: 2em;
}

#source {
  color: blue;
  border: 1px solid black;
}

#target {
  border: 1px solid black;
}
```

### [JavaScript](#javascript)

js

```
const source = document.getElementById("source");
const target = document.getElementById("target");

source.addEventListener("dragstart", (ev) => {
  console.log("dragStart");

  // Add this element's id to the drag payload so the drop handler will
  // know which element to add to its tree
  const dataList = ev.dataTransfer.items;
  dataList.add(ev.target.id, "text/plain");

  // Add some other items to the drag payload
  dataList.add("<p>Paragraph…</p>", "text/html");
  dataList.add("http://www.example.org", "text/uri-list");
});

source.addEventListener("dragend", (ev) => {
  console.log("dragEnd");
  const dataList = ev.dataTransfer.items;

  // Clear any remaining drag data
  dataList.clear();
});

target.addEventListener("drop", (ev) => {
  console.log("Drop");
  ev.preventDefault();

  // Loop through the dropped items and log their data
  for (const item of ev.dataTransfer.items) {
    if (item.kind === "string" && item.type.match(/^text\/plain/)) {
      // This item is the target node
      item.getAsString((s) => {
        ev.target.appendChild(document.getElementById(s));
      });
    } else if (item.kind === "string" && item.type.match(/^text\/html/)) {
      // Drag data item is HTML
      item.getAsString((s) => {
        console.log(`… Drop: HTML = ${s}`);
      });
    } else if (item.kind === "string" && item.type.match(/^text\/uri-list/)) {
      // Drag data item is URI
      item.getAsString((s) => {
        console.log(`… Drop: URI = ${s}`);
      });
    }
  }
});

target.addEventListener("dragover", (ev) => {
  console.log("dragOver");
  ev.preventDefault();

  // Set the dropEffect to move
  ev.dataTransfer.dropEffect = "move";
});
```

### [Result](#result)

## [Specifications](#specifications)

Specification
[HTML# the-datatransferitemlist-interface](https://html.spec.whatwg.org/multipage/dnd.html#the-datatransferitemlist-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DataTransferItemList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/datatransferitemlist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDataTransferItemList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdatatransferitemlist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDataTransferItemList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdatatransferitemlist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F06bb5f22d50ff3579a12aebf7e8c9f02cfa2468b%0A*+Document+last+modified%3A+2025-06-03T17%3A33%3A23.000Z%0A%0A%3C%2Fdetails%3E)
