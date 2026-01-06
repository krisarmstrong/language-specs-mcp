# Channel Messaging API

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Channel Messaging API allows two separate scripts running in different browsing contexts attached to the same document (e.g., two IFrames, or the main document and an IFrame, two documents via a [SharedWorker](/en-US/docs/Web/API/SharedWorker), or two workers) to communicate directly, passing messages between one another through two-way channels (or pipes) with a port at each end.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

A message channel is created using the [MessageChannel()](/en-US/docs/Web/API/MessageChannel/MessageChannel) constructor. Once created, the two ports of the channel can be accessed through the [MessageChannel.port1](/en-US/docs/Web/API/MessageChannel/port1) and [MessageChannel.port2](/en-US/docs/Web/API/MessageChannel/port2) properties (which both return [MessagePort](/en-US/docs/Web/API/MessagePort) objects.) The app that created the channel uses `port1`, and the app at the other end of the port uses `port2` — you send a message to `port2`, and transfer the port over to the other browsing context using [window.postMessage](/en-US/docs/Web/API/Window/postMessage) along with two arguments (the message to send, and the object to transfer ownership of, in this case the port itself.)

When these transferable objects are transferred, they are no longer usable on the context they previously belonged to. A port, after it is sent, can no longer be used by the original context.

The other browsing context can listen for the message using [onmessage](/en-US/docs/Web/API/MessagePort/message_event), and grab the contents of the message using the event's `data` attribute. You could then respond by sending a message back to the original document using [MessagePort.postMessage](/en-US/docs/Web/API/MessagePort/postMessage).

When you want to stop sending messages down the channel, you can invoke [MessagePort.close](/en-US/docs/Web/API/MessagePort/close) to close the ports.

Find out more about how to use this API in [Using channel messaging](/en-US/docs/Web/API/Channel_Messaging_API/Using_channel_messaging).

## [Interfaces](#interfaces)

[MessageChannel](/en-US/docs/Web/API/MessageChannel)

Creates a new message channel to send messages across.

[MessagePort](/en-US/docs/Web/API/MessagePort)

Controls the ports on the message channel, allowing sending of messages from one port and listening out for them arriving at the other.

## [Examples](#examples)

- We have published a [channel messaging basic demo](https://github.com/mdn/dom-examples/tree/main/channel-messaging-basic) on GitHub ([run it live too](https://mdn.github.io/dom-examples/channel-messaging-basic/)), which shows a really simple single message transfer between a page and an embedded [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe).
- You can also see a [multimessaging demo](https://github.com/mdn/dom-examples/tree/main/channel-messaging-multimessage) ([run this live](https://mdn.github.io/dom-examples/channel-messaging-multimessage/)), which shows a slightly more complex setup that can send multiple messages between main page and IFrame.

## [Specifications](#specifications)

Specification
[HTML# channel-messaging](https://html.spec.whatwg.org/multipage/web-messaging.html#channel-messaging)

## [Browser compatibility](#browser_compatibility)

### [api.MessageChannel](#api.MessageChannel)

### [api.MessagePort](#api.MessagePort)

## [See also](#see_also)

- [Using channel messaging](/en-US/docs/Web/API/Channel_Messaging_API/Using_channel_messaging)
- [Web Workers API](/en-US/docs/Web/API/Web_Workers_API)
- [Broadcast Channel API](/en-US/docs/Web/API/Broadcast_Channel_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 6, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Channel_Messaging_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/channel_messaging_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FChannel_Messaging_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fchannel_messaging_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FChannel_Messaging_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fchannel_messaging_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2c641e08878722bf29fb784d58c61873ce4a133a%0A*+Document+last+modified%3A+2024-03-06T05%3A58%3A29.000Z%0A%0A%3C%2Fdetails%3E)
