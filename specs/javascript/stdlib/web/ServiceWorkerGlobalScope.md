# ServiceWorkerGlobalScope

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FServiceWorkerGlobalScope&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `ServiceWorkerGlobalScope` interface of the [Service Worker API](/en-US/docs/Web/API/Service_Worker_API) represents the global execution context of a service worker.

Developers should keep in mind that the ServiceWorker state is not persisted across the termination/restart cycle, so each event handler should assume it's being invoked with a bare, default global state.

Once successfully registered, a service worker can and will be terminated when idle to conserve memory and processor power. An active service worker is automatically restarted to respond to events, such as [fetch](/en-US/docs/Web/API/ServiceWorkerGlobalScope/fetch_event) or [message](/en-US/docs/Web/API/ServiceWorkerGlobalScope/message_event).

Additionally, synchronous requests are not allowed from within a service worker — only asynchronous requests, like those initiated via the [fetch()](/en-US/docs/Web/API/WorkerGlobalScope/fetch) method, can be used.

This interface inherits from the [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope) interface, and its parent [EventTarget](/en-US/docs/Web/API/EventTarget).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface inherits properties from the [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope) interface, and its parent [EventTarget](/en-US/docs/Web/API/EventTarget).

[ServiceWorkerGlobalScope.clients](/en-US/docs/Web/API/ServiceWorkerGlobalScope/clients)Read only

Contains the [Clients](/en-US/docs/Web/API/Clients) object associated with the service worker.

[ServiceWorkerGlobalScope.cookieStore](/en-US/docs/Web/API/ServiceWorkerGlobalScope/cookieStore)Read only

Returns a reference to the [CookieStore](/en-US/docs/Web/API/CookieStore) object associated with the service worker.

[ServiceWorkerGlobalScope.registration](/en-US/docs/Web/API/ServiceWorkerGlobalScope/registration)Read only

Contains the [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration) object that represents the service worker's registration.

[ServiceWorkerGlobalScope.serviceWorker](/en-US/docs/Web/API/ServiceWorkerGlobalScope/serviceWorker)Read only

Contains the [ServiceWorker](/en-US/docs/Web/API/ServiceWorker) object that represents the service worker.

## [Instance methods](#instance_methods)

This interface inherits methods from the [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope) interface, and its parent [EventTarget](/en-US/docs/Web/API/EventTarget).

[ServiceWorkerGlobalScope.skipWaiting()](/en-US/docs/Web/API/ServiceWorkerGlobalScope/skipWaiting)

Allows the current service worker registration to progress from waiting to active state while service worker clients are using it.

## [Events](#events)

Listen to this event using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[activate](/en-US/docs/Web/API/ServiceWorkerGlobalScope/activate_event)

Occurs when a [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration) acquires a new [ServiceWorkerRegistration.active](/en-US/docs/Web/API/ServiceWorkerRegistration/active) worker.

[backgroundfetchabort](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchabort_event)Experimental

Fired when a [background fetch](/en-US/docs/Web/API/Background_Fetch_API) operation has been canceled by the user or the app.

[backgroundfetchclick](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchclick_event)Experimental

Fired when the user has clicked on the UI for a [background fetch](/en-US/docs/Web/API/Background_Fetch_API) operation.

[backgroundfetchfail](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchfail_event)Experimental

Fired when at least one of the requests in a [background fetch](/en-US/docs/Web/API/Background_Fetch_API) operation has failed.

[backgroundfetchsuccess](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchsuccess_event)Experimental

Fired when all of the requests in a [background fetch](/en-US/docs/Web/API/Background_Fetch_API) operation have succeeded.

[canmakepayment](/en-US/docs/Web/API/ServiceWorkerGlobalScope/canmakepayment_event)Experimental

Fired on a payment app's service worker to check whether it is ready to handle a payment. Specifically, it is fired when the merchant website calls the [PaymentRequest()](/en-US/docs/Web/API/PaymentRequest/PaymentRequest) constructor.

[contentdelete](/en-US/docs/Web/API/ServiceWorkerGlobalScope/contentdelete_event)Experimental

Occurs when an item is removed from the [ContentIndex](/en-US/docs/Web/API/ContentIndex).

[cookiechange](/en-US/docs/Web/API/ServiceWorkerGlobalScope/cookiechange_event)

Fired when a cookie change has occurred that matches the service worker's cookie change subscription list.

[fetch](/en-US/docs/Web/API/ServiceWorkerGlobalScope/fetch_event)

Occurs when a [fetch()](/en-US/docs/Web/API/WorkerGlobalScope/fetch) is called.

[install](/en-US/docs/Web/API/ServiceWorkerGlobalScope/install_event)

Occurs when a [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration) acquires a new [ServiceWorkerRegistration.installing](/en-US/docs/Web/API/ServiceWorkerRegistration/installing) worker.

[message](/en-US/docs/Web/API/ServiceWorkerGlobalScope/message_event)

Occurs when incoming messages are received. Controlled pages can use the [MessagePort.postMessage()](/en-US/docs/Web/API/MessagePort/postMessage) method to send messages to service workers.

[messageerror](/en-US/docs/Web/API/ServiceWorkerGlobalScope/messageerror_event)

Occurs when incoming messages can't be deserialized.

[notificationclick](/en-US/docs/Web/API/ServiceWorkerGlobalScope/notificationclick_event)

Occurs when a user clicks on a displayed notification.

[notificationclose](/en-US/docs/Web/API/ServiceWorkerGlobalScope/notificationclose_event)

Occurs when a user closes a displayed notification.

[paymentrequest](/en-US/docs/Web/API/ServiceWorkerGlobalScope/paymentrequest_event)Experimental

Fired on a payment app when a payment flow has been initiated on the merchant website via the [PaymentRequest.show()](/en-US/docs/Web/API/PaymentRequest/show) method.

[sync](/en-US/docs/Web/API/ServiceWorkerGlobalScope/sync_event)

Triggered when a call to [SyncManager.register](/en-US/docs/Web/API/SyncManager/register) is made from a service worker client page. The attempt to sync is made either immediately if the network is available or as soon as the network becomes available.

[periodicsync](/en-US/docs/Web/API/ServiceWorkerGlobalScope/periodicsync_event)Experimental

Occurs at periodic intervals, which were specified when registering a [PeriodicSyncManager](/en-US/docs/Web/API/PeriodicSyncManager).

[push](/en-US/docs/Web/API/ServiceWorkerGlobalScope/push_event)

Occurs when a server push notification is received.

[pushsubscriptionchange](/en-US/docs/Web/API/ServiceWorkerGlobalScope/pushsubscriptionchange_event)

Occurs when a push subscription has been invalidated, or is about to be invalidated (e.g., when a push service sets an expiration time).

## [Examples](#examples)

This code snippet is from the [service worker prefetch sample](https://github.com/GoogleChrome/samples/blob/gh-pages/service-worker/prefetch/service-worker.js) (see [prefetch example live](https://googlechrome.github.io/samples/service-worker/prefetch/).) The [onfetch](/en-US/docs/Web/API/ServiceWorkerGlobalScope/fetch_event) event handler listens for the `fetch` event. When fired, the code returns a promise that resolves to the first matching request in the [Cache](/en-US/docs/Web/API/Cache) object. If no match is found, the code fetches a response from the network.

The code also handles exceptions thrown from the [fetch()](/en-US/docs/Web/API/WorkerGlobalScope/fetch) operation. Note that an HTTP error response (e.g., 404) will not trigger an exception. It will return a normal response object that has the appropriate error code set.

js

```
self.addEventListener("fetch", (event) => {
  console.log("Handling fetch event for", event.request.url);

  event.respondWith(
    caches.match(event.request).then((response) => {
      if (response) {
        console.log("Found response in cache:", response);

        return response;
      }
      console.log("No response found in cache. About to fetch from network…");

      return fetch(event.request).then(
        (response) => {
          console.log("Response from network is:", response);

          return response;
        },
        (error) => {
          console.error("Fetching failed:", error);

          throw error;
        },
      );
    }),
  );
});
```

## [Specifications](#specifications)

Specification
[Service Workers Nightly# serviceworkerglobalscope-interface](https://w3c.github.io/ServiceWorker/#serviceworkerglobalscope-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using Service Workers](/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)
- [Service workers basic code example](https://github.com/mdn/dom-examples/tree/main/service-worker/simple-service-worker)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ServiceWorkerGlobalScope/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/serviceworkerglobalscope/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FServiceWorkerGlobalScope&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fserviceworkerglobalscope%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FServiceWorkerGlobalScope%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fserviceworkerglobalscope%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F828ae6eee278f30c3fa3677a74915d28d9e338b2%0A*+Document+last+modified%3A+2025-05-30T03%3A30%3A21.000Z%0A%0A%3C%2Fdetails%3E)
