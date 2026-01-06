# PushEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushEvent&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `PushEvent` interface of the [Push API](/en-US/docs/Web/API/Push_API) represents a push message that has been received. This event is sent to the [global scope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) of a [ServiceWorker](/en-US/docs/Web/API/ServiceWorker). It contains the information sent from an application server to a [PushSubscription](/en-US/docs/Web/API/PushSubscription).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[PushEvent()](/en-US/docs/Web/API/PushEvent/PushEvent)

Creates a new `PushEvent` object.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent). Additional properties:

[PushEvent.data](/en-US/docs/Web/API/PushEvent/data)Read only

Returns a reference to a [PushMessageData](/en-US/docs/Web/API/PushMessageData) object containing data sent to the [PushSubscription](/en-US/docs/Web/API/PushSubscription).

## [Instance methods](#instance_methods)

Inherits methods from its parent, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

## [Examples](#examples)

The following example takes data from a `PushEvent` and displays it on all of the service worker's clients.

js

```
self.addEventListener("push", (event) => {
  if (!(self.Notification && self.Notification.permission === "granted")) {
    return;
  }

  const data = event.data?.json() ?? {};
  const title = data.title || "Something Has Happened";
  const message =
    data.message || "Here's something you might want to check out.";
  const icon = "images/new-notification.png";

  const notification = new self.Notification(title, {
    body: message,
    tag: "simple-push-demo-notification",
    icon,
  });

  notification.addEventListener("click", () => {
    clients.openWindow(
      "https://example.blog.com/2015/03/04/something-new.html",
    );
  });
});
```

## [Specifications](#specifications)

Specification
[Push API# pushevent-interface](https://w3c.github.io/push-api/#pushevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Push API](/en-US/docs/Web/API/Push_API)
- [Service Worker API](/en-US/docs/Web/API/Service_Worker_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 22, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PushEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/pushevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpushevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpushevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3a91caa0ebbc5131ed75afe0e5168cd5bffc0976%0A*+Document+last+modified%3A+2024-04-22T08%3A12%3A36.000Z%0A%0A%3C%2Fdetails%3E)
