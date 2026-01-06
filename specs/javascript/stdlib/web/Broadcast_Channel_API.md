# Broadcast Channel API

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2022⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBroadcast_Channel_API&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Broadcast Channel API allows basic communication between [browsing contexts](/en-US/docs/Glossary/Browsing_context) (that is, windows, tabs, frames, or iframes) and workers on the same [origin](/en-US/docs/Glossary/Origin).

Note: To be exact, communication is allowed between browsing contexts using the same [storage partition](/en-US/docs/Web/Privacy/Guides/State_Partitioning). Storage is first partitioned according to top-level sites—so for example, if you have one opened page at `a.com` that embeds an iframe from `b.com`, and another page opened to `b.com`, then the iframe cannot communicate with the second page despite them being technically same-origin. However, if the first page is also on `b.com`, then the iframe can communicate with the second page.

By creating a [BroadcastChannel](/en-US/docs/Web/API/BroadcastChannel) object, you can receive any messages that are posted to it. You don't have to maintain a reference to the frames or workers you wish to communicate with: they can "subscribe" to a particular channel by constructing their own [BroadcastChannel](/en-US/docs/Web/API/BroadcastChannel) with the same name, and have bi-directional communication between all of them.

## In this article

- [Broadcast Channel interface](#broadcast_channel_interface)
- [Conclusion](#conclusion)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Broadcast Channel interface](#broadcast_channel_interface)

### [Creating or joining a channel](#creating_or_joining_a_channel)

A client joins a broadcast channel by creating a [BroadcastChannel](/en-US/docs/Web/API/BroadcastChannel) object. Its [constructor](/en-US/docs/Web/API/BroadcastChannel/BroadcastChannel) takes one single parameter: the name of the channel. If it is the first to connect to that broadcast channel name, the underlying channel is created.

js

```
// Connection to a broadcast channel
const bc = new BroadcastChannel("test_channel");
```

### [Sending a message](#sending_a_message)

It is enough to call the [postMessage()](/en-US/docs/Web/API/BroadcastChannel/postMessage) method on the created `BroadcastChannel` object, which takes any object as an argument. An example string message:

js

```
// Example of sending of a very simple message
bc.postMessage("This is a test message.");
```

Data sent to the channel is serialized using the [structured clone algorithm](/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm). That means you can send a broad variety of data objects safely without having to serialize them yourself.

The API doesn't associate any semantics to messages, so it is up to the code to know what kind of messages to expect and what to do with them.

### [Receiving a message](#receiving_a_message)

When a message is posted, a [message](/en-US/docs/Web/API/BroadcastChannel/message_event) event is dispatched to each [BroadcastChannel](/en-US/docs/Web/API/BroadcastChannel) object connected to this channel. A function can be run for this event using the [onmessage](/en-US/docs/Web/API/BroadcastChannel/message_event) event handler:

js

```
// A handler that only logs the event to the console:
bc.onmessage = (event) => {
  console.log(event);
};
```

### [Disconnecting a channel](#disconnecting_a_channel)

To leave a channel, call the [close()](/en-US/docs/Web/API/BroadcastChannel/close) method on the object. This disconnects the object from the underlying channel, allowing garbage collection.

js

```
// Disconnect the channel
bc.close();
```

## [Conclusion](#conclusion)

The Broadcast Channel API's self-contained interface allows cross-context communication. It can be used to detect user actions in other tabs within a same origin, like when the user logs in or out.

The messaging protocol is not defined and the different browsing contexts need to implement it themselves; there is no negotiation nor requirement from the specification.

## [Interfaces](#interfaces)

[BroadcastChannel](/en-US/docs/Web/API/BroadcastChannel)

Represents a named channel that any [browsing context](/en-US/docs/Glossary/Browsing_context) of a given [origin](/en-US/docs/Glossary/Origin) can subscribe to.

## [Specifications](#specifications)

Specification
[HTML# broadcasting-to-other-browsing-contexts](https://html.spec.whatwg.org/multipage/web-messaging.html#broadcasting-to-other-browsing-contexts)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [BroadcastChannel](/en-US/docs/Web/API/BroadcastChannel), the interface implementing it.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 21, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Broadcast_Channel_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/broadcast_channel_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBroadcast_Channel_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbroadcast_channel_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBroadcast_Channel_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbroadcast_channel_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F775df1c62a1cbe555c4374ff9122d4ef15bd6f60%0A*+Document+last+modified%3A+2025-02-21T17%3A38%3A46.000Z%0A%0A%3C%2Fdetails%3E)
