# ExtendableMessageEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FExtendableMessageEvent&level=high)

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `ExtendableMessageEvent` interface of the [Service Worker API](/en-US/docs/Web/API/Service_Worker_API) represents the event object of a [message](/en-US/docs/Web/API/ServiceWorkerGlobalScope/message_event) event fired on a service worker (when a message is received on the [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) from another context) — extends the lifetime of such events.

This interface inherits from the [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent) interface.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ExtendableMessageEvent()](/en-US/docs/Web/API/ExtendableMessageEvent/ExtendableMessageEvent)

Creates a new `ExtendableMessageEvent` object instance.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

[ExtendableMessageEvent.data](/en-US/docs/Web/API/ExtendableMessageEvent/data)Read only

Returns the event's data. It can be any data type. If dispatched in `messageerror` event, the property will be `null`.

[ExtendableMessageEvent.origin](/en-US/docs/Web/API/ExtendableMessageEvent/origin)Read only

Returns the origin of the [Client](/en-US/docs/Web/API/Client) that sent the message.

[ExtendableMessageEvent.lastEventId](/en-US/docs/Web/API/ExtendableMessageEvent/lastEventId)Read only

Represents, in [server-sent events](/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events), the last event ID of the event source.

[ExtendableMessageEvent.source](/en-US/docs/Web/API/ExtendableMessageEvent/source)Read only

Returns a reference to the [Client](/en-US/docs/Web/API/Client) object that sent the message.

[ExtendableMessageEvent.ports](/en-US/docs/Web/API/ExtendableMessageEvent/ports)Read only

Returns the array containing the [MessagePort](/en-US/docs/Web/API/MessagePort) objects representing the ports of the associated message channel.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

## [Examples](#examples)

In the below example a page gets a handle to the [ServiceWorker](/en-US/docs/Web/API/ServiceWorker) object via [ServiceWorkerRegistration.active](/en-US/docs/Web/API/ServiceWorkerRegistration/active), and then calls its `postMessage()` function.

js

```
// in the page being controlled
if (navigator.serviceWorker) {
  navigator.serviceWorker.register("service-worker.js");

  navigator.serviceWorker.addEventListener("message", (event) => {
    // event is a MessageEvent object
    console.log(`The service worker sent me a message: ${event.data}`);
  });

  navigator.serviceWorker.ready.then((registration) => {
    registration.active.postMessage("Hi service worker");
  });
}
```

The service worker can receive the message by listening to the `message` event:

js

```
// in the service worker
addEventListener("message", (event) => {
  // event is an ExtendableMessageEvent object
  console.log(`The client sent me a message: ${event.data}`);

  event.source.postMessage("Hi client");
});
```

## [Specifications](#specifications)

Specification
[Service Workers Nightly# extendablemessageevent-interface](https://w3c.github.io/ServiceWorker/#extendablemessageevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using Service Workers](/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)
- [Service workers basic code example](https://github.com/mdn/dom-examples/tree/main/service-worker/simple-service-worker)
- [Channel Messaging](/en-US/docs/Web/API/Channel_Messaging_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 13, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/ExtendableMessageEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/extendablemessageevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FExtendableMessageEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fextendablemessageevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FExtendableMessageEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fextendablemessageevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2ef36a6d6f380e79c88bc3a80033e1d3c4629994%0A*+Document+last+modified%3A+2024-05-13T06%3A21%3A16.000Z%0A%0A%3C%2Fdetails%3E)
