# PaymentRequestUpdateEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaymentRequestUpdateEvent&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `PaymentRequestUpdateEvent` interface is used for events sent to a [PaymentRequest](/en-US/docs/Web/API/PaymentRequest) instance when changes are made to shipping-related information for a pending [PaymentRequest](/en-US/docs/Web/API/PaymentRequest). Those events are:

[shippingaddresschange](/en-US/docs/Web/API/PaymentRequest/shippingaddresschange_event)

Dispatched whenever the user changes their shipping address.

[shippingoptionchange](/en-US/docs/Web/API/PaymentRequest/shippingoptionchange_event)

Dispatched whenever the user changes a shipping option.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[PaymentRequestUpdateEvent()](/en-US/docs/Web/API/PaymentRequestUpdateEvent/PaymentRequestUpdateEvent)

Creates a new `PaymentRequestUpdateEvent` object.

## [Instance properties](#instance_properties)

Provides only the properties inherited from its parent interface, [Event](/en-US/docs/Web/API/Event).

## [Instance methods](#instance_methods)

In addition to methods inherited from the parent interface, [Event](/en-US/docs/Web/API/Event), `PaymentRequestUpdateEvent` offers the following methods:

[PaymentRequestUpdateEvent.updateWith()](/en-US/docs/Web/API/PaymentRequestUpdateEvent/updateWith)

If the event handler determines that information included in the payment request needs to be changed, or that new information needs to be added, it calls `updateWith()` with the information that needs to be replaced or added.

## [Specifications](#specifications)

Specification
[Payment Request API# paymentrequestupdateevent-interface](https://w3c.github.io/payment-request/#paymentrequestupdateevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Payment Request API](/en-US/docs/Web/API/Payment_Request_API/Using_the_Payment_Request_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 26, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/PaymentRequestUpdateEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/paymentrequestupdateevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaymentRequestUpdateEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpaymentrequestupdateevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaymentRequestUpdateEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpaymentrequestupdateevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F89c7b111d380e607e94b58abbd0d37951cf395c4%0A*+Document+last+modified%3A+2023-12-26T18%3A54%3A26.000Z%0A%0A%3C%2Fdetails%3E)
