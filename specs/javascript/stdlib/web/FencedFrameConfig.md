# FencedFrameConfig

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFencedFrameConfig&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `FencedFrameConfig` interface represents the navigation of a [<fencedframe>](/en-US/docs/Web/HTML/Reference/Elements/fencedframe), i.e., what content will be displayed in it.

`FencedFrameConfig` objects cannot be constructed manually via JavaScript. They are returned from a source such as the [Protected Audience API](https://privacysandbox.google.com/private-advertising/protected-audience) and set as the value of [HTMLFencedFrameElement.config](/en-US/docs/Web/API/HTMLFencedFrameElement/config).

A `FencedFrameConfig` object instance has an exposed method, but it also maps to internal config information containing opaque properties not accessible from JavaScript. This includes information such as the source of the loaded content and interest groups for advertising purposes. It is key to how fenced frames help to implement key use cases while respecting user privacy.

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[setSharedStorageContext()](/en-US/docs/Web/API/FencedFrameConfig/setSharedStorageContext)Experimental

Passes in data from the embedding document to the `<fencedframe>`'s shared storage.

## [Examples](#examples)

### [Basic usage](#basic_usage)

To set what content will be shown in a `<fencedframe>`, a utilizing API (such as [Protected Audience](https://privacysandbox.google.com/private-advertising/protected-audience) or [Shared Storage](https://privacysandbox.google.com/private-advertising/shared-storage)) generates a `FencedFrameConfig` object, which is then set as the value of the `<fencedframe>`'s `config` property.

The following example gets a `FencedFrameConfig` from a Protected Audience API's ad auction, which is then used to display the winning ad in a `<fencedframe>`:

js

```
const frameConfig = await navigator.runAdAuction({
  // … auction configuration
  resolveToConfig: true,
});

const frame = document.createElement("fencedframe");
frame.config = frameConfig;
```

Note:`resolveToConfig: true` must be passed in to the `runAdAuction()` call to obtain a `FencedFrameConfig` object. If it is not set, the resulting [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) will resolve to a URN that can only be used in an [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe).

### [Passing contextual data via setSharedStorageContext()](#passing_contextual_data_via_setsharedstoragecontext)

You can use the [Private Aggregation API](https://privacysandbox.google.com/private-advertising/private-aggregation) to create reports that combine event-level data inside fenced frames with contextual data from the embedding document. `setSharedStorageContext()` can be used to pass contextual data from the embedder to shared storage worklets initiated by the [Protected Audience API](https://privacysandbox.google.com/private-advertising/protected-audience).

In the following example, we store data from both the embedding page and the fenced frame in [shared storage](https://privacysandbox.google.com/private-advertising/shared-storage).

In the embedding page, we will set a mock event ID as the shared storage context using `setSharedStorageContext()`:

js

```
const frameConfig = await navigator.runAdAuction({ resolveToConfig: true });

// Data from the embedder that you want to pass to the shared storage worklet
frameConfig.setSharedStorageContext("some-event-id");

const frame = document.createElement("fencedframe");
frame.config = frameConfig;
```

Inside the fenced frame, we add the worklet module with [window.sharedStorage.worklet.addModule()](/en-US/docs/Web/API/Worklet/addModule), and then send the event-level data into the shared storage worklet using [window.sharedStorage.run()](/en-US/docs/Web/API/WindowSharedStorage/run) (this is unrelated to the contextual data from the embedding document):

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

In the `reporting-worklet.js` worklet, we read the embedding document's event ID from `sharedStorage.context` and the frame's event-level data from the data object, then report them through [Private Aggregation](https://privacysandbox.google.com/private-advertising/private-aggregation):

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

Specification
[Fenced Frame# fenced-frame-config-interface](https://wicg.github.io/fenced-frame/#fenced-frame-config-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Fenced frames](https://privacysandbox.google.com/private-advertising/fenced-frame) on privacysandbox.google.com
- [The Privacy Sandbox](https://privacysandbox.google.com/) on privacysandbox.google.com

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FencedFrameConfig/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fencedframeconfig/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFencedFrameConfig&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffencedframeconfig%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFencedFrameConfig%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffencedframeconfig%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa84b606ffd77c40a7306be6c932a74ab9ce6ab96%0A*+Document+last+modified%3A+2025-06-24T06%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
