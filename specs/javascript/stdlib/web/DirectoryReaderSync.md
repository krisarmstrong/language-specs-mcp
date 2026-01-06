# DirectoryReaderSync

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `DirectoryReaderSync` interface lets you read the entries in a directory.

Warning: This interface is deprecated and is no more on the standard track. Do not use it anymore. Use the [File and Directory Entries API](/en-US/docs/Web/API/File_and_Directory_Entries_API) instead.

## In this article

- [Basic concepts](#basic_concepts)
- [Method](#method)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Basic concepts](#basic_concepts)

Before you call the only method in this interface, [readEntries()](#readentries), create the [DirectoryEntrySync](/en-US/docs/Web/API/DirectoryEntrySync) object. But DirectoryEntrySync (as well as [FileEntrySync](/en-US/docs/Web/API/FileEntrySync)) is not a data type that you can pass between a calling app and Web Worker thread. It's not a big deal, because you don't really need to have the main app and the worker thread see the same JavaScript object; you just need them to access the same files. You can do that by passing a list of `filesystem:` URLs—which are just strings—instead of a list of entries. You can also use the `filesystem:` URL to look up the entry with `resolveLocalFileSystemURL()`. That gets you back to a DirectoryEntrySync (as well as FileEntrySync) object.

### [Example](#example)

In the following code snippet from [HTML5Rocks (web.dev)](https://web.dev/articles/filesystem-sync), we create Web Workers and pass data from it to the main app.

js

```
// Taking care of the browser-specific prefixes.
window.resolveLocalFileSystemURL =
  window.resolveLocalFileSystemURL || window.webkitResolveLocalFileSystemURL;

// Create web workers
const worker = new Worker("worker.js");
worker.onmessage = (e) => {
  const urls = e.data.entries;
  urls.forEach((url) => {
    window.resolveLocalFileSystemURL(url, (fileEntry) => {
      // Print out file's name.
      console.log(fileEntry.name);
    });
  });
};

worker.postMessage({ cmd: "list" });
```

The following is `worker.js` code that gets the contents of the directory.

js

```
// worker.js

// Taking care of the browser-specific prefixes.
self.requestFileSystemSync =
  self.webkitRequestFileSystemSync || self.requestFileSystemSync;

// Global for holding the list of entry file system URLs.
const paths = [];

function getAllEntries(dirReader) {
  const entries = dirReader.readEntries();

  for (const entry of entries) {
    // Stash this entry's filesystem in URL
    paths.push(entry.toURL());

    // If this is a directory, traverse.
    if (entry.isDirectory) {
      getAllEntries(entry.createReader());
    }
  }
}

// Forward the error to main app.
function onError(e) {
  postMessage(`ERROR: ${e.toString()}`);
}

self.onmessage = (e) => {
  const cmd = e.data.cmd;

  // Ignore everything else except our 'list' command.
  if (!cmd || cmd !== "list") {
    return;
  }

  try {
    const fs = requestFileSystemSync(TEMPORARY, 1024 * 1024 /* 1MB */);

    getAllEntries(fs.root.createReader());

    self.postMessage({ entries: paths });
  } catch (e) {
    onError(e);
  }
};
```

## [Method](#method)

### [readEntries()](#readentries)

Returns a list of entries from a specific directory. Call this method until an empty array is returned.

#### Syntax

js

```
readEntries()
```

##### Parameters

None.

##### Return value

Array containing [FileEntrySync](/en-US/docs/Web/API/FileEntrySync) and [DirectoryEntrySync](/en-US/docs/Web/API/DirectoryEntrySync).

##### Exceptions

This method can raise a [DOMException](/en-US/docs/Web/API/DOMException) with the following codes:

ExceptionDescription`NOT_FOUND_ERR`The directory does not exist.`INVALID_STATE_ERR`The directory has been modified since the first call to readEntries was processed.`SECURITY_ERR`The browser determined that it was not safe to look up the metadata.

## [Specifications](#specifications)

This feature is not part of any specification anymore. It is no longer on track to become a standard.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [File and Directory Entries API](/en-US/docs/Web/API/File_and_Directory_Entries_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DirectoryReaderSync/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/directoryreadersync/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDirectoryReaderSync&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdirectoryreadersync%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDirectoryReaderSync%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdirectoryreadersync%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe6d43da6c6d28a6ac92cdd47882809ffbdf987ce%0A*+Document+last+modified%3A+2025-05-23T11%3A17%3A22.000Z%0A%0A%3C%2Fdetails%3E)
