# Response

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2017⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FResponse&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `Response` interface of the [Fetch API](/en-US/docs/Web/API/Fetch_API) represents the response to a request.

You can create a new `Response` object using the [Response()](/en-US/docs/Web/API/Response/Response) constructor, but you are more likely to encounter a `Response` object being returned as the result of another API operation—for example, a service worker [FetchEvent.respondWith](/en-US/docs/Web/API/FetchEvent/respondWith), or a simple [fetch()](/en-US/docs/Web/API/Window/fetch).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[Response()](/en-US/docs/Web/API/Response/Response)

Creates a new `Response` object.

## [Instance properties](#instance_properties)

[Response.body](/en-US/docs/Web/API/Response/body)Read only

A [ReadableStream](/en-US/docs/Web/API/ReadableStream) of the body contents.

[Response.bodyUsed](/en-US/docs/Web/API/Response/bodyUsed)Read only

Stores a boolean value that declares whether the body has been used in a response yet.

[Response.headers](/en-US/docs/Web/API/Response/headers)Read only

The [Headers](/en-US/docs/Web/API/Headers) object associated with the response.

[Response.ok](/en-US/docs/Web/API/Response/ok)Read only

A boolean indicating whether the response was successful (status in the range `200` – `299`) or not.

[Response.redirected](/en-US/docs/Web/API/Response/redirected)Read only

Indicates whether or not the response is the result of a redirect (that is, its URL list has more than one entry).

[Response.status](/en-US/docs/Web/API/Response/status)Read only

The status code of the response. (This will be `200` for a success).

[Response.statusText](/en-US/docs/Web/API/Response/statusText)Read only

The status message corresponding to the status code. (e.g., `OK` for `200`).

[Response.type](/en-US/docs/Web/API/Response/type)Read only

The type of the response (e.g., `basic`, `cors`).

[Response.url](/en-US/docs/Web/API/Response/url)Read only

The URL of the response.

## [Static methods](#static_methods)

[Response.error()](/en-US/docs/Web/API/Response/error_static)

Returns a new `Response` object associated with a network error.

[Response.redirect()](/en-US/docs/Web/API/Response/redirect_static)

Returns a new response with a different URL.

[Response.json()](/en-US/docs/Web/API/Response/json_static)

Returns a new `Response` object for returning the provided JSON encoded data.

## [Instance methods](#instance_methods)

[Response.arrayBuffer()](/en-US/docs/Web/API/Response/arrayBuffer)

Returns a promise that resolves with an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) representation of the response body.

[Response.blob()](/en-US/docs/Web/API/Response/blob)

Returns a promise that resolves with a [Blob](/en-US/docs/Web/API/Blob) representation of the response body.

[Response.bytes()](/en-US/docs/Web/API/Response/bytes)

Returns a promise that resolves with a [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) representation of the response body.

[Response.clone()](/en-US/docs/Web/API/Response/clone)

Creates a clone of a `Response` object.

[Response.formData()](/en-US/docs/Web/API/Response/formData)

Returns a promise that resolves with a [FormData](/en-US/docs/Web/API/FormData) representation of the response body.

[Response.json()](/en-US/docs/Web/API/Response/json)

Returns a promise that resolves with the result of parsing the response body text as [JSON](/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON).

[Response.text()](/en-US/docs/Web/API/Response/text)

Returns a promise that resolves with a text representation of the response body.

## [Examples](#examples)

### [Fetching an image](#fetching_an_image)

In our [basic fetch example](https://github.com/mdn/dom-examples/tree/main/fetch/basic-fetch) ([run example live](https://mdn.github.io/dom-examples/fetch/basic-fetch/)) we use a simple `fetch()` call to grab an image and display it in an [<img>](/en-US/docs/Web/HTML/Reference/Elements/img) element. The `fetch()` call returns a promise, which resolves to the `Response` object associated with the resource fetch operation.

You'll notice that since we are requesting an image, we need to run [Response.blob](/en-US/docs/Web/API/Response/blob) to give the response its correct MIME type.

js

```
const image = document.querySelector(".my-image");
fetch("flowers.jpg")
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.blob();
  })
  .then((blob) => {
    const objectURL = URL.createObjectURL(blob);
    image.src = objectURL;
  })
  .catch((error) => {
    console.error("Error fetching the image:", error);
  });
```

You can also use the [Response()](/en-US/docs/Web/API/Response/Response) constructor to create your own custom `Response` object:

js

```
const response = new Response();
```

### [A PHP Call](#a_php_call)

Here we call a PHP program file that generates a JSON string, displaying the result as a JSON value.

js

```
// Function to fetch JSON using PHP
const getJSON = async () => {
  // Generate the Response object
  const response = await fetch("getJSON.php");
  if (response.ok) {
    // Get JSON value from the response body
    return response.json();
  }
  throw new Error("*** PHP file not found");
};

// Call the function and output value or error message to console
getJSON()
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
```

## [Specifications](#specifications)

Specification
[Fetch# response-class](https://fetch.spec.whatwg.org/#response-class)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [ServiceWorker API](/en-US/docs/Web/API/Service_Worker_API)
- [HTTP access control (CORS)](/en-US/docs/Web/HTTP/Guides/CORS)
- [HTTP](/en-US/docs/Web/HTTP)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Response/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/response/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FResponse&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fresponse%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FResponse%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fresponse%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F252040efa8f6ca0f737fd7ec04e610354e58b98c%0A*+Document+last+modified%3A+2025-12-23T04%3A31%3A17.000Z%0A%0A%3C%2Fdetails%3E)
