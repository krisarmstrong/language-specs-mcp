# SharedStorageWorkletGlobalScope

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `SharedStorageWorkletGlobalScope` interface of the [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API) represents the global scope of a [SharedStorageWorklet](/en-US/docs/Web/API/SharedStorageWorklet) module.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[sharedStorage](/en-US/docs/Web/API/SharedStorageWorkletGlobalScope/sharedStorage)Deprecated

Contains an instance of the [WorkletSharedStorage](/en-US/docs/Web/API/WorkletSharedStorage) object, representing the shared storage for a particular origin as exposed in a worklet context.

## [Instance methods](#instance_methods)

[register()](/en-US/docs/Web/API/SharedStorageWorkletGlobalScope/register)Deprecated

Registers an [operation](/en-US/docs/Web/API/SharedStorageOperation) defined inside the current worklet module.

## [Examples](#examples)

js

```
// ab-testing-worklet.js
class SelectURLOperation {
  async run(urls, data) {
    // Read the user's experiment group from shared storage
    const experimentGroup = await this.sharedStorage.get("ab-testing-group");

    // Return the group number
    return experimentGroup;
  }
}

register("ab-testing", SelectURLOperation);
```

See the [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API) landing page for a walkthrough of this example and links to other examples.

## [Specifications](#specifications)

Specification
[Shared Storage API# sharedstorageworkletglobalscope](https://wicg.github.io/shared-storage/#sharedstorageworkletglobalscope)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SharedStorageWorkletGlobalScope/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/sharedstorageworkletglobalscope/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedStorageWorkletGlobalScope&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsharedstorageworkletglobalscope%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedStorageWorkletGlobalScope%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsharedstorageworkletglobalscope%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe936e7271df947f25184a5ba8a21445bbd4d056c%0A*+Document+last+modified%3A+2025-12-13T02%3A55%3A18.000Z%0A%0A%3C%2Fdetails%3E)
