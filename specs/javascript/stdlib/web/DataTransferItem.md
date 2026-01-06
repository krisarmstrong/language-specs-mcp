# DataTransferItem

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨November 2016⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDataTransferItem&level=high)

The `DataTransferItem` object represents one drag data item. During a drag operation, each [DragEvent](/en-US/docs/Web/API/DragEvent) has a [dataTransfer](/en-US/docs/Web/API/DragEvent/dataTransfer) property which contains a [list](/en-US/docs/Web/API/DataTransferItemList) of drag data items. Each item in the list is a `DataTransferItem` object.

`DataTransferItem` was primarily designed for the [HTML Drag and Drop API](/en-US/docs/Web/API/HTML_Drag_and_Drop_API), and is still specified in the HTML drag-and-drop section, but it is now also used by other APIs, such as [ClipboardEvent.clipboardData](/en-US/docs/Web/API/ClipboardEvent/clipboardData) and [InputEvent.dataTransfer](/en-US/docs/Web/API/InputEvent/dataTransfer). Documentation of `DataTransferItem` will primarily discuss its usage in drag-and-drop operations, and you should refer to the other APIs' documentation for usage of `DataTransferItem` in those contexts.

This interface has no constructor.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[DataTransferItem.kind](/en-US/docs/Web/API/DataTransferItem/kind)Read only

The kind of drag data item, `string` or `file`.

[DataTransferItem.type](/en-US/docs/Web/API/DataTransferItem/type)Read only

The drag data item's type, typically a MIME type.

## [Instance methods](#instance_methods)

[DataTransferItem.getAsFile()](/en-US/docs/Web/API/DataTransferItem/getAsFile)

Returns the [File](/en-US/docs/Web/API/File) object associated with the drag data item (or null if the drag item is not a file).

[DataTransferItem.getAsFileSystemHandle()](/en-US/docs/Web/API/DataTransferItem/getAsFileSystemHandle)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [FileSystemFileHandle](/en-US/docs/Web/API/FileSystemFileHandle) if the dragged item is a file, or fulfills with a [FileSystemDirectoryHandle](/en-US/docs/Web/API/FileSystemDirectoryHandle) if the dragged item is a directory.

[DataTransferItem.getAsString()](/en-US/docs/Web/API/DataTransferItem/getAsString)

Invokes the specified callback with the drag data item string as its argument.

[DataTransferItem.webkitGetAsEntry()](/en-US/docs/Web/API/DataTransferItem/webkitGetAsEntry)

Returns an object based on [FileSystemEntry](/en-US/docs/Web/API/FileSystemEntry) representing the selected file's entry in its file system. This will generally be either a [FileSystemFileEntry](/en-US/docs/Web/API/FileSystemFileEntry) or [FileSystemDirectoryEntry](/en-US/docs/Web/API/FileSystemDirectoryEntry) object.

## [Example](#example)

All of this interface's methods and properties have their own reference page, and each reference page has an example of its usage.

## [Specifications](#specifications)

Specification
[HTML# the-datatransferitem-interface](https://html.spec.whatwg.org/multipage/dnd.html#the-datatransferitem-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DataTransferItem/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/datatransferitem/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDataTransferItem&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdatatransferitem%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDataTransferItem%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdatatransferitem%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F59d87e8756161420f3f40dc554562858f4427e72%0A*+Document+last+modified%3A+2025-03-15T18%3A03%3A46.000Z%0A%0A%3C%2Fdetails%3E)
