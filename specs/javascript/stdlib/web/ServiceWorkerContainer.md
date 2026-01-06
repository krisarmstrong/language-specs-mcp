# ServiceWorkerContainer

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FServiceWorkerContainer&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ServiceWorkerContainer` interface of the [Service Worker API](/en-US/docs/Web/API/Service_Worker_API) provides an object representing the service worker as an overall unit in the network ecosystem, including facilities to register, unregister and update service workers, and access the state of service workers and their registrations.

Most importantly, it exposes the [ServiceWorkerContainer.register()](/en-US/docs/Web/API/ServiceWorkerContainer/register) method used to register service workers, and the [ServiceWorkerContainer.controller](/en-US/docs/Web/API/ServiceWorkerContainer/controller) property used to determine whether or not the current page is actively controlled.

`ServiceWorkerContainer` objects are exposed in the Window scope through [Navigator.serviceWorker](/en-US/docs/Web/API/Navigator/serviceWorker) and in workers using [WorkerNavigator.serviceWorker](/en-US/docs/Web/API/WorkerNavigator/serviceWorker) (if supported — check [browser compatibility](#browser_compatibility)).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[ServiceWorkerContainer.controller](/en-US/docs/Web/API/ServiceWorkerContainer/controller)Read only

A [ServiceWorker](/en-US/docs/Web/API/ServiceWorker) object that represents the active service worker controlling the current page or `null` if the page has no active or activating service worker.

[ServiceWorkerContainer.ready](/en-US/docs/Web/API/ServiceWorkerContainer/ready)Read only

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with the [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration) associated with the current page, but only when there is an active service worker. This provides a mechanism to defer code execution until a service worker is active.

## [Instance methods](#instance_methods)

[ServiceWorkerContainer.getRegistration()](/en-US/docs/Web/API/ServiceWorkerContainer/getRegistration)

Gets a [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration) object whose scope matches the provided document URL. The method returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to a [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration) or `undefined`.

[ServiceWorkerContainer.getRegistrations()](/en-US/docs/Web/API/ServiceWorkerContainer/getRegistrations)

Returns all [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration) objects associated with a `ServiceWorkerContainer` in an array. The method returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to an array of [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration).

[ServiceWorkerContainer.register()](/en-US/docs/Web/API/ServiceWorkerContainer/register)

Creates or updates a [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration) for the given `scriptURL`.

[ServiceWorkerContainer.startMessages()](/en-US/docs/Web/API/ServiceWorkerContainer/startMessages)

Explicitly starts the flow of messages being dispatched from a service worker to pages under its control (e.g., sent via [Client.postMessage()](/en-US/docs/Web/API/Client/postMessage)). This can be used to react to sent messages earlier, even before that page's content has finished loading.

## [Events](#events)

[controllerchange](/en-US/docs/Web/API/ServiceWorkerContainer/controllerchange_event)

Fired when the document's associated [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration) acquires a new [active](/en-US/docs/Web/API/ServiceWorkerRegistration/active) worker.

[message](/en-US/docs/Web/API/ServiceWorkerContainer/message_event)

Fired when incoming messages are received by the `ServiceWorkerContainer` object (e.g., via a [MessagePort.postMessage()](/en-US/docs/Web/API/MessagePort/postMessage) call).

[messageerror](/en-US/docs/Web/API/ServiceWorkerContainer/messageerror_event)

Fired when incoming messages can not deserialized by the `ServiceWorkerContainer` object (e.g., via a [MessagePort.postMessage()](/en-US/docs/Web/API/MessagePort/postMessage) call).

## [Examples](#examples)

The example below first checks to see if the browser supports service workers. If supported, the code registers the service worker and determines if the page is actively controlled by the service worker. If it isn't, it prompts the user to reload the page so the service worker can take control. The code also reports any registration failures.

js

```
if ("serviceWorker" in navigator) {
  // Register a service worker hosted at the root of the
  // site using the default scope.
  navigator.serviceWorker
    .register("/sw.js")
    .then((registration) => {
      console.log("Service worker registration succeeded:", registration);

      // At this point, you can optionally do something
      // with registration. See https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerRegistration
    })
    .catch((error) => {
      console.error(`Service worker registration failed: ${error}`);
    });

  // Independent of the registration, let's also display
  // information about whether the current page is controlled
  // by an existing service worker, and when that
  // controller changes.

  // First, do a one-off check if there's currently a
  // service worker in control.
  if (navigator.serviceWorker.controller) {
    console.log(
      "This page is currently controlled by:",
      navigator.serviceWorker.controller,
    );
  }

  // Then, register a handler to detect when a new or
  // updated service worker takes control.
  navigator.serviceWorker.oncontrollerchange = () => {
    console.log(
      "This page is now controlled by",
      navigator.serviceWorker.controller,
    );
  };
} else {
  console.log("Service workers are not supported.");
}
```

## [Specifications](#specifications)

Specification
[Service Workers Nightly# serviceworkercontainer-interface](https://w3c.github.io/ServiceWorker/#serviceworkercontainer-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using Service Workers](/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)
- [Service workers basic code example](https://github.com/mdn/dom-examples/tree/main/service-worker/simple-service-worker)
- [Using web workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 11, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ServiceWorkerContainer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/serviceworkercontainer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FServiceWorkerContainer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fserviceworkercontainer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FServiceWorkerContainer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fserviceworkercontainer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F981e2d17e897c6280fd27364746a34d8560d30d1%0A*+Document+last+modified%3A+2025-07-11T01%3A37%3A08.000Z%0A%0A%3C%2Fdetails%3E)
