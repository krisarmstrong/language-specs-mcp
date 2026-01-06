# StorageManager

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨December 2021⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStorageManager&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `StorageManager` interface of the [Storage API](/en-US/docs/Web/API/Storage_API) provides an interface for managing persistence permissions and estimating available storage. You can get a reference to this interface using either [navigator.storage](/en-US/docs/Web/API/Navigator/storage) or [WorkerNavigator.storage](/en-US/docs/Web/API/WorkerNavigator/storage).

## In this article

- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance methods](#instance_methods)

[StorageManager.estimate()](/en-US/docs/Web/API/StorageManager/estimate)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to an object containing usage and quota numbers for your origin.

[StorageManager.getDirectory()](/en-US/docs/Web/API/StorageManager/getDirectory)

Used to obtain a reference to a [FileSystemDirectoryHandle](/en-US/docs/Web/API/FileSystemDirectoryHandle) object allowing access to a directory and its contents, stored in the [origin private file system](/en-US/docs/Web/API/File_System_API/Origin_private_file_system). Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [FileSystemDirectoryHandle](/en-US/docs/Web/API/FileSystemDirectoryHandle) object.

[StorageManager.persist()](/en-US/docs/Web/API/StorageManager/persist)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to `true` if the user agent is able to persist your site's storage.

[StorageManager.persisted()](/en-US/docs/Web/API/StorageManager/persisted)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to `true` if persistence has already been granted for your site's storage.

## [Specifications](#specifications)

Specification
[Storage# storagemanager](https://storage.spec.whatwg.org/#storagemanager)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 6, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/StorageManager/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/storagemanager/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStorageManager&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fstoragemanager%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStorageManager%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fstoragemanager%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4de6f76bbfd76229db78ffb7d52cf6b4cb9f31f8%0A*+Document+last+modified%3A+2024-03-06T06%3A23%3A15.000Z%0A%0A%3C%2Fdetails%3E)
