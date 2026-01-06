# SharedStorageRunOperation

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `SharedStorageRunOperation` interface of the [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API) represents a [Run output gate](/en-US/docs/Web/API/Shared_Storage_API#run) operation.

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[run()](/en-US/docs/Web/API/SharedStorageRunOperation/run)Deprecated

Defines the structure to which the `run()` method defined inside a Run output gate operation should conform.

## [Examples](#examples)

In this example, a class called `ReachMeasurementOperation` is defined in a worklet and is registered using [SharedStorageWorkletGlobalScope.register()](/en-US/docs/Web/API/SharedStorageWorkletGlobalScope/register) with the name `reach-measurement`. `SharedStorageRunOperation` defines the structure to which this class must conform, essentially defining the parameters required for the `run()` method. Other than this requirement, the functionality of the class can be defined flexibly.

js

```
// reach-measurement-worklet.js
const SCALE_FACTOR = 65536;

function convertContentIdToBucket(contentId) {
  return BigInt(contentId);
}

class ReachMeasurementOperation {
  async run(data) {
    const { contentId } = data;

    // Read from Shared Storage
    const key = "has-reported-content";
    const hasReportedContent = (await this.sharedStorage.get(key)) === "true";

    // Do not report if a report has been sent already
    if (hasReportedContent) {
      return;
    }

    // Generate the aggregation key and the aggregatable value
    const bucket = convertContentIdToBucket(contentId);
    const value = 1 * SCALE_FACTOR;

    // Send an aggregatable report via the Private Aggregation API
    privateAggregation.sendHistogramReport({ bucket, value });

    // Set the report submission status flag
    await this.sharedStorage.set(key, true);
  }
}

// Register the operation
register("reach-measurement", ReachMeasurementOperation);
```

Note: It is possible to define and register multiple operations in the same shared storage worklet module script with different names. See [SharedStorageOperation](/en-US/docs/Web/API/SharedStorageOperation) for an example.

In the main browsing context, the `reach-measurement` operation is invoked using the [WindowSharedStorage.run()](/en-US/docs/Web/API/WindowSharedStorage/run) method:

js

```
async function measureUniqueReach() {
  // Load the Shared Storage worklet
  await window.sharedStorage.worklet.addModule("reach-measurement-worklet.js");

  // Run the reach measurement operation
  await window.sharedStorage.run("reach-measurement", {
    data: { contentId: "1234" },
  });
}

measureUniqueReach();
```

For more details about this example, see [Unique reach measurement](https://privacysandbox.google.com/private-advertising/private-aggregation/unique-reach). See [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API) for more examples.

## [Specifications](#specifications)

This feature does not appear to be defined in any specification.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SharedStorageRunOperation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/sharedstoragerunoperation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedStorageRunOperation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsharedstoragerunoperation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedStorageRunOperation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsharedstoragerunoperation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F923adb616baa87402ca965ebd18a73380cc84d27%0A*+Document+last+modified%3A+2025-12-15T16%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
