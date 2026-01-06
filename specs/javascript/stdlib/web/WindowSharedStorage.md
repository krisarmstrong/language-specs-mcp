# WindowSharedStorage

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `WindowSharedStorage` interface of the [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API) represents the shared storage for a particular origin within a standard browsing context.

`WindowSharedStorage` is accessed via [Window.sharedStorage](/en-US/docs/Web/API/Window/sharedStorage).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[worklet](/en-US/docs/Web/API/WindowSharedStorage/worklet)Deprecated

Contains the [SharedStorageWorklet](/en-US/docs/Web/API/SharedStorageWorklet) instance representing the shared storage worklet for the current origin. `SharedStorageWorklet` includes the [addModule()](/en-US/docs/Web/API/Worklet/addModule) method, which is used to add a module to the shared storage worklet.

## [Instance methods](#instance_methods)

`WindowSharedStorage` inherits properties from its parent interface, [SharedStorage](/en-US/docs/Web/API/SharedStorage).

[run()](/en-US/docs/Web/API/WindowSharedStorage/run)Deprecated

Executes a [Run output gate](/en-US/docs/Web/API/Shared_Storage_API#run) operation that has been registered in a module added to the [SharedStorageWorklet](/en-US/docs/Web/API/SharedStorageWorklet) of the current origin.

[selectURL()](/en-US/docs/Web/API/WindowSharedStorage/selectURL)Deprecated

Executes a [URL Selection output gate](/en-US/docs/Web/API/Shared_Storage_API#url_selection) operation that has been registered in a module added to the [SharedStorageWorklet](/en-US/docs/Web/API/SharedStorageWorklet) of the current origin.

## [Examples](#examples)

js

```
// Randomly assigns a user to a group 0 or 1
function getExperimentGroup() {
  return Math.round(Math.random());
}

async function injectContent() {
  // Add the module to the shared storage worklet
  await window.sharedStorage.worklet.addModule("ab-testing-worklet.js");

  // Assign user to a random group (0 or 1) and store it in shared storage
  window.sharedStorage.set("ab-testing-group", getExperimentGroup(), {
    ignoreIfPresent: true,
  });

  // Run the URL selection operation
  const fencedFrameConfig = await window.sharedStorage.selectURL(
    "ab-testing",
    [
      { url: `https://your-server.example/content/default-content.html` },
      { url: `https://your-server.example/content/experiment-content-a.html` },
    ],
    {
      resolveToConfig: true,
    },
  );

  // Render the chosen URL into a fenced frame
  document.getElementById("content-slot").config = fencedFrameConfig;
}

injectContent();
```

See the [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API) landing page for a walkthrough of this example and links to other examples.

## [Specifications](#specifications)

This feature does not appear to be defined in any specification.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WindowSharedStorage/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/windowsharedstorage/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindowSharedStorage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwindowsharedstorage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindowSharedStorage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwindowsharedstorage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F923adb616baa87402ca965ebd18a73380cc84d27%0A*+Document+last+modified%3A+2025-12-15T16%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
