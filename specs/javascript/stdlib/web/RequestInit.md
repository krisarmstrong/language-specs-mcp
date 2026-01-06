# RequestInit

The `RequestInit` dictionary of the [Fetch API](/en-US/docs/Web/API/Fetch_API) represents the set of options that can be used to configure a [fetch request](/en-US/docs/Web/API/Window/fetch).

You can pass a `RequestInit` object into the [Request()](/en-US/docs/Web/API/Request/Request) constructor, or directly into the [fetch()](/en-US/docs/Web/API/Window/fetch) function call.

You can also construct a `Request` with a `RequestInit`, and pass the `Request` to a `fetch()` call along with another `RequestInit`. If you do this, and the same option is set in both places, then the value passed directly into `fetch()` is used.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[attributionReporting Optional 
Deprecated](#attributionreporting)

Indicates that you want the request's response to be able to register a JavaScript-based [attribution source](/en-US/docs/Web/API/Attribution_Reporting_API/Registering_sources#javascript-based_event_sources) or [attribution trigger](/en-US/docs/Web/API/Attribution_Reporting_API/Registering_triggers#javascript-based_attribution_triggers). `attributionReporting` is an object containing the following properties:

[eventSourceEligible](#eventsourceeligible)

A boolean. If set to `true`, the request's response is eligible to register an attribution source. If set to `false`, it isn't.

[triggerEligible](#triggereligible)

A boolean. If set to `true`, the request's response is eligible to register an attribution trigger. If set to `false`, it isn't.

See the [Attribution Reporting API](/en-US/docs/Web/API/Attribution_Reporting_API) for more details.

[body Optional](#body)

The request body contains content to send to the server, for example in a [POST](/en-US/docs/Web/HTTP/Reference/Methods/POST) or [PUT](/en-US/docs/Web/HTTP/Reference/Methods/PUT) request. It is specified as an instance of any of the following types:

- a string
- [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
- [Blob](/en-US/docs/Web/API/Blob)
- [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView)
- [File](/en-US/docs/Web/API/File)
- [FormData](/en-US/docs/Web/API/FormData)
- [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
- [URLSearchParams](/en-US/docs/Web/API/URLSearchParams)
- [ReadableStream](/en-US/docs/Web/API/ReadableStream)

See [Setting a body](/en-US/docs/Web/API/Fetch_API/Using_Fetch#setting_a_body) for more details.

[browsingTopics Optional 
Deprecated](#browsingtopics)

A boolean specifying that the selected topics for the current user should be sent in a [Sec-Browsing-Topics](/en-US/docs/Web/HTTP/Reference/Headers/Sec-Browsing-Topics) header with the associated request.

See [Using the Topics API](/en-US/docs/Web/API/Topics_API/Using) for more details.

[cache Optional](#cache)

The [cache mode](/en-US/docs/Web/API/Request/cache) you want to use for the request. This may be any one of the following values:

[default](#default)

The browser looks in its HTTP cache for a response matching the request.

- If there is a match and it is [fresh](/en-US/docs/Web/HTTP/Guides/Caching#fresh_and_stale_based_on_age), it will be returned from the cache.
- If there is a match but it is [stale](/en-US/docs/Web/HTTP/Guides/Caching#fresh_and_stale_based_on_age), the browser will make a [conditional request](/en-US/docs/Web/HTTP/Guides/Conditional_requests) to the remote server. If the server indicates that the resource has not changed, it will be returned from the cache. Otherwise the resource will be downloaded from the server and the cache will be updated.
- If there is no match, the browser will make a normal request, and will update the cache with the downloaded resource.

[no-store](#no-store)

The browser fetches the resource from the remote server without first looking in the cache, and will not update the cache with the downloaded resource.

[reload](#reload)

The browser fetches the resource from the remote server without first looking in the cache, but then will update the cache with the downloaded resource.

[no-cache](#no-cache)

The browser looks in its HTTP cache for a response matching the request.

- If there is a match, fresh or stale, the browser will make a [conditional request](/en-US/docs/Web/HTTP/Guides/Conditional_requests) to the remote server. If the server indicates that the resource has not changed, it will be returned from the cache. Otherwise the resource will be downloaded from the server and the cache will be updated.
- If there is no match, the browser will make a normal request, and will update the cache with the downloaded resource.

[force-cache](#force-cache)

The browser looks in its HTTP cache for a response matching the request.

- If there is a match, fresh or stale, it will be returned from the cache.
- If there is no match, the browser will make a normal request, and will update the cache with the downloaded resource.

[only-if-cached](#only-if-cached)

The browser looks in its HTTP cache for a response matching the request. Experimental

- If there is a match, fresh or stale, it will be returned from the cache.
- If there is no match, a network error is returned.

The `"only-if-cached"` mode can only be used if the request's [mode](/en-US/docs/Web/API/Request/mode) is `"same-origin"`. Cached redirects will be followed if the request's `redirect` property is `"follow"` and the redirects do not violate the `"same-origin"` mode.

[credentials Optional](#credentials)

Controls whether or not the browser sends credentials with the request, as well as whether any `Set-Cookie` response headers are respected. Credentials are cookies, [TLS](/en-US/docs/Glossary/TLS) client certificates, or authentication headers containing a username and password. This option may be any one of the following values:

[omit](#omit)

Never send credentials in the request or include credentials in the response.

[same-origin](#same-origin)

Only send and include credentials for same-origin requests.

[include](#include)

Always include credentials, even for cross-origin requests.

Including credentials in cross-origin requests can make a site vulnerable to [CSRF](/en-US/docs/Glossary/CSRF) attacks, so even if `credentials` is set to `include`, the server must also agree to their inclusion by including the [Access-Control-Allow-Credentials](/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Credentials) in its response. Additionally, in this situation the server must explicitly specify the client's origin in the [Access-Control-Allow-Origin](/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin) response header (that is, `*` is not allowed).

See [Including credentials](/en-US/docs/Web/API/Fetch_API/Using_Fetch#including_credentials) for more details.

Defaults to `same-origin`.

[duplex Optional 
Experimental](#duplex)

Controls duplex behavior of the request. If this is present it must have the value `half`, meaning that the browser must send the entire request before processing the response.

This option must be present when [body](#body) is a [ReadableStream](/en-US/docs/Web/API/ReadableStream).

[headers Optional](#headers)

Any headers you want to add to your request, contained within a [Headers](/en-US/docs/Web/API/Headers) object or an object literal whose keys are the names of headers and whose values are the header values.

Many headers are set automatically by the browser and can't be set by a script: these are called [Forbidden request headers](/en-US/docs/Glossary/Forbidden_request_header).

If the `mode` option is set to `no-cors`, you can only set [CORS-safelisted request headers](/en-US/docs/Glossary/CORS-safelisted_request_header).

See [Setting headers](/en-US/docs/Web/API/Fetch_API/Using_Fetch#setting_headers) for more details.

[integrity Optional](#integrity)

Contains the [subresource integrity](/en-US/docs/Web/Security/Defenses/Subresource_Integrity) value of the request.

This will be checked when the resource is fetched, just as it would be when the [integrity](/en-US/docs/Web/HTML/Reference/Elements/script#integrity) attribute is set on a [<script>](/en-US/docs/Web/HTML/Reference/Elements/script) element. The browser will compute the [hash](/en-US/docs/Glossary/Hash_function) of the fetched resource using the specified algorithm, and if the result does not match the value specified, the browser will reject the fetch request with a network error.

The format of this option is `<hash-algo>-<hash-source>` where:

- `<hash-algo>` is one of the following values: `sha256`, `sha384`, or `sha512`
- `<hash-source>` is the [Base64-encoding](/en-US/docs/Glossary/Base64) of the result of hashing the resource with the specified hash algorithm.

Defaults to an empty string.

[keepalive Optional](#keepalive)

A boolean. When set to `true`, the browser will not abort the associated request if the page that initiated it is unloaded before the request is complete. This enables a [fetch()](/en-US/docs/Web/API/Window/fetch) request to send analytics at the end of a session even if the user navigates away from or closes the page.

This has some advantages over using [Navigator.sendBeacon()](/en-US/docs/Web/API/Navigator/sendBeacon) for the same purpose. For example, you can use HTTP methods other than [POST](/en-US/docs/Web/HTTP/Reference/Methods/POST), customize request properties, and access the server response via the fetch [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) fulfillment. It is also available in [service workers](/en-US/docs/Web/API/Service_Worker_API).

The body size for `keepalive` requests is limited to 64 kibibytes.

Defaults to `false`.

[method Optional](#method)

The [request method](/en-US/docs/Web/HTTP/Reference/Methods).

Defaults to [GET](/en-US/docs/Web/HTTP/Reference/Methods/GET).

[mode Optional](#mode)

Sets cross-origin behavior for the request. One of the following values:

[same-origin](#same-origin_2)

Disallows cross-origin requests. If a `same-origin` request is sent to a different origin, the result is a network error.

[cors](#cors)

If the request is cross-origin then it will use the [Cross-Origin Resource Sharing (CORS)](/en-US/docs/Web/HTTP/Guides/CORS) mechanism. Only [CORS-safelisted response headers](/en-US/docs/Glossary/CORS-safelisted_response_header) are exposed in the response.

[no-cors](#no-cors)

Disables CORS for cross-origin requests. This option comes with the following restrictions:

- The method may only be one of `HEAD`, `GET` or `POST`.
- The headers may only be [CORS-safelisted request headers](/en-US/docs/Glossary/CORS-safelisted_request_header), with the additional restriction that the [Range](/en-US/docs/Web/HTTP/Reference/Headers/Range) header is also not allowed. This also applies to any headers added by service workers.
- The response is opaque, meaning that its headers and body are not available to JavaScript, and its [status code](/en-US/docs/Web/API/Response/status) is always `0`.

The main application for `no-cors` is for a service worker: although the response to a `no-cors` request can't be read by JavaScript, it can be cached by a service worker and then used as a response to an intercepted fetch request. Note that in this situation you don't know whether the request succeeded or not, so you should adopt a caching strategy which enables the cached response to be updated from the network (such as [cache first with cache refresh](/en-US/docs/Web/Progressive_web_apps/Guides/Caching#cache_first_with_cache_refresh)).

[navigate](#navigate)

Used only by HTML navigation. A `navigate` request is created only while navigating between documents.

See [Making cross-origin requests](/en-US/docs/Web/API/Fetch_API/Using_Fetch#making_cross-origin_requests) for more details.

Defaults to `cors`.

[priority Optional](#priority)

Specifies the priority of the fetch request relative to other requests of the same type. Must be one of the following:

[high](#high)

A high priority fetch request relative to other requests of the same type.

[low](#low)

A low priority fetch request relative to other requests of the same type.

[auto](#auto)

No user preference for the fetch priority. It is used if no value is set or if an invalid value is set.

Defaults to `auto`.

[privateToken Optional](#privatetoken)

An object containing options for initiating a [private state token](/en-US/docs/Web/API/Private_State_Token_API/Using) operation. Possible properties include:

[issuers](#issuers)

An array of strings containing the URLs of issuers that you want to forward redemption records for. This setting is ignored unless `operation` is set to `send-redemption-record`, in which case the `issuers` array must be included.

[operation](#operation)

A string representing the type of token operation you want to initiate. When specifying the `privateToken` option, this property is mandatory. Possible values are:

[token-request](#token-request)

Initiates a [token request](/en-US/docs/Web/API/Private_State_Token_API/Using#issuing_a_token_via_your_server) operation.

[token-redemption](#token-redemption)

Initiates a [token redemption](/en-US/docs/Web/API/Private_State_Token_API/Using#redeeming_a_token_via_your_server) operation.

[send-redemption-record](#send-redemption-record)

Initiates a [send redemption record](/en-US/docs/Web/API/Private_State_Token_API/Using#redemption_record_usage_2) operation.

[refreshPolicy](#refreshpolicy)

An enumerated value that specifies the expected behavior when a non-expired redemption record for the current user and site has previously been set. This setting is ignored unless `operation` is set to `token-redemption`. Possible values are:

[none](#none)

The previously-set redemption record should be used, and a new one should not be issued. This is the default value.

[refresh](#refresh)

A new redemption record is always issued.

[version](#version)

A number indicating the version of the cryptographic protocol you wish to use when generating a token. Currently this is always set to `1`, which is the only version that the specification supports. When specifying the `privateToken` option, this property is mandatory.

[redirect Optional](#redirect)

Determines the browser's behavior in case the server replies with a [redirect status](/en-US/docs/Web/HTTP/Reference/Status#redirection_messages). One of the following values:

[follow](#follow)

Automatically follow redirects.

[error](#error)

Reject the promise with a network error when a redirect status is returned.

[manual](#manual)

Return a response with almost all fields filtered out, to enable a service worker to store the response and later replay it.

Defaults to `follow`.

[referrer Optional](#referrer)

A string specifying the value to use for the request's [Referer](/en-US/docs/Web/HTTP/Reference/Headers/Referer) header. One of the following:

[A same-origin relative or absolute URL](#a_same-origin_relative_or_absolute_url)

Set the `Referer` header to the given value. Relative URLs are resolved relative to the URL of the page that made the request.

[An empty string](#an_empty_string)

Omit the `Referer` header.

[about:client](#aboutclient)

Set the `Referer` header to the default value for the context of the request (for example, the URL of the page that made the request).

Defaults to `about:client`.

[referrerPolicy Optional](#referrerpolicy)

A string that sets a policy for the [Referer](/en-US/docs/Web/HTTP/Reference/Headers/Referer) header. The syntax and semantics of this option are exactly the same as for the [Referrer-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy) header.

[signal Optional](#signal)

An [AbortSignal](/en-US/docs/Web/API/AbortSignal). If this option is set, the request can be canceled by calling [abort()](/en-US/docs/Web/API/AbortController/abort) on the corresponding `AbortController`.

## [Examples](#examples)

### [Passing options into fetch()](#passing_options_into_fetch)

In this example we pass the `method`, `body`, and `headers` options directly into the [fetch()](/en-US/docs/Web/API/Window/fetch) method call:

js

```
async function post() {
  const response = await fetch("https://example.org/post", {
    method: "POST",
    body: JSON.stringify({ username: "example" }),
    headers: {
      "Content-Type": "application/json",
    },
  });

  console.log(response.status);
}
```

### [Passing options into the Request() constructor](#passing_options_into_the_request_constructor)

In this example we create a [Request](/en-US/docs/Web/API/Request), passing the same set of options into its constructor, and then pass the request into `fetch()`:

js

```
async function post() {
  const request = new Request("https://example.org/post", {
    method: "POST",
    body: JSON.stringify({ username: "example" }),
    headers: {
      "Content-Type": "application/json",
    },
  });

  const response = await fetch(request);

  console.log(response.status);
}
```

### [Passing options into both Request() and fetch()](#passing_options_into_both_request_and_fetch)

In this example we create a [Request](/en-US/docs/Web/API/Request), passing the `method`, `headers`, and `body` options into its constructor. We then pass the request into `fetch()` along with `body` and `referrer` options:

js

```
async function post() {
  const request = new Request("https://example.org/post", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username: "example1" }),
  });

  const response = await fetch(request, {
    body: JSON.stringify({ username: "example2" }),
    referrer: "",
  });

  console.log(response.status);
}
```

In this case the request will be sent with the following options:

- `method: "POST"`
- `headers: {"Content-Type": "application/json"}`
- `body: '{"username":"example2"}'`
- `referrer: ""`

## [Specifications](#specifications)

Specification
[Fetch# requestinit](https://fetch.spec.whatwg.org/#requestinit)

## [See also](#see_also)

- [Using Fetch](/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [ServiceWorker API](/en-US/docs/Web/API/Service_Worker_API)
- [HTTP access control (CORS)](/en-US/docs/Web/HTTP/Guides/CORS)
- [HTTP](/en-US/docs/Web/HTTP)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 16, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RequestInit/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/requestinit/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRequestInit&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frequestinit%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRequestInit%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frequestinit%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff6e66d18205c93fcaeb2ea9ad51541b5b4d7d2b1%0A*+Document+last+modified%3A+2025-12-16T10%3A03%3A04.000Z%0A%0A%3C%2Fdetails%3E)
