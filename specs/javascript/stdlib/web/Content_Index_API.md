# Content Index API

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Content Index API allows developers to register their offline enabled content with the browser.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

As it stands, offline web content is not easily discoverable by users. Content indexing allows developers to tell the browser about their specific offline content. This allows users to discover and view what is available, whilst giving developers the ability to add and manage this content. Examples could be a news website prefetching the latest articles in the background, or a content streaming app registering downloaded content.

The Content Index API is an extension to [service workers](/en-US/docs/Web/API/Service_Worker_API), which allows developers to add URLs and metadata of already cached pages, under the scope of the current service worker. The browser can then use these entries to display offline reading to a user. As a developer you can also display these entries within your application.

Indexed entries do not automatically expire. It's good practice to present an interface for clearing out entries, or periodically remove older entries.

Note: The API supports indexing URLs corresponding to HTML documents. A URL for a cached media file, for example, can't be indexed directly. Instead, you need to provide a URL for a page that displays media, and which works offline.

## [Interfaces](#interfaces)

[ContentIndex](/en-US/docs/Web/API/ContentIndex)Experimental

Provides functionality to register content available offline.

[ContentIndexEvent](/en-US/docs/Web/API/ContentIndexEvent)Experimental

Defines the object used to represent the [contentdelete](/en-US/docs/Web/API/ServiceWorkerGlobalScope/contentdelete_event) event.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

The following additions to the [ServiceWorker](/en-US/docs/Web/API/ServiceWorker) have been specified in the Content Index API spec to provide an entry point for using content indexing.

[ServiceWorkerRegistration.index](/en-US/docs/Web/API/ServiceWorkerRegistration/index)Read onlyExperimental

Returns a reference to the [ContentIndex](/en-US/docs/Web/API/ContentIndex) interface for indexing cached pages.

[contentdelete](/en-US/docs/Web/API/ServiceWorkerGlobalScope/contentdelete_event) event Experimental

Fired when content is removed by the user agent.

## [Examples](#examples)

All the following examples assume a service worker has been registered. For more information see the [Service Worker API](/en-US/docs/Web/API/Service_Worker_API).

### [Feature detection and interface access](#feature_detection_and_interface_access)

Here we get a reference to the [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration), then check for the `index` property, which gives us access to the content index interface.

js

```
// reference registration
const registration = await navigator.serviceWorker.ready;

// feature detection
if ("index" in registration) {
  // Content Index API functionality
  const contentIndex = registration.index;
}
```

### [Adding to the content index](#adding_to_the_content_index)

Here we're declaring an item in the correct format and creating an asynchronous function which uses the [add()](/en-US/docs/Web/API/ContentIndex/add) method to register it with the content index.

js

```
// our content
const item = {
  id: "post-1",
  url: "/posts/amet.html",
  title: "Amet consectetur adipisicing",
  description:
    "Repellat et quia iste possimus ducimus aliquid a aut eaque nostrum.",
  icons: [
    {
      src: "/media/dark.png",
      sizes: "128x128",
      type: "image/png",
    },
  ],
  category: "article",
};

// our asynchronous function to add indexed content
async function registerContent(data) {
  const registration = await navigator.serviceWorker.ready;

  // feature detect Content Index
  if (!registration.index) {
    return;
  }

  // register content
  try {
    await registration.index.add(data);
  } catch (e) {
    console.log("Failed to register content: ", e.message);
  }
}
```

### [Retrieving items within the current index](#retrieving_items_within_the_current_index)

The below example shows an asynchronous function that retrieves items within the content index and iterates over each entry, building a list for the interface.

js

```
async function createReadingList() {
  // access our service worker registration
  const registration = await navigator.serviceWorker.ready;

  // get our index entries
  const entries = await registration.index.getAll();

  // create a containing element
  const readingListElem = document.createElement("div");

  // test for entries
  if (entries.length === 0) {
    // if there are no entries, display a message
    const message = document.createElement("p");
    message.innerText =
      "You currently have no articles saved for offline reading.";

    readingListElem.append(message);
  } else {
    // if entries are present, display in a list of links to the content
    const listElem = document.createElement("ul");

    for (const entry of entries) {
      const listItem = document.createElement("li");

      const anchorElem = document.createElement("a");
      anchorElem.innerText = entry.title;
      anchorElem.setAttribute("href", entry.url);

      listElem.append(listItem);
    }

    readingListElem.append(listElem);
  }
}
```

### [Unregistering indexed content](#unregistering_indexed_content)

Below is an asynchronous function, that removes an item from the content index.

js

```
async function unregisterContent(article) {
  // reference registration
  const registration = await navigator.serviceWorker.ready;

  // feature detect Content Index
  if (!registration.index) return;

  // unregister content from index
  await registration.index.delete(article.id);
}
```

All the above methods are available within the scope of the [service worker](/en-US/docs/Web/API/ServiceWorker). They are accessible from the [WorkerGlobalScope.self](/en-US/docs/Web/API/WorkerGlobalScope/self) property:

js

```
// service worker script

self.registration.index.add(item);

self.registration.index.delete(item.id);

const contentIndexItems = self.registration.index.getAll();
```

### [The contentdelete event](#the_contentdelete_event)

When an item is removed from the user agent interface, a `contentdelete` event is received by the service worker.

js

```
self.addEventListener("contentdelete", (event) => {
  console.log(event.id);

  // logs content index id, which can then be used to determine what content to delete from your cache
});
```

The [contentdelete](/en-US/docs/Web/API/ServiceWorkerGlobalScope/contentdelete_event) event is only fired when the deletion happens due to interaction with the browser's built-in user interface. It is not fired when the [ContentIndex.delete()](/en-US/docs/Web/API/ContentIndex/delete) method is called.

## [Specifications](#specifications)

Specification[Content Index](https://wicg.github.io/content-index/spec/)

## [Browser compatibility](#browser_compatibility)

### [api.ContentIndex](#api.ContentIndex)

### [api.ServiceWorkerRegistration.index](#api.ServiceWorkerRegistration.index)

## [See also](#see_also)

- [An introductory article on the Content Index API](https://developer.chrome.com/docs/capabilities/web-apis/content-indexing-api)
- [Service Worker API, along with information about Cache and CacheStorage](/en-US/docs/Web/API/Service_Worker_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 29, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Content_Index_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/content_index_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContent_Index_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcontent_index_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContent_Index_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcontent_index_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6c3bed9bcd275fd4ad714c4df0ed874e9bf87681%0A*+Document+last+modified%3A+2024-08-29T15%3A26%3A12.000Z%0A%0A%3C%2Fdetails%3E)
