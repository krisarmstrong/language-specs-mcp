# PushManager

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushManager&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `PushManager` interface of the [Push API](/en-US/docs/Web/API/Push_API) provides a way to receive notifications from third-party servers as well as request URLs for push notifications.

This interface is accessed via the [ServiceWorkerRegistration.pushManager](/en-US/docs/Web/API/ServiceWorkerRegistration/pushManager) property.

## In this article

- [Static properties](#static_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Static properties](#static_properties)

[PushManager.supportedContentEncodings](/en-US/docs/Web/API/PushManager/supportedContentEncodings_static)

Returns an array of supported content codings that can be used to encrypt the payload of a push message.

## [Instance methods](#instance_methods)

[PushManager.getSubscription()](/en-US/docs/Web/API/PushManager/getSubscription)

Retrieves an existing push subscription. It returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to a [PushSubscription](/en-US/docs/Web/API/PushSubscription) object containing details of an existing subscription. If no existing subscription exists, this resolves to a `null` value.

[PushManager.permissionState()](/en-US/docs/Web/API/PushManager/permissionState)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to the permission state of the current `PushManager`, which will be one of `'granted'`, `'denied'`, or `'prompt'`.

[PushManager.subscribe()](/en-US/docs/Web/API/PushManager/subscribe)

Subscribes to a push service. It returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to a [PushSubscription](/en-US/docs/Web/API/PushSubscription) object containing details of a push subscription. A new push subscription is created if the current service worker does not have an existing subscription.

### [Deprecated methods](#deprecated_methods)

[PushManager.hasPermission()](/en-US/docs/Web/API/PushManager/hasPermission)DeprecatedNon-standard

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to the `PushPermissionStatus` of the requesting webapp, which will be one of `granted`, `denied`, or `default`. Replaced by [PushManager.permissionState()](/en-US/docs/Web/API/PushManager/permissionState).

[PushManager.register()](/en-US/docs/Web/API/PushManager/register)DeprecatedNon-standard

Subscribes to a push subscription. Replaced by [PushManager.subscribe()](/en-US/docs/Web/API/PushManager/subscribe).

[PushManager.registrations()](/en-US/docs/Web/API/PushManager/registrations)DeprecatedNon-standard

Retrieves existing push subscriptions. Replaced by [PushManager.getSubscription()](/en-US/docs/Web/API/PushManager/getSubscription).

[PushManager.unregister()](/en-US/docs/Web/API/PushManager/unregister)DeprecatedNon-standard

Unregisters and deletes a specified subscription endpoint. In the updated API, a subscription is unregistered by calling the [PushSubscription.unsubscribe()](/en-US/docs/Web/API/PushSubscription/unsubscribe) method.

## [Example](#example)

js

```
this.onpush = (event) => {
  console.log(event.data);
  // From here we can write the data to IndexedDB, send it to any open
  // windows, display a notification, etc.
};

navigator.serviceWorker
  .register("serviceworker.js")
  .then((serviceWorkerRegistration) => {
    serviceWorkerRegistration.pushManager.subscribe().then(
      (pushSubscription) => {
        console.log(pushSubscription.endpoint);
        // The push subscription details needed by the application
        // server are now available, and can be sent to it using,
        // for example, the fetch() API.
      },
      (error) => {
        console.error(error);
      },
    );
  });
```

## [Specifications](#specifications)

Specification
[Push API# pushmanager-interface](https://w3c.github.io/push-api/#pushmanager-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Push API](/en-US/docs/Web/API/Push_API)
- [Service Worker API](/en-US/docs/Web/API/Service_Worker_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PushManager/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/pushmanager/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushManager&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpushmanager%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushManager%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpushmanager%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32305cc3cf274fbfdcc73a296bbd400a26f38296%0A*+Document+last+modified%3A+2024-07-24T20%3A47%3A46.000Z%0A%0A%3C%2Fdetails%3E)
