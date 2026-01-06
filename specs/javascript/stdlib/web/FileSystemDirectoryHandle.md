# FileSystemDirectoryHandle

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemDirectoryHandle&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `FileSystemDirectoryHandle` interface of the [File System API](/en-US/docs/Web/API/File_System_API) provides a handle to a file system directory.

The interface can be accessed via the [window.showDirectoryPicker()](/en-US/docs/Web/API/Window/showDirectoryPicker), [StorageManager.getDirectory()](/en-US/docs/Web/API/StorageManager/getDirectory), [DataTransferItem.getAsFileSystemHandle()](/en-US/docs/Web/API/DataTransferItem/getAsFileSystemHandle), and [FileSystemDirectoryHandle.getDirectoryHandle()](/en-US/docs/Web/API/FileSystemDirectoryHandle/getDirectoryHandle) methods.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [FileSystemHandle](/en-US/docs/Web/API/FileSystemHandle).

## [Instance methods](#instance_methods)

Inherits methods from its parent, [FileSystemHandle](/en-US/docs/Web/API/FileSystemHandle).

Regular methods:

[FileSystemDirectoryHandle.getDirectoryHandle()](/en-US/docs/Web/API/FileSystemDirectoryHandle/getDirectoryHandle)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) fulfilled with a `FileSystemDirectoryHandle` for a subdirectory with the specified name within the directory handle on which the method is called.

[FileSystemDirectoryHandle.getFileHandle()](/en-US/docs/Web/API/FileSystemDirectoryHandle/getFileHandle)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) fulfilled with a [FileSystemFileHandle](/en-US/docs/Web/API/FileSystemFileHandle) for a file with the specified name, within the directory the method is called.

[FileSystemDirectoryHandle.removeEntry()](/en-US/docs/Web/API/FileSystemDirectoryHandle/removeEntry)

Attempts to asynchronously remove an entry if the directory handle contains a file or directory called the name specified.

[FileSystemDirectoryHandle.resolve()](/en-US/docs/Web/API/FileSystemDirectoryHandle/resolve)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) fulfilled with an [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of directory names from the parent handle to the specified child entry, with the name of the child entry as the last array item.

[Asynchronous iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_async_iterator_and_async_iterable_protocols) methods:

[FileSystemDirectoryHandle.entries()](/en-US/docs/Web/API/FileSystemDirectoryHandle/entries)

Returns a new async iterator of a given object's own enumerable property `[key, value]` pairs.

[FileSystemDirectoryHandle.keys()](/en-US/docs/Web/API/FileSystemDirectoryHandle/keys)

Returns a new async iterator containing the keys for each item in `FileSystemDirectoryHandle`.

[FileSystemDirectoryHandle.values()](/en-US/docs/Web/API/FileSystemDirectoryHandle/values)

Returns a new async iterator containing the values for each index in the `FileSystemDirectoryHandle` object.

[FileSystemDirectoryHandle[Symbol.asyncIterator]()](#filesystemdirectoryhandlesymbol.asynciterator)

Returns a new async iterator of a given object's own enumerable property `[key, value]` pairs.

## [Examples](#examples)

### [Return directory handle](#return_directory_handle)

The following example returns a directory handle with the specified name; if the directory does not already exist it is created.

js

```
const dirName = "directoryToGetName";

// assuming we have a directory handle: 'currentDirHandle'
const subDir = await currentDirHandle.getDirectoryHandle(dirName, {
  create: true,
});
```

### [Return file path](#return_file_path)

The following asynchronous function uses `resolve()` to find the path to a chosen file, relative to a specified directory handle.

js

```
async function returnPathDirectories(directoryHandle) {
  // Get a file handle by showing a file picker:
  const handle = await self.showOpenFilePicker();
  if (!handle) {
    // User cancelled, or otherwise failed to open a file.
    return;
  }

  // Check if handle exists inside our directory handle
  const relativePaths = await directoryHandle.resolve(handle);

  if (relativePath === null) {
    // Not inside directory handle
  } else {
    // relativePath is an array of names, giving the relative path

    for (const name of relativePaths) {
      // log each entry
      console.log(name);
    }
  }
}
```

### [Return handles for all files in a directory](#return_handles_for_all_files_in_a_directory)

The following example scans recursively through a directory to return [FileSystemFileHandle](/en-US/docs/Web/API/FileSystemFileHandle) objects for each file in that directory:

js

```
async function* getFilesRecursively(entry) {
  if (entry.kind === "file") {
    const file = await entry.getFile();
    if (file !== null) {
      file.relativePath = getRelativePath(entry);
      yield file;
    }
  } else if (entry.kind === "directory") {
    for await (const handle of entry.values()) {
      yield* getFilesRecursively(handle);
    }
  }
}
for await (const fileHandle of getFilesRecursively(directoryHandle)) {
  console.log(fileHandle);
}
```

## [Specifications](#specifications)

Specification
[File System# api-filesystemdirectoryhandle](https://fs.spec.whatwg.org/#api-filesystemdirectoryhandle)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File System API](/en-US/docs/Web/API/File_System_API)
- [The File System Access API: simplifying access to local files](https://developer.chrome.com/docs/capabilities/web-apis/file-system-access)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 20, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FileSystemDirectoryHandle/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/filesystemdirectoryhandle/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemDirectoryHandle&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffilesystemdirectoryhandle%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemDirectoryHandle%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffilesystemdirectoryhandle%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fab7254fb329302ddc101fc2d09947429077368e6%0A*+Document+last+modified%3A+2025-10-20T13%3A17%3A06.000Z%0A%0A%3C%2Fdetails%3E)
