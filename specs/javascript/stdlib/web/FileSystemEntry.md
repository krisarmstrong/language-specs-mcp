# FileSystemEntry

The `FileSystemEntry` interface of the File and Directory Entries API represents a single entry in a file system. The entry can be a file or a directory (directories are represented by the [FileSystemDirectoryEntry](/en-US/docs/Web/API/FileSystemDirectoryEntry) interface). It includes methods for working with files—including copying, moving, removing, and reading files—as well as information about a file it points to—including the file name and its path from the root to the entry.

## In this article

- [Basic concepts](#basic_concepts)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Basic concepts](#basic_concepts)

You don't create `FileSystemEntry` objects directly. Instead, you will receive an object based on this interface through other APIs. This interface serves as a base class for the [FileSystemFileEntry](/en-US/docs/Web/API/FileSystemFileEntry) and [FileSystemDirectoryEntry](/en-US/docs/Web/API/FileSystemDirectoryEntry) interfaces, which provide features specific to file system entries representing files and directories, respectively.

The `FileSystemEntry` interface includes methods that you would expect for manipulating files and directories, but it also includes a convenient method for obtaining the URL of the entry: [toURL()](/en-US/docs/Web/API/FileSystemEntry/toURL). It also introduces a new URL scheme: `filesystem:`.

You can use the `filesystem:` scheme on Google Chrome to see all the files and folders that are stored in the origin of your app. Just use `filesystem:` scheme for the root directory of the origin of the app. For example, if your app is in [http://www.example.com](https://www.example.com/), open `filesystem:http://www.example.com/temporary/` in a tab. Chrome shows a read-only list of all the files and folders stored the origin of your app.

### [Example](#example)

To see an example of how `toURL()` works, see the [method description](/en-US/docs/Web/API/FileSystemEntry/toURL). The snippet below shows you how you can remove a file by name.

js

```
// Taking care of the browser-specific prefixes.
window.requestFileSystem =
  window.requestFileSystem || window.webkitRequestFileSystem;

// …

// Opening a file system with temporary storage
window.requestFileSystem(
  TEMPORARY,
  1024 * 1024 /* 1MB */,
  (fs) => {
    fs.root.getFile(
      "log.txt",
      {},
      (fileEntry) => {
        fileEntry.remove(() => {
          console.log("File removed.");
        }, onError);
      },
      onError,
    );
  },
  onError,
);
```

## [Instance properties](#instance_properties)

This interface provides the following properties.

[filesystem](/en-US/docs/Web/API/FileSystemEntry/filesystem)Read only

A [FileSystem](/en-US/docs/Web/API/FileSystem) object representing the file system in which the entry is located.

[fullPath](/en-US/docs/Web/API/FileSystemEntry/fullPath)Read only

A string which provides the full, absolute path from the file system's root to the entry; it can also be thought of as a path which is relative to the root directory, prepended with a "/" character.

[isDirectory](/en-US/docs/Web/API/FileSystemEntry/isDirectory)Read only

A boolean value which is `true` if the entry represents a directory; otherwise, it's `false`.

[isFile](/en-US/docs/Web/API/FileSystemEntry/isFile)Read only

A Boolean which is `true` if the entry represents a file. If it's not a file, this value is `false`.

[name](/en-US/docs/Web/API/FileSystemEntry/name)Read only

A string containing the name of the entry (the final part of the path, after the last "/" character).

## [Instance methods](#instance_methods)

This interface defines the following methods.

[copyTo()](/en-US/docs/Web/API/FileSystemEntry/copyTo)DeprecatedNon-standard

Copies the file or directory to a new location on the file system.

[getMetadata()](/en-US/docs/Web/API/FileSystemEntry/getMetadata)DeprecatedNon-standard

Obtains metadata about the file, such as its modification date and size.

[getParent()](/en-US/docs/Web/API/FileSystemEntry/getParent)

Returns a [FileSystemDirectoryEntry](/en-US/docs/Web/API/FileSystemDirectoryEntry) representing the entry's parent directory.

[moveTo()](/en-US/docs/Web/API/FileSystemEntry/moveTo)DeprecatedNon-standard

Moves the file or directory to a new location on the file system, or renames the file or directory.

[remove()](/en-US/docs/Web/API/FileSystemEntry/remove)DeprecatedNon-standard

Removes the specified file or directory. You can only remove directories which are empty.

[toURL()](/en-US/docs/Web/API/FileSystemEntry/toURL)DeprecatedNon-standard

Creates and returns a URL which identifies the entry. This URL uses the URL scheme `"filesystem:"`.

## [Specifications](#specifications)

Specification
[File and Directory Entries API# api-entry](https://wicg.github.io/entries-api/#api-entry)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File and Directory Entries API](/en-US/docs/Web/API/File_and_Directory_Entries_API)
- [FileSystemFileEntry](/en-US/docs/Web/API/FileSystemFileEntry) and [FileSystemDirectoryEntry](/en-US/docs/Web/API/FileSystemDirectoryEntry) are based on `FileSystemEntry`.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FileSystemEntry/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/filesystementry/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemEntry&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffilesystementry%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemEntry%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffilesystementry%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe6d43da6c6d28a6ac92cdd47882809ffbdf987ce%0A*+Document+last+modified%3A+2025-05-23T11%3A17%3A22.000Z%0A%0A%3C%2Fdetails%3E)
