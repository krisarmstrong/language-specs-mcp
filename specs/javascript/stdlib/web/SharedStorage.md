# SharedStorage

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `SharedStorage` interface of the [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API) represents the shared storage for a particular origin, defining methods to write data to the shared storage.

`SharedStorage` is the base class for:

- [WindowSharedStorage](/en-US/docs/Web/API/WindowSharedStorage), accessed via [Window.sharedStorage](/en-US/docs/Web/API/Window/sharedStorage).
- [WorkletSharedStorage](/en-US/docs/Web/API/WorkletSharedStorage), accessed via [SharedStorageWorkletGlobalScope.sharedStorage](/en-US/docs/Web/API/SharedStorageWorkletGlobalScope/sharedStorage).

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[append()](/en-US/docs/Web/API/SharedStorage/append)Deprecated

Appends a string to the value of an existing key-value pair in the current origin's shared storage.

[clear()](/en-US/docs/Web/API/SharedStorage/clear)Deprecated

Clears the current origin's shared storage, removing all data from it.

[delete()](/en-US/docs/Web/API/SharedStorage/delete)Deprecated

Deletes an existing key-value pair from the current origin's shared storage.

[set()](/en-US/docs/Web/API/SharedStorage/set)Deprecated

Stores a new key-value pair in the current origin's shared storage or updates an existing one.

## [Examples](#examples)

js

```
window.sharedStorage
  .set("ab-testing-group", "0")
  .then(() => console.log("Value saved to shared storage"));
```

## [Specifications](#specifications)

Specification
[Shared Storage API# sharedstorage](https://wicg.github.io/shared-storage/#sharedstorage)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WindowSharedStorage](/en-US/docs/Web/API/WindowSharedStorage)
- [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SharedStorage/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/sharedstorage/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedStorage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsharedstorage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedStorage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsharedstorage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe936e7271df947f25184a5ba8a21445bbd4d056c%0A*+Document+last+modified%3A+2025-12-13T02%3A55%3A18.000Z%0A%0A%3C%2Fdetails%3E)
