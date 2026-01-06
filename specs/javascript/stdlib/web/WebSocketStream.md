# WebSocketStream

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WebSocketStream` interface of the [WebSockets API](/en-US/docs/Web/API/WebSockets_API) is a promise-based API for connecting to a WebSocket server. It uses [streams](/en-US/docs/Web/API/Streams_API) to send and receive data on the connection, and can therefore take advantage of stream [backpressure](/en-US/docs/Web/API/Streams_API/Concepts#backpressure) automatically, regulating the speed of reading or writing to avoid bottlenecks in the application.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[WebSocketStream()](/en-US/docs/Web/API/WebSocketStream/WebSocketStream)Experimental

Creates a new `WebSocketStream` object instance.

## [Instance properties](#instance_properties)

[url](/en-US/docs/Web/API/WebSocketStream/url)Read onlyExperimental

Returns the URL of the WebSocket server that the `WebSocketStream` instance was created with.

[closed](/en-US/docs/Web/API/WebSocketStream/closed)Read onlyExperimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with an object once the socket connection is closed. The object contains the closing code and reason as sent by the server.

[opened](/en-US/docs/Web/API/WebSocketStream/opened)Read onlyExperimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with an object once the socket connection is successfully opened. Among other features, this object contains a [ReadableStream](/en-US/docs/Web/API/ReadableStream) and a [WritableStream](/en-US/docs/Web/API/WritableStream) instance for receiving and sending data on the connection.

## [Instance methods](#instance_methods)

[close()](/en-US/docs/Web/API/WebSocketStream/close)Experimental

Closes the WebSocket connection.

## [Examples](#examples)

js

```
const output = document.querySelector("#output");

function writeToScreen(message) {
  const pElem = document.createElement("p");
  pElem.textContent = message;
  output.appendChild(pElem);
}

if (!("WebSocketStream" in self)) {
  writeToScreen("Your browser does not support WebSocketStream");
} else {
  const wsURL = "ws://127.0.0.1/";
  const wss = new WebSocketStream(wsURL);

  console.log(wss.url);

  async function start() {
    const { readable, writable, extensions, protocol } = await wss.opened;
    writeToScreen("CONNECTED");
    closeBtn.disabled = false;
    const reader = readable.getReader();
    const writer = writable.getWriter();

    writer.write("ping");
    writeToScreen("SENT: ping");

    while (true) {
      const { value, done } = await reader.read();
      writeToScreen(`RECEIVED: ${value}`);
      if (done) {
        break;
      }

      setTimeout(() => {
        writer.write("ping");
        writeToScreen("SENT: ping");
      }, 5000);
    }
  }

  start();
}
```

See [Using WebSocketStream to write a client](/en-US/docs/Web/API/WebSockets_API/Using_WebSocketStream) for a complete example with full explanation.

## [Specifications](#specifications)

Not currently a part of any specification. See [https://github.com/whatwg/websockets/pull/48](https://github.com/whatwg/websockets/pull/48) for standardization progress.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebSocketStream: integrating streams with the WebSocket API](https://developer.chrome.com/docs/capabilities/web-apis/websocketstream), developer.chrome.com (2020)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 25, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/WebSocketStream/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/websocketstream/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebSocketStream&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebsocketstream%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebSocketStream%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebsocketstream%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffb311d7305937497570966f015d8cc0eb1a0c29c%0A*+Document+last+modified%3A+2024-09-25T06%3A05%3A22.000Z%0A%0A%3C%2Fdetails%3E)
