# NotificationEvent

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNotificationEvent&level=high)

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `NotificationEvent` interface of the [Notifications API](/en-US/docs/Web/API/Notifications_API) represents a notification event dispatched on the [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) of a [ServiceWorker](/en-US/docs/Web/API/ServiceWorker).

This interface inherits from the [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent) interface.

Note: Only persistent notification events, fired at the [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) object, implement the `NotificationEvent` interface. Non-persistent notification events, fired at the [Notification](/en-US/docs/Web/API/Notification) object, implement the `Event` interface.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[NotificationEvent()](/en-US/docs/Web/API/NotificationEvent/NotificationEvent)

Creates a new `NotificationEvent` object.

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

[NotificationEvent.notification](/en-US/docs/Web/API/NotificationEvent/notification)Read only

Returns a [Notification](/en-US/docs/Web/API/Notification) object representing the notification that was clicked to fire the event.

[NotificationEvent.action](/en-US/docs/Web/API/NotificationEvent/action)Read only

Returns the string ID of the notification button the user clicked. This value returns an empty string if the user clicked the notification somewhere other than an action button, or the notification does not have a button.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

## [Example](#example)

js

```
self.addEventListener("notificationclick", (event) => {
  console.log(`On notification click: ${event.notification.tag}`);
  event.notification.close();

  // This looks to see if the current is already open and
  // focuses if it is
  event.waitUntil(
    clients
      .matchAll({
        type: "window",
      })
      .then((clientList) => {
        for (const client of clientList) {
          if (client.url === "/" && "focus" in client) return client.focus();
        }
        if (clients.openWindow) return clients.openWindow("/");
      }),
  );
});
```

## [Specifications](#specifications)

Specification
[Notifications API# notificationevent](https://notifications.spec.whatwg.org/#notificationevent)

Note: This interface is specified in the [Notifications API](/en-US/docs/Web/API/Notifications_API), but accessed through [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope).

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/NotificationEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/notificationevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNotificationEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnotificationevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNotificationEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnotificationevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Faa8fa82a902746b0bd97839180fc2b5397088140%0A*+Document+last+modified%3A+2024-07-26T02%3A56%3A16.000Z%0A%0A%3C%2Fdetails%3E)
