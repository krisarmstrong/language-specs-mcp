# Notifications API

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Notifications API allows web pages to control the display of system notifications to the end user. These are outside the top-level browsing context viewport, so therefore can be displayed even when the user has switched tabs or moved to a different app. The API is designed to be compatible with existing notification systems, across different platforms.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

On supported platforms, showing a system notification generally involves two things. First, the user needs to grant the current origin permission to display system notifications, which is generally done when the app or site initializes, using the [Notification.requestPermission()](/en-US/docs/Web/API/Notification/requestPermission_static) method. This method should only be called when handling a user gesture, such as when handling a mouse click. For example:

js

```
btn.addEventListener("click", () => {
  let promise = Notification.requestPermission();
  // wait for permission
});
```

This will spawn a request dialog, along the following lines:

From here the user can choose to allow notifications from this origin, or block them. Once a choice has been made, the setting will generally persist for the current session.

Next, a new notification is created using the [Notification()](/en-US/docs/Web/API/Notification/Notification) constructor. This must be passed a title argument, and can optionally be passed an options object to specify options, such as text direction, body text, icon to display, notification sound to play, and more.

In addition, the Notifications API spec specifies a number of additions to the [ServiceWorker API](/en-US/docs/Web/API/Service_Worker_API), to allow service workers to fire notifications.

Note: To find out more about using notifications in your own app, read [Using the Notifications API](/en-US/docs/Web/API/Notifications_API/Using_the_Notifications_API).

## [Interfaces](#interfaces)

[Notification](/en-US/docs/Web/API/Notification)

Defines a notification object.

[NotificationEvent](/en-US/docs/Web/API/NotificationEvent)

Represents a notification event dispatched on the [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) of a [ServiceWorker](/en-US/docs/Web/API/ServiceWorker).

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[notificationclick](/en-US/docs/Web/API/ServiceWorkerGlobalScope/notificationclick_event) event

Occurs when a user clicks on a displayed notification.

[notificationclose](/en-US/docs/Web/API/ServiceWorkerGlobalScope/notificationclose_event) event

Occurs when a user closes a displayed notification.

[ServiceWorkerRegistration.getNotifications()](/en-US/docs/Web/API/ServiceWorkerRegistration/getNotifications)

Returns a list of the notifications in the order that they were created from the current origin via the current service worker registration.

[ServiceWorkerRegistration.showNotification()](/en-US/docs/Web/API/ServiceWorkerRegistration/showNotification)

Displays the notification with the requested title.

## [Specifications](#specifications)

Specification[Notifications API](https://notifications.spec.whatwg.org/)

## [Browser compatibility](#browser_compatibility)

### [api.Notification](#api.Notification)

### [api.ServiceWorkerRegistration.showNotification](#api.ServiceWorkerRegistration.showNotification)

### [api.ServiceWorkerRegistration.getNotifications](#api.ServiceWorkerRegistration.getNotifications)

## [See also](#see_also)

- [Using the Notifications API](/en-US/docs/Web/API/Notifications_API/Using_the_Notifications_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Notifications_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/notifications_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNotifications_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnotifications_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNotifications_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnotifications_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Faa8fa82a902746b0bd97839180fc2b5397088140%0A*+Document+last+modified%3A+2024-07-26T02%3A56%3A16.000Z%0A%0A%3C%2Fdetails%3E)
