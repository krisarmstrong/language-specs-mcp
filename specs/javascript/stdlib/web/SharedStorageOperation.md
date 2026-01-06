# SharedStorageOperation

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `SharedStorageOperation` interface of the [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API) represents the base class for all output gate operation types.

The output gate types are detailed below:

NameDescriptionDefined byInvoked byURL SelectionUsed to select a URL to display to the user based on shared storage data.[SharedStorageSelectURLOperation](/en-US/docs/Web/API/SharedStorageSelectURLOperation)[selectURL()](/en-US/docs/Web/API/WindowSharedStorage/selectURL)RunA generic way to process some shared storage data. Used, for example, by the [Private Aggregation API](https://privacysandbox.google.com/private-advertising/private-aggregation) to process shared storage data and generate aggregated reports. [SharedStorageRunOperation](/en-US/docs/Web/API/SharedStorageRunOperation)[run()](/en-US/docs/Web/API/WindowSharedStorage/run)

## In this article

- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Examples](#examples)

### [Defining individual operations](#defining_individual_operations)

Many shared storage worklet module scripts only define and register a single operation; you can see examples on the [SharedStorageSelectURLOperation](/en-US/docs/Web/API/SharedStorageSelectURLOperation) and [SharedStorageRunOperation](/en-US/docs/Web/API/SharedStorageRunOperation) pages.

### [Defining multiple operations](#defining_multiple_operations)

In more advanced cases, it is possible to define and register multiple operations in the same shared storage worklet module script with different names. In the following worklet module script, we define a URL Selection operation called `SelectURLOperation` that selects a URL for A/B testing, and a Run operation called `ExperimentGroupReportingOperation`, which runs a histogram report based on the user's A/B testing group:

js

```
// ab-testing-worklet.js

class SelectURLOperation {
  async run(urls, data) {
    // Read the user's group from shared storage
    const experimentGroup = await sharedStorage.get("ab-testing-group");

    // Log to console for the demo
    console.log(`urls = ${JSON.stringify(urls)}`);
    console.log(`data = ${JSON.stringify(data)}`);
    console.log(`ab-testing-group in shared storage is ${experimentGroup}`);

    // Return the index of the group
    return data.indexOf(experimentGroup);
  }
}

function getBucketForTestingGroup(testingGroup) {
  switch (testingGroup) {
    case "control":
      return 0;
    case "experiment-a":
      return 1;
    case "experiment-b":
      return 2;
  }
}

class ExperimentGroupReportingOperation {
  async run() {
    const experimentGroup = await sharedStorage.get("ab-testing-group");

    const bucket = BigInt(getBucketForTestingGroup(experimentGroup));
    privateAggregation.contributeToHistogram({ bucket, value: 1 });
  }
}

// Register the operations
register("ab-testing", SelectURLOperation);
register("experiment-group-reporting", ExperimentGroupReportingOperation);
```

In the main browsing context, these operations are invoked by [selectURL()](/en-US/docs/Web/API/WindowSharedStorage/selectURL) and [run()](/en-US/docs/Web/API/WindowSharedStorage/run), respectively. The operations to invoke via these methods are selected using the names they were registered with, and they are also required to conform to the structures defined by the [SharedStorageSelectURLOperation](/en-US/docs/Web/API/SharedStorageSelectURLOperation) and [SharedStorageRunOperation](/en-US/docs/Web/API/SharedStorageRunOperation) classes and their `run()` methods.

js

```
// For demo purposes. The hostname is used to determine the usage of
// development localhost URL vs production URL
const contentProducerUrl = window.location.host;

// Map the experiment groups to the URLs
const EXPERIMENT_MAP = [
  {
    group: "control",
    url: `https://${contentProducerUrl}/ads/default-ad.html`,
  },
  {
    group: "experiment-a",
    url: `https://${contentProducerUrl}/ads/experiment-ad-a.html`,
  },
  {
    group: "experiment-b",
    url: `https://${contentProducerUrl}/ads/experiment-ad-b.html`,
  },
];

// Choose a random group for the initial experiment
function getRandomExperiment() {
  const randomIndex = Math.floor(Math.random() * EXPERIMENT_MAP.length);
  return EXPERIMENT_MAP[randomIndex].group;
}

async function injectAd() {
  // Load the worklet module
  await window.sharedStorage.worklet.addModule("ab-testing-worklet.js");

  // Set the initial value in the storage to a random experiment group
  window.sharedStorage.set("ab-testing-group", getRandomExperiment(), {
    ignoreIfPresent: true,
  });

  const urls = EXPERIMENT_MAP.map(({ url }) => ({ url }));
  const groups = EXPERIMENT_MAP.map(({ group }) => group);

  // Resolve the selectURL call to a fenced frame config only when it exists on the page
  const resolveToConfig = typeof window.FencedFrameConfig !== "undefined";

  // Run the URL selection operation to select an ad based on the experiment group in shared storage
  const selectedUrl = await window.sharedStorage.selectURL("ab-testing", urls, {
    data: groups,
    resolveToConfig,
    keepAlive: true,
  });

  const adSlot = document.getElementById("ad-slot");

  if (resolveToConfig && selectedUrl instanceof FencedFrameConfig) {
    adSlot.config = selectedUrl;
  } else {
    adSlot.src = selectedUrl;
  }

  // Run the reporting operation
  await window.sharedStorage.run("experiment-group-reporting");
}

injectAd();
```

## [Specifications](#specifications)

This feature does not appear to be defined in any specification.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Shared Storage API](/en-US/docs/Web/API/Shared_Storage_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SharedStorageOperation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/sharedstorageoperation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedStorageOperation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsharedstorageoperation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedStorageOperation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsharedstorageoperation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F923adb616baa87402ca965ebd18a73380cc84d27%0A*+Document+last+modified%3A+2025-12-15T16%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
