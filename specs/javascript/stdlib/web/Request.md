# Request

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2017⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRequest&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `Request` interface of the [Fetch API](/en-US/docs/Web/API/Fetch_API) represents a resource request.

You can create a new `Request` object using the [Request()](/en-US/docs/Web/API/Request/Request) constructor, but you are more likely to encounter a `Request` object being returned as the result of another API operation, such as a service worker [FetchEvent.request](/en-US/docs/Web/API/FetchEvent/request).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[Request()](/en-US/docs/Web/API/Request/Request)

Creates a new `Request` object.

## [Instance properties](#instance_properties)

[Request.body](/en-US/docs/Web/API/Request/body)Read only

A [ReadableStream](/en-US/docs/Web/API/ReadableStream) of the body contents.

[Request.bodyUsed](/en-US/docs/Web/API/Request/bodyUsed)Read only

Stores `true` or `false` to indicate whether or not the body has been used in a request yet.

[Request.cache](/en-US/docs/Web/API/Request/cache)Read only

Contains the cache mode of the request (e.g., `default`, `reload`, `no-cache`).

[Request.credentials](/en-US/docs/Web/API/Request/credentials)Read only

Contains a value controlling whether credentials should be included with the request (e.g., `omit`, `same-origin`, `include`). The default is `same-origin`.

[Request.destination](/en-US/docs/Web/API/Request/destination)Read only

A string describing the type of content being requested.

[Request.duplex](/en-US/docs/Web/API/Request/duplex)Read onlyExperimental

The duplex mode of the request, which determines whether the browser must send the entire request before processing the response.

[Request.headers](/en-US/docs/Web/API/Request/headers)Read only

Contains the associated [Headers](/en-US/docs/Web/API/Headers) object of the request.

[Request.integrity](/en-US/docs/Web/API/Request/integrity)Read only

Contains the [subresource integrity](/en-US/docs/Web/Security/Defenses/Subresource_Integrity) value of the request (e.g., `sha256-BpfBw7ivV8q2jLiT13fxDYAe2tJllusRSZ273h2nFSE=`).

[Request.isHistoryNavigation](/en-US/docs/Web/API/Request/isHistoryNavigation)Read only

A boolean indicating whether the request is a history navigation.

[Request.keepalive](/en-US/docs/Web/API/Request/keepalive)Read only

Contains the request's `keepalive` setting (`true` or `false`), which indicates whether the browser will keep the associated request alive if the page that initiated it is unloaded before the request is complete.

[Request.method](/en-US/docs/Web/API/Request/method)Read only

Contains the request's method (`GET`, `POST`, etc.)

[Request.mode](/en-US/docs/Web/API/Request/mode)Read only

Contains the mode of the request (e.g., `cors`, `no-cors`, `same-origin`, `navigate`.)

[Request.redirect](/en-US/docs/Web/API/Request/redirect)Read only

Contains the mode for how redirects are handled. It may be one of `follow`, `error`, or `manual`.

[Request.referrer](/en-US/docs/Web/API/Request/referrer)Read only

Contains the referrer of the request (e.g., `client`).

[Request.referrerPolicy](/en-US/docs/Web/API/Request/referrerPolicy)Read only

Contains the referrer policy of the request (e.g., `no-referrer`).

[Request.signal](/en-US/docs/Web/API/Request/signal)Read only

Returns the [AbortSignal](/en-US/docs/Web/API/AbortSignal) associated with the request

[Request.url](/en-US/docs/Web/API/Request/url)Read only

Contains the URL of the request.

## [Instance methods](#instance_methods)

[Request.arrayBuffer()](/en-US/docs/Web/API/Request/arrayBuffer)

Returns a promise that resolves with an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) representation of the request body.

[Request.blob()](/en-US/docs/Web/API/Request/blob)

Returns a promise that resolves with a [Blob](/en-US/docs/Web/API/Blob) representation of the request body.

[Request.bytes()](/en-US/docs/Web/API/Request/bytes)

Returns a promise that resolves with a [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) representation of the request body.

[Request.clone()](/en-US/docs/Web/API/Request/clone)

Creates a copy of the current `Request` object.

[Request.formData()](/en-US/docs/Web/API/Request/formData)

Returns a promise that resolves with a [FormData](/en-US/docs/Web/API/FormData) representation of the request body.

[Request.json()](/en-US/docs/Web/API/Request/json)

Returns a promise that resolves with the result of parsing the request body as [JSON](/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON).

[Request.text()](/en-US/docs/Web/API/Request/text)

Returns a promise that resolves with a text representation of the request body.

Note: The request body functions can be run only once; subsequent calls will reject with TypeError showing that the body stream has already used.

## [Examples](#examples)

In the following snippet, we create a new request using the `Request()` constructor (for an image file in the same directory as the script), then return some property values of the request:

js

```
const request = new Request("https://www.mozilla.org/favicon.ico");

const url = request.url;
const method = request.method;
const credentials = request.credentials;
```

You could then fetch this request by passing the `Request` object in as a parameter to a [fetch()](/en-US/docs/Web/API/Window/fetch) call, for example:

js

```
fetch(request)
  .then((response) => response.blob())
  .then((blob) => {
    image.src = URL.createObjectURL(blob);
  });
```

In the following snippet, we create a new request using the `Request()` constructor with some initial data and body content for an API request which needs a body payload:

js

```
const request = new Request("https://example.com", {
  method: "POST",
  body: '{"foo": "bar"}',
});

const url = request.url;
const method = request.method;
const credentials = request.credentials;
const bodyUsed = request.bodyUsed;
```

Note: The body can only be a [Blob](/en-US/docs/Web/API/Blob), an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), a [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray), a [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView), a [FormData](/en-US/docs/Web/API/FormData), a [URLSearchParams](/en-US/docs/Web/API/URLSearchParams), a [ReadableStream](/en-US/docs/Web/API/ReadableStream), or a [String](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) object, as well as a string literal, so for adding a JSON object to the payload you need to stringify that object.

You could then fetch this API request by passing the `Request` object in as a parameter to a [fetch()](/en-US/docs/Web/API/Window/fetch) call, for example and get the response:

js

```
fetch(request)
  .then((response) => {
    if (response.status !== 200) {
      throw new Error("Something went wrong on API server!");
    }
    return response.json();
  })
  .then((response) => {
    console.debug(response);
    // …
  })
  .catch((error) => {
    console.error(error);
  });
```

## [Specifications](#specifications)

Specification
[Fetch# request-class](https://fetch.spec.whatwg.org/#request-class)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [ServiceWorker API](/en-US/docs/Web/API/Service_Worker_API)
- [HTTP access control (CORS)](/en-US/docs/Web/HTTP/Guides/CORS)
- [HTTP](/en-US/docs/Web/HTTP)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Request/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/request/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRequest&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frequest%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRequest%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frequest%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
