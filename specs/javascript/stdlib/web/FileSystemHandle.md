# FileSystemHandle

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemHandle&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `FileSystemHandle` interface of the [File System API](/en-US/docs/Web/API/File_System_API) is an object which represents a file or directory entry. Multiple handles can represent the same entry. For the most part you do not work with `FileSystemHandle` directly but rather its child interfaces [FileSystemFileHandle](/en-US/docs/Web/API/FileSystemFileHandle) and [FileSystemDirectoryHandle](/en-US/docs/Web/API/FileSystemDirectoryHandle).

## In this article

- [Interfaces based on FileSystemHandle](#interfaces_based_on_filesystemhandle)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces based on FileSystemHandle](#interfaces_based_on_filesystemhandle)

Below is a list of interfaces based on the `FileSystemHandle` interface.

[FileSystemFileHandle](/en-US/docs/Web/API/FileSystemFileHandle)

Represents a handle to a file entry.

[FileSystemDirectoryHandle](/en-US/docs/Web/API/FileSystemDirectoryHandle)

Provides a handle to a directory entry.

## [Instance properties](#instance_properties)

[kind](/en-US/docs/Web/API/FileSystemHandle/kind)Read only

Returns the type of entry. This is `'file'` if the associated entry is a file or `'directory'`.

[name](/en-US/docs/Web/API/FileSystemHandle/name)Read only

Returns the name of the associated entry.

## [Instance methods](#instance_methods)

[isSameEntry()](/en-US/docs/Web/API/FileSystemHandle/isSameEntry)

Compares two handles to see if the associated entries (either a file or directory) match.

[queryPermission()](/en-US/docs/Web/API/FileSystemHandle/queryPermission)Experimental

Queries the current permission state of the current handle.

[remove()](/en-US/docs/Web/API/FileSystemHandle/remove)ExperimentalNon-standard

Requests removal of the entry represented by the handle from the underlying file system.

[requestPermission()](/en-US/docs/Web/API/FileSystemHandle/requestPermission)Experimental

Requests read or readwrite permissions for the file handle.

## [Examples](#examples)

### [Checking Type](#checking_type)

The below code allows the user to choose a file from the file picker and then tests to see whether the handle returned is a file or directory

js

```
// store a reference to our file handle
let fileHandle;

async function getFile() {
  // open file picker
  [fileHandle] = await window.showOpenFilePicker();

  if (fileHandle.kind === "file") {
    // run file code
  } else if (fileHandle.kind === "directory") {
    // run directory code
  }
}
```

### [Query/Request Permissions](#queryrequest_permissions)

The following asynchronous function returns true if user has granted read or readwrite permissions to the file handle. Permission is requested if not.

js

```
// fileHandle is a FileSystemFileHandle
// withWrite is a boolean set to true if write

async function verifyPermission(fileHandle, withWrite) {
  const opts = {};
  if (withWrite) {
    opts.mode = "readwrite";
  }

  // Check if we already have permission, if so, return true.
  if ((await fileHandle.queryPermission(opts)) === "granted") {
    return true;
  }

  // Request permission to the file, if the user grants permission, return true.
  if ((await fileHandle.requestPermission(opts)) === "granted") {
    return true;
  }

  // The user did not grant permission, return false.
  return false;
}
```

### [Comparing Entries](#comparing_entries)

The following function compares a single entry with an array of entries, and returns a new array with any matching entries removed.

js

```
function removeMatches(fileEntry, entriesArr) {
  const newArr = entriesArr.filter((entry) => !fileEntry.isSameEntry(entry));

  return newArr;
}
```

## [Specifications](#specifications)

Specification
[File System# api-filesystemhandle](https://fs.spec.whatwg.org/#api-filesystemhandle)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File System API](/en-US/docs/Web/API/File_System_API)
- [The File System Access API: simplifying access to local files](https://developer.chrome.com/docs/capabilities/web-apis/file-system-access)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 17, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/FileSystemHandle/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/filesystemhandle/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemHandle&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffilesystemhandle%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemHandle%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffilesystemhandle%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6c592023efa1f762eaa1eb1f36241750626be51c%0A*+Document+last+modified%3A+2024-07-17T23%3A29%3A22.000Z%0A%0A%3C%2Fdetails%3E)
