# XMLHttpRequest API

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequest_API&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API), except for [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The XMLHttpRequest API enables web apps to make HTTP requests to web servers and receive the responses programmatically using JavaScript. This in turn enables a website to update just part of a page with data from the server, rather than having to navigate to a whole new page. This practice is also sometimes known as [AJAX](/en-US/docs/Glossary/AJAX).

The [Fetch API](/en-US/docs/Web/API/Fetch_API) is the more flexible and powerful replacement for the XMLHttpRequest API. The Fetch API uses [promises](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) instead of events to handle asynchronous responses, integrates well with [service workers](/en-US/docs/Web/API/Service_Worker_API), and supports advanced aspects of HTTP such as [CORS](/en-US/docs/Web/HTTP/Guides/CORS). For these reasons, the Fetch API is usually used in modern web apps instead of [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest).

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

The central interface in the XMLHttpRequest API is [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest). To make an HTTP request:

1. Create a new `XMLHttpRequest` instance by calling its [constructor](/en-US/docs/Web/API/XMLHttpRequest/XMLHttpRequest).
2. Initialize it by calling [XMLHttpRequest.open()](/en-US/docs/Web/API/XMLHttpRequest/open). At this point you provide the URL for the request, the [HTTP method](/en-US/docs/Web/HTTP/Reference/Methods) to use, and optionally, a username and password.
3. Attach event handlers to get the result of the request. For example, the [load](/en-US/docs/Web/API/XMLHttpRequestEventTarget/load_event) event is fired when the request has successfully completed, and the [error](/en-US/docs/Web/API/XMLHttpRequestEventTarget/error_event) event is fired in various error conditions.
4. Send the request by calling [XMLHttpRequest.send()](/en-US/docs/Web/API/XMLHttpRequest/send).

For an in-depth guide to the XMLHttpRequest API, see [Using XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest_API/Using_XMLHttpRequest).

## [Interfaces](#interfaces)

[FormData](/en-US/docs/Web/API/FormData)

An object representing [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) fields and their values, which can be sent to a server using [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest) or [fetch()](/en-US/docs/Web/API/Window/fetch).

[ProgressEvent](/en-US/docs/Web/API/ProgressEvent)

A subclass of [Event](/en-US/docs/Web/API/Event) which is passed into the [progress](/en-US/docs/Web/API/XMLHttpRequestEventTarget/progress_event), and which contains information about how much of the request has been completed.

[XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest)

Represents a single HTTP request.

[XMLHttpRequestEventTarget](/en-US/docs/Web/API/XMLHttpRequestEventTarget)

A superclass of both [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest) and [XMLHttpRequestUpload](/en-US/docs/Web/API/XMLHttpRequestUpload), defining the events that are available in both of those interfaces.

[XMLHttpRequestUpload](/en-US/docs/Web/API/XMLHttpRequestUpload)

Represents the upload process for an HTTP upload. Provides events enabling code to track the progress of an upload.

## [Examples](#examples)

### [Fetching JSON data from the server](#fetching_json_data_from_the_server)

In this example we fetch a JSON file from `https://raw.githubusercontent.com/mdn/content/main/files/en-us/_wikihistory.json`, adding event listeners to show the progress of the event.

#### HTML

html

```
<div class="controls">
  <button class="xhr" type="button">Click to start XHR</button>
</div>

<textarea readonly class="event-log"></textarea>
```

```
.event-log {
  width: 25rem;
  height: 5rem;
  border: 1px solid black;
  margin: 0.5rem;
  padding: 0.2rem;
}

button {
  width: 12rem;
  margin: 0.5rem;
}
```

#### JavaScript

js

```
const xhrButton = document.querySelector(".xhr");
const log = document.querySelector(".event-log");
const url =
  "https://raw.githubusercontent.com/mdn/content/main/files/en-us/_wikihistory.json";

function handleEvent(e) {
  log.textContent = `${log.textContent}${e.type}: ${e.loaded} bytes transferred\n`;
}

function addListeners(xhr) {
  xhr.addEventListener("loadstart", handleEvent);
  xhr.addEventListener("load", handleEvent);
  xhr.addEventListener("loadend", handleEvent);
  xhr.addEventListener("progress", handleEvent);
  xhr.addEventListener("error", handleEvent);
  xhr.addEventListener("abort", handleEvent);
}

xhrButton.addEventListener("click", () => {
  log.textContent = "";

  const xhr = new XMLHttpRequest();
  xhr.open("GET", url);
  addListeners(xhr);
  xhr.send();
});
```

#### Result

## [Specifications](#specifications)

Specification[XMLHttpRequest](https://xhr.spec.whatwg.org/)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Fetch API](/en-US/docs/Web/API/Fetch_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 26, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/XMLHttpRequest_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xmlhttprequest_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequest_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxmlhttprequest_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequest_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxmlhttprequest_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0cc63ce1d7f43eb98746a908a9aba68ef6a36f7b%0A*+Document+last+modified%3A+2025-08-26T12%3A44%3A08.000Z%0A%0A%3C%2Fdetails%3E)
