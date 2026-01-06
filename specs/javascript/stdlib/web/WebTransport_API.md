# WebTransport API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransport_API&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The WebTransport API provides a modern update to [WebSockets](/en-US/docs/Web/API/WebSockets_API), transmitting data between client and server using [HTTP/3 Transport](https://datatracker.ietf.org/doc/html/draft-ietf-webtrans-http3/). WebTransport provides support for multiple streams, unidirectional streams, and out-of-order delivery. It enables reliable transport via [streams](/en-US/docs/Web/API/Streams_API) and unreliable transport via UDP-like datagrams.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

[HTTP/3](https://en.wikipedia.org/wiki/HTTP/3) has been in progress since 2018. It is based on Google's QUIC protocol (which is itself based on UDP), and fixes several issues around the classic TCP protocol, on which HTTP and WebSockets are based.

These include:

[Head-of-line blocking](/en-US/docs/Glossary/Head_of_line_blocking)

HTTP/2 allows multiplexing, so a single connection can stream multiple resources simultaneously. However, if a single resource fails, all other resources on that connection are held up until any missing packets are retransmitted. With QUIC, only the failing resource is affected.

[Faster performance](#faster_performance)

QUIC is more performant than TCP in many ways. QUIC can handle security features by itself, rather than handing responsibility off to other protocols like TLS — meaning fewer round trips. And streams provide better transport efficiency than the older packet mechanism. That can make a significant difference, especially on high-latency networks.

[Better network transitions](#better_network_transitions)

QUIC uses a unique connection ID to handle the source and destination of each request — to ensure that packets are delivered correctly. This ID can persist between different networks, meaning that, for example, a download can continue without getting interrupted if you switch from Wi-Fi to a mobile network. HTTP/2, on the other hand, uses IP addresses as identifiers, so network transitions can be problematic.

[Unreliable transport](#unreliable_transport)

HTTP/3 supports unreliable data transmission via datagrams.

The WebTransport API provides low-level access to two-way communication via HTTP/3, taking advantage of the above benefits, and supporting both reliable and unreliable data transmission.

### [Initial connection](#initial_connection)

To open a connection to an HTTP/3 server, you pass its URL to the [WebTransport()](/en-US/docs/Web/API/WebTransport/WebTransport) constructor. Note that the scheme needs to be HTTPS, and the port number needs to be explicitly specified. Once the [WebTransport.ready](/en-US/docs/Web/API/WebTransport/ready) promise fulfills, you can start using the connection.

Also note that you can respond to the connection closing by waiting for the [WebTransport.closed](/en-US/docs/Web/API/WebTransport/closed) promise to fulfill. Errors returned by WebTransport operations are of type [WebTransportError](/en-US/docs/Web/API/WebTransportError), and contain additional data on top of the standard [DOMException](/en-US/docs/Web/API/DOMException) set.

js

```
const url = "https://example.com:4999/wt";

async function initTransport(url) {
  // Initialize transport connection
  const transport = new WebTransport(url);

  // The connection can be used once ready fulfills
  await transport.ready;

  // …
}

// …

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

### [Unreliable transmission via datagrams](#unreliable_transmission_via_datagrams)

"Unreliable" means that transmission of data is not guaranteed, nor is arrival in a specific order. This is fine in some situations and provides very fast delivery. For example, you might want to transmit regular game state updates where each message supersedes the last one that arrives, and order is not important.

Unreliable data transmission is handled via the [WebTransport.datagrams](/en-US/docs/Web/API/WebTransport/datagrams) property — this returns a [WebTransportDatagramDuplexStream](/en-US/docs/Web/API/WebTransportDatagramDuplexStream) object containing everything you need to send datagrams to the server, and receive them back.

The [WebTransportDatagramDuplexStream.writable](/en-US/docs/Web/API/WebTransportDatagramDuplexStream/writable) property returns a [WritableStream](/en-US/docs/Web/API/WritableStream) object that you can write data to using a writer, for transmission to the server:

js

```
const writer = transport.datagrams.writable.getWriter();
const data1 = new Uint8Array([65, 66, 67]);
const data2 = new Uint8Array([68, 69, 70]);
writer.write(data1);
writer.write(data2);
```

The [WebTransportDatagramDuplexStream.readable](/en-US/docs/Web/API/WebTransportDatagramDuplexStream/readable) property returns a [ReadableStream](/en-US/docs/Web/API/ReadableStream) object that you can use to receive data from the server:

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

### [Reliable transmission via streams](#reliable_transmission_via_streams)

"Reliable" means that transmission and order of data are guaranteed. That provides slower delivery (albeit faster than with WebSockets), and is needed in situations where reliability and ordering are important (such as chat applications, for example).

When using reliable transmission via streams you can also set the relative priority of different streams over the same transport.

### [Unidirectional transmission](#unidirectional_transmission)

To open a unidirectional stream from a user agent, you use the [WebTransport.createUnidirectionalStream()](/en-US/docs/Web/API/WebTransport/createUnidirectionalStream) method to get a reference to a [WritableStream](/en-US/docs/Web/API/WritableStream). From this you can [get a writer](/en-US/docs/Web/API/WritableStream/getWriter) to allow data to be written to the stream and sent to the server.

js

```
async function writeData() {
  const stream = await transport.createUnidirectionalStream();
  const writer = stream.writable.getWriter();
  const data1 = new Uint8Array([65, 66, 67]);
  const data2 = new Uint8Array([68, 69, 70]);
  writer.write(data1);
  writer.write(data2);

  try {
    await writer.close();
    console.log("All data has been sent.");
  } catch (error) {
    console.error(`An error occurred: ${error}`);
  }
}
```

Note also the use of the [WritableStreamDefaultWriter.close()](/en-US/docs/Web/API/WritableStreamDefaultWriter/close) method to close the associated HTTP/3 connection once all data has been sent.

If the server opens a unidirectional stream to transmit data to the client, this can be accessed on the client via the [WebTransport.incomingUnidirectionalStreams](/en-US/docs/Web/API/WebTransport/incomingUnidirectionalStreams) property, which returns a [ReadableStream](/en-US/docs/Web/API/ReadableStream) of [WebTransportReceiveStream](/en-US/docs/Web/API/WebTransportReceiveStream) objects. These can be used to read [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) instances sent by the server.

In this case, the first thing to do is set up a function to read a `WebTransportReceiveStream`. These objects inherit from the `ReadableStream` class, so can be used in just the same way:

js

```
async function readData(receiveStream) {
  const reader = receiveStream.getReader();
  while (true) {
    const { done, value } = await reader.read();
    if (done) {
      break;
    }
    // value is a Uint8Array
    console.log(value);
  }
}
```

Next, call [WebTransport.incomingUnidirectionalStreams](/en-US/docs/Web/API/WebTransport/incomingUnidirectionalStreams) and get a reference to the reader available on the `ReadableStream` it returns, and then use the reader to read the data from the server. Each chunk is a `WebTransportReceiveStream`, and we use the `readFrom()` set up earlier to read them:

js

```
async function receiveUnidirectional() {
  const uds = transport.incomingUnidirectionalStreams;
  const reader = uds.getReader();
  while (true) {
    const { done, value } = await reader.read();
    if (done) {
      break;
    }
    // value is an instance of WebTransportReceiveStream
    await readData(value);
  }
}
```

#### Bidirectional transmission

To open a bidirectional stream from a user agent, you use the [WebTransport.createBidirectionalStream()](/en-US/docs/Web/API/WebTransport/createBidirectionalStream) method to get a reference to a [WebTransportBidirectionalStream](/en-US/docs/Web/API/WebTransportBidirectionalStream). This contains `readable` and `writable` properties returning references to `WebTransportReceiveStream` and `WebTransportSendStream` instances that can be used to read from and write to the server.

Note:`WebTransportBidirectionalStream` is similar to [WebTransportDatagramDuplexStream](/en-US/docs/Web/API/WebTransportDatagramDuplexStream), except that in that interface the `readable` and `writable` properties are `ReadableStream` and `WritableStream` respectively.

js

```
async function setUpBidirectional() {
  const stream = await transport.createBidirectionalStream();
  // stream is a WebTransportBidirectionalStream
  // stream.readable is a WebTransportReceiveStream
  const readable = stream.readable;
  // stream.writable is a WebTransportSendStream
  const writable = stream.writable;

  // …
}
```

Reading from the `WebTransportReceiveStream` can then be done as follows:

js

```
async function readData(readable) {
  const reader = readable.getReader();
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

And writing to the `WebTransportSendStream` can be done like this:

js

```
async function writeData(writable) {
  const writer = writable.getWriter();
  const data1 = new Uint8Array([65, 66, 67]);
  const data2 = new Uint8Array([68, 69, 70]);
  writer.write(data1);
  writer.write(data2);
}
```

If the server opens a bidirectional stream to transmit data to and receive it from the client, this can be accessed via the [WebTransport.incomingBidirectionalStreams](/en-US/docs/Web/API/WebTransport/incomingBidirectionalStreams) property, which returns a [ReadableStream](/en-US/docs/Web/API/ReadableStream) of `WebTransportBidirectionalStream` objects. Each one can be used to read and write [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) instances as shown above. However, as with the unidirectional example, you need an initial function to read the bidirectional stream in the first place:

js

```
async function receiveBidirectional() {
  const bds = transport.incomingBidirectionalStreams;
  const reader = bds.getReader();
  while (true) {
    const { done, value } = await reader.read();
    if (done) {
      break;
    }
    // value is an instance of WebTransportBidirectionalStream
    await readData(value.readable);
    await writeData(value.writable);
  }
}
```

## [Interfaces](#interfaces)

[WebTransport](/en-US/docs/Web/API/WebTransport)

Provides functionality to enable a user agent to connect to an HTTP/3 server, initiate reliable and unreliable transport in either or both directions, and close the connection once it is no longer needed.

[WebTransportBidirectionalStream](/en-US/docs/Web/API/WebTransportBidirectionalStream)

Represents a bidirectional stream created by a server or a client that can be used for reliable transport. Provides access to a [ReadableStream](/en-US/docs/Web/API/ReadableStream) for reading incoming data, and a [WritableStream](/en-US/docs/Web/API/WritableStream) for writing outgoing data.

[WebTransportDatagramDuplexStream](/en-US/docs/Web/API/WebTransportDatagramDuplexStream)

Represents a duplex stream that can be used for unreliable transport of datagrams between client and server. Provides access to a [ReadableStream](/en-US/docs/Web/API/ReadableStream) for reading incoming datagrams, a [WritableStream](/en-US/docs/Web/API/WritableStream) for writing outgoing datagrams, and various settings and statistics related to the stream.

[WebTransportError](/en-US/docs/Web/API/WebTransportError)

Represents an error related to the WebTransport API, which can arise from server errors, network connection problems, or client-initiated abort operations (for example, arising from a [WritableStream.abort()](/en-US/docs/Web/API/WritableStream/abort) call).

[WebTransportReceiveStream](/en-US/docs/Web/API/WebTransportReceiveStream)

Provides streaming features for an incoming WebTransport unidirectional or bidirectional [WebTransport](/en-US/docs/Web/API/WebTransport) stream.

[WebTransportSendStream](/en-US/docs/Web/API/WebTransportSendStream)

Provides streaming features for an outgoing WebTransport unidirectional or bidirectional [WebTransport](/en-US/docs/Web/API/WebTransport) stream.

## [Examples](#examples)

For complete examples, see:

- [WebTransport over HTTP/3 client](https://webtransport.day/)

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

 This page was last modified on ⁨Jul 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WebTransport_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webtransport_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransport_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebtransport_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransport_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebtransport_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F30c9f71e6a6cac4d894688cabf7e4b50af87cfe5%0A*+Document+last+modified%3A+2025-07-19T12%3A19%3A17.000Z%0A%0A%3C%2Fdetails%3E)
