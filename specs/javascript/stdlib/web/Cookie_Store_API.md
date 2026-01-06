# Cookie Store API

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The Cookie Store API is an asynchronous API for managing cookies, available in windows and also [service workers](/en-US/docs/Web/API/Service_Worker_API).

## In this article

- [Concepts and Usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and Usage](#concepts_and_usage)

The original method of getting and setting cookies involves working with [document.cookie](/en-US/docs/Web/API/Document/cookie) to get and set cookie information as a string of key/value pairs. In addition to this being cumbersome and error prone, it also has a host of issues in the context of modern web development.

The `document.cookie` interface is [synchronous](/en-US/docs/Glossary/Synchronous), single-threaded, and blocking. When writing a cookie you must wait for the browser to update the string of all cookies. In addition, the reliance on [document](/en-US/docs/Web/API/Document) means that cookies cannot be accessed by service workers, as they cannot access the `document` object.

The Cookie Store API provides an updated method of managing cookies. It is [asynchronous](/en-US/docs/Glossary/Asynchronous) and promise-based, therefore does not block the event loop. It does not rely on [Document](/en-US/docs/Web/API/Document) and so is available to service workers. The methods for getting and setting cookies also provide more feedback by way of error messages. This means that web developers do not have to set then immediately read back a cookie to check that setting was successful.

## [Interfaces](#interfaces)

[CookieStore](/en-US/docs/Web/API/CookieStore)Experimental

The `CookieStore` interface enables getting and setting cookies.

[CookieStoreManager](/en-US/docs/Web/API/CookieStoreManager)Experimental

The `CookieStoreManager` interface provides a service worker registration to enable service workers to subscribe to cookie change events.

[CookieChangeEvent](/en-US/docs/Web/API/CookieChangeEvent)Experimental

A `CookieChangeEvent` named `change` is dispatched against `CookieStore` objects in [Window](/en-US/docs/Web/API/Window) contexts when any script-visible cookies changes occur.

[ExtendableCookieChangeEvent](/en-US/docs/Web/API/ExtendableCookieChangeEvent)

An `ExtendableCookieChangeEvent` named `cookiechange` is dispatched in [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) contexts when any script-visible cookie changes occur that match the service worker's cookie change subscription list.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[ServiceWorkerGlobalScope.cookieStore](/en-US/docs/Web/API/ServiceWorkerGlobalScope/cookieStore)Read onlyExperimental

Returns a reference to the [CookieStore](/en-US/docs/Web/API/CookieStore) object associated with the service worker.

[ServiceWorkerRegistration.cookies](/en-US/docs/Web/API/ServiceWorkerRegistration/cookies)Read onlyExperimental

Returns a reference to the [CookieStoreManager](/en-US/docs/Web/API/CookieStoreManager) interface, which enables a web app to subscribe to and unsubscribe from cookie change events.

[Window.cookieStore](/en-US/docs/Web/API/Window/cookieStore)Read onlyExperimental

Returns a reference to the [CookieStore](/en-US/docs/Web/API/CookieStore) object for the current document context.

[cookiechange](/en-US/docs/Web/API/ServiceWorkerGlobalScope/cookiechange_event) event Experimental

Fired when any cookie changes have occurred which match the service worker's cookie change subscription list.

## [Specifications](#specifications)

Specification[Cookie Store API](https://cookiestore.spec.whatwg.org/)

## [Browser compatibility](#browser_compatibility)

### [api.CookieStore](#api.CookieStore)

### [api.CookieStoreManager](#api.CookieStoreManager)

## [See also](#see_also)

- [Service Worker API](/en-US/docs/Web/API/Service_Worker_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 26, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Cookie_Store_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cookie_store_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCookie_Store_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcookie_store_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCookie_Store_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcookie_store_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb87a7ca843b0762664c660ec916e42a3e6afd4d9%0A*+Document+last+modified%3A+2025-09-26T15%3A25%3A07.000Z%0A%0A%3C%2Fdetails%3E)
