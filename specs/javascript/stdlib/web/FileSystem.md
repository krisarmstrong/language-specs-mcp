# FileSystem

The File and Directory Entries API interface `FileSystem` is used to represent a file system. These objects can be obtained from the [filesystem](/en-US/docs/Web/API/FileSystemEntry/filesystem) property on any file system entry. Some browsers offer additional APIs to create and manage file systems, such as Chrome's [requestFileSystem()](/en-US/docs/Web/API/Window/requestFileSystem) method.

This interface will not grant you access to the users' filesystem. Instead, you will have a "virtual drive" within the browser sandbox if you want to gain access to the users' file system, you need to invoke the user, for example by installing a Chrome extension. The relevant Chrome API can be found [in the Chrome developer docs](https://developer.chrome.com/docs/apps/reference/fileSystem).

## In this article

- [Basic concepts](#basic_concepts)
- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Basic concepts](#basic_concepts)

There are two ways to get access to a `FileSystem` object:

1. You can directly ask for one representing a sandboxed file system created just for your web app directly by calling `window.requestFileSystem()`. If that call is successful, it executes a callback handler, which receives as a parameter a `FileSystem` object describing the file system.
2. You can get it from a file system entry object, through its [filesystem](/en-US/docs/Web/API/FileSystemEntry/filesystem) property.

## [Instance properties](#instance_properties)

[FileSystem.name](/en-US/docs/Web/API/FileSystem/name)Read only

A string representing the file system's name. This name is unique among the entire list of exposed file systems.

[FileSystem.root](/en-US/docs/Web/API/FileSystem/root)Read only

A [FileSystemDirectoryEntry](/en-US/docs/Web/API/FileSystemDirectoryEntry) object which represents the file system's root directory. Through this object, you can gain access to all files and directories in the file system.

## [Specifications](#specifications)

Specification
[File and Directory Entries API# api-domfilesystem](https://wicg.github.io/entries-api/#api-domfilesystem)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File and Directory Entries API](/en-US/docs/Web/API/File_and_Directory_Entries_API)
- [FileSystemEntry](/en-US/docs/Web/API/FileSystemEntry), [FileSystemFileEntry](/en-US/docs/Web/API/FileSystemFileEntry), and [FileSystemDirectoryEntry](/en-US/docs/Web/API/FileSystemDirectoryEntry)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 14, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FileSystem/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/filesystem/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystem&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffilesystem%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystem%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffilesystem%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe488eba036b2fee56444fd579c3759ef45ff2ca8%0A*+Document+last+modified%3A+2025-05-14T04%3A00%3A04.000Z%0A%0A%3C%2Fdetails%3E)
