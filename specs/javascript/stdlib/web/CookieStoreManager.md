# CookieStoreManager

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCookieStoreManager&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `CookieStoreManager` interface of the [Cookie Store API](/en-US/docs/Web/API/Cookie_Store_API) allows service workers to subscribe to cookie change events. Call [subscribe()](/en-US/docs/Web/API/CookieStoreManager/subscribe) on a particular service worker registration to receive change events.

A `CookieStoreManager` has an associated [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration). Each service worker registration has a cookie change subscription list, which is a list of cookie change subscriptions each containing a name and URL. The methods in this interface allow the service worker to add and remove subscriptions from this list, and to get a list of all subscriptions.

To get a `CookieStoreManager`, call [ServiceWorkerRegistration.cookies](/en-US/docs/Web/API/ServiceWorkerRegistration/cookies).

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance methods](#instance_methods)

[CookieStoreManager.getSubscriptions()](/en-US/docs/Web/API/CookieStoreManager/getSubscriptions)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves to a list of the cookie change subscriptions for this service worker registration.

[CookieStoreManager.subscribe()](/en-US/docs/Web/API/CookieStoreManager/subscribe)

Subscribes to changes to cookies. It returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves when the subscription is successful.

[CookieStoreManager.unsubscribe()](/en-US/docs/Web/API/CookieStoreManager/unsubscribe)

Unsubscribes the registered service worker from changes to cookies. It returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves when the operation is successful.

## [Examples](#examples)

In this example, the [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration) represented by `registration` is subscribing to change events on the cookie named `"cookie1"` with a scope of `"/path1"`.

js

```
const subscriptions = [{ name: "cookie1", url: `/path1` }];
await registration.cookies.subscribe(subscriptions);
```

If the [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration) has subscribed to any cookies, then [getSubscriptions()](/en-US/docs/Web/API/CookieStoreManager/getSubscriptions) will return a list of cookies represented by objects in the same format as used for the original subscription.

js

```
const subscriptions = await self.registration.cookies.getSubscriptions();
```

## [Specifications](#specifications)

Specification
[Cookie Store API# cookiestoremanager](https://cookiestore.spec.whatwg.org/#cookiestoremanager)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 22, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/CookieStoreManager/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cookiestoremanager/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCookieStoreManager&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcookiestoremanager%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCookieStoreManager%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcookiestoremanager%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F60c3843f55839380e0c0cdc293ea694fe9943158%0A*+Document+last+modified%3A+2024-04-22T08%3A39%3A40.000Z%0A%0A%3C%2Fdetails%3E)
