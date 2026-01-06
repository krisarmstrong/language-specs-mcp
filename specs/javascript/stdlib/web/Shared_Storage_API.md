# Shared Storage API

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Warning: This feature is currently opposed by one browser vendor. See the [Standards positions](#standards_positions) section below for details.

The Shared Storage API is a client-side storage mechanism that enables unpartitioned, cross-site data access while preserving privacy (i.e., without relying on tracking cookies).

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Output gates](#output_gates)
- [Understanding how shared storage works](#understanding_how_shared_storage_works)
- [Differences between shared storage and web storage](#differences_between_shared_storage_and_web_storage)
- [Interfaces](#interfaces)
- [Enrollment and local testing](#enrollment_and_local_testing)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

One major source of [privacy](/en-US/docs/Web/Privacy) and [security](/en-US/docs/Web/Security) problems on the web is the use of cookies set on third-party content embedded in sites (for example via [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe) elements). These cookies can be used to track and profile users, and share information across sites.

To prevent cross-site tracking, browsers are working towards partitioning all storage types, including [Cookies](/en-US/docs/Web/HTTP/Guides/Cookies), [Web Storage](/en-US/docs/Web/API/Web_Storage_API), [IndexedDB](/en-US/docs/Web/API/IndexedDB_API), and the [Cache API](/en-US/docs/Web/API/Cache). However, a major barrier to achieving this is the need for several legitimate use cases that rely on cross-site information sharing. Examples of such use cases include advertisers wanting to measure the reach of their ads across sites and generate reports, and site owners wanting to customize user experiences based on the group they are in or their previous site interactions.

The Shared Storage API provides a flexible solution for such use cases. It aims to provide the required data storage, processing, and sharing capabilities without the ability to track and profile users.

Like other storage APIs, you can write to shared storage at any time. However, you can only read shared storage data from inside a [worklet](/en-US/docs/Web/API/SharedStorageWorklet). Worklets provide a secure environment inside which you can process shared storage data and return useful results, but you can't directly share the data with the associated browsing context.

To extract useful results from a shared storage worklet, you need to use an output gate. These gates serve specific purposes such as selecting a URL from a provided list to display to the user based on shared storage data. Results meant for the user are shown securely inside a [fenced frame](/en-US/docs/Web/API/Fenced_frame_API) where they can't be accessed from the embedding page.

## [Output gates](#output_gates)

The currently available output gates for the Shared Storage API are discussed in the sections below. In each section, we list typical use cases for each gate and provide links to guides with more information and code examples.

Note: More output gates will likely be added in the future to support additional use cases.

### [URL Selection](#url_selection)

The URL Selection output gate, accessed via the [selectURL()](/en-US/docs/Web/API/WindowSharedStorage/selectURL) method, is used to select a URL from a provided list to display to the user, based on shared storage data. This gate be used for the following purposes:

- [Creative rotation](https://privacysandbox.google.com/private-advertising/select-url/creative-rotation): Use stored data such as creative IDs, view counts, and user interaction to determine which creative content users see across different sites. This approach helps in balancing views and prevents overexposure of certain content, which in turn can help avoid a negative user experience.
- [A/B testing](https://privacysandbox.google.com/private-advertising/select-url/ab-testing): Assign a user to an experiment group, then store group details in shared storage for cross-site access.
- [Custom user experiences](https://privacysandbox.google.com/private-advertising/select-url/known-customer): Share custom content and calls-to-action based on a user's registration status or other user states.

### [Run](#run)

The Run output gate, accessed via the [run()](/en-US/docs/Web/API/WindowSharedStorage/run) method, is intended to be used in a generic way to process some shared storage data.

The [Private Aggregation API](https://privacysandbox.google.com/private-advertising/private-aggregation) can use the Run output gate to process shared storage data and generate aggregated reports. These reports can be used in the following use cases:

- [Unique reach reporting](https://privacysandbox.google.com/private-advertising/private-aggregation/unique-reach): Content producers and advertisers often want to know the number of unique viewers for their content. You can use shared storage to report the first time a user sees your ad or embedded publication and prevent duplicate counting for the same user on a different site, giving you an aggregated noisy report of approximate unique reach.
- [User demographic reporting](https://privacysandbox.google.com/private-advertising/private-aggregation/user-demographics): Content producers often want to understand the demographics of their audience. You can use shared storage to record user demographic data on your main site, and use aggregated reporting to report on it across other sites in embedded contexts.
- [K+ frequency measurement](https://privacysandbox.google.com/private-advertising/private-aggregation/k-freq-reach): Sometimes described as "effective frequency", K+ frequency refers to the minimum number of views needed before a user will recognize or recall certain content (often used in the context of ad views). You can use shared storage to build reports of unique users who have seen a piece of content at least K times.

## [Understanding how shared storage works](#understanding_how_shared_storage_works)

There are two parts to using the Shared Storage API — writing data to storage and reading/processing it. To give you an idea of how these parts are handled, we'll walk you through the basic [A/B testing](https://privacysandbox.google.com/private-advertising/select-url/ab-testing) example from developer.chrome.com. In this example, a user is assigned to an experiment group, and the group details are stored in shared storage. Other sites are able to use this data when choosing a URL to display in a [fenced frame](/en-US/docs/Web/API/Fenced_frame_API).

### [Writing to shared storage](#writing_to_shared_storage)

Writing data to shared storage is simple — you use methods defined on the [SharedStorage](/en-US/docs/Web/API/SharedStorage) interface to [set](/en-US/docs/Web/API/SharedStorage/set), [append](/en-US/docs/Web/API/SharedStorage/append), or [delete](/en-US/docs/Web/API/SharedStorage/delete)/[clear](/en-US/docs/Web/API/SharedStorage/clear) data.

This functionality is available in two different contexts:

- In the main browsing context, where your site or app runs, on [WindowSharedStorage](/en-US/docs/Web/API/WindowSharedStorage). This is available via `window.sharedStorage`.
- In the context of your shared storage worklet, on [WorkletSharedStorage](/en-US/docs/Web/API/WorkletSharedStorage). This is available via `this.sharedStorage`.

In our A/B testing example, we define a function in our app context that generates a random number — 0 or 1 — to represent an experiment group. We then run the [window.sharedStorage.set()](/en-US/docs/Web/API/SharedStorage/set) function to assign the user to a group and save the result in shared storage:

js

```
// Randomly assigns a user to a group 0 or 1
function getExperimentGroup() {
  return Math.round(Math.random());
}

async function injectContent() {
  // Assign user to a random group (0 or 1) and store it in shared storage
  window.sharedStorage.set("ab-testing-group", getExperimentGroup(), {
    ignoreIfPresent: true,
  });
}
```

Note: The `ignoreIfPresent: true` option causes the `set()` function to abort if the shared storage already contains a data item with the specified key.

### [Reading and processing data from shared storage](#reading_and_processing_data_from_shared_storage)

As mentioned above, to extract useful results from a shared storage worklet, you need to use an output gate. In this example, we'll use the [URL Selection output gate](#url_selection) to read the user's experiment group and then display a URL in a fenced frame based on their group.

To use the output gate, you need to:

1. Define an operation in a worklet module script to handle choosing the URL, and register it.
2. Add the module to your shared storage worklet.
3. Choose the URL using the worklet operation and load it in a fenced frame.

Below we'll look at these steps one by one.

#### Define an operation in a worklet module

The URL selection is based on the experiment group stored in shared storage. To retrieve this value and choose a URL based on it, we need to define an operation in a [SharedStorageWorklet](/en-US/docs/Web/API/SharedStorageWorklet) context. This ensures the raw data is hidden from other contexts, thereby preserving privacy.

The URL Selection operation is a JavaScript class that must follow the rules below (these rules vary for each output gate, depending on their intended use case):

- The actual functionality must be contained in an asynchronous `run()` method, which takes an array of objects containing URLs as its first parameter and a data object as its second parameter (when called, the data argument is optional).
- The `run()` method must return a number, which will equate to the number of the URL chosen.

Note: Each output gate has a corresponding interface that defines the required structure of its class and `run()` method. For URL Selection, see [SharedStorageSelectURLOperation](/en-US/docs/Web/API/SharedStorageSelectURLOperation).

Once the operation is defined, it needs to be registered using [SharedStorageWorkletGlobalScope.register()](/en-US/docs/Web/API/SharedStorageWorkletGlobalScope/register).

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

Notice how the value set in our main app context is retrieved using [WorkletSharedStorage.get()](/en-US/docs/Web/API/WorkletSharedStorage/get). To reiterate, to preserve privacy and mitigate data leakage, you can read values from shared storage only within a worklet.

Note: It is possible to define and register multiple operations in the same shared storage worklet module script with different names; see [SharedStorageOperation](/en-US/docs/Web/API/SharedStorageOperation) for an example.

#### Add the module to the shared storage worklet

To use the operation defined in the worklet module, it needs to be added to the shared storage worklet using [window.sharedStorage.worklet.addModule()](/en-US/docs/Web/API/Worklet/addModule). In our main app context, this is done before we set the experiment group value, so that it is ready to use when needed:

js

```
async function injectContent() {
  // Add the module to the shared storage worklet
  await window.sharedStorage.worklet.addModule("ab-testing-worklet.js");

  // Assign user to a random group (0 or 1) and store it in shared storage
  window.sharedStorage.set("ab-testing-group", getExperimentGroup(), {
    ignoreIfPresent: true,
  });
}
```

#### Choose a URL and load it in a fenced frame

To run the operation defined in the worklet, we call [WindowSharedStorage.selectURL()](/en-US/docs/Web/API/WindowSharedStorage/selectURL). This method acts as a proxy to our worklet operation, accessing it securely and returning the result without leaking any data. `selectURL()` is the correct method to call our user-defined worklet operation because it was defined with the appropriate class structure for a URL Selection operation, as discussed above.

`selectURL()` expects an array of objects containing URLs to choose from, an optional options object, and for the underlying operation to return an integer that it can use to choose a URL.

js

```
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
```

Because the options object contains `resolveToConfig: true`, the returned [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) will resolve with a [FencedFrameConfig](/en-US/docs/Web/API/FencedFrameConfig) object. This object can be set as the value of the [HTMLFencedFrameElement.config](/en-US/docs/Web/API/HTMLFencedFrameElement/config) property, resulting in the content of the chosen URL being displayed in the corresponding [<fencedframe>](/en-US/docs/Web/HTML/Reference/Elements/fencedframe) element:

js

```
document.getElementById("content-slot").config = fencedFrameConfig;
```

The full app script looks like so:

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

## [Differences between shared storage and web storage](#differences_between_shared_storage_and_web_storage)

The key difference is that shared storage is intended for use with cross-origin data after storage has been partitioned.

- If you are a publisher and you want to store first-party data that is accessible to only you, use the [localStorage](/en-US/docs/Web/API/Window/localStorage) version of [web storage](/en-US/docs/Web/API/Web_Storage_API).
- If you want data to persist only during a browser session, use [sessionStorage](/en-US/docs/Web/API/Window/sessionStorage).
- If you are operating as a third-party on another site, and you want to record data from that site to access later on another site, use shared storage.

Another important difference between shared storage and web storage is that reading from shared storage is guarded (writing to storage behaves similarly). With `localStorage` and `sessionStorage`, you can read freely. With shared storage, reading can happen only within a shared storage worklet, and the origin used for reading in the worklet is the same as the browsing context that created it.

Additionally, you cannot extract shared storage data outside of a shared storage worklet, as a tracking protection. You must use one of the output gates to work with your data in shared storage.

Lastly, data in `localStorage` persists until it is manually cleared. `sessionStorage` clears at the end of a browsing session, whereas shared storage data clears 30 days after the last write call.

## [Interfaces](#interfaces)

[SharedStorage](/en-US/docs/Web/API/SharedStorage)

Represents the shared storage for a particular origin. It defines methods to write data to the shared storage.

[WindowSharedStorage](/en-US/docs/Web/API/WindowSharedStorage)

Represents the shared storage for a particular origin as exposed to a standard browsing context. Among other things, it defines methods to use the available output gates, which act as proxies for the operations defined in the worklet.

[WorkletSharedStorage](/en-US/docs/Web/API/WorkletSharedStorage)

Represents the shared storage for a particular origin within a worklet context. Among other things, it defines methods to read the shared storage data.

[SharedStorageWorklet](/en-US/docs/Web/API/SharedStorageWorklet)

Represents the current origin's shared storage worklet. It contains the [addModule()](/en-US/docs/Web/API/Worklet/addModule) method for adding modules. Unlike a regular [Worklet](/en-US/docs/Web/API/Worklet), the `SharedStorageWorklet` can have only a single module added to it, for privacy reasons.

[SharedStorageWorkletGlobalScope](/en-US/docs/Web/API/SharedStorageWorkletGlobalScope)

Represents the global scope of a [SharedStorageWorklet](/en-US/docs/Web/API/SharedStorageWorklet) module. It contains the functionality to [register](/en-US/docs/Web/API/SharedStorageWorkletGlobalScope/register) a defined operation and [access the shared storage](/en-US/docs/Web/API/SharedStorageWorkletGlobalScope/sharedStorage).

### [Output gate operation signature definitions](#output_gate_operation_signature_definitions)

[SharedStorageOperation](/en-US/docs/Web/API/SharedStorageOperation)

Represents the base class for all different output gate operation types.

[SharedStorageRunOperation](/en-US/docs/Web/API/SharedStorageRunOperation)

Represents a Run output gate operation.

[SharedStorageSelectURLOperation](/en-US/docs/Web/API/SharedStorageSelectURLOperation)

Represents a URL Selection output gate operation.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Window.sharedStorage](/en-US/docs/Web/API/Window/sharedStorage)

Returns the [WindowSharedStorage](/en-US/docs/Web/API/WindowSharedStorage) object for the current origin.

## [Enrollment and local testing](#enrollment_and_local_testing)

To use the Shared Storage API in your sites, you must specify it in the [privacy sandbox enrollment process](/en-US/docs/Web/Privacy/Guides/Privacy_sandbox/Enrollment). If you don't, the Shared Storage API methods won't run successfully.

You can test your Shared Storage API code locally without enrollment. To allow local testing, enable the following Chrome developer flag:

`chrome://flags/#privacy-sandbox-enrollment-overrides`

## [Examples](#examples)

For extensive demos, see the [Shared Storage API demo site](https://shared-storage-demo.web.app/), which also includes some Private Aggregation API examples.

## [Specifications](#specifications)

Specification
[Shared Storage API# sharedstorage](https://wicg.github.io/shared-storage/#sharedstorage)

### [Standards positions](#standards_positions)

One browser vendor [opposes](/en-US/docs/Glossary/Web_standards#opposing_standards) this specification. Known standards positions are as follows:

- Mozilla (Firefox): [Negative](https://github.com/mozilla/standards-positions/issues/646)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Shared Storage](https://privacysandbox.google.com/private-advertising/shared-storage) on privacysandbox.google.com
- [The Privacy Sandbox](https://privacysandbox.google.com/) on privacysandbox.google.com

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Shared_Storage_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/shared_storage_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FShared_Storage_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fshared_storage_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FShared_Storage_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fshared_storage_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe936e7271df947f25184a5ba8a21445bbd4d056c%0A*+Document+last+modified%3A+2025-12-13T02%3A55%3A18.000Z%0A%0A%3C%2Fdetails%3E)
