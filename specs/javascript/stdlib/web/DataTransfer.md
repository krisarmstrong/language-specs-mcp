# DataTransfer

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDataTransfer&level=high)

The `DataTransfer` object is used to hold any data transferred between contexts, such as a drag and drop operation, or clipboard read/write. It may hold one or more data items, each of one or more data types.

`DataTransfer` was primarily designed for the [HTML Drag and Drop API](/en-US/docs/Web/API/HTML_Drag_and_Drop_API), as the [DragEvent.dataTransfer](/en-US/docs/Web/API/DragEvent/dataTransfer) property, and is still specified in the HTML drag-and-drop section, but it is now also used by other APIs, such as [ClipboardEvent.clipboardData](/en-US/docs/Web/API/ClipboardEvent/clipboardData) and [InputEvent.dataTransfer](/en-US/docs/Web/API/InputEvent/dataTransfer). However, other APIs only use certain parts of its interface, ignoring properties such as `dropEffect`. Documentation of `DataTransfer` will primarily discuss its usage in drag-and-drop operations, and you should refer to the other APIs' documentation for usage of `DataTransfer` in those contexts.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[DataTransfer()](/en-US/docs/Web/API/DataTransfer/DataTransfer)

Creates and returns a new `DataTransfer` object.

## [Instance properties](#instance_properties)

[DataTransfer.dropEffect](/en-US/docs/Web/API/DataTransfer/dropEffect)

Gets the type of drag-and-drop operation currently selected or sets the operation to a new type. The value must be `none`, `copy`, `link` or `move`.

[DataTransfer.effectAllowed](/en-US/docs/Web/API/DataTransfer/effectAllowed)

Provides all of the types of operations that are possible. Must be one of `none`, `copy`, `copyLink`, `copyMove`, `link`, `linkMove`, `move`, `all` or `uninitialized`.

[DataTransfer.files](/en-US/docs/Web/API/DataTransfer/files)Read only

Contains a list of all the local files available on the data transfer. If the drag operation doesn't involve dragging files, this property is an empty list.

[DataTransfer.items](/en-US/docs/Web/API/DataTransfer/items)Read only

Gives a [DataTransferItemList](/en-US/docs/Web/API/DataTransferItemList) object which is a list of all of the drag data.

[DataTransfer.types](/en-US/docs/Web/API/DataTransfer/types)Read only

An array of strings giving the formats that were set in the [dragstart](/en-US/docs/Web/API/HTMLElement/dragstart_event) event.

## [Instance methods](#instance_methods)

[DataTransfer.addElement()](/en-US/docs/Web/API/DataTransfer/addElement)ExperimentalNon-standard

Sets the drag source for the given element. This will be the element on which [drag](/en-US/docs/Web/API/HTMLElement/drag_event) and [dragend](/en-US/docs/Web/API/HTMLElement/dragend_event) events are fired, and not the default target (the node that was dragged). Firefox-specific.

[DataTransfer.clearData()](/en-US/docs/Web/API/DataTransfer/clearData)

Remove the data associated with a given type. The type argument is optional. If the type is empty or not specified, the data associated with all types is removed. If data for the specified type does not exist, or the data transfer contains no data, this method will have no effect.

[DataTransfer.getData()](/en-US/docs/Web/API/DataTransfer/getData)

Retrieves the data for a given type, or an empty string if data for that type does not exist or the data transfer contains no data.

[DataTransfer.setData()](/en-US/docs/Web/API/DataTransfer/setData)

Set the data for a given type. If data for the type does not exist, it is added at the end, such that the last item in the types list will be the new format. If data for the type already exists, the existing data is replaced in the same position.

[DataTransfer.setDragImage()](/en-US/docs/Web/API/DataTransfer/setDragImage)

Set the image to be used for dragging if a custom one is desired.

## [Examples](#examples)

Every method and property listed in this document has its own reference page and each reference page either directly includes an example of the interface or has a link to an example.

### [Reading the data in a paste or drop event](#reading_the_data_in_a_paste_or_drop_event)

In the following example, we have a [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) containing three different types of text inputs: a text [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) element, a [<textarea>](/en-US/docs/Web/HTML/Reference/Elements/textarea) element, and a [<div>](/en-US/docs/Web/HTML/Reference/Elements/div) element with [contenteditable](/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable) set to `true`. The user can paste or drop text into any of these elements, and the data in the [ClipboardEvent.clipboardData](/en-US/docs/Web/API/ClipboardEvent/clipboardData) or [DragEvent.dataTransfer](/en-US/docs/Web/API/DragEvent/dataTransfer) object will be displayed.

#### HTML

html

```
<form>
  <fieldset>
    <legend>&lt;input /></legend>
    <input type="text" />
    <table class="center">
      <tbody>
        <tr>
          <th scope="row">Operation type</th>
          <td></td>
        </tr>
        <tr>
          <th scope="row">Content type</th>
          <td></td>
        </tr>
      </tbody>
    </table>
  </fieldset>
  <fieldset>
    <legend>&lt;textarea /></legend>
    <textarea></textarea>
    <table class="center">
      <tbody>
        <tr>
          <th scope="row">Operation type</th>
          <td></td>
        </tr>
        <tr>
          <th scope="row">Content type</th>
          <td></td>
        </tr>
      </tbody>
    </table>
  </fieldset>
  <fieldset>
    <legend>&lt;div contenteditable /></legend>
    <div contenteditable></div>
    <table class="center">
      <tbody>
        <tr>
          <th scope="row">Operation type</th>
          <td></td>
        </tr>
        <tr>
          <th scope="row">Content type</th>
          <td></td>
        </tr>
      </tbody>
    </table>
  </fieldset>
  <p class="center">
    <input type="reset" />
  </p>
</form>
```

#### CSS

css

```
.center {
  text-align: center;
}

form > fieldset > * {
  vertical-align: top;
}
form input,
form textarea,
form [contenteditable] {
  min-width: 15rem;
  padding: 0.25rem;
}
[contenteditable] {
  appearance: textfield;
  display: inline-block;
  min-height: 1rem;
  border: 1px solid;
}

form table {
  display: inline-table;
}
table ol {
  text-align: left;
}
```

#### JavaScript

js

```
const form = document.querySelector("form");

function displayData(event) {
  if (event.type === "drop") event.preventDefault();

  const cells = event.target.nextElementSibling.querySelectorAll("td");
  cells[0].textContent = event.type;
  const transfer = event.clipboardData || event.dataTransfer;
  const ol = document.createElement("ol");
  cells[1].textContent = "";
  cells[1].appendChild(ol);
  for (const item of transfer.items) {
    const li = document.createElement("li");
    li.textContent = `${item.kind} ${item.type}`;
    ol.appendChild(li);
  }
}

form.addEventListener("paste", displayData);
form.addEventListener("drop", displayData);
form.addEventListener("reset", () => {
  for (const cell of form.querySelectorAll("[contenteditable], td")) {
    cell.textContent = "";
  }
});
```

#### Result

## [Specifications](#specifications)

Specification
[HTML# the-datatransfer-interface](https://html.spec.whatwg.org/multipage/dnd.html#the-datatransfer-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Drag and drop](/en-US/docs/Web/API/HTML_Drag_and_Drop_API)
- [Drag Operations](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Drag_operations)
- [Working with the drag data store](/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Drag_data_store)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DataTransfer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/datatransfer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDataTransfer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdatatransfer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDataTransfer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdatatransfer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0b5859108411e47d228a4bb9f30a5556ab17f63c%0A*+Document+last+modified%3A+2025-11-03T18%3A14%3A11.000Z%0A%0A%3C%2Fdetails%3E)
