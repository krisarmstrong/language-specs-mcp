# Server-sent events

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

Traditionally, a web page has to send a request to the server to receive new data; that is, the page requests data from the server. With server-sent events, it's possible for a server to send new data to a web page at any time, by pushing messages to the web page. These incoming messages can be treated as [Events](/en-US/docs/Web/API/Event) + data inside the web page.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

To learn how to use server-sent events, see our article [Using server-sent events](/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events).

## [Interfaces](#interfaces)

[EventSource](/en-US/docs/Web/API/EventSource)

Defines all the features that handle connecting to a server, receiving events/data, errors, closing a connection, etc.

## [Examples](#examples)

- [Simple SSE demo using PHP](https://github.com/mdn/dom-examples/tree/main/server-sent-events)

## [Specifications](#specifications)

Specification
[HTML# server-sent-events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events)

## [See also](#see_also)

### [Tools](#tools)

- [Mercure: a real-time communication protocol (publish-subscribe) built on top of SSE](https://mercure.rocks/)
- [Transmit: a native opinionated Server-Sent-Event (SSE) module built for AdonisJS](https://docs.adonisjs.com/guides/digging-deeper/transmit)
- [EventSource polyfill for Node.js](https://github.com/EventSource/eventsource)
- Remy Sharp's [EventSource polyfill](https://github.com/remy/polyfills/blob/master/EventSource.js)
- Yaffle's [EventSource polyfill](https://github.com/Yaffle/EventSource)
- Rick Waldron's [jquery plugin](https://github.com/rwaldron/jquery.eventsource)
- intercooler.js [declarative SSE support](https://intercoolerjs.org/docs.html#sse)

### [Related Topics](#related_topics)

- [Learn: Making network requests with JavaScript](/en-US/docs/Learn_web_development/Core/Scripting/Network_requests)
- [JavaScript](/en-US/docs/Web/JavaScript)
- [WebSockets](/en-US/docs/Web/API/WebSockets_API)

### [Other resources](#other_resources)

- [Creating a wall/feed social application](https://hacks.mozilla.org/2011/06/a-wall-powered-by-eventsource-and-server-sent-events/) powered by server-sent events and [its code on GitHub](https://github.com/mozilla/webowonder-demos/tree/master/demos/friends%20timeline).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 20, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Server-sent_events/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/server-sent_events/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FServer-sent_events&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fserver-sent_events%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FServer-sent_events%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fserver-sent_events%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F65d664a83ca055135f38ff22ff4966ccc8a6061a%0A*+Document+last+modified%3A+2025-03-20T16%3A04%3A56.000Z%0A%0A%3C%2Fdetails%3E)
