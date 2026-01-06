# Web Workers API

Web Workers makes it possible to run a script operation in a background thread separate from the main execution thread of a web application. The advantage of this is that laborious processing can be performed in a separate thread, allowing the main (usually the UI) thread to run without being blocked/slowed down.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

A worker is an object created using a constructor (e.g., [Worker()](/en-US/docs/Web/API/Worker/Worker)) that runs a named JavaScript file — this file contains the code that will run in the worker thread.

In addition to the standard [JavaScript](/en-US/docs/Web/JavaScript) set of functions (such as [String](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String), [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), [Object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object), [JSON](/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON), etc.), you can run almost any code you like inside a worker thread. There are some exceptions: for example, you can't directly manipulate the DOM from inside a worker, or use some default methods and properties of the [Window](/en-US/docs/Web/API/Window) object. For information about the code that you can run see [supported functions](/en-US/docs/Web/API/Web_Workers_API/Functions_and_classes_available_to_workers#functions_available_in_workers), and [supported Web APIs](/en-US/docs/Web/API/Web_Workers_API/Functions_and_classes_available_to_workers#web_apis_available_in_workers).

Data is sent between workers and the main thread via a system of messages — both sides send their messages using the `postMessage()` method, and respond to messages via the `onmessage` event handler (the message is contained within the [message](/en-US/docs/Web/API/Worker/message_event) event's `data` property). The data is copied rather than shared.

Workers may in turn spawn new workers, as long as those workers are hosted within the same [origin](/en-US/docs/Glossary/Origin) as the parent page.

In addition, workers can make network requests using the [fetch()](/en-US/docs/Web/API/WorkerGlobalScope/fetch) or [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest) APIs (although note that the [responseXML](/en-US/docs/Web/API/XMLHttpRequest/responseXML) attribute of `XMLHttpRequest` will always be `null`).

### [Worker types](#worker_types)

There are a number of different types of workers:

- [Dedicated workers](/en-US/docs/Web/API/Worker) are workers that are utilized by a single script. This context is represented by a [DedicatedWorkerGlobalScope](/en-US/docs/Web/API/DedicatedWorkerGlobalScope) object.
- [Shared workers](/en-US/docs/Web/API/SharedWorker) are workers that can be utilized by multiple scripts running in different windows, IFrames, etc., as long as they are in the same domain as the worker. They are a little more complex than dedicated workers — scripts must communicate via an active port.
- [Service Workers](/en-US/docs/Web/API/Service_Worker_API) essentially act as proxy servers that sit between web applications, the browser, and the network (when available). They are intended, among other things, to enable the creation of effective offline experiences, intercept network requests and take appropriate action based on whether the network is available, and update assets residing on the server. They will also allow access to push notifications and background sync APIs.

### [Worker contexts](#worker_contexts)

While [Window](/en-US/docs/Web/API/Window) is not directly available to workers, many of the same methods are defined in a shared mixin (`WindowOrWorkerGlobalScope`), and made available to workers through their own [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope)-derived contexts:

- [DedicatedWorkerGlobalScope](/en-US/docs/Web/API/DedicatedWorkerGlobalScope) for dedicated workers
- [SharedWorkerGlobalScope](/en-US/docs/Web/API/SharedWorkerGlobalScope) for shared workers
- [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) for [service workers](/en-US/docs/Web/API/Service_Worker_API)

## [Interfaces](#interfaces)

[Worker](/en-US/docs/Web/API/Worker)

Represents a running worker thread, allowing you to pass messages to the running worker code.

[WorkerLocation](/en-US/docs/Web/API/WorkerLocation)

Defines the absolute location of the script executed by the [Worker](/en-US/docs/Web/API/Worker).

[SharedWorker](/en-US/docs/Web/API/SharedWorker)

Represents a specific kind of worker that can be accessed from several [browsing contexts](/en-US/docs/Glossary/Browsing_context) (i.e., windows, tabs, or iframes) or even other workers.

[WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope)

Represents the generic scope of any worker (doing the same job as [Window](/en-US/docs/Web/API/Window) does for normal web content). Different types of worker have scope objects that inherit from this interface and add more specific features.

[DedicatedWorkerGlobalScope](/en-US/docs/Web/API/DedicatedWorkerGlobalScope)

Represents the scope of a dedicated worker, inheriting from [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope) and adding some dedicated features.

[SharedWorkerGlobalScope](/en-US/docs/Web/API/SharedWorkerGlobalScope)

Represents the scope of a shared worker, inheriting from [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope) and adding some dedicated features.

[WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator)

Represents the identity and state of the user agent (the client).

## [Examples](#examples)

We have created a couple of demos to show web worker usage:

- [Basic dedicated worker example](https://github.com/mdn/dom-examples/tree/main/web-workers/simple-web-worker) ([run dedicated worker](https://mdn.github.io/dom-examples/web-workers/simple-web-worker/)).
- [Basic shared worker example](https://github.com/mdn/dom-examples/tree/main/web-workers/simple-shared-worker) ([run shared worker](https://mdn.github.io/dom-examples/web-workers/simple-shared-worker/)).
- [OffscreenCanvas worker example](https://github.com/mdn/dom-examples/tree/main/web-workers/offscreen-canvas-worker) ([run OffscreenCanvas worker](https://mdn.github.io/dom-examples/web-workers/offscreen-canvas-worker/)).

You can find out more information on how these demos work in [Using Web Workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers).

## [Specifications](#specifications)

Specification
[HTML# workers](https://html.spec.whatwg.org/multipage/workers.html#workers)

## [See also](#see_also)

- [Using Web Workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
- [Worker](/en-US/docs/Web/API/Worker) interface
- [SharedWorker](/en-US/docs/Web/API/SharedWorker) interface
- [Service Worker API](/en-US/docs/Web/API/Service_Worker_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Web_Workers_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/web_workers_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Workers_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fweb_workers_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Workers_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fweb_workers_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
