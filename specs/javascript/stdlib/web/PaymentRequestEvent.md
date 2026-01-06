# PaymentRequestEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaymentRequestEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `PaymentRequestEvent` interface of the [Payment Handler API](/en-US/docs/Web/API/Payment_Handler_API) is the object passed to a payment handler when a [PaymentRequest](/en-US/docs/Web/API/PaymentRequest) is made.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[PaymentRequestEvent()](/en-US/docs/Web/API/PaymentRequestEvent/PaymentRequestEvent)Experimental

Creates a new `PaymentRequestEvent` object instance.

## [Instance properties](#instance_properties)

[methodData](/en-US/docs/Web/API/PaymentRequestEvent/methodData)Read onlyExperimental

Returns an array of objects containing payment method identifiers for the payment methods that the website accepts and any associated payment method specific data.

[modifiers](/en-US/docs/Web/API/PaymentRequestEvent/modifiers)Read onlyExperimental

Returns an array of objects containing changes to payment details.

[paymentRequestId](/en-US/docs/Web/API/PaymentRequestEvent/paymentRequestId)Read onlyExperimental

Returns the ID of the [PaymentRequest](/en-US/docs/Web/API/PaymentRequest) object.

[paymentRequestOrigin](/en-US/docs/Web/API/PaymentRequestEvent/paymentRequestOrigin)Read onlyExperimental

Returns the origin where the [PaymentRequest](/en-US/docs/Web/API/PaymentRequest) object was initialized.

[topOrigin](/en-US/docs/Web/API/PaymentRequestEvent/topOrigin)Read onlyExperimental

Returns the top-level origin where the [PaymentRequest](/en-US/docs/Web/API/PaymentRequest) object was initialized.

[total](/en-US/docs/Web/API/PaymentRequestEvent/total)Read onlyExperimental

Returns the total amount being requested for payment.

## [Instance methods](#instance_methods)

[changePaymentMethod()](/en-US/docs/Web/API/PaymentRequestEvent/changePaymentMethod)Experimental

Gets an updated total, given payment method details.

[openWindow()](/en-US/docs/Web/API/PaymentRequestEvent/openWindow)Experimental

Opens the specified URL in a new window, if and only if the given URL is on the same origin as the calling page. It returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a reference to a [WindowClient](/en-US/docs/Web/API/WindowClient).

[respondWith()](/en-US/docs/Web/API/PaymentRequestEvent/respondWith)Experimental

Prevents the default event handling and allows you to provide a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) for a [PaymentResponse](/en-US/docs/Web/API/PaymentResponse) object yourself.

## [Examples](#examples)

When the [PaymentRequest.show()](/en-US/docs/Web/API/PaymentRequest/show) method is invoked, a [paymentrequest](/en-US/docs/Web/API/ServiceWorkerGlobalScope/paymentrequest_event) event is fired on the service worker of the payment app. This event is listened for inside the payment app's service worker to begin the next stage of the payment process.

js

```
let paymentRequestEvent;
let resolver;
let client;

// `self` is the global object in service worker
self.addEventListener("paymentrequest", async (e) => {
  if (paymentRequestEvent) {
    // If there's an ongoing payment transaction, reject it.
    resolver.reject();
  }
  // Preserve the event for future use
  paymentRequestEvent = e;

  // …
});
```

When a `paymentrequest` event is received, the payment app can open a payment handler window by calling [PaymentRequestEvent.openWindow()](/en-US/docs/Web/API/PaymentRequestEvent/openWindow). The payment handler window will present the customers with a payment app interface where they can authenticate, choose shipping address and options, and authorize the payment.

When the payment has been handled, [PaymentRequestEvent.respondWith()](/en-US/docs/Web/API/PaymentRequestEvent/respondWith) is used to pass the payment result back to the merchant website.

See [Receive a payment request event from the merchant](https://web.dev/articles/orchestrating-payment-transactions#receive-payment-request-event) for more details of this stage.

## [Specifications](#specifications)

Specification
[Payment Handler API# the-paymentrequestevent](https://w3c.github.io/payment-handler/#the-paymentrequestevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web-based payment apps overview](https://web.dev/articles/web-based-payment-apps-overview)
- [Setting up a payment method](https://web.dev/articles/setting-up-a-payment-method)
- [Life of a payment transaction](https://web.dev/articles/life-of-a-payment-transaction)
- [Using the Payment Request API](/en-US/docs/Web/API/Payment_Request_API/Using_the_Payment_Request_API)
- [Payment processing concepts](/en-US/docs/Web/API/Payment_Request_API/Concepts)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PaymentRequestEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/paymentrequestevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaymentRequestEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpaymentrequestevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaymentRequestEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpaymentrequestevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff336c5b6795a562c64fe859aa9ee2becf223ad8a%0A*+Document+last+modified%3A+2025-11-03T18%3A29%3A25.000Z%0A%0A%3C%2Fdetails%3E)
