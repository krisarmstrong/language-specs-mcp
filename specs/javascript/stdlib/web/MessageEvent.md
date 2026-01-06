# MessageEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMessageEvent&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `MessageEvent` interface represents a message received by a target object.

This is used to represent messages in:

- [Server-sent events](/en-US/docs/Web/API/Server-sent_events) (see the [message](/en-US/docs/Web/API/EventSource/message_event) event of [EventSource](/en-US/docs/Web/API/EventSource)).
- [Web sockets](/en-US/docs/Web/API/WebSockets_API) (see the [message](/en-US/docs/Web/API/WebSocket/message_event) event of [WebSocket](/en-US/docs/Web/API/WebSocket)).
- Cross-document messaging (see [Window.postMessage()](/en-US/docs/Web/API/Window/postMessage) and the [message](/en-US/docs/Web/API/Window/message_event) event of [Window](/en-US/docs/Web/API/Window)).
- [Channel messaging](/en-US/docs/Web/API/Channel_Messaging_API) (see [MessagePort.postMessage()](/en-US/docs/Web/API/MessagePort/postMessage) and the [message](/en-US/docs/Web/API/MessagePort/message_event) event of [MessagePort](/en-US/docs/Web/API/MessagePort)).
- Cross-worker/document messaging (see the above two entries, but also [Worker.postMessage()](/en-US/docs/Web/API/Worker/postMessage), the [message](/en-US/docs/Web/API/Worker/message_event) event of [Worker](/en-US/docs/Web/API/Worker), the [message](/en-US/docs/Web/API/ServiceWorkerGlobalScope/message_event) event of [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope), etc.)
- [Broadcast channels](/en-US/docs/Web/API/Broadcast_Channel_API) (see [BroadcastChannel.postMessage()](/en-US/docs/Web/API/BroadcastChannel/postMessage) and the [message](/en-US/docs/Web/API/BroadcastChannel/message_event) event of [BroadcastChannel](/en-US/docs/Web/API/BroadcastChannel)).
- WebRTC data channels (see the [message](/en-US/docs/Web/API/RTCDataChannel/message_event) event of [RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel)).

The action triggered by this event is defined in a function set as the event handler for the relevant `message` event.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[MessageEvent()](/en-US/docs/Web/API/MessageEvent/MessageEvent)

Creates a new `MessageEvent`.

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[MessageEvent.data](/en-US/docs/Web/API/MessageEvent/data)Read only

The data sent by the message emitter.

[MessageEvent.origin](/en-US/docs/Web/API/MessageEvent/origin)Read only

A string representing the origin of the message emitter.

[MessageEvent.lastEventId](/en-US/docs/Web/API/MessageEvent/lastEventId)Read only

A string representing a unique ID for the event.

[MessageEvent.source](/en-US/docs/Web/API/MessageEvent/source)Read only

A `MessageEventSource` (which can be a [WindowProxy](/en-US/docs/Glossary/WindowProxy), [MessagePort](/en-US/docs/Web/API/MessagePort), or [ServiceWorker](/en-US/docs/Web/API/ServiceWorker) object) representing the message emitter.

[MessageEvent.ports](/en-US/docs/Web/API/MessageEvent/ports)Read only

An array of [MessagePort](/en-US/docs/Web/API/MessagePort) objects containing all [MessagePort](/en-US/docs/Web/API/MessagePort) objects sent with the message, in order.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent, [Event](/en-US/docs/Web/API/Event).

`initMessageEvent()`Deprecated

Initializes a message event. Do not use this anymore — use the [MessageEvent()](/en-US/docs/Web/API/MessageEvent/MessageEvent) constructor instead.

## [Examples](#examples)

In our [Basic shared worker example](https://github.com/mdn/dom-examples/tree/main/web-workers/simple-shared-worker) ([run shared worker](https://mdn.github.io/dom-examples/web-workers/simple-shared-worker/)), we have two HTML pages, each of which uses some JavaScript to perform a calculation. The different scripts are using the same worker file to perform the calculation — they can both access it, even if their pages are running inside different windows.

The following code snippet shows creation of a [SharedWorker](/en-US/docs/Web/API/SharedWorker) object using the [SharedWorker()](/en-US/docs/Web/API/SharedWorker/SharedWorker) constructor. Both scripts contain this:

js

```
const myWorker = new SharedWorker("worker.js");
```

Both scripts then access the worker through a [MessagePort](/en-US/docs/Web/API/MessagePort) object created using the [SharedWorker.port](/en-US/docs/Web/API/SharedWorker/port) property. If the onmessage event is attached using addEventListener, the port is manually started using its `start()` method:

js

```
myWorker.port.start();
```

When the port is started, both scripts post messages to the worker and handle messages sent from it using `port.postMessage()` and `port.onmessage`, respectively:

js

```
[first, second].forEach((input) => {
  input.onchange = () => {
    myWorker.port.postMessage([first.value, second.value]);
    console.log("Message posted to worker");
  };
});

myWorker.port.onmessage = (e) => {
  result1.textContent = e.data;
  console.log("Message received from worker");
};
```

Inside the worker we use the [onconnect](/en-US/docs/Web/API/SharedWorkerGlobalScope/connect_event) handler to connect to the same port discussed above. The ports associated with that worker are accessible in the [connect](/en-US/docs/Web/API/SharedWorkerGlobalScope/connect_event) event's `ports` property — we then use [MessagePort](/en-US/docs/Web/API/MessagePort)`start()` method to start the port, and the `onmessage` handler to deal with messages sent from the main threads.

js

```
onconnect = (e) => {
  const port = e.ports[0];

  port.addEventListener("message", (e) => {
    const workerResult = `Result: ${e.data[0] * e.data[1]}`;
    port.postMessage(workerResult);
  });

  port.start(); // Required when using addEventListener. Otherwise called implicitly by onmessage setter.
};
```

## [Specifications](#specifications)

Specification
[HTML# the-messageevent-interface](https://html.spec.whatwg.org/multipage/comms.html#the-messageevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [ExtendableMessageEvent](/en-US/docs/Web/API/ExtendableMessageEvent) — similar to this interface but used in interfaces that needs to give more flexibility to authors.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 31, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MessageEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/messageevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMessageEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmessageevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMessageEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmessageevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F875215de95e76ff145fc85902d32c1142a1ccf53%0A*+Document+last+modified%3A+2024-12-31T09%3A04%3A40.000Z%0A%0A%3C%2Fdetails%3E)
