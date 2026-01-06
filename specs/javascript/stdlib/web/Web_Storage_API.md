# Web Storage API

The Web Storage API provides mechanisms by which browsers can store key/value pairs, in a much more intuitive fashion than using [cookies](/en-US/docs/Glossary/Cookie).

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Determining storage access by a third party](#determining_storage_access_by_a_third_party)
- [Web Storage interfaces](#web_storage_interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [Private Browsing / Incognito modes](#private_browsing_incognito_modes)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

The two mechanisms within Web Storage are as follows:

- `sessionStorage` is partitioned by browser tabs and by [origin](/en-US/docs/Glossary/Origin). The main document, and all embedded [browsing contexts](/en-US/docs/Glossary/Browsing_context) (iframes), are grouped by their origin and each origin has access to its own separate storage area. Closing the browser tab destroys all `sessionStorage` data associated with that tab.
- `localStorage` is partitioned by [origin](/en-US/docs/Glossary/Origin) only. All documents with the same origin have access to the same `localStorage` area, and it persists even when the browser is closed and reopened.

These mechanisms are available via the [Window.sessionStorage](/en-US/docs/Web/API/Window/sessionStorage) and [Window.localStorage](/en-US/docs/Web/API/Window/localStorage) properties. Accessing one of these will return an instance of a [Storage](/en-US/docs/Web/API/Storage) object, through which data items can be set, retrieved and removed. A different storage object is used for the `sessionStorage` and `localStorage` for each origin — they function and are controlled separately.

To learn about the amount of storage available using the APIs, and what happens when storage limits are exceeded, see [Storage quotas and eviction criteria](/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria).

Both `sessionStorage` and `localStorage` in Web Storage are synchronous in nature. This means that when data is set, retrieved, or removed from these storage mechanisms, the operations are performed synchronously, blocking the execution of other JavaScript code until the operation is completed. This synchronous behavior can potentially affect the performance of the web application, especially if there is a large amount of data being stored or retrieved.

Developers should be cautious when performing operations on `sessionStorage` or `localStorage` that involve a significant amount of data or computationally intensive tasks. It is important to optimize code and minimize synchronous operations to prevent blocking the user interface and causing delays in the application's responsiveness.

Asynchronous alternatives, such as [IndexedDB](/en-US/docs/Web/API/IndexedDB_API), may be more suitable for scenarios where performance is a concern or when dealing with larger datasets. These alternatives allow for non-blocking operations, enabling smoother user experiences and better performance in web applications.

Note: Access to Web Storage from third-party IFrames is denied if the user has [disabled third-party cookies](https://support.mozilla.org/en-US/kb/third-party-cookies-firefox-tracking-protection).

## [Determining storage access by a third party](#determining_storage_access_by_a_third_party)

Each origin has its own storage — this is true for both web storage and [shared storage](/en-US/docs/Web/API/Shared_Storage_API). However, access of third-party (i.e., embedded) code to shared storage depends on its [browsing context](/en-US/docs/Glossary/Browsing_context). The context in which a third-party code from another origin runs determines the storage access of the third-party code.

Third-party code can be added to another site by injecting it with a [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element or by setting the source of an [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe) to a site that contains third-party code. The method used for integrating third-party code determines the browsing context of the code.

- If your third-party code is added to another site with a `<script>` element, your code will be executed in the browsing context of the embedder. Therefore, when you call [Storage.setItem()](/en-US/docs/Web/API/Storage/setItem) or [SharedStorage.set()](/en-US/docs/Web/API/SharedStorage/set), the key/value pair will be written to the embedder's storage. From the browser's perspective, there is no difference between first-party code and third-party code when a `<script>` tag is used.
- When your third-party code is added to another site within an `<iframe>`, the code inside the `<iframe>` will be executed with the origin of the `<iframe>`'s browsing context. If the code inside the `<iframe>` calls [Storage.setItem()](/en-US/docs/Web/API/Storage/setItem), data will be written into the local or session storage of the `<iframe>`'s origin. If the `<iframe>` code calls [SharedStorage.set()](/en-US/docs/Web/API/SharedStorage/set), the data will be written into the shared storage of the `<iframe>`'s origin.

## [Web Storage interfaces](#web_storage_interfaces)

[Storage](/en-US/docs/Web/API/Storage)

Allows you to set, retrieve and remove data for a specific domain and storage type (session or local).

[Window](/en-US/docs/Web/API/Window)

The Web Storage API extends the [Window](/en-US/docs/Web/API/Window) object with two new properties — [Window.sessionStorage](/en-US/docs/Web/API/Window/sessionStorage) and [Window.localStorage](/en-US/docs/Web/API/Window/localStorage) — which provide access to the current domain's session and local [Storage](/en-US/docs/Web/API/Storage) objects respectively, and a [storage](/en-US/docs/Web/API/Window/storage_event) event handler that fires when a storage area changes (e.g., a new item is stored).

[StorageEvent](/en-US/docs/Web/API/StorageEvent)

The `storage` event is fired on a document's `Window` object when a storage area changes.

## [Examples](#examples)

To illustrate some typical web storage usage, we have created an example, imaginatively called [Web Storage Demo](https://github.com/mdn/dom-examples/tree/main/web-storage). The [landing page](https://mdn.github.io/dom-examples/web-storage/) provides controls that can be used to customize the color, font and decorative image. When you choose different options, the page is instantly updated; in addition your choices are stored in `localStorage`, so that when you leave the page then load it again later on your choices are remembered.

In addition, we have provided an [event output page](https://mdn.github.io/dom-examples/web-storage/event.html) — if you load this page in another tab, then make changes to your choices in the landing page, you'll see the updated storage information outputted as the [StorageEvent](/en-US/docs/Web/API/StorageEvent) is fired.

## [Specifications](#specifications)

Specification
[HTML# dom-localstorage-dev](https://html.spec.whatwg.org/multipage/webstorage.html#dom-localstorage-dev)
[HTML# dom-sessionstorage-dev](https://html.spec.whatwg.org/multipage/webstorage.html#dom-sessionstorage-dev)

## [Browser compatibility](#browser_compatibility)

### [api.Window.localStorage](#api.Window.localStorage)

### [api.Window.sessionStorage](#api.Window.sessionStorage)

## [Private Browsing / Incognito modes](#private_browsing_incognito_modes)

Private windows, incognito mode, and similarly named privacy browsing options, don't store data like history and cookies. In private mode, `localStorage` is treated like `sessionStorage`. The storage APIs are still available and fully functional, but all data stored in the private window is deleted when the browser or browser tab is closed.

## [See also](#see_also)

- [Using the Web Storage API](/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API)
- [Browser storage quotas and eviction criteria](/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 22, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Web_Storage_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/web_storage_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Storage_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fweb_storage_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Storage_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fweb_storage_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbc2cef34be29df5439a5a6162bd9e5b07d173571%0A*+Document+last+modified%3A+2025-02-22T01%3A29%3A39.000Z%0A%0A%3C%2Fdetails%3E)
