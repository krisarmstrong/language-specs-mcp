# PushSubscriptionOptions

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushSubscriptionOptions&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `PushSubscriptionOptions` interface of the [Push API](/en-US/docs/Web/API/Push_API) represents the options associated with a push subscription.

The read-only `PushSubscriptionOptions` object is returned by calling [PushSubscription.options](/en-US/docs/Web/API/PushSubscription/options) on a [PushSubscription](/en-US/docs/Web/API/PushSubscription). This interface has no constructor of its own.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[PushSubscriptionOptions.userVisibleOnly](/en-US/docs/Web/API/PushSubscriptionOptions/userVisibleOnly)Read only

A boolean value indicating that the returned push subscription will only be used for messages whose effect is made visible to the user.

[PushSubscriptionOptions.applicationServerKey](/en-US/docs/Web/API/PushSubscriptionOptions/applicationServerKey)Read only

A public key your push server will use to send messages to client apps via a push server.

## [Examples](#examples)

Calling [PushSubscription.options](/en-US/docs/Web/API/PushSubscription/options) on a [PushSubscription](/en-US/docs/Web/API/PushSubscription) returns a `PushSubscriptionOptions` object. In the example below this is printed to the console.

js

```
navigator.serviceWorker.ready.then((reg) => {
  reg.pushManager.getSubscription().then((subscription) => {
    const options = subscription.options;
    console.log(options); // a PushSubscriptionOptions object
  });
});
```

## [Specifications](#specifications)

Specification
[Push API# dom-pushsubscriptionoptions](https://w3c.github.io/push-api/#dom-pushsubscriptionoptions)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 6, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PushSubscriptionOptions/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/pushsubscriptionoptions/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushSubscriptionOptions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpushsubscriptionoptions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPushSubscriptionOptions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpushsubscriptionoptions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F11f58a4cd8758f89056900a6fb7c21e2d42fa6f1%0A*+Document+last+modified%3A+2024-08-06T16%3A16%3A02.000Z%0A%0A%3C%2Fdetails%3E)
