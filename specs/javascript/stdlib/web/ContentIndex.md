# ContentIndex

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContentIndex&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ContentIndex` interface of the [Content Index API](/en-US/docs/Web/API/Content_Index_API) allows developers to register their offline enabled content with the browser.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

There are no properties of this interface.

## [Instance methods](#instance_methods)

[ContentIndex.add()](/en-US/docs/Web/API/ContentIndex/add)Experimental

Registers an item with the [content index](/en-US/docs/Web/API/Content_Index_API).

[ContentIndex.delete()](/en-US/docs/Web/API/ContentIndex/delete)Experimental

Unregisters an item from the currently indexed content.

[ContentIndex.getAll()](/en-US/docs/Web/API/ContentIndex/getAll)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with an iterable list of content index entries.

## [Examples](#examples)

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

Here we're declaring an item in the correct format and creating an asynchronous function which uses the [add()](/en-US/docs/Web/API/ContentIndex/add) method to register it with the [content index](/en-US/docs/Web/API/Content_Index_API).

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

The below example shows an asynchronous function that retrieves items within the [content index](/en-US/docs/Web/API/Content_Index_API) and iterates over each entry, building a list for the interface.

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

Below is an asynchronous function, that removes an item from the [content index](/en-US/docs/Web/API/Content_Index_API).

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

## [Specifications](#specifications)

Specification
[Content Index# content-index](https://wicg.github.io/content-index/spec/#content-index)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [An introductory article on the Content Index API](https://developer.chrome.com/docs/capabilities/web-apis/content-indexing-api)
- [Service Worker API, along with information about Cache and CacheStorage](/en-US/docs/Web/API/Service_Worker_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 29, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/ContentIndex/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/contentindex/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContentIndex&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcontentindex%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContentIndex%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcontentindex%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6c3bed9bcd275fd4ad714c4df0ed874e9bf87681%0A*+Document+last+modified%3A+2024-08-29T15%3A26%3A12.000Z%0A%0A%3C%2Fdetails%3E)
