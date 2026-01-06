# BroadcastChannel

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2022⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBroadcastChannel&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `BroadcastChannel` interface represents a named channel that any [browsing context](/en-US/docs/Glossary/Browsing_context) of a given [origin](/en-US/docs/Glossary/Origin) can subscribe to. It allows communication between different documents (in different windows, tabs, frames or iframes) of the same origin. Messages are broadcasted via a [message](/en-US/docs/Web/API/BroadcastChannel/message_event) event fired at all `BroadcastChannel` objects listening to the channel, except the object that sent the message.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[BroadcastChannel()](/en-US/docs/Web/API/BroadcastChannel/BroadcastChannel)

Creates an object linking to the named channel.

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[BroadcastChannel.name](/en-US/docs/Web/API/BroadcastChannel/name)Read only

Returns a string, the name of the channel.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[BroadcastChannel.postMessage()](/en-US/docs/Web/API/BroadcastChannel/postMessage)

Sends the message, of any type of object, to each `BroadcastChannel` object listening to the same channel.

[BroadcastChannel.close()](/en-US/docs/Web/API/BroadcastChannel/close)

Closes the channel object, indicating it won't get any new messages, and allowing it to be, eventually, garbage collected.

## [Events](#events)

This interface also inherits events from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[message](/en-US/docs/Web/API/BroadcastChannel/message_event)

Fired when a message arrives on the channel. Also available via the `onmessage` property.

[messageerror](/en-US/docs/Web/API/BroadcastChannel/messageerror_event)

Fired when a message arrives that can't be deserialized. Also available via the `onmessageerror` property.

## [Specifications](#specifications)

Specification
[HTML# broadcasting-to-other-browsing-contexts](https://html.spec.whatwg.org/multipage/web-messaging.html#broadcasting-to-other-browsing-contexts)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- Another, more heavyweight, way of communicating between browser contexts: [ServiceWorker](/en-US/docs/Web/API/ServiceWorker).
- [Broadcast Channel API overview](/en-US/docs/Web/API/Broadcast_Channel_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 3, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/BroadcastChannel/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/broadcastchannel/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBroadcastChannel&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbroadcastchannel%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBroadcastChannel%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbroadcastchannel%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F50a45d52fd9f45f1ca30b546af5920d0ccda82dc%0A*+Document+last+modified%3A+2024-06-03T00%3A14%3A24.000Z%0A%0A%3C%2Fdetails%3E)
