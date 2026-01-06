# SharedWorker

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedWorker&level=not)

The `SharedWorker` interface represents a specific kind of worker that can be accessed from several browsing contexts, such as several windows, iframes or even workers. They implement an interface different than dedicated workers and have a different global scope, [SharedWorkerGlobalScope](/en-US/docs/Web/API/SharedWorkerGlobalScope).

Note: If SharedWorker can be accessed from several browsing contexts, all those browsing contexts must share the exact same origin (same protocol, host and port).

## In this article

- [Constructors](#constructors)
- [Instance properties](#instance_properties)
- [Events](#events)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructors](#constructors)

[SharedWorker()](/en-US/docs/Web/API/SharedWorker/SharedWorker)

Creates a shared web worker that executes the script at the specified URL.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[SharedWorker.port](/en-US/docs/Web/API/SharedWorker/port)Read only

Returns a [MessagePort](/en-US/docs/Web/API/MessagePort) object used to communicate with and control the shared worker.

## [Events](#events)

[error](/en-US/docs/Web/API/SharedWorker/error_event)

Fires when an error occurs in the shared worker.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Example](#example)

In our [Basic shared worker example](https://github.com/mdn/dom-examples/tree/main/web-workers/simple-shared-worker) ([run shared worker](https://mdn.github.io/dom-examples/web-workers/simple-shared-worker/)), we have two HTML pages, each of which uses some JavaScript to perform a simple calculation. The different scripts are using the same worker file to perform the calculation — they can both access it, even if their pages are running inside different windows.

The following code snippet shows creation of a `SharedWorker` object using the [SharedWorker()](/en-US/docs/Web/API/SharedWorker/SharedWorker) constructor. Both scripts contain this:

js

```
const myWorker = new SharedWorker("worker.js");
```

Note: Once a shared worker is created, any script running in the same origin can obtain a reference to that worker and communicate with it. The shared worker will be alive as long as its global scope's owner set (a set of `Document` and `WorkerGlobalScope` objects) is not empty (for example, if there is any live page holding a reference to it, maybe through `new SharedWorker()`). To read more about shared worker lifetime, see [The worker's lifetime](https://html.spec.whatwg.org/multipage/workers.html#the-worker's-lifetime) section of the HTML specification.

Both scripts then access the worker through a [MessagePort](/en-US/docs/Web/API/MessagePort) object created using the [SharedWorker.port](/en-US/docs/Web/API/SharedWorker/port) property. If the onmessage event is attached using addEventListener, the port is manually started using its `start()` method:

js

```
myWorker.port.start();
```

When the port is started, both scripts post messages to the worker and handle messages sent from it using `port.postMessage()` and `port.onmessage`, respectively:

Note: You can use browser devtools to debug your SharedWorker, by entering a URL in your browser address bar to access the devtools workers inspector; for example, in Chrome, the URL `chrome://inspect/#workers`, and in Firefox, the URL `about:debugging#workers`.

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
[HTML# shared-workers-and-the-sharedworker-interface](https://html.spec.whatwg.org/multipage/workers.html#shared-workers-and-the-sharedworker-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Worker](/en-US/docs/Web/API/Worker)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 31, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/SharedWorker/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/sharedworker/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedWorker&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsharedworker%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedWorker%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsharedworker%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F875215de95e76ff145fc85902d32c1142a1ccf53%0A*+Document+last+modified%3A+2024-12-31T09%3A04%3A40.000Z%0A%0A%3C%2Fdetails%3E)
