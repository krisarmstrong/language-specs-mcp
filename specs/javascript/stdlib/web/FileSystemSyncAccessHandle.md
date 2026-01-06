# FileSystemSyncAccessHandle

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemSyncAccessHandle&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is only available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `FileSystemSyncAccessHandle` interface of the [File System API](/en-US/docs/Web/API/File_System_API) represents a synchronous handle to a file system entry.

This class is only accessible inside dedicated [Web Workers](/en-US/docs/Web/API/Web_Workers_API) (so that its methods do not block execution on the main thread) for files within the [origin private file system](/en-US/docs/Web/API/File_System_API/Origin_private_file_system), which is not visible to end-users.

As a result, its methods are not subject to the same security checks as methods running on files within the user-visible file system, and so are much more performant. This makes them suitable for significant, large-scale file updates such as [SQLite](https://sqlite.org/wasm) database modifications.

The interface is accessed through the [FileSystemFileHandle.createSyncAccessHandle()](/en-US/docs/Web/API/FileSystemFileHandle/createSyncAccessHandle) method.

Note: In earlier versions of the spec, [close()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/close), [flush()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/flush), [getSize()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/getSize), and [truncate()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/truncate) were wrongly specified as asynchronous methods, and older versions of some browsers implement them in this way. However, all current browsers that support these methods implement them as synchronous methods.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

None.

## [Instance methods](#instance_methods)

[close()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/close)

Closes an open synchronous file handle, disabling any further operations on it and releasing the exclusive lock previously put on the file associated with the file handle.

[flush()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/flush)

Persists any changes made to the file associated with the handle via the [write()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/write) method to disk.

[getSize()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/getSize)

Returns the size of the file associated with the handle in bytes.

[read()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/read)

Reads the content of the file associated with the handle into a specified buffer, optionally at a given offset.

[truncate()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/truncate)

Resizes the file associated with the handle to a specified number of bytes.

[write()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/write)

Writes the content of a specified buffer to the file associated with the handle, optionally at a given offset.

## [Examples](#examples)

The following asynchronous event handler function is contained inside a Web Worker. On receiving a message from the main thread it:

- Creates a synchronous file access handle.
- Gets the size of the file and creates an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) to contain it.
- Reads the file contents into the buffer.
- Encodes the message and writes it to the end of the file.
- Persists the changes to disk and closes the access handle.

js

```
onmessage = async (e) => {
  // Retrieve message sent to work from main script
  const message = e.data;

  // Get handle to draft file
  const root = await navigator.storage.getDirectory();
  const draftHandle = await root.getFileHandle("draft.txt", { create: true });
  // Get sync access handle
  const accessHandle = await draftHandle.createSyncAccessHandle();

  // Get size of the file.
  const fileSize = accessHandle.getSize();
  // Read file content to a buffer.
  const buffer = new DataView(new ArrayBuffer(fileSize));
  const readBuffer = accessHandle.read(buffer, { at: 0 });

  // Write the message to the end of the file.
  const encoder = new TextEncoder();
  const encodedMessage = encoder.encode(message);
  const writeBuffer = accessHandle.write(encodedMessage, { at: readBuffer });

  // Persist changes to disk.
  accessHandle.flush();

  // Always close FileSystemSyncAccessHandle if done.
  accessHandle.close();
};
```

## [Specifications](#specifications)

Specification
[File System# api-filesystemsyncaccesshandle](https://fs.spec.whatwg.org/#api-filesystemsyncaccesshandle)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File System API](/en-US/docs/Web/API/File_System_API)
- [The File System Access API: simplifying access to local files](https://developer.chrome.com/docs/capabilities/web-apis/file-system-access)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 9, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FileSystemSyncAccessHandle/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/filesystemsyncaccesshandle/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemSyncAccessHandle&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffilesystemsyncaccesshandle%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemSyncAccessHandle%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffilesystemsyncaccesshandle%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd65517535ae067fa876d5fae83626dff838e9796%0A*+Document+last+modified%3A+2025-04-09T20%3A20%3A44.000Z%0A%0A%3C%2Fdetails%3E)
