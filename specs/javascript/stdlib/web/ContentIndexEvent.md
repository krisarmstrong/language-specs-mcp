# ContentIndexEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContentIndexEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `ContentIndexEvent` interface of the [content index](/en-US/docs/Web/API/Content_Index_API) defines the object used to represent the [contentdelete](/en-US/docs/Web/API/ServiceWorkerGlobalScope/contentdelete_event) event.

This event is sent to the [global scope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) of a [ServiceWorker](/en-US/docs/Web/API/ServiceWorker). It contains the id of the indexed content to be removed.

The [contentdelete](/en-US/docs/Web/API/ServiceWorkerGlobalScope/contentdelete_event) event is only fired when the deletion happens due to interaction with the browser's built-in user interface. It is not fired when the [ContentIndex.delete](/en-US/docs/Web/API/ContentIndex/delete) method is called.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ContentIndexEvent()](/en-US/docs/Web/API/ContentIndexEvent/ContentIndexEvent)Experimental

Creates and returns a new `ContentIndexEvent` object whose type and other options are configured as specified.

## [Instance properties](#instance_properties)

In addition to the properties listed below, this interface inherits the properties of its parent interface, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

[id](/en-US/docs/Web/API/ContentIndexEvent/id)Read onlyExperimental

A [String](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) which identifies the deleted content index via it's `id`.

## [Instance methods](#instance_methods)

While `ContentIndexEvent` offers no methods of its own, it inherits any specified by its parent interface, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

## [Examples](#examples)

This example shows the [service worker](/en-US/docs/Web/API/ServiceWorker) script listening for the [contentdelete](/en-US/docs/Web/API/ServiceWorkerGlobalScope/contentdelete_event) event and logs the removed content index id.

js

```
self.addEventListener("contentdelete", (event) => {
  console.log(event.id);

  // logs content index id, which can then be used to determine what content to delete from your cache
});
```

## [Specifications](#specifications)

Specification
[Content Index# content-index-event](https://wicg.github.io/content-index/spec/#content-index-event)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [An introductory article on the Content Index API](https://developer.chrome.com/docs/capabilities/web-apis/content-indexing-api)
- [Service Worker API, along with information about Cache and CacheStorage](/en-US/docs/Web/API/Service_Worker_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 29, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/ContentIndexEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/contentindexevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContentIndexEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcontentindexevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContentIndexEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcontentindexevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6c3bed9bcd275fd4ad714c4df0ed874e9bf87681%0A*+Document+last+modified%3A+2024-08-29T15%3A26%3A12.000Z%0A%0A%3C%2Fdetails%3E)
