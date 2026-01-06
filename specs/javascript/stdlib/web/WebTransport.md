# WebTransport

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransport&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WebTransport` interface of the [WebTransport API](/en-US/docs/Web/API/WebTransport_API) provides functionality to enable a user agent to connect to an HTTP/3 server, initiate reliable and unreliable transport in either or both directions, and close the connection once it is no longer needed.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[WebTransport()](/en-US/docs/Web/API/WebTransport/WebTransport)

Creates a new `WebTransport` object instance.

## [Instance properties](#instance_properties)

[closed](/en-US/docs/Web/API/WebTransport/closed)Read only

Returns a promise that resolves when the transport is closed.

[datagrams](/en-US/docs/Web/API/WebTransport/datagrams)Read only

Returns a [WebTransportDatagramDuplexStream](/en-US/docs/Web/API/WebTransportDatagramDuplexStream) instance that can be used to send and receive datagrams.

[congestionControl](/en-US/docs/Web/API/WebTransport/congestionControl)Read onlyExperimental

Returns a string that indicates the application preference for either high throughput or low-latency when sending data.

[incomingBidirectionalStreams](/en-US/docs/Web/API/WebTransport/incomingBidirectionalStreams)Read only

Represents one or more bidirectional streams opened by the server. Returns a [ReadableStream](/en-US/docs/Web/API/ReadableStream) of [WebTransportBidirectionalStream](/en-US/docs/Web/API/WebTransportBidirectionalStream) objects. Each one can be used to read data from the server and write data back to it.

[incomingUnidirectionalStreams](/en-US/docs/Web/API/WebTransport/incomingUnidirectionalStreams)Read only

Represents one or more unidirectional streams opened by the server. Returns a [ReadableStream](/en-US/docs/Web/API/ReadableStream) of [WebTransportReceiveStream](/en-US/docs/Web/API/WebTransportReceiveStream) objects. Each one can be used to read data from the server.

[ready](/en-US/docs/Web/API/WebTransport/ready)Read only

Returns a promise that resolves when the transport is ready to use.

[reliability](/en-US/docs/Web/API/WebTransport/reliability)Read onlyExperimental

Returns a string that indicates whether the connection supports reliable transports only, or whether it also supports unreliable transports (such as UDP).

## [Instance methods](#instance_methods)

[close()](/en-US/docs/Web/API/WebTransport/close)

Closes an ongoing WebTransport session.

[createBidirectionalStream()](/en-US/docs/Web/API/WebTransport/createBidirectionalStream)

Asynchronously opens a bidirectional stream ([WebTransportBidirectionalStream](/en-US/docs/Web/API/WebTransportBidirectionalStream)) that can be used to read from and write to the server.

[createUnidirectionalStream()](/en-US/docs/Web/API/WebTransport/createUnidirectionalStream)

Asynchronously opens a unidirectional stream ([WritableStream](/en-US/docs/Web/API/WritableStream)) that can be used to write to the server.

[getStats()](/en-US/docs/Web/API/WebTransport/getStats)Experimental

Asynchronously returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with an object containing HTTP/3 connection statistics.

## [Examples](#examples)

The example code below shows how you'd connect to an HTTP/3 server by passing its URL to the [WebTransport()](/en-US/docs/Web/API/WebTransport/WebTransport) constructor. Note that the scheme needs to be HTTPS, and the port number needs to be explicitly specified. Once the [WebTransport.ready](/en-US/docs/Web/API/WebTransport/ready) promise fulfills, you can start using the connection.

js

```
async function initTransport(url) {
  // Initialize transport connection
  const transport = new WebTransport(url);

  // The connection can be used once ready fulfills
  await transport.ready;
  return transport;
}
```

You can respond to the connection closing by waiting for the [WebTransport.closed](/en-US/docs/Web/API/WebTransport/closed) promise to fulfill. Errors returned by `WebTransport` operations are of type [WebTransportError](/en-US/docs/Web/API/WebTransportError), and contain additional data on top of the standard [DOMException](/en-US/docs/Web/API/DOMException) set.

The `closeTransport()` method below shows a possible implementation. Within a `try...catch` block it uses `await` to wait for the `closed` promise to fulfill or reject, and then reports whether or not the connection closed intentionally or due to error.

js

```
async function closeTransport(transport) {
  // Respond to connection closing
  try {
    await transport.closed;
    console.log(`The HTTP/3 connection to ${url} closed gracefully.`);
  } catch (error) {
    console.error(`The HTTP/3 connection to ${url} closed due to ${error}.`);
  }
}
```

We might call the asynchronous functions above in their own asynchronous function, as shown below.

js

```
// Use the transport
async function useTransport(url) {
  const transport = await initTransport(url);

  // Use the transport object to send and receive data
  // …

  // When done, close the transport
  await closeTransport(transport);
}

const url = "https://example.com:4999/wt";
useTransport(url);
```

For other example code, see the individual property and method pages.

## [Specifications](#specifications)

Specification
[WebTransport# web-transport](https://w3c.github.io/webtransport/#web-transport)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using WebTransport](https://developer.chrome.com/docs/capabilities/web-apis/webtransport)
- [WebSockets API](/en-US/docs/Web/API/WebSockets_API)
- [Streams API](/en-US/docs/Web/API/Streams_API)
- [WebTransport over HTTP/3](https://datatracker.ietf.org/doc/html/draft-ietf-webtrans-http3/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WebTransport/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webtransport/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransport&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebtransport%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransport%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebtransport%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F759102220c07fb140b3e06971cd5981d8f0f134f%0A*+Document+last+modified%3A+2025-04-28T15%3A45%3A41.000Z%0A%0A%3C%2Fdetails%3E)
