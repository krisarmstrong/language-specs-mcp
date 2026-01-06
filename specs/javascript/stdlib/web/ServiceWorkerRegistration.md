# ServiceWorkerRegistration

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FServiceWorkerRegistration&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ServiceWorkerRegistration` interface of the [Service Worker API](/en-US/docs/Web/API/Service_Worker_API) represents the service worker registration. You register a service worker to control one or more pages that share the same origin.

The lifetime of a service worker registration is beyond that of the `ServiceWorkerRegistration` objects that represent them within the lifetime of their corresponding service worker clients. The browser maintains a persistent list of active `ServiceWorkerRegistration` objects.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface,[EventTarget](/en-US/docs/Web/API/EventTarget).

[ServiceWorkerRegistration.active](/en-US/docs/Web/API/ServiceWorkerRegistration/active)Read only

Returns a service worker whose state is `activating` or `activated`. This is initially set to `null`. An active worker will control a [Client](/en-US/docs/Web/API/Client) if the client's URL falls within the scope of the registration (the `scope` option set when [ServiceWorkerContainer.register](/en-US/docs/Web/API/ServiceWorkerContainer/register) is first called.)

[ServiceWorkerRegistration.backgroundFetch](/en-US/docs/Web/API/ServiceWorkerRegistration/backgroundFetch)Read onlyExperimental

Returns a reference to a [BackgroundFetchManager](/en-US/docs/Web/API/BackgroundFetchManager) object, which manages background fetch operations.

[ServiceWorkerRegistration.cookies](/en-US/docs/Web/API/ServiceWorkerRegistration/cookies)Read only

Returns a reference to the [CookieStoreManager](/en-US/docs/Web/API/CookieStoreManager) interface, which allows subscribe and unsubscribe to cookie change events.

[ServiceWorkerRegistration.index](/en-US/docs/Web/API/ServiceWorkerRegistration/index)Read onlyExperimental

Returns a reference to the [ContentIndex](/en-US/docs/Web/API/ContentIndex) interface, for managing indexed content for offline viewing.

[ServiceWorkerRegistration.installing](/en-US/docs/Web/API/ServiceWorkerRegistration/installing)Read only

Returns a service worker whose state is `installing`. This is initially set to `null`.

[ServiceWorkerRegistration.navigationPreload](/en-US/docs/Web/API/ServiceWorkerRegistration/navigationPreload)Read only

Returns the instance of [NavigationPreloadManager](/en-US/docs/Web/API/NavigationPreloadManager) associated with the current service worker registration.

[ServiceWorkerRegistration.paymentManager](/en-US/docs/Web/API/ServiceWorkerRegistration/paymentManager)Read onlyExperimental

Returns a payment app's [PaymentManager](/en-US/docs/Web/API/PaymentManager) instance, which is used to manage various payment app functionality.

[ServiceWorkerRegistration.periodicSync](/en-US/docs/Web/API/ServiceWorkerRegistration/periodicSync)Read onlyExperimental

Returns a reference to the [PeriodicSyncManager](/en-US/docs/Web/API/PeriodicSyncManager) interface, which allows for registering of tasks to run at specific intervals.

[ServiceWorkerRegistration.pushManager](/en-US/docs/Web/API/ServiceWorkerRegistration/pushManager)Read only

Returns a reference to the [PushManager](/en-US/docs/Web/API/PushManager) interface for managing push subscriptions including subscribing, getting an active subscription, and accessing push permission status.

[ServiceWorkerRegistration.scope](/en-US/docs/Web/API/ServiceWorkerRegistration/scope)Read only

Returns a string representing a URL that defines a service worker's registration scope; that is, the range of URLs the service worker can control.

[ServiceWorkerRegistration.sync](/en-US/docs/Web/API/ServiceWorkerRegistration/sync)Read only

Returns a reference to the [SyncManager](/en-US/docs/Web/API/SyncManager) interface, which manages background synchronization processes.

[ServiceWorkerRegistration.updateViaCache](/en-US/docs/Web/API/ServiceWorkerRegistration/updateViaCache)Read only

Returns the value of the setting used to determine the circumstances in which the browser will consult the HTTP cache when it tries to update the service worker or any scripts that are imported via [importScripts()](/en-US/docs/Web/API/WorkerGlobalScope/importScripts). It can be one of the following: `imports`, `all`, or `none`.

[ServiceWorkerRegistration.waiting](/en-US/docs/Web/API/ServiceWorkerRegistration/waiting)Read only

Returns a service worker whose state is `installed`. This is initially set to `null`.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface,[EventTarget](/en-US/docs/Web/API/EventTarget).

[ServiceWorkerRegistration.getNotifications()](/en-US/docs/Web/API/ServiceWorkerRegistration/getNotifications)

Returns a list of the notifications in the order that they were created from the current origin via the current service worker registration.

[ServiceWorkerRegistration.showNotification()](/en-US/docs/Web/API/ServiceWorkerRegistration/showNotification)

Displays the notification with the requested title.

[ServiceWorkerRegistration.unregister()](/en-US/docs/Web/API/ServiceWorkerRegistration/unregister)

Unregisters the service worker registration and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise). The service worker will finish any ongoing operations before it is unregistered.

[ServiceWorkerRegistration.update()](/en-US/docs/Web/API/ServiceWorkerRegistration/update)

Checks the server for an updated version of the service worker without consulting caches.

## [Events](#events)

[updatefound](/en-US/docs/Web/API/ServiceWorkerRegistration/updatefound_event)

Fired any time the [ServiceWorkerRegistration.installing](/en-US/docs/Web/API/ServiceWorkerRegistration/installing) property acquires a new service worker.

## [Examples](#examples)

In this example, the code first checks whether the browser supports service workers and if so registers one. Next, it adds an `updatefound` listener in which it uses the service worker registration to listen for further changes to the service worker's state. If the service worker hasn't changed since the last time it was registered, then the `updatefound` event will not be fired.

js

```
if ("serviceWorker" in navigator) {
  navigator.serviceWorker
    .register("/sw.js")
    .then((registration) => {
      registration.addEventListener("updatefound", () => {
        // If updatefound is fired, it means that there's
        // a new service worker being installed.
        const installingWorker = registration.installing;
        console.log(
          "A new service worker is being installed:",
          installingWorker,
        );

        // You can listen for changes to the installing service worker's
        // state via installingWorker.onstatechange
      });
    })
    .catch((error) => {
      console.error(`Service worker registration failed: ${error}`);
    });
} else {
  console.error("Service workers are not supported.");
}
```

## [Specifications](#specifications)

Specification
[Service Workers Nightly# serviceworkerregistration-interface](https://w3c.github.io/ServiceWorker/#serviceworkerregistration-interface)
[Push API# extensions-to-the-serviceworkerregistration-interface](https://w3c.github.io/push-api/#extensions-to-the-serviceworkerregistration-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using Service Workers](/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)
- [Service workers basic code example](https://github.com/mdn/dom-examples/tree/main/service-worker/simple-service-worker)
- [Using web workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ServiceWorkerRegistration/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/serviceworkerregistration/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FServiceWorkerRegistration&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fserviceworkerregistration%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FServiceWorkerRegistration%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fserviceworkerregistration%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F828ae6eee278f30c3fa3677a74915d28d9e338b2%0A*+Document+last+modified%3A+2025-05-30T03%3A30%3A21.000Z%0A%0A%3C%2Fdetails%3E)
