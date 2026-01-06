# ExtendableCookieChangeEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FExtendableCookieChangeEvent&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `ExtendableCookieChangeEvent` interface of the [Cookie Store API](/en-US/docs/Web/API/Cookie_Store_API) is the event type passed to [cookiechange](/en-US/docs/Web/API/ServiceWorkerGlobalScope/cookiechange_event) event fired at the [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) when any cookie changes occur which match the service worker's cookie change subscription list. A cookie change event consists of a cookie and a type (either "changed" or "deleted").

Cookie changes that cause the `ExtendableCookieChangeEvent` to be dispatched are:

- A cookie is newly created and not immediately removed, or if a cookies is replaced. In this case `type` is "changed".
- A cookie is newly created and immediately removed. In this case `type` is "deleted"
- A cookie is removed. In this case `type` is "deleted".

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[ExtendableCookieChangeEvent()](/en-US/docs/Web/API/ExtendableCookieChangeEvent/ExtendableCookieChangeEvent)

Creates a new `ExtendableCookieChangeEvent`.

## [Instance properties](#instance_properties)

This interface also inherits properties from [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

[ExtendableCookieChangeEvent.changed](/en-US/docs/Web/API/ExtendableCookieChangeEvent/changed)Read only

Returns an array containing the changed cookies.

[ExtendableCookieChangeEvent.deleted](/en-US/docs/Web/API/ExtendableCookieChangeEvent/deleted)Read only

Returns an array containing the deleted cookies.

## [Instance methods](#instance_methods)

This interface also inherits methods from [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

## [Examples](#examples)

In the below example, we use [CookieStoreManager.getSubscriptions()](/en-US/docs/Web/API/CookieStoreManager/getSubscriptions) to get a list of existing subscriptions. (In service workers, a subscription is required in order to listen for events.) We unsubscribe from existing subscriptions using [CookieStoreManager.unsubscribe()](/en-US/docs/Web/API/CookieStoreManager/unsubscribe), then subscribe to the cookie with a name of 'COOKIE_NAME' using [CookieStoreManager.subscribe()](/en-US/docs/Web/API/CookieStoreManager/subscribe). If that cookie is changed, the event listener logs the event to the console. This will be an `ExtendableCookieChangeEvent` object, with the [changed](/en-US/docs/Web/API/ExtendableCookieChangeEvent/changed) or [deleted](/en-US/docs/Web/API/ExtendableCookieChangeEvent/deleted) property containing the modified cookie.

js

```
self.addEventListener("activate", (event) => {
  event.waitUntil(async () => {
    const subscriptions = await self.registration.cookies.getSubscriptions();

    await self.registration.cookies.unsubscribe(subscriptions);

    await self.registration.cookies.subscribe([
      {
        name: "COOKIE_NAME",
      },
    ]);
  });
});

self.addEventListener("cookiechange", (event) => {
  console.log(event);
});
```

## [Specifications](#specifications)

Specification
[Cookie Store API# ExtendableCookieChangeEvent](https://cookiestore.spec.whatwg.org/#ExtendableCookieChangeEvent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ExtendableCookieChangeEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/extendablecookiechangeevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FExtendableCookieChangeEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fextendablecookiechangeevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FExtendableCookieChangeEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fextendablecookiechangeevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F335a6f38068e697c64009243648c75fb97650402%0A*+Document+last+modified%3A+2025-06-10T08%3A16%3A05.000Z%0A%0A%3C%2Fdetails%3E)
