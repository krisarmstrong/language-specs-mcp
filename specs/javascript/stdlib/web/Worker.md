# Worker

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorker&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API), except for [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `Worker` interface of the [Web Workers API](/en-US/docs/Web/API/Web_Workers_API) represents a background task that can be created via script, which can send messages back to its creator.

Creating a worker is done by calling the `Worker("path/to/worker/script")` constructor.

Workers may themselves spawn new workers, as long as those workers are hosted at the same [origin](/en-US/docs/Web/Security/Defenses/Same-origin_policy) as the parent page.

Note that not all interfaces and functions are available to web workers. See [Functions and classes available to Web Workers](/en-US/docs/Web/API/Web_Workers_API/Functions_and_classes_available_to_workers) for details.

## In this article

- [Constructors](#constructors)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructors](#constructors)

[Worker()](/en-US/docs/Web/API/Worker/Worker)

Creates a dedicated web worker that executes the script at the specified URL. This also works for [Blob URLs](/en-US/docs/Web/API/Blob).

## [Instance properties](#instance_properties)

Inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Instance methods](#instance_methods)

Inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[Worker.postMessage()](/en-US/docs/Web/API/Worker/postMessage)

Sends a message — consisting of any JavaScript object — to the worker's inner scope.

[Worker.terminate()](/en-US/docs/Web/API/Worker/terminate)

Immediately terminates the worker. This does not let worker finish its operations; it is halted at once. [ServiceWorker](/en-US/docs/Web/API/ServiceWorker) instances do not support this method.

## [Events](#events)

[error](/en-US/docs/Web/API/Worker/error_event)

Fires when an error occurs in the worker.

[message](/en-US/docs/Web/API/Worker/message_event)

Fires when the worker's parent receives a message from that worker.

[messageerror](/en-US/docs/Web/API/Worker/messageerror_event)

Fires when a `Worker` object receives a message that can't be [deserialized](/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm).

## [Example](#example)

The following code snippet creates a `Worker` object using the [Worker()](/en-US/docs/Web/API/Worker/Worker) constructor, then uses the worker object:

js

```
const myWorker = new Worker("/worker.js");
const first = document.querySelector("input#number1");
const second = document.querySelector("input#number2");

first.onchange = () => {
  myWorker.postMessage([first.value, second.value]);
  console.log("Message posted to worker");
};
```

For a full example, see our [Basic dedicated worker example](https://github.com/mdn/dom-examples/tree/main/web-workers/simple-web-worker) ([run dedicated worker](https://mdn.github.io/dom-examples/web-workers/simple-web-worker/)).

## [Specifications](#specifications)

Specification
[HTML# dedicated-workers-and-the-worker-interface](https://html.spec.whatwg.org/multipage/workers.html#dedicated-workers-and-the-worker-interface)

## [Browser compatibility](#browser_compatibility)

Support varies for different types of workers. See each worker type's page for specifics.

### [Cross-origin worker error behavior](#cross-origin_worker_error_behavior)

In early versions of the spec, loading a cross-origin worker script threw a `SecurityError`. Nowadays, an [error](/en-US/docs/Web/API/Worker/error_event) event is thrown instead.

## [See also](#see_also)

- [Using Web Workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
- [Functions and classes available to Web Workers](/en-US/docs/Web/API/Web_Workers_API/Functions_and_classes_available_to_workers)
- Other kind of workers: [SharedWorker](/en-US/docs/Web/API/SharedWorker) and [Service Worker](/en-US/docs/Web/API/Service_Worker_API).
- [OffscreenCanvas](/en-US/docs/Web/API/OffscreenCanvas) interface

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Worker/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/worker/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorker&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fworker%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorker%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fworker%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
