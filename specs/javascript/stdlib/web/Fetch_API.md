# Fetch API

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2017⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFetch_API&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Fetch API provides an interface for fetching resources (including across the network). It is a more powerful and flexible replacement for [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest).

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

The Fetch API uses [Request](/en-US/docs/Web/API/Request) and [Response](/en-US/docs/Web/API/Response) objects (and other things involved with network requests), as well as related concepts such as CORS and the HTTP Origin header semantics.

For making a request and fetching a resource, use the [fetch()](/en-US/docs/Web/API/Window/fetch) method. It is a global method in both [Window](/en-US/docs/Web/API/Window) and [Worker](/en-US/docs/Web/API/WorkerGlobalScope) contexts. This makes it available in pretty much any context you might want to fetch resources in.

The `fetch()` method takes one mandatory argument, the path to the resource you want to fetch. It returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to the [Response](/en-US/docs/Web/API/Response) to that request — as soon as the server responds with headers — even if the server response is an HTTP error status. You can also optionally pass in an `init` options object as the second argument (see [Request](/en-US/docs/Web/API/Request)).

Once a [Response](/en-US/docs/Web/API/Response) is retrieved, there are a number of methods available to define what the body content is and how it should be handled.

You can create a request and response directly using the [Request()](/en-US/docs/Web/API/Request/Request) and [Response()](/en-US/docs/Web/API/Response/Response) constructors, but it's uncommon to do this directly. Instead, these are more likely to be created as results of other API actions (for example, [FetchEvent.respondWith()](/en-US/docs/Web/API/FetchEvent/respondWith) from service workers).

Find out more about using the Fetch API features in [Using Fetch](/en-US/docs/Web/API/Fetch_API/Using_Fetch).

## [Interfaces](#interfaces)

[Window.fetch()](/en-US/docs/Web/API/Window/fetch) and [WorkerGlobalScope.fetch()](/en-US/docs/Web/API/WorkerGlobalScope/fetch)

The `fetch()` method used to fetch a resource.

[Headers](/en-US/docs/Web/API/Headers)

Represents response/request headers, allowing you to query them and take different actions depending on the results.

[Request](/en-US/docs/Web/API/Request)

Represents a resource request.

[Response](/en-US/docs/Web/API/Response)

Represents the response to a request.

## [Specifications](#specifications)

Specification
[Fetch# fetch-method](https://fetch.spec.whatwg.org/#fetch-method)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using Fetch](/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [Service Worker API](/en-US/docs/Web/API/Service_Worker_API)
- [HTTP access control (CORS)](/en-US/docs/Web/HTTP/Guides/CORS)
- [HTTP](/en-US/docs/Web/HTTP)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 9, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Fetch_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fetch_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFetch_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffetch_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFetch_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffetch_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F31ba9f6da2dd1175250ece8d8d467d523e79b447%0A*+Document+last+modified%3A+2025-04-09T12%3A12%3A12.000Z%0A%0A%3C%2Fdetails%3E)
