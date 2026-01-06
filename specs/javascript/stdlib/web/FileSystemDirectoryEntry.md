# FileSystemDirectoryEntry

The `FileSystemDirectoryEntry` interface of the [File and Directory Entries API](/en-US/docs/Web/API/File_and_Directory_Entries_API) represents a directory in a file system. It provides methods which make it possible to access and manipulate the files in a directory, as well as to access the entries within the directory.

## In this article

- [Basic concepts](#basic_concepts)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Basic concepts](#basic_concepts)

You can create a new directory by calling [getDirectory()](/en-US/docs/Web/API/FileSystemDirectoryEntry/getDirectory). If you want to create subdirectories, create each child directory in sequence. If you try creating a directory using a full path that includes parent directories that do not exist yet, an error is returned. So create the hierarchy by recursively adding a new path after creating the parent directory.

### [Example](#example)

In the following code snippet, we create a directory called "Documents."

js

```
// Taking care of the browser-specific prefixes.
window.requestFileSystem =
  window.requestFileSystem || window.webkitRequestFileSystem;
window.directoryEntry = window.directoryEntry || window.webkitDirectoryEntry;

// …

function onFs(fs) {
  fs.root.getDirectory(
    "Documents",
    { create: true },
    (directoryEntry) => {
      // directoryEntry.isFile === false
      // directoryEntry.isDirectory === true
      // directoryEntry.name === 'Documents'
      // directoryEntry.fullPath === '/Documents'
    },
    onError,
  );
}

// Opening a file system with temporary storage
window.requestFileSystem(TEMPORARY, 1024 * 1024 /* 1MB */, onFs, onError);
```

## [Instance properties](#instance_properties)

This interface has no properties of its own, but inherits properties from its parent interface, [FileSystemEntry](/en-US/docs/Web/API/FileSystemEntry).

## [Instance methods](#instance_methods)

This interface inherits methods from its parent interface, [FileSystemEntry](/en-US/docs/Web/API/FileSystemEntry).

[createReader()](/en-US/docs/Web/API/FileSystemDirectoryEntry/createReader)

Creates a [FileSystemDirectoryReader](/en-US/docs/Web/API/FileSystemDirectoryReader) object which can be used to read the entries in this directory.

[getDirectory()](/en-US/docs/Web/API/FileSystemDirectoryEntry/getDirectory)

Returns a `FileSystemDirectoryEntry` object representing a directory located at a given path, relative to the directory on which the method is called.

[getFile()](/en-US/docs/Web/API/FileSystemDirectoryEntry/getFile)

Returns a [FileSystemFileEntry](/en-US/docs/Web/API/FileSystemFileEntry) object representing a file located within the directory's hierarchy, given a path relative to the directory on which the method is called.

[removeRecursively()](/en-US/docs/Web/API/FileSystemDirectoryEntry/removeRecursively)DeprecatedNon-standard

Removes the directory as well as all of its content, hierarchically iterating over its entire subtree of descendant files and directories.

## [Specifications](#specifications)

Specification
[File and Directory Entries API# api-directoryentry](https://wicg.github.io/entries-api/#api-directoryentry)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File and Directory Entries API](/en-US/docs/Web/API/File_and_Directory_Entries_API)
- [FileSystemDirectoryReader](/en-US/docs/Web/API/FileSystemDirectoryReader)
- [FileSystemEntry](/en-US/docs/Web/API/FileSystemEntry)
- [FileSystemFileEntry](/en-US/docs/Web/API/FileSystemFileEntry)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FileSystemDirectoryEntry/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/filesystemdirectoryentry/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemDirectoryEntry&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffilesystemdirectoryentry%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemDirectoryEntry%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffilesystemdirectoryentry%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe6d43da6c6d28a6ac92cdd47882809ffbdf987ce%0A*+Document+last+modified%3A+2025-05-23T11%3A17%3A22.000Z%0A%0A%3C%2Fdetails%3E)
