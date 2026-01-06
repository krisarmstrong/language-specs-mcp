# SharedStorageSelectURLOperation

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `SharedStorageSelectURLOperation` interface of the [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API) represents a [URL Selection output gate](/en-US/docs/Web/API/Shared_Storage_API#url_selection) operation.

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[run()](/en-US/docs/Web/API/SharedStorageSelectURLOperation/run)Deprecated

Defines the structure to which the `run()` method defined inside a URL Selection output gate operation should conform.

## [Examples](#examples)

In this example, a class called `SelectURLOperation` is defined in a worklet and is registered using [SharedStorageWorkletGlobalScope.register()](/en-US/docs/Web/API/SharedStorageWorkletGlobalScope/register) with the name `ab-testing`. `SharedStorageSelectURLOperation` defines the structure to which this class needs to conform, essentially defining the parameters required for the `run()` method. Other than this requirement, the functionality of the class can be defined flexibly.

js

```
// ab-testing-worklet.js
class SelectURLOperation {
  async run(urls, data) {
    // Read the user's experiment group from Shared Storage
    const experimentGroup = await this.sharedStorage.get("ab-testing-group");

    // Return the group number
    return experimentGroup;
  }
}

// Register the operation
register("ab-testing", SelectURLOperation);
```

Note: It is possible to define and register multiple operations in the same shared storage worklet module script with different names; see [SharedStorageOperation](/en-US/docs/Web/API/SharedStorageOperation) for an example.

In the main browsing context, the `ab-testing` operation is invoked using the [WindowSharedStorage.selectURL()](/en-US/docs/Web/API/WindowSharedStorage/selectURL) method:

js

```
// Randomly assigns a user to a group 0 or 1
function getExperimentGroup() {
  return Math.round(Math.random());
}

async function injectContent() {
  // Register the Shared Storage worklet
  await window.sharedStorage.worklet.addModule("ab-testing-worklet.js");

  // Assign user to a random group (0 or 1) and store it in Shared Storage
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

For more details about this example and links to other examples, see the [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API) landing page.

## [Specifications](#specifications)

This feature does not appear to be defined in any specification.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SharedStorageSelectURLOperation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/sharedstorageselecturloperation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedStorageSelectURLOperation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsharedstorageselecturloperation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedStorageSelectURLOperation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsharedstorageselecturloperation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F923adb616baa87402ca965ebd18a73380cc84d27%0A*+Document+last+modified%3A+2025-12-15T16%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
