# XMLHttpRequest

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequest&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API), except for [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

`XMLHttpRequest` (XHR) objects are used to interact with servers. You can retrieve data from a URL without having to do a full page refresh. This enables a Web page to update just part of a page without disrupting what the user is doing.

Despite its name, `XMLHttpRequest` can be used to retrieve any type of data, not just XML.

If your communication needs to involve receiving event data or message data from a server, consider using [server-sent events](/en-US/docs/Web/API/Server-sent_events) through the [EventSource](/en-US/docs/Web/API/EventSource) interface. For full-duplex communication, [WebSockets](/en-US/docs/Web/API/WebSockets_API) may be a better choice.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[XMLHttpRequest()](/en-US/docs/Web/API/XMLHttpRequest/XMLHttpRequest)

The constructor initializes an `XMLHttpRequest`. It must be called before any other method calls.

## [Instance properties](#instance_properties)

This interface also inherits properties of [XMLHttpRequestEventTarget](/en-US/docs/Web/API/XMLHttpRequestEventTarget) and of [EventTarget](/en-US/docs/Web/API/EventTarget).

[XMLHttpRequest.readyState](/en-US/docs/Web/API/XMLHttpRequest/readyState)Read only

Returns a number representing the state of the request.

[XMLHttpRequest.response](/en-US/docs/Web/API/XMLHttpRequest/response)Read only

Returns an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), a [Blob](/en-US/docs/Web/API/Blob), a [Document](/en-US/docs/Web/API/Document), a JavaScript object, or a string, depending on the value of [XMLHttpRequest.responseType](/en-US/docs/Web/API/XMLHttpRequest/responseType), that contains the response entity body.

[XMLHttpRequest.responseText](/en-US/docs/Web/API/XMLHttpRequest/responseText)Read only

Returns a string that contains the response to the request as text, or `null` if the request was unsuccessful or has not yet been sent.

[XMLHttpRequest.responseType](/en-US/docs/Web/API/XMLHttpRequest/responseType)

Specifies the type of the response.

[XMLHttpRequest.responseURL](/en-US/docs/Web/API/XMLHttpRequest/responseURL)Read only

Returns the serialized URL of the response or the empty string if the URL is null.

[XMLHttpRequest.responseXML](/en-US/docs/Web/API/XMLHttpRequest/responseXML)Read only

Returns a [Document](/en-US/docs/Web/API/Document) containing the response to the request, or `null` if the request was unsuccessful, has not yet been sent, or cannot be parsed as XML or HTML. Not available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

[XMLHttpRequest.status](/en-US/docs/Web/API/XMLHttpRequest/status)Read only

Returns the [HTTP response status code](/en-US/docs/Web/HTTP/Reference/Status) of the request.

[XMLHttpRequest.statusText](/en-US/docs/Web/API/XMLHttpRequest/statusText)Read only

Returns a string containing the response string returned by the HTTP server. Unlike [XMLHttpRequest.status](/en-US/docs/Web/API/XMLHttpRequest/status), this includes the entire text of the response message (`"OK"`, for example).

Note: According to the HTTP/2 specification [RFC 7540, section 8.1.2.4: Response Pseudo-Header Fields](https://datatracker.ietf.org/doc/html/rfc7540#section-8.1.2.4), HTTP/2 does not define a way to carry the version or reason phrase that is included in an HTTP/1.1 status line.

[XMLHttpRequest.timeout](/en-US/docs/Web/API/XMLHttpRequest/timeout)

The time in milliseconds a request can take before automatically being terminated.

[XMLHttpRequest.upload](/en-US/docs/Web/API/XMLHttpRequest/upload)Read only

A [XMLHttpRequestUpload](/en-US/docs/Web/API/XMLHttpRequestUpload) representing the upload process.

[XMLHttpRequest.withCredentials](/en-US/docs/Web/API/XMLHttpRequest/withCredentials)

Returns `true` if cross-site `Access-Control` requests should be made using credentials such as cookies or authorization headers; otherwise `false`.

### [Non-standard properties](#non-standard_properties)

[XMLHttpRequest.mozAnon Read only 
Non-standard](#xmlhttprequest.mozanon)

A boolean. If true, the request will be sent without cookie and authentication headers.

[XMLHttpRequest.mozSystem Read only 
Non-standard](#xmlhttprequest.mozsystem)

A boolean. If true, the same origin policy will not be enforced on the request.

## [Instance methods](#instance_methods)

[XMLHttpRequest.abort()](/en-US/docs/Web/API/XMLHttpRequest/abort)

Aborts the request if it has already been sent.

[XMLHttpRequest.getAllResponseHeaders()](/en-US/docs/Web/API/XMLHttpRequest/getAllResponseHeaders)

Returns all the response headers, separated by [CRLF](/en-US/docs/Glossary/CRLF), as a string, or `null` if no response has been received.

[XMLHttpRequest.getResponseHeader()](/en-US/docs/Web/API/XMLHttpRequest/getResponseHeader)

Returns the string containing the text of the specified header, or `null` if either the response has not yet been received or the header doesn't exist in the response.

[XMLHttpRequest.open()](/en-US/docs/Web/API/XMLHttpRequest/open)

Initializes a request.

[XMLHttpRequest.overrideMimeType()](/en-US/docs/Web/API/XMLHttpRequest/overrideMimeType)

Overrides the MIME type returned by the server.

[XMLHttpRequest.send()](/en-US/docs/Web/API/XMLHttpRequest/send)

Sends the request. If the request is asynchronous (which is the default), this method returns as soon as the request is sent.

[XMLHttpRequest.setAttributionReporting()](/en-US/docs/Web/API/XMLHttpRequest/setAttributionReporting)Secure contextDeprecated

Indicates that you want the request's response to be able to register an attribution source or trigger event.

[XMLHttpRequest.setPrivateToken()](/en-US/docs/Web/API/XMLHttpRequest/setPrivateToken)Experimental

Adds [private state token](/en-US/docs/Web/API/Private_State_Token_API/Using) information to an `XMLHttpRequest` call, to initiate private state token operations.

[XMLHttpRequest.setRequestHeader()](/en-US/docs/Web/API/XMLHttpRequest/setRequestHeader)

Sets the value of an HTTP request header. You must call `setRequestHeader()` after [open()](/en-US/docs/Web/API/XMLHttpRequest/open), but before [send()](/en-US/docs/Web/API/XMLHttpRequest/send).

## [Events](#events)

This interface also inherits events of [XMLHttpRequestEventTarget](/en-US/docs/Web/API/XMLHttpRequestEventTarget).

[readystatechange](/en-US/docs/Web/API/XMLHttpRequest/readystatechange_event)

Fired whenever the [readyState](/en-US/docs/Web/API/XMLHttpRequest/readyState) property changes. Also available via the `onreadystatechange` event handler property.

## [Specifications](#specifications)

Specification
[XMLHttpRequest# interface-xmlhttprequest](https://xhr.spec.whatwg.org/#interface-xmlhttprequest)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XMLSerializer](/en-US/docs/Web/API/XMLSerializer): Serializing a DOM tree into XML
- [Using XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest_API/Using_XMLHttpRequest)
- [Fetch API](/en-US/docs/Web/API/Fetch_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 16, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/XMLHttpRequest/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xmlhttprequest/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequest&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxmlhttprequest%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequest%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxmlhttprequest%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff6e66d18205c93fcaeb2ea9ad51541b5b4d7d2b1%0A*+Document+last+modified%3A+2025-12-16T10%3A03%3A04.000Z%0A%0A%3C%2Fdetails%3E)
