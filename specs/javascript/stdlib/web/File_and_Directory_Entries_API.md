# File and Directory Entries API

The File and Directory Entries API provides a way to process directories and file lists provided by the user via a form input or a drag-and-drop operation. It is a more advanced version of the [File API](/en-US/docs/Web/API/File), which allows you to work with a single file. It was originally intended to support a full virtual file system, but now only supports read operations on user-provided data.

See [Relationship to other file-related APIs](/en-US/docs/Web/API/File_API#relationship_to_other_file-related_apis) for a comparison between this API, the [File System API](/en-US/docs/Web/API/File_System_API), and the [File API](/en-US/docs/Web/API/File_API).

## In this article

- [Getting access to a file system](#getting_access_to_a_file_system)
- [History](#history)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Getting access to a file system](#getting_access_to_a_file_system)

There are two ways to get access to file systems defined in the current specification draft:

- When handling a [drop](/en-US/docs/Web/API/HTMLElement/drop_event) event for drag and drop, you can call [DataTransferItem.webkitGetAsEntry()](/en-US/docs/Web/API/DataTransferItem/webkitGetAsEntry) to get the [FileSystemEntry](/en-US/docs/Web/API/FileSystemEntry) for a dropped item. If the result isn't `null`, then it's a dropped file or directory, and you can use file system calls to work with it.
- The [HTMLInputElement.webkitEntries](/en-US/docs/Web/API/HTMLInputElement/webkitEntries) property lets you access the [FileSystemFileEntry](/en-US/docs/Web/API/FileSystemFileEntry) objects for the currently selected files, but only if they are dragged-and-dropped onto the file chooser ([Firefox bug 1326031](https://bugzil.la/1326031)). If [HTMLInputElement.webkitdirectory](/en-US/docs/Web/API/HTMLInputElement/webkitdirectory) is `true`, the [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) element is instead a directory picker, and you get [FileSystemDirectoryEntry](/en-US/docs/Web/API/FileSystemDirectoryEntry) objects for each selected directory.

## [History](#history)

The original File System API was created to let browsers implement support for accessing a sandboxed virtual file system on the user's storage device. Work to standardize the specification was abandoned back in 2012, but by that point, Google Chrome included its own implementation of the API. Over time, a number of popular sites and Web applications came to use it, often without providing any means of falling back to standard APIs or even checking to be sure the API is available before using it. Mozilla instead opted to implement other APIs which can be used to solve many of the same problems, such as [IndexedDB](/en-US/docs/Web/API/IndexedDB_API); see the blog post [Why no FileSystem API in Firefox?](https://hacks.mozilla.org/2012/07/why-no-filesystem-api-in-firefox/) for more insights.

As a result, a number of popular websites did not work properly on browsers other than Chrome. To resolve that, the features of Google's API for which consensus could be reached were standardized as the File and Directory Entries API, and this was then implemented in other browsers.

## [Interfaces](#interfaces)

The File and Directory Entries API includes the following interfaces:

[FileSystem](/en-US/docs/Web/API/FileSystem)

Represents a file system.

[FileSystemEntry](/en-US/docs/Web/API/FileSystemEntry)

The basic interface representing a single entry in a file system. This is implemented by other interfaces which represent files or directories.

[FileSystemFileEntry](/en-US/docs/Web/API/FileSystemFileEntry)

Represents a single file in a file system.

[FileSystemDirectoryEntry](/en-US/docs/Web/API/FileSystemDirectoryEntry)

Represents a single directory in a file system.

[FileSystemDirectoryReader](/en-US/docs/Web/API/FileSystemDirectoryReader)

Created by calling [FileSystemDirectoryEntry.createReader()](/en-US/docs/Web/API/FileSystemDirectoryEntry/createReader), this interface provides the functionality which lets you read the contents of a directory.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[DataTransferItem.webkitGetAsEntry()](/en-US/docs/Web/API/DataTransferItem/webkitGetAsEntry)

Returns an object based on [FileSystemEntry](/en-US/docs/Web/API/FileSystemEntry) representing the selected file's entry in its file system. This will generally be either a [FileSystemFileEntry](/en-US/docs/Web/API/FileSystemFileEntry) or [FileSystemDirectoryEntry](/en-US/docs/Web/API/FileSystemDirectoryEntry) object.

[File.webkitRelativePath](/en-US/docs/Web/API/File/webkitRelativePath)

Returns the path the URL of the `File` is relative to.

[HTMLInputElement.webkitdirectory](/en-US/docs/Web/API/HTMLInputElement/webkitdirectory)

A boolean that represents the [webkitdirectory](/en-US/docs/Web/HTML/Reference/Elements/input#webkitdirectory) attribute. If `true`, the file-system-picker interface only accepts directories instead of files.

[HTMLInputElement.webkitEntries](/en-US/docs/Web/API/HTMLInputElement/webkitEntries)

Describes the currently selected files or directories.

## [Specifications](#specifications)

Specification
[File and Directory Entries API# api-domfilesystem](https://wicg.github.io/entries-api/#api-domfilesystem)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File API](/en-US/docs/Web/API/File_API)
- [File System API](/en-US/docs/Web/API/File_System_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/File_and_Directory_Entries_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/file_and_directory_entries_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFile_and_Directory_Entries_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffile_and_directory_entries_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFile_and_Directory_Entries_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffile_and_directory_entries_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9b6cd1b7fa8612257b72b2a85a96dd7d45c0200%0A*+Document+last+modified%3A+2025-04-10T14%3A56%3A07.000Z%0A%0A%3C%2Fdetails%3E)
