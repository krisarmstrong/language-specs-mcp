# WebTransportBidirectionalStream

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransportBidirectionalStream&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WebTransportBidirectionalStream` interface of the [WebTransport API](/en-US/docs/Web/API/WebTransport_API) represents a bidirectional stream created by a server or a client that can be used for reliable transport. Provides access to a [WebTransportReceiveStream](/en-US/docs/Web/API/WebTransportReceiveStream) for reading incoming data, and a [WebTransportSendStream](/en-US/docs/Web/API/WebTransportSendStream) for writing outgoing data.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[readable](/en-US/docs/Web/API/WebTransportBidirectionalStream/readable)Read only

Returns a [WebTransportReceiveStream](/en-US/docs/Web/API/WebTransportReceiveStream) instance that can be used to read incoming data.

[writable](/en-US/docs/Web/API/WebTransportBidirectionalStream/writable)Read only

Returns a [WebTransportSendStream](/en-US/docs/Web/API/WebTransportSendStream) instance that can be used to write outgoing data.

## [Examples](#examples)

### [Bidirectional transmission initiated by the user agent](#bidirectional_transmission_initiated_by_the_user_agent)

To open a bidirectional stream from a user agent, you use the [WebTransport.createBidirectionalStream()](/en-US/docs/Web/API/WebTransport/createBidirectionalStream) method to get a reference to a `WebTransportBidirectionalStream`. The `readable` and `writable` properties return references to `WebTransportReceiveStream` and `WebTransportSendStream` instances. These inherit from `ReadableStream` and `WritableStream` respectively, and can be used to read from and write to the server.

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

Reading from the `WebTransportReceiveStream` can be done in the same way as you would read a `ReadableStream`:

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

### [Bidirectional transmission initiated by the server](#bidirectional_transmission_initiated_by_the_server)

If the server opens a bidirectional stream to transmit data to and receive it from the client, this can be accessed via the [WebTransport.incomingBidirectionalStreams](/en-US/docs/Web/API/WebTransport/incomingBidirectionalStreams) property, which returns a [ReadableStream](/en-US/docs/Web/API/ReadableStream) of `WebTransportBidirectionalStream` objects. Each one can be used to read and write [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) instances as shown above. However, you need an initial function to read the bidirectional stream in the first place:

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

## [Specifications](#specifications)

Specification
[WebTransport# webtransportbidirectionalstream](https://w3c.github.io/webtransport/#webtransportbidirectionalstream)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using WebTransport](https://developer.chrome.com/docs/capabilities/web-apis/webtransport)
- [WebSockets API](/en-US/docs/Web/API/WebSockets_API)
- [Streams API](/en-US/docs/Web/API/Streams_API)
- [WebTransport over HTTP/3](https://datatracker.ietf.org/doc/html/draft-ietf-webtrans-http3/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WebTransportBidirectionalStream/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webtransportbidirectionalstream/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransportBidirectionalStream&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebtransportbidirectionalstream%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransportBidirectionalStream%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebtransportbidirectionalstream%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcc41ecd796870c2b6c77ad0b04fcb8d8c7d877d2%0A*+Document+last+modified%3A+2025-04-03T13%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
