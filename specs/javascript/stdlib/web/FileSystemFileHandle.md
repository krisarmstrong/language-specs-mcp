# FileSystemFileHandle

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemFileHandle&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `FileSystemFileHandle` interface of the [File System API](/en-US/docs/Web/API/File_System_API) represents a handle to a file system entry. The interface is accessed through the [window.showOpenFilePicker()](/en-US/docs/Web/API/Window/showOpenFilePicker) method.

Note that read and write operations depend on file-access permissions that do not persist after a page refresh if no other tabs for that origin remain open. The [queryPermission](/en-US/docs/Web/API/FileSystemHandle/queryPermission) method of the [FileSystemHandle](/en-US/docs/Web/API/FileSystemHandle) interface can be used to verify permission state before accessing a file.

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

[getFile()](/en-US/docs/Web/API/FileSystemFileHandle/getFile)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves to a [File](/en-US/docs/Web/API/File) object representing the state on disk of the entry represented by the handle.

[createSyncAccessHandle()](/en-US/docs/Web/API/FileSystemFileHandle/createSyncAccessHandle)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves to a [FileSystemSyncAccessHandle](/en-US/docs/Web/API/FileSystemSyncAccessHandle) object that can be used to synchronously read from and write to a file. The synchronous nature of this method brings performance advantages, but it is only usable inside dedicated [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

[createWritable()](/en-US/docs/Web/API/FileSystemFileHandle/createWritable)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves to a newly created [FileSystemWritableFileStream](/en-US/docs/Web/API/FileSystemWritableFileStream) object that can be used to write to a file.

## [Examples](#examples)

### [Reading a File](#reading_a_file)

The following asynchronous function presents a file picker and once a file is chosen, uses the `getFile()` method to retrieve the contents.

js

```
async function getTheFile() {
  const pickerOpts = {
    types: [
      {
        description: "Images",
        accept: {
          "image/*": [".png", ".gif", ".jpeg", ".jpg"],
        },
      },
    ],
    excludeAcceptAllOption: true,
    multiple: false,
  };

  // open file picker
  const [fileHandle] = await window.showOpenFilePicker(pickerOpts);
  // get file contents
  const fileData = await fileHandle.getFile();
  return fileData;
}
```

### [Writing a File](#writing_a_file)

The following asynchronous function writes the given contents to the file handle, and thus to disk.

js

```
async function writeFile(fileHandle, contents) {
  // Create a FileSystemWritableFileStream to write to.
  const writable = await fileHandle.createWritable();

  // Write the contents of the file to the stream.
  await writable.write(contents);

  // Close the file and write the contents to disk.
  await writable.close();
}
```

### [Synchronously reading and writing a file](#synchronously_reading_and_writing_a_file)

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

Note: In earlier versions of the spec, [close()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/close), [flush()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/flush), [getSize()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/getSize), and [truncate()](/en-US/docs/Web/API/FileSystemSyncAccessHandle/truncate) were wrongly specified as asynchronous methods, and older versions of some browsers implement them in this way. However, all current browsers that support these methods implement them as synchronous methods.

## [Specifications](#specifications)

Specification
[File System# api-filesystemfilehandle](https://fs.spec.whatwg.org/#api-filesystemfilehandle)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File System API](/en-US/docs/Web/API/File_System_API)
- [The File System Access API: simplifying access to local files](https://developer.chrome.com/docs/capabilities/web-apis/file-system-access)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/FileSystemFileHandle/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/filesystemfilehandle/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemFileHandle&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffilesystemfilehandle%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemFileHandle%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffilesystemfilehandle%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd8f04d843dd81ab8cea1cfc0577ae3c5c9b77d5c%0A*+Document+last+modified%3A+2024-07-26T03%3A29%3A50.000Z%0A%0A%3C%2Fdetails%3E)
