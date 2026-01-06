# WorkletSharedStorage

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `WorkletSharedStorage` interface of the [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API) represents the shared storage for a particular origin within a worklet context.

`WorkletSharedStorage` is accessed via [SharedStorageWorkletGlobalScope.sharedStorage](/en-US/docs/Web/API/SharedStorageWorkletGlobalScope/sharedStorage).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[context](/en-US/docs/Web/API/WorkletSharedStorage/context)DeprecatedNon-standard

Contains contextual data passed into the shared storage worklet from the associated browsing context via the [FencedFrameConfig.setSharedStorageContext()](/en-US/docs/Web/API/FencedFrameConfig/setSharedStorageContext) method.

## [Instance methods](#instance_methods)

`WorkletSharedStorage` inherits properties from its parent interface, [SharedStorage](/en-US/docs/Web/API/SharedStorage).

[get()](/en-US/docs/Web/API/WorkletSharedStorage/get)Deprecated

Retrieves a value from the shared storage.

[length()](/en-US/docs/Web/API/WorkletSharedStorage/length)Deprecated

Returns the number of entries currently stored in the shared storage for the current origin.

[remainingBudget()](/en-US/docs/Web/API/WorkletSharedStorage/remainingBudget)Deprecated

Returns the remaining navigation budget for the current origin.

`WorkletSharedStorage` also includes the following methods because it has an [async iterator](/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator) defined on it:

[entries()](/en-US/docs/Web/API/WorkletSharedStorage/entries)Deprecated

Returns a new async iterator for the key-value pairs of a `WorkletSharedStorage` object instance's enumerable properties.

[keys()](/en-US/docs/Web/API/WorkletSharedStorage/keys)Deprecated

Returns a new async iterator containing the keys for each item in a `WorkletSharedStorage` object instance.

[WorkletSharedStorage[Symbol.asyncIterator]() 
Deprecated](#workletsharedstoragesymbol.asynciterator)

Returns the [entries()](/en-US/docs/Web/API/WorkletSharedStorage/entries) function by default.

## [Examples](#examples)

### [Passing contextual data via setSharedStorageContext()](#passing_contextual_data_via_setsharedstoragecontext)

You can use the [Private Aggregation API](https://privacysandbox.google.com/private-advertising/private-aggregation) to create reports that combine event-level data inside fenced frames with contextual data from the embedding document. `setSharedStorageContext()` can be used to pass contextual data from the embedder to shared storage worklets initiated by the [Protected Audience API](https://privacysandbox.google.com/private-advertising/protected-audience).

In this example, we store data from both the embedding page and the fenced frame using [shared storage](https://privacysandbox.google.com/private-advertising/shared-storage).

On the embedding page, we set a mock event ID as the shared storage context using `setSharedStorageContext()`:

js

```
const frameConfig = await navigator.runAdAuction({ resolveToConfig: true });

// Data from the embedder that you want to pass to the shared storage worklet
frameConfig.setSharedStorageContext("some-event-id");

const frame = document.createElement("fencedframe");
frame.config = frameConfig;
```

Within the fenced frame, after adding the worklet module with [window.sharedStorage.worklet.addModule()](/en-US/docs/Web/API/Worklet/addModule), we send the event-level data into the shared storage worklet module using [window.sharedStorage.run()](/en-US/docs/Web/API/WindowSharedStorage/run) (this is unrelated to the contextual data from the embedding document):

js

```
const frameData = {
  // Data available only inside the fenced frame
};

await window.sharedStorage.worklet.addModule("reporting-worklet.js");

await window.sharedStorage.run("send-report", {
  data: {
    frameData,
  },
});
```

In the `reporting-worklet.js` worklet, we read the embedding document's event ID from `sharedStorage.context` and the frame's event-level data from the data object. We then report them through Private Aggregation:

js

```
class ReportingOperation {
  convertEventIdToBucket(eventId) {
    // …
  }
  convertEventPayloadToValue(info) {
    // …
  }

  async run(data) {
    // Data from the embedder
    const eventId = sharedStorage.context;

    // Data from the fenced frame
    const eventPayload = data.frameData;

    privateAggregation.sendHistogramReport({
      bucket: convertEventIdToBucket(eventId),
      value: convertEventPayloadToValue(eventPayload),
    });
  }
}

register("send-report", ReportingOperation);
```

## [Specifications](#specifications)

This feature does not appear to be defined in any specification.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WorkletSharedStorage/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/workletsharedstorage/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorkletSharedStorage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fworkletsharedstorage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorkletSharedStorage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fworkletsharedstorage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F923adb616baa87402ca965ebd18a73380cc84d27%0A*+Document+last+modified%3A+2025-12-15T16%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
