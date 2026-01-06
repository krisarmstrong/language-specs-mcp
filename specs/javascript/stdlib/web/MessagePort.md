# MessagePort

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMessagePort&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `MessagePort` interface of the [Channel Messaging API](/en-US/docs/Web/API/Channel_Messaging_API) represents one of the two ports of a [MessageChannel](/en-US/docs/Web/API/MessageChannel), allowing messages to be sent from one port and listening out for them arriving at the other.

`MessagePort` is a [transferable object](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects).

## In this article

- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

Inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[postMessage()](/en-US/docs/Web/API/MessagePort/postMessage)

Sends a message from the port, and optionally, transfers ownership of objects to other browsing contexts.

[start()](/en-US/docs/Web/API/MessagePort/start)

Starts the sending of messages queued on the port (only needed when using [EventTarget.addEventListener](/en-US/docs/Web/API/EventTarget/addEventListener); it is implied when using [onmessage](/en-US/docs/Web/API/MessagePort/message_event)).

[close()](/en-US/docs/Web/API/MessagePort/close)

Disconnects the port, so it is no longer active.

## [Events](#events)

Inherits events from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[message](/en-US/docs/Web/API/MessagePort/message_event)

Fired when a `MessagePort` object receives a message.

[messageerror](/en-US/docs/Web/API/MessagePort/messageerror_event)

Fired when a `MessagePort` object receives a message that can't be deserialized.

## [Example](#example)

In the following example, you can see a new channel being created using the [MessageChannel()](/en-US/docs/Web/API/MessageChannel/MessageChannel) constructor.

When the IFrame has loaded, we register an [onmessage](/en-US/docs/Web/API/MessagePort/message_event) handler for [MessageChannel.port1](/en-US/docs/Web/API/MessageChannel/port1) and transfer [MessageChannel.port2](/en-US/docs/Web/API/MessageChannel/port2) to the IFrame using the [window.postMessage](/en-US/docs/Web/API/Window/postMessage) method along with a message.

When a message is received back from the IFrame, the `onMessage` function outputs the message to a paragraph.

js

```
const channel = new MessageChannel();
const output = document.querySelector(".output");
const iframe = document.querySelector("iframe");

// Wait for the iframe to load
iframe.addEventListener("load", onLoad);

function onLoad() {
  // Listen for messages on port1
  channel.port1.onmessage = onMessage;

  // Transfer port2 to the iframe
  iframe.contentWindow.postMessage("Hello from the main page!", "*", [
    channel.port2,
  ]);
}

// Handle messages received on port1
function onMessage(e) {
  output.innerHTML = e.data;
}
```

For a full working example, see our [channel messaging basic demo](https://github.com/mdn/dom-examples/tree/main/channel-messaging-basic) on GitHub ([run it live too](https://mdn.github.io/dom-examples/channel-messaging-basic/)).

## [Specifications](#specifications)

Specification
[HTML# message-ports](https://html.spec.whatwg.org/multipage/web-messaging.html#message-ports)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using channel messaging](/en-US/docs/Web/API/Channel_Messaging_API/Using_channel_messaging)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 6, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MessagePort/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/messageport/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMessagePort&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmessageport%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMessagePort%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmessageport%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe4c0939929e1b3e1fa3fd3da82b827fca3ed4c79%0A*+Document+last+modified%3A+2024-03-06T06%3A22%3A42.000Z%0A%0A%3C%2Fdetails%3E)
