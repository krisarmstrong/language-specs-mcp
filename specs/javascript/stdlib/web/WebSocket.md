# WebSocket

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebSocket&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WebSocket` object provides the API for creating and managing a [WebSocket](/en-US/docs/Web/API/WebSockets_API) connection to a server, as well as for sending and receiving data on the connection.

To construct a `WebSocket`, use the [WebSocket()](/en-US/docs/Web/API/WebSocket/WebSocket) constructor.

Note: The `WebSocket` API has no way to apply [backpressure](/en-US/docs/Web/API/Streams_API/Concepts#backpressure), therefore when messages arrive faster than the application can process them, the application will either fill up the device's memory by buffering those messages, become unresponsive due to 100% CPU usage, or both. For an alternative that provides backpressure automatically, see [WebSocketStream](/en-US/docs/Web/API/WebSocketStream).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[WebSocket()](/en-US/docs/Web/API/WebSocket/WebSocket)

Returns a newly created `WebSocket` object.

## [Instance properties](#instance_properties)

[WebSocket.binaryType](/en-US/docs/Web/API/WebSocket/binaryType)

The binary data type used by the connection.

[WebSocket.bufferedAmount](/en-US/docs/Web/API/WebSocket/bufferedAmount)Read only

The number of bytes of queued data.

[WebSocket.extensions](/en-US/docs/Web/API/WebSocket/extensions)Read only

The extensions selected by the server.

[WebSocket.protocol](/en-US/docs/Web/API/WebSocket/protocol)Read only

The sub-protocol selected by the server.

[WebSocket.readyState](/en-US/docs/Web/API/WebSocket/readyState)Read only

The current state of the connection.

[WebSocket.url](/en-US/docs/Web/API/WebSocket/url)Read only

The absolute URL of the WebSocket.

## [Instance methods](#instance_methods)

[WebSocket.close()](/en-US/docs/Web/API/WebSocket/close)

Closes the connection.

[WebSocket.send()](/en-US/docs/Web/API/WebSocket/send)

Enqueues data to be transmitted.

## [Events](#events)

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

[close](/en-US/docs/Web/API/WebSocket/close_event)

Fired when a connection with a `WebSocket` is closed. Also available via the `onclose` property

[error](/en-US/docs/Web/API/WebSocket/error_event)

Fired when a connection with a `WebSocket` has been closed because of an error, such as when some data couldn't be sent. Also available via the `onerror` property.

[message](/en-US/docs/Web/API/WebSocket/message_event)

Fired when data is received through a `WebSocket`. Also available via the `onmessage` property.

[open](/en-US/docs/Web/API/WebSocket/open_event)

Fired when a connection with a `WebSocket` is opened. Also available via the `onopen` property.

## [Examples](#examples)

js

```
// Create WebSocket connection.
const socket = new WebSocket("ws://localhost:8080");

// Connection opened
socket.addEventListener("open", (event) => {
  socket.send("Hello Server!");
});

// Listen for messages
socket.addEventListener("message", (event) => {
  console.log("Message from server ", event.data);
});
```

## [Specifications](#specifications)

Specification
[WebSockets# the-websocket-interface](https://websockets.spec.whatwg.org/#the-websocket-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Writing WebSocket client applications](/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 25, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/WebSocket/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/websocket/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebSocket&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebsocket%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebSocket%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebsocket%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffb311d7305937497570966f015d8cc0eb1a0c29c%0A*+Document+last+modified%3A+2024-09-25T06%3A05%3A22.000Z%0A%0A%3C%2Fdetails%3E)
