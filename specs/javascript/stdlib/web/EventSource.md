# EventSource

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEventSource&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `EventSource` interface is web content's interface to [server-sent events](/en-US/docs/Web/API/Server-sent_events).

An `EventSource` instance opens a persistent connection to an [HTTP](/en-US/docs/Web/HTTP) server, which sends [events](/en-US/docs/Learn_web_development/Core/Scripting/Events) in `text/event-stream` format. The connection remains open until closed by calling [EventSource.close()](/en-US/docs/Web/API/EventSource/close).

Once the connection is opened, incoming messages from the server are delivered to your code in the form of events. If there is an event field in the incoming message, the triggered event is the same as the event field value. If no event field is present, then a generic [message](/en-US/docs/Web/API/EventSource/message_event) event is fired.

Unlike [WebSockets](/en-US/docs/Web/API/WebSockets_API), server-sent events are unidirectional; that is, data messages are delivered in one direction, from the server to the client (such as a user's web browser). That makes them an excellent choice when there's no need to send data from the client to the server in message form. For example, `EventSource` is a useful approach for handling things like social media status updates, news feeds, or delivering data into a [client-side storage](/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Client-side_storage) mechanism like [IndexedDB](/en-US/docs/Web/API/IndexedDB_API) or [web storage](/en-US/docs/Web/API/Web_Storage_API).

Warning: When not used over HTTP/2, SSE suffers from a limitation to the maximum number of open connections, which can be specially painful when opening various tabs as the limit is per browser and set to a very low number (6). The issue has been marked as "Won't fix" in [Chrome](https://crbug.com/275955) and [Firefox](https://bugzil.la/906896). This limit is per browser + domain, so that means that you can open 6 SSE connections across all of the tabs to `www.example1.com` and another 6 SSE connections to `www.example2.com`. (from [Stack Overflow](https://stackoverflow.com/questions/5195452/websockets-vs-server-sent-events-eventsource/5326159)). When using HTTP/2, the maximum number of simultaneous HTTP streams is negotiated between the server and the client (defaults to 100).

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

[EventSource()](/en-US/docs/Web/API/EventSource/EventSource)

Creates a new `EventSource` to handle receiving server-sent events from a specified URL, optionally in credentials mode.

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[EventSource.readyState](/en-US/docs/Web/API/EventSource/readyState)Read only

A number representing the state of the connection. Possible values are `CONNECTING` (`0`), `OPEN` (`1`), or `CLOSED` (`2`).

[EventSource.url](/en-US/docs/Web/API/EventSource/url)Read only

A string representing the URL of the source.

[EventSource.withCredentials](/en-US/docs/Web/API/EventSource/withCredentials)Read only

A boolean value indicating whether the `EventSource` object was instantiated with cross-origin ([CORS](/en-US/docs/Web/HTTP/Guides/CORS)) credentials set (`true`), or not (`false`, the default).

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[EventSource.close()](/en-US/docs/Web/API/EventSource/close)

Closes the connection, if any, and sets the `readyState` attribute to `CLOSED`. If the connection is already closed, the method does nothing.

## [Events](#events)

[error](/en-US/docs/Web/API/EventSource/error_event)

Fired when a connection to an event source failed to open.

[message](/en-US/docs/Web/API/EventSource/message_event)

Fired when data is received from an event source.

[open](/en-US/docs/Web/API/EventSource/open_event)

Fired when a connection to an event source has opened.

Additionally, the event source itself may send messages with an event field, which will create ad hoc events keyed to that value.

## [Examples](#examples)

In this basic example, an `EventSource` is created to receive unnamed events from the server; a page with the name `sse.php` is responsible for generating the events.

js

```
const evtSource = new EventSource("sse.php");
const eventList = document.querySelector("ul");

evtSource.onmessage = (e) => {
  const newElement = document.createElement("li");

  newElement.textContent = `message: ${e.data}`;
  eventList.appendChild(newElement);
};
```

Each received event causes our `EventSource` object's `onmessage` event handler to be run. It, in turn, creates a new [<li>](/en-US/docs/Web/HTML/Reference/Elements/li) element and writes the message's data into it, then appends the new element to the list element already in the document.

Note: You can find a full example on GitHub — see [Simple SSE demo using PHP](https://github.com/mdn/dom-examples/tree/main/server-sent-events).

To listen to named events, you'll require a listener for each type of event sent.

js

```
const sse = new EventSource("/api/v1/sse");

/*
 * This will listen only for events
 * similar to the following:
 *
 * event: notice
 * data: useful data
 * id: some-id
 */
sse.addEventListener("notice", (e) => {
  console.log(e.data);
});

/*
 * Similarly, this will listen for events
 * with the field `event: update`
 */
sse.addEventListener("update", (e) => {
  console.log(e.data);
});

/*
 * The event "message" is a special case, as it
 * will capture events without an event field
 * as well as events that have the specific type
 * `event: message` It will not trigger on any
 * other event type.
 */
sse.addEventListener("message", (e) => {
  console.log(e.data);
});
```

## [Specifications](#specifications)

Specification
[HTML# the-eventsource-interface](https://html.spec.whatwg.org/multipage/server-sent-events.html#the-eventsource-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Server-sent events](/en-US/docs/Web/API/Server-sent_events)
- [Using server-sent events](/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/EventSource/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/eventsource/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEventSource&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Feventsource%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEventSource%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Feventsource%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d929bb0a021c7130d5a71a4bf505bcb8070378d%0A*+Document+last+modified%3A+2025-03-13T12%3A48%3A23.000Z%0A%0A%3C%2Fdetails%3E)
