# ServiceWorker

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FServiceWorker&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ServiceWorker` interface of the [Service Worker API](/en-US/docs/Web/API/Service_Worker_API) provides a reference to a service worker. Multiple [browsing contexts](/en-US/docs/Glossary/Browsing_context) (e.g., pages, workers, etc.) can be associated with the same service worker, each through a unique `ServiceWorker` object.

A `ServiceWorker` object is available via a number of properties:

- [ServiceWorkerRegistration.active](/en-US/docs/Web/API/ServiceWorkerRegistration/active)
- [ServiceWorkerGlobalScope.serviceWorker](/en-US/docs/Web/API/ServiceWorkerGlobalScope/serviceWorker)
- [ServiceWorkerContainer.controller](/en-US/docs/Web/API/ServiceWorkerContainer/controller) — when the service worker is in `activating` or `activated` state
- [ServiceWorkerRegistration.installing](/en-US/docs/Web/API/ServiceWorkerRegistration/installing) — when the service worker is in `installing` state
- [ServiceWorkerRegistration.waiting](/en-US/docs/Web/API/ServiceWorkerRegistration/waiting) — when the service worker is in `installed` state

The [ServiceWorker.state](/en-US/docs/Web/API/ServiceWorker/state) property and [statechange event](/en-US/docs/Web/API/ServiceWorker/statechange_event) can be used to check and observe changes in the lifecycle-state of the object's associated service worker. Related lifecycle events, such as [install](/en-US/docs/Web/API/ServiceWorkerGlobalScope/install_event) and [activate](/en-US/docs/Web/API/ServiceWorkerGlobalScope/activate_event) are fired at the service worker itself.

Service workers allow static import of [ECMAScript modules](/en-US/docs/Web/JavaScript/Guide/Modules), if supported, using [import](/en-US/docs/Web/JavaScript/Reference/Statements/import). Dynamic import is disallowed by the specification — calling [import()](/en-US/docs/Web/JavaScript/Reference/Operators/import) will throw.

Service workers can only be registered in the Window scope in some or all browsers, because the `ServiceWorker` object is not exposed to [DedicatedWorkerGlobalScope](/en-US/docs/Web/API/DedicatedWorkerGlobalScope) and [SharedWorkerGlobalScope](/en-US/docs/Web/API/SharedWorkerGlobalScope). Check the [browser compatibility](#browser_compatibility) for information.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `ServiceWorker` interface inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[ServiceWorker.scriptURL](/en-US/docs/Web/API/ServiceWorker/scriptURL)Read only

Returns the `ServiceWorker` serialized script URL defined as part of [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration). The URL must be on the same origin as the document that registers the `ServiceWorker`.

[ServiceWorker.state](/en-US/docs/Web/API/ServiceWorker/state)Read only

Returns the state of the service worker. It returns one of the following values: `parsed`, `installing`, `installed`, `activating`, `activated`, or `redundant`.

## [Instance methods](#instance_methods)

The `ServiceWorker` interface inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[ServiceWorker.postMessage()](/en-US/docs/Web/API/ServiceWorker/postMessage)

Sends a message — consisting of any [structured-cloneable](/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm) JavaScript object — to the service worker. The message is transmitted to the service worker using a [message](/en-US/docs/Web/API/ServiceWorkerGlobalScope/message_event) event on its global scope.

## [Events](#events)

[statechange](/en-US/docs/Web/API/ServiceWorker/statechange_event)

Fired when [ServiceWorker.state](/en-US/docs/Web/API/ServiceWorker/state) changes.

[error](/en-US/docs/Web/API/ServiceWorker/error_event)

Fired when an error happens inside the `ServiceWorker` object.

## [Examples](#examples)

This code snippet is from the [service worker registration-events sample](https://github.com/GoogleChrome/samples/blob/gh-pages/service-worker/registration-events/index.html) ([live demo](https://googlechrome.github.io/samples/service-worker/registration-events/)). The code listens for any change in the [ServiceWorker.state](/en-US/docs/Web/API/ServiceWorker/state) and returns its value.

js

```
if ("serviceWorker" in navigator) {
  navigator.serviceWorker
    .register("service-worker.js", {
      scope: "./",
    })
    .then((registration) => {
      let serviceWorker;
      if (registration.installing) {
        serviceWorker = registration.installing;
        document.querySelector("#kind").textContent = "installing";
      } else if (registration.waiting) {
        serviceWorker = registration.waiting;
        document.querySelector("#kind").textContent = "waiting";
      } else if (registration.active) {
        serviceWorker = registration.active;
        document.querySelector("#kind").textContent = "active";
      }
      if (serviceWorker) {
        // logState(serviceWorker.state);
        serviceWorker.addEventListener("statechange", (e) => {
          // logState(e.target.state);
        });
      }
    })
    .catch((error) => {
      // Something went wrong during registration. The service-worker.js file
      // might be unavailable or contain a syntax error.
    });
} else {
  // The current browser doesn't support service workers.
  // Perhaps it is too old or we are not in a Secure Context.
}
```

## [Specifications](#specifications)

Specification
[Service Workers Nightly# serviceworker-interface](https://w3c.github.io/ServiceWorker/#serviceworker-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [The Offline Cookbook](https://web.dev/articles/offline-cookbook) (service workers)
- [Using Service Workers](/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)
- [Service worker basic code example](https://github.com/mdn/dom-examples/tree/main/service-worker/simple-service-worker)
- [Using web workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ServiceWorker/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/serviceworker/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FServiceWorker&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fserviceworker%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FServiceWorker%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fserviceworker%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
