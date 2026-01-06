# CanMakePaymentEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCanMakePaymentEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `CanMakePaymentEvent` interface of the [Payment Handler API](/en-US/docs/Web/API/Payment_Handler_API) is the event object for the [canmakepayment](/en-US/docs/Web/API/ServiceWorkerGlobalScope/canmakepayment_event) event, fired on a payment app's service worker to check whether it is ready to handle a payment. Specifically, it is fired when the merchant website calls the [PaymentRequest()](/en-US/docs/Web/API/PaymentRequest/PaymentRequest) constructor.

## In this article

- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[CanMakePaymentEvent()](/en-US/docs/Web/API/CanMakePaymentEvent/CanMakePaymentEvent)Experimental

Creates a new `CanMakePaymentEvent` object instance.

## [Instance methods](#instance_methods)

[respondWith()](/en-US/docs/Web/API/CanMakePaymentEvent/respondWith)Experimental

Enables the service worker to respond appropriately to signal whether it is ready to handle payments.

## [Examples](#examples)

js

```
self.addEventListener("canmakepayment", (e) => {
  e.respondWith(
    new Promise((resolve, reject) => {
      someAppSpecificLogic()
        .then((result) => {
          resolve(result);
        })
        .catch((error) => {
          reject(error);
        });
    }),
  );
});
```

## [Specifications](#specifications)

Specification
[Payment Handler API# the-canmakepaymentevent](https://w3c.github.io/payment-handler/#the-canmakepaymentevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Payment Handler API](/en-US/docs/Web/API/Payment_Handler_API)
- [Web-based payment apps overview](https://web.dev/articles/web-based-payment-apps-overview)
- [Setting up a payment method](https://web.dev/articles/setting-up-a-payment-method)
- [Life of a payment transaction](https://web.dev/articles/life-of-a-payment-transaction)
- [Using the Payment Request API](/en-US/docs/Web/API/Payment_Request_API/Using_the_Payment_Request_API)
- [Payment processing concepts](/en-US/docs/Web/API/Payment_Request_API/Concepts)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 25, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/CanMakePaymentEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/canmakepaymentevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCanMakePaymentEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcanmakepaymentevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCanMakePaymentEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcanmakepaymentevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4675b9077ae32f989c7ecac94f454db2653c4fc%0A*+Document+last+modified%3A+2024-07-25T22%3A06%3A52.000Z%0A%0A%3C%2Fdetails%3E)
