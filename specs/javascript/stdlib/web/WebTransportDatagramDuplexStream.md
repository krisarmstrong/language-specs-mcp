# WebTransportDatagramDuplexStream

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransportDatagramDuplexStream&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WebTransportDatagramDuplexStream` interface of the [WebTransport API](/en-US/docs/Web/API/WebTransport_API) represents a duplex stream that can be used for unreliable transport of datagrams between client and server. Provides access to a [ReadableStream](/en-US/docs/Web/API/ReadableStream) for reading incoming datagrams, a [WritableStream](/en-US/docs/Web/API/WritableStream) for writing outgoing datagrams, and various settings and statistics related to the stream.

This is accessed via the [WebTransport.datagrams](/en-US/docs/Web/API/WebTransport/datagrams) property.

"Unreliable" means that transmission of data is not guaranteed, nor is arrival in a specific order. This is fine in some situations and provides very fast delivery. For example, you might want to transmit regular game state updates where each message supersedes the last one that arrives, and order is not important.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[incomingHighWaterMark](/en-US/docs/Web/API/WebTransportDatagramDuplexStream/incomingHighWaterMark)

Gets or sets the high water mark for incoming chunks of data — this is the maximum size, in chunks, that the incoming [ReadableStream](/en-US/docs/Web/API/ReadableStream)'s internal queue can reach before it is considered full. See [Internal queues and queuing strategies](/en-US/docs/Web/API/Streams_API/Concepts#internal_queues_and_queuing_strategies) for more information.

[incomingMaxAge](/en-US/docs/Web/API/WebTransportDatagramDuplexStream/incomingMaxAge)

Gets or sets the maximum age for incoming datagrams, in milliseconds. Returns `null` if no maximum age has been set.

[maxDatagramSize](/en-US/docs/Web/API/WebTransportDatagramDuplexStream/maxDatagramSize)Read only

Returns the maximum allowable size of outgoing datagrams, in bytes, that can be written to [writable](/en-US/docs/Web/API/WebTransportDatagramDuplexStream/writable).

[outgoingHighWaterMark](/en-US/docs/Web/API/WebTransportDatagramDuplexStream/outgoingHighWaterMark)

Gets or sets the high water mark for outgoing chunks of data — this is the maximum size, in chunks, that the outgoing [WritableStream](/en-US/docs/Web/API/WritableStream)'s internal queue can reach before it is considered full. See [Internal queues and queuing strategies](/en-US/docs/Web/API/Streams_API/Concepts#internal_queues_and_queuing_strategies) for more information.

[outgoingMaxAge](/en-US/docs/Web/API/WebTransportDatagramDuplexStream/outgoingMaxAge)

Gets or sets the maximum age for outgoing datagrams, in milliseconds. Returns `null` if no maximum age has been set.

[readable](/en-US/docs/Web/API/WebTransportDatagramDuplexStream/readable)Read only

Returns a [ReadableStream](/en-US/docs/Web/API/ReadableStream) instance that can be used to read incoming datagrams from the stream.

[writable](/en-US/docs/Web/API/WebTransportDatagramDuplexStream/writable)Read onlyDeprecated

Returns a [WritableStream](/en-US/docs/Web/API/WritableStream) instance that can be used to write outgoing datagrams to the stream.

## [Examples](#examples)

### [Writing outgoing datagrams](#writing_outgoing_datagrams)

The [writable](/en-US/docs/Web/API/WebTransportDatagramDuplexStream/writable) property returns a [WritableStream](/en-US/docs/Web/API/WritableStream) object that you can write data to using a writer, for transmission to the server:

js

```
const writer = transport.datagrams.writable.getWriter();
const data1 = new Uint8Array([65, 66, 67]);
const data2 = new Uint8Array([68, 69, 70]);
writer.write(data1);
writer.write(data2);
```

### [Reading incoming datagrams](#reading_incoming_datagrams)

The [readable](/en-US/docs/Web/API/WebTransportDatagramDuplexStream/readable) property returns a [ReadableStream](/en-US/docs/Web/API/ReadableStream) object that you can use to receive data from the server:

js

```
async function readData() {
  const reader = transport.datagrams.readable.getReader();
  while (true) {
    const { value, done } = await reader.read();
    if (done) {
      break;
    }
    // value is a Uint8Array.
    console.log(value);
  }
}
```

## [Specifications](#specifications)

Specification
[WebTransport# webtransportdatagramduplexstream](https://w3c.github.io/webtransport/#webtransportdatagramduplexstream)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using WebTransport](https://developer.chrome.com/docs/capabilities/web-apis/webtransport)
- [WebSockets API](/en-US/docs/Web/API/WebSockets_API)
- [Streams API](/en-US/docs/Web/API/Streams_API)
- [WebTransport over HTTP/3](https://datatracker.ietf.org/doc/html/draft-ietf-webtrans-http3/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 1, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WebTransportDatagramDuplexStream/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webtransportdatagramduplexstream/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransportDatagramDuplexStream&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebtransportdatagramduplexstream%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransportDatagramDuplexStream%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebtransportdatagramduplexstream%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3b1efe57f3b22a97acb9db335f2848c90cdfe40e%0A*+Document+last+modified%3A+2025-07-01T23%3A51%3A25.000Z%0A%0A%3C%2Fdetails%3E)
