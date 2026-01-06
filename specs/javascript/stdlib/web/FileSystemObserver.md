# FileSystemObserver

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `FileSystemObserver` interface of the [File System API](/en-US/docs/Web/API/File_System_API) provides a mechanism to observe changes to the user-observable file system and the [Origin Private File System](/en-US/docs/Web/API/File_System_API/Origin_private_file_system) (OPFS). This means web applications don't have to poll the file system to find changes in the files or folder structure, which can be time-consuming and wasteful.

## In this article

- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[FileSystemObserver()](/en-US/docs/Web/API/FileSystemObserver/FileSystemObserver)ExperimentalNon-standard

Creates a new `FileSystemObserver` object instance.

## [Instance methods](#instance_methods)

[disconnect()](/en-US/docs/Web/API/FileSystemObserver/disconnect)ExperimentalNon-standard

Stop observing the filesystem.

[observe()](/en-US/docs/Web/API/FileSystemObserver/observe)ExperimentalNon-standard

Start observing changes to a given file or directory.

## [Examples](#examples)

Note: For a complete working example, check out [File System Observer Demo](https://mdn.github.io/dom-examples/file-system-api/filesystemobserver/) ([source code](https://github.com/mdn/dom-examples/tree/main/file-system-api/filesystemobserver)).

### [Initialize a FileSystemObserver](#initialize_a_filesystemobserver)

Before you can start observing file or directory changes, you need to initialize a `FileSystemObserver` to handle the observations. This is done using the [FileSystemObserver()](/en-US/docs/Web/API/FileSystemObserver/FileSystemObserver) constructor, which takes a callback function as an argument:

js

```
const observer = new FileSystemObserver(callback);
```

The [callback function](/en-US/docs/Web/API/FileSystemObserver/FileSystemObserver#callback) body can be specified to return and process file change observations in any way you want:

js

```
const callback = (records, observer) => {
  for (const record of records) {
    console.log("Change detected:", record);
    const reportContent = `Change observed to ${record.changedHandle.kind} ${record.changedHandle.name}. Type: ${record.type}.`;
    sendReport(reportContent); // Some kind of user-defined reporting function
  }

  observer.disconnect();
};
```

### [Observe a file or directory](#observe_a_file_or_directory)

Once a `FileSystemObserver` instance is available, you can start observing changes to a file system entry by calling the [FileSystemObserver.observe()](/en-US/docs/Web/API/FileSystemObserver/observe) method.

You can observe a file or directory in the user-observable file system or the [Origin Private File System](/en-US/docs/Web/API/File_System_API/Origin_private_file_system) (OPFS) by passing a [FileSystemFileHandle](/en-US/docs/Web/API/FileSystemFileHandle) or [FileSystemDirectoryHandle](/en-US/docs/Web/API/FileSystemDirectoryHandle) to `observe()`. Instances of these objects can be returned, for example, when asking the user to select a file or directory using [Window.showSaveFilePicker()](/en-US/docs/Web/API/Window/showSaveFilePicker) or [Window.showDirectoryPicker()](/en-US/docs/Web/API/Window/showDirectoryPicker):

js

```
// Observe a file
async function observeFile() {
  const fileHandle = await window.showSaveFilePicker();

  await observer.observe(fileHandle);
}

// Observe a directory
async function observeDirectory() {
  const directoryHandle = await window.showDirectoryPicker();

  await observer.observe(directoryHandle);
}
```

You can also observe changes to the OPFS by passing a [FileSystemSyncAccessHandle](/en-US/docs/Web/API/FileSystemSyncAccessHandle) to `observe()`:

js

```
// Observe an OPFS file system entry
async function observeOPFSFile() {
  const root = await navigator.storage.getDirectory();
  const draftHandle = await root.getFileHandle("draft.txt", { create: true });
  const syncHandle = await draftHandle.createSyncAccessHandle();

  await observer.observe(syncHandle);
}
```

### [Stop observing the file system](#stop_observing_the_file_system)

When you want to stop observing changes to the file system entry, you can call [FileSystemObserver.disconnect()](/en-US/docs/Web/API/FileSystemObserver/disconnect):

js

```
observer.disconnect();
```

## [Specifications](#specifications)

Not currently part of a specification. See [https://github.com/whatwg/fs/pull/165](https://github.com/whatwg/fs/pull/165) for the relevant specification PR.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File System API](/en-US/docs/Web/API/File_System_API)
- [The File System Observer API origin trial](https://developer.chrome.com/blog/file-system-observer#stop-observing-the-file-system) on developer.chrome.com (2024)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FileSystemObserver/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/filesystemobserver/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemObserver&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffilesystemobserver%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFileSystemObserver%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffilesystemobserver%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fac7a39584dc77b42aac19473cc522bbedbf13717%0A*+Document+last+modified%3A+2025-07-04T19%3A29%3A27.000Z%0A%0A%3C%2Fdetails%3E)
