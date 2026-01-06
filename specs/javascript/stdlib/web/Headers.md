# Headers

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2017⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHeaders&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `Headers` interface of the [Fetch API](/en-US/docs/Web/API/Fetch_API) allows you to perform various actions on [HTTP request and response headers](/en-US/docs/Web/HTTP/Reference/Headers). These actions include retrieving, setting, adding to, and removing headers from the list of the request's headers.

You can retrieve a `Headers` object via the [Request.headers](/en-US/docs/Web/API/Request/headers) and [Response.headers](/en-US/docs/Web/API/Response/headers) properties, and create a new `Headers` object using the [Headers()](/en-US/docs/Web/API/Headers/Headers) constructor. Compared to using plain objects, using `Headers` objects to send requests provides some additional input sanitization. For example, it normalizes header names to lowercase, strips leading and trailing whitespace from header values, and prevents certain headers from being set.

Note: You can find out more about the available headers by reading our [HTTP headers](/en-US/docs/Web/HTTP/Reference/Headers) reference.

## In this article

- [Description](#description)
- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Description](#description)

A `Headers` object has an associated header list, which is initially empty and consists of zero or more name and value pairs. You can add to this using methods like [append()](/en-US/docs/Web/API/Headers/append) (see [Examples](#examples).) In all methods of this interface, header names are matched by case-insensitive byte sequence.

An object implementing `Headers` can directly be used in a [for...of](/en-US/docs/Web/JavaScript/Reference/Statements/for...of) structure, instead of [entries()](/en-US/docs/Web/API/Headers/entries): `for (const p of myHeaders)` is equivalent to `for (const p of myHeaders.entries())`.

### [Modification restrictions](#modification_restrictions)

Some `Headers` objects have restrictions on whether the [set()](/en-US/docs/Web/API/Headers/set), [delete()](/en-US/docs/Web/API/Headers/delete), and [append()](/en-US/docs/Web/API/Headers/append) methods can mutate the header. The modification restrictions are set depending on how the `Headers` object is created.

- For headers created with [Headers()](/en-US/docs/Web/API/Headers/Headers) constructor, there are no modification restrictions.
- For headers of [Request](/en-US/docs/Web/API/Request) objects: 

  - If the request's [mode](/en-US/docs/Web/API/Request/mode) is `no-cors`, you can modify any [CORS-safelisted request header](/en-US/docs/Glossary/CORS-safelisted_request_header) name/value.
  - Otherwise, you can modify any [non-forbidden request header](/en-US/docs/Glossary/Forbidden_request_header) name/value.

- For headers of [Response](/en-US/docs/Web/API/Response) objects: 

  - If the response is created using [Response.error()](/en-US/docs/Web/API/Response/error_static) or [Response.redirect()](/en-US/docs/Web/API/Response/redirect_static), or received from a [fetch()](/en-US/docs/Web/API/Window/fetch) call, the headers are immutable and cannot be modified.
  - Otherwise, if the response is created using [Response()](/en-US/docs/Web/API/Response/Response) or [Response.json()](/en-US/docs/Web/API/Response/json_static), you can modify any [non-forbidden response header](/en-US/docs/Glossary/Forbidden_response_header_name) name/value.

All of the Headers methods will throw a [TypeError](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError) if you try to pass in a reference to a name that isn't a [valid HTTP Header name](https://fetch.spec.whatwg.org/#concept-header-name). The mutation operations will throw a `TypeError` if the header is immutable. In any other failure case they fail silently.

## [Constructor](#constructor)

[Headers()](/en-US/docs/Web/API/Headers/Headers)

Creates a new `Headers` object.

## [Instance methods](#instance_methods)

[Headers.append()](/en-US/docs/Web/API/Headers/append)

Appends a new value onto an existing header inside a `Headers` object, or adds the header if it does not already exist.

[Headers.delete()](/en-US/docs/Web/API/Headers/delete)

Deletes a header from a `Headers` object.

[Headers.entries()](/en-US/docs/Web/API/Headers/entries)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) allowing to go through all key/value pairs contained in this object.

[Headers.forEach()](/en-US/docs/Web/API/Headers/forEach)

Executes a provided function once for each key/value pair in this `Headers` object.

[Headers.get()](/en-US/docs/Web/API/Headers/get)

Returns a [String](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) sequence of all the values of a header within a `Headers` object with a given name.

[Headers.getSetCookie()](/en-US/docs/Web/API/Headers/getSetCookie)

Returns an array containing the values of all [Set-Cookie](/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie) headers associated with a response.

[Headers.has()](/en-US/docs/Web/API/Headers/has)

Returns a boolean stating whether a `Headers` object contains a certain header.

[Headers.keys()](/en-US/docs/Web/API/Headers/keys)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) allowing you to go through all keys of the key/value pairs contained in this object.

[Headers.set()](/en-US/docs/Web/API/Headers/set)

Sets a new value for an existing header inside a `Headers` object, or adds the header if it does not already exist.

[Headers.values()](/en-US/docs/Web/API/Headers/values)

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) allowing you to go through all values of the key/value pairs contained in this object.

Note: To be clear, the difference between [Headers.set()](/en-US/docs/Web/API/Headers/set) and [Headers.append()](/en-US/docs/Web/API/Headers/append) is that if the specified header does already exist and does accept multiple values, [Headers.set()](/en-US/docs/Web/API/Headers/set) will overwrite the existing value with the new one, whereas [Headers.append()](/en-US/docs/Web/API/Headers/append) will append the new value onto the end of the set of values. See their dedicated pages for example code.

Note: When Header values are iterated over, they are automatically sorted in lexicographical order, and values from duplicate header names are combined.

## [Examples](#examples)

In the following snippet, we create a new header using the `Headers()` constructor, add a new header to it using `append()`, then return that header value using `get()`:

js

```
const myHeaders = new Headers();

myHeaders.append("Content-Type", "text/xml");
myHeaders.get("Content-Type"); // should return 'text/xml'
```

The same can be achieved by passing an array of arrays or an object literal to the constructor:

js

```
let myHeaders = new Headers({
  "Content-Type": "text/xml",
});

// or, using an array of arrays:
myHeaders = new Headers([["Content-Type", "text/xml"]]);

myHeaders.get("Content-Type"); // should return 'text/xml'
```

## [Specifications](#specifications)

Specification
[Fetch# headers-class](https://fetch.spec.whatwg.org/#headers-class)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [ServiceWorker API](/en-US/docs/Web/API/Service_Worker_API)
- [HTTP access control (CORS)](/en-US/docs/Web/HTTP/Guides/CORS)
- [HTTP](/en-US/docs/Web/HTTP)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Headers/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/headers/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHeaders&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fheaders%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHeaders%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fheaders%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d929bb0a021c7130d5a71a4bf505bcb8070378d%0A*+Document+last+modified%3A+2025-03-13T12%3A48%3A23.000Z%0A%0A%3C%2Fdetails%3E)
