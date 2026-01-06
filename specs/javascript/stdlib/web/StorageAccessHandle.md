# StorageAccessHandle

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStorageAccessHandle&level=not)

The `StorageAccessHandle` interface represents access to [unpartitioned state](/en-US/docs/Web/Privacy/Guides/State_Partitioning#state_partitioning) granted by a call to [Document.requestStorageAccess()](/en-US/docs/Web/API/Document/requestStorageAccess).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[StorageAccessHandle.sessionStorage](/en-US/docs/Web/API/StorageAccessHandle/sessionStorage)Read only

Returns an unpartitioned session [Storage](/en-US/docs/Web/API/Storage) object if access was granted.

[StorageAccessHandle.localStorage](/en-US/docs/Web/API/StorageAccessHandle/localStorage)Read only

Returns an unpartitioned local [Storage](/en-US/docs/Web/API/Storage) object if access was granted.

[StorageAccessHandle.indexedDB](/en-US/docs/Web/API/StorageAccessHandle/indexedDB)Read only

Returns an unpartitioned [IDBFactory](/en-US/docs/Web/API/IDBFactory) object if access was granted.

[StorageAccessHandle.locks](/en-US/docs/Web/API/StorageAccessHandle/locks)Read only

Returns an unpartitioned [LockManager](/en-US/docs/Web/API/LockManager) object if access was granted.

[StorageAccessHandle.caches](/en-US/docs/Web/API/StorageAccessHandle/caches)Read only

Returns an unpartitioned [CacheStorage](/en-US/docs/Web/API/CacheStorage) object if access was granted.

## [Instance methods](#instance_methods)

[StorageAccessHandle.getDirectory()](/en-US/docs/Web/API/StorageAccessHandle/getDirectory)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with an unpartitioned [FileSystemDirectoryHandle](/en-US/docs/Web/API/FileSystemDirectoryHandle) object if access was granted, and rejects otherwise.

[StorageAccessHandle.estimate()](/en-US/docs/Web/API/StorageAccessHandle/estimate)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with an unpartitioned [StorageEstimate](/en-US/docs/Web/API/StorageManager/estimate) object if access was granted, and rejects otherwise.

[StorageAccessHandle.createObjectURL()](/en-US/docs/Web/API/StorageAccessHandle/createObjectURL)

Returns a string representing the unpartitioned blob storage url created if access was granted, and throws otherwise.

[StorageAccessHandle.revokeObjectURL()](/en-US/docs/Web/API/StorageAccessHandle/revokeObjectURL)

Revokes the unpartitioned blob storage url passed in if access was granted, and throws otherwise.

[StorageAccessHandle.BroadcastChannel()](/en-US/docs/Web/API/StorageAccessHandle/BroadcastChannel)

Returns the unpartitioned [BroadcastChannel](/en-US/docs/Web/API/BroadcastChannel) created if access was granted, and throws otherwise.

[StorageAccessHandle.SharedWorker()](/en-US/docs/Web/API/StorageAccessHandle/SharedWorker)

Returns the unpartitioned [SharedWorker](/en-US/docs/Web/API/SharedWorker) created if access was granted, and throws otherwise.

## [Example](#example)

js

```
document.requestStorageAccess({ localStorage: true }).then(
  (handle) => {
    console.log("localStorage access granted");
    handle.localStorage.setItem("foo", "bar");
  },
  () => {
    console.log("localStorage access denied");
  },
);
```

Note: See [Using the Storage Access API](/en-US/docs/Web/API/Storage_Access_API/Using) for a more complete example.

## [Specifications](#specifications)

Specification
[Extending Storage Access API (SAA) to non-cookie storage# storageaccesshandle](https://privacycg.github.io/saa-non-cookie-storage/#storageaccesshandle)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Document.requestStorageAccess()](/en-US/docs/Web/API/Document/requestStorageAccess)
- [Using the Storage Access API](/en-US/docs/Web/API/Storage_Access_API/Using)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 21, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/StorageAccessHandle/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/storageaccesshandle/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStorageAccessHandle&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fstorageaccesshandle%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStorageAccessHandle%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fstorageaccesshandle%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F775df1c62a1cbe555c4374ff9122d4ef15bd6f60%0A*+Document+last+modified%3A+2025-02-21T17%3A38%3A46.000Z%0A%0A%3C%2Fdetails%3E)
