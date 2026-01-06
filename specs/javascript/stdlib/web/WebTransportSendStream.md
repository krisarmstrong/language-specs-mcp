# WebTransportSendStream

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransportSendStream&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WebTransportSendStream` interface of the [WebTransport API](/en-US/docs/Web/API/WebTransport_API) is a specialized [WritableStream](/en-US/docs/Web/API/WritableStream) that is used to send outbound data in both unidirectional or bidirectional [WebTransport](/en-US/docs/Web/API/WebTransport) streams.

The send stream is a [writable stream](/en-US/docs/Web/API/Streams_API/Using_writable_streams) of [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array), that can be written to in order to send data to a server. It additionally provides streaming features such as setting the send order, and getting stream statistics.

Objects of this type are not constructed directly. When creating a unidirectional stream the [WebTransport.createUnidirectionalStream()](/en-US/docs/Web/API/WebTransport/createUnidirectionalStream) returns an object of this type for sending data. When creating a bidirectional stream using [WebTransport.createBidirectionalStream()](/en-US/docs/Web/API/WebTransport/createBidirectionalStream), the method returns a [WebTransportBidirectionalStream](/en-US/docs/Web/API/WebTransportBidirectionalStream), and the send stream object can be obtained from its [writable](/en-US/docs/Web/API/WebTransportBidirectionalStream/writable) property. When a bidirectional stream is initiated by the remote end, an object of this type can similarly be obtained using [WebTransport.incomingBidirectionalStreams](/en-US/docs/Web/API/WebTransport/incomingBidirectionalStreams).

`WebTransportSendStream` is a [transferable object](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [WritableStream](/en-US/docs/Web/API/WritableStream).

[WebTransportSendStream.getStats()](/en-US/docs/Web/API/WebTransportSendStream/getStats)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with statistics related to this stream.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [WritableStream](/en-US/docs/Web/API/WritableStream).

[WebTransportSendStream.sendOrder](/en-US/docs/Web/API/WebTransportSendStream/sendOrder)Experimental

Indicates the send priority of this stream relative to other streams for which the value has been set.

## [Examples](#examples)

See [WebTransport.incomingUnidirectionalStreams](/en-US/docs/Web/API/WebTransport/incomingUnidirectionalStreams) for an example of how to get a [ReadableStream](/en-US/docs/Web/API/ReadableStream) of `WebTransportSendStream` objects.

## [Specifications](#specifications)

Specification
[WebTransport# webtransportsendstream](https://w3c.github.io/webtransport/#webtransportsendstream)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using WebTransport](https://developer.chrome.com/docs/capabilities/web-apis/webtransport)
- [Streams API](/en-US/docs/Web/API/Streams_API)
- [WebTransport over HTTP/3](https://datatracker.ietf.org/doc/html/draft-ietf-webtrans-http3/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 6, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/WebTransportSendStream/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webtransportsendstream/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransportSendStream&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebtransportsendstream%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebTransportSendStream%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebtransportsendstream%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4de6f76bbfd76229db78ffb7d52cf6b4cb9f31f8%0A*+Document+last+modified%3A+2024-03-06T06%3A23%3A15.000Z%0A%0A%3C%2Fdetails%3E)
