# Notification

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNotification&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `Notification` interface of the [Notifications API](/en-US/docs/Web/API/Notifications_API) is used to configure and display desktop notifications to the user.

These notifications' appearance and specific functionality vary across platforms but generally they provide a way to asynchronously provide information to the user.

## In this article

- [Constructor](#constructor)
- [Static properties](#static_properties)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[Notification()](/en-US/docs/Web/API/Notification/Notification)

Creates a new instance of the `Notification` object.

## [Static properties](#static_properties)

Also inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[Notification.permission](/en-US/docs/Web/API/Notification/permission_static)Read only

A string representing the current permission to display notifications. Possible values are:

- `denied` — The user refuses to have notifications displayed.
- `granted` — The user accepts having notifications displayed.
- `default` — The user choice is unknown and therefore the browser will act as if the value were denied.

[Notification.maxActions](/en-US/docs/Web/API/Notification/maxActions_static)Read onlyExperimental

The maximum number of actions supported by the device and the User Agent.

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[Notification.actions](/en-US/docs/Web/API/Notification/actions)Read onlyExperimental

The actions array of the notification as specified in the constructor's `options` parameter.

[Notification.badge](/en-US/docs/Web/API/Notification/badge)Read only

A string containing the URL of an image to represent the notification when there is not enough space to display the notification itself such as for example, the Android Notification Bar. On Android devices, the badge should accommodate devices up to 4x resolution, about 96 by 96 px, and the image will be automatically masked.

[Notification.body](/en-US/docs/Web/API/Notification/body)Read only

The body string of the notification as specified in the constructor's `options` parameter.

[Notification.data](/en-US/docs/Web/API/Notification/data)Read only

Returns a structured clone of the notification's data.

[Notification.dir](/en-US/docs/Web/API/Notification/dir)Read only

The text direction of the notification as specified in the constructor's `options` parameter.

[Notification.icon](/en-US/docs/Web/API/Notification/icon)Read only

The URL of the image used as an icon of the notification as specified in the constructor's `options` parameter.

[Notification.image](/en-US/docs/Web/API/Notification/image)Read onlyExperimental

The URL of an image to be displayed as part of the notification, as specified in the constructor's `options` parameter.

[Notification.lang](/en-US/docs/Web/API/Notification/lang)Read only

The language code of the notification as specified in the constructor's `options` parameter.

[Notification.renotify](/en-US/docs/Web/API/Notification/renotify)Read onlyExperimental

Specifies whether the user should be notified after a new notification replaces an old one.

[Notification.requireInteraction](/en-US/docs/Web/API/Notification/requireInteraction)Read only

A boolean value indicating that a notification should remain active until the user clicks or dismisses it, rather than closing automatically.

[Notification.silent](/en-US/docs/Web/API/Notification/silent)Read only

Specifies whether the notification should be silent — i.e., no sounds or vibrations should be issued regardless of the device settings.

[Notification.tag](/en-US/docs/Web/API/Notification/tag)Read only

The ID of the notification (if any) as specified in the constructor's `options` parameter.

[Notification.timestamp](/en-US/docs/Web/API/Notification/timestamp)Read onlyExperimental

Specifies the time at which a notification is created or applicable (past, present, or future).

[Notification.title](/en-US/docs/Web/API/Notification/title)Read only

The title of the notification as specified in the first parameter of the constructor.

[Notification.vibrate](/en-US/docs/Web/API/Notification/vibrate)Read onlyExperimental

Specifies a vibration pattern for devices with vibration hardware to emit.

## [Static methods](#static_methods)

Also inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[Notification.requestPermission()](/en-US/docs/Web/API/Notification/requestPermission_static)

Requests permission from the user to display notifications.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[Notification.close()](/en-US/docs/Web/API/Notification/close)

Programmatically closes a notification instance.

## [Events](#events)

Also inherits events from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[click](/en-US/docs/Web/API/Notification/click_event)

Fires when the user clicks the notification.

[close](/en-US/docs/Web/API/Notification/close_event)

Fires when the user closes the notification.

[error](/en-US/docs/Web/API/Notification/error_event)

Fires when the notification encounters an error.

[show](/en-US/docs/Web/API/Notification/show_event)

Fires when the notification is displayed.

## [Examples](#examples)

Assume this basic HTML:

html

```
<button>Notify me!</button>
```

It's possible to send a notification as follows — here we present a fairly verbose and complete set of code you could use if you wanted to first check whether notifications are supported, then check if permission has been granted for the current origin to send notifications, then request permission if required, before then sending a notification.

js

```
document.querySelector("button").addEventListener("click", notifyMe);

function notifyMe() {
  if (!("Notification" in window)) {
    // Check if the browser supports notifications
    alert("This browser does not support desktop notification");
  } else if (Notification.permission === "granted") {
    // Check whether notification permissions have already been granted;
    // if so, create a notification
    const notification = new Notification("Hi there!");
    // …
  } else if (Notification.permission !== "denied") {
    // We need to ask the user for permission
    Notification.requestPermission().then((permission) => {
      // If the user accepts, let's create a notification
      if (permission === "granted") {
        const notification = new Notification("Hi there!");
        // …
      }
    });
  }

  // At last, if the user has denied notifications, and you
  // want to be respectful there is no need to bother them anymore.
}
```

We no longer show a live sample on this page, as Chrome and Firefox no longer allow notification permissions to be requested from cross-origin [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe)s, with other browsers to follow. To see an example in action, check out our [To-do list example](https://github.com/mdn/dom-examples/tree/main/to-do-notifications) (also see [the app running live](https://mdn.github.io/dom-examples/to-do-notifications/)).

Note: In the above example we spawn notifications in response to a user gesture (clicking a button). This is not only best practice — you should not be spamming users with notifications they didn't agree to — but going forward browsers will explicitly disallow notifications not triggered in response to a user gesture. Firefox is already doing this from version 72, for example.

## [Specifications](#specifications)

Specification
[Notifications API# api](https://notifications.spec.whatwg.org/#api)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Notifications API](/en-US/docs/Web/API/Notifications_API/Using_the_Notifications_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Notification/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/notification/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNotification&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnotification%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNotification%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnotification%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
