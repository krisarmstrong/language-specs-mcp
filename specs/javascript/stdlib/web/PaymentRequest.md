# PaymentRequest

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaymentRequest&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The [Payment Request API's](/en-US/docs/Web/API/Payment_Request_API)`PaymentRequest` interface is the primary access point into the API, and lets web content and apps accept payments from the end user on behalf of the operator of the site or the publisher of the app.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[PaymentRequest()](/en-US/docs/Web/API/PaymentRequest/PaymentRequest)

Creates a new `PaymentRequest` object.

## [Instance properties](#instance_properties)

[PaymentRequest.id](/en-US/docs/Web/API/PaymentRequest/id)Read only

A unique identifier for a particular `PaymentRequest`, which can be set via `details.id`. When none is set, it defaults to a UUID.

[PaymentRequest.shippingAddress](/en-US/docs/Web/API/PaymentRequest/shippingAddress)Read onlyDeprecatedNon-standard

If requested via payment options, returns the shipping address chosen by the user for the purposes of calculating shipping. This property is only populated if the constructor is called with the `requestShipping` flag set to true. Additionally, in some browsers, the parts of the address will be redacted for privacy until the user indicates they are ready to complete the transaction (i.e., they hit "Pay").

[PaymentRequest.shippingOption](/en-US/docs/Web/API/PaymentRequest/shippingOption)Read onlyDeprecatedNon-standard

Returns the identifier of the selected shipping option. This property is only populated if the constructor is called with the `requestShipping` flag set to true.

[PaymentRequest.shippingType](/en-US/docs/Web/API/PaymentRequest/shippingType)Read onlyDeprecatedNon-standard

Returns the type of shipping used to fulfill the transaction. This will be one of `shipping`, `delivery`, `pickup`, or `null` if a value was not provided in the constructor.

## [Static methods](#static_methods)

[PaymentRequest.securePaymentConfirmationAvailability()](/en-US/docs/Web/API/PaymentRequest/securePaymentConfirmationAvailability_static)Experimental

Indicates whether the [Secure payment confirmation](/en-US/docs/Web/API/Payment_Request_API/Using_secure_payment_confirmation) feature is available.

## [Instance methods](#instance_methods)

[PaymentRequest.canMakePayment()](/en-US/docs/Web/API/PaymentRequest/canMakePayment)

Indicates whether the `PaymentRequest` object can make a payment before calling `show()`.

[PaymentRequest.show()](/en-US/docs/Web/API/PaymentRequest/show)

Causes the user agent to begin the user interaction for the payment request.

[PaymentRequest.abort()](/en-US/docs/Web/API/PaymentRequest/abort)

Causes the user agent to end the payment request and to remove any user interface that might be shown.

## [Events](#events)

[merchantvalidation](/en-US/docs/Web/API/PaymentRequest/merchantvalidation_event)Deprecated

With some payment handlers (e.g., Apple Pay), this event handler is called to handle the [merchantvalidation](/en-US/docs/Web/API/PaymentRequest/merchantvalidation_event) event, which is dispatched when the user agent requires that the merchant validate that the merchant or vendor requesting payment is legitimate.

[paymentmethodchange](/en-US/docs/Web/API/PaymentRequest/paymentmethodchange_event)

With some payment handlers (e.g., Apple Pay), dispatched whenever the user changes payment instrument, like switching from a credit card to a debit card.

[shippingaddresschange](/en-US/docs/Web/API/PaymentRequest/shippingaddresschange_event)DeprecatedNon-standard

Dispatched whenever the user changes their shipping address.

[shippingoptionchange](/en-US/docs/Web/API/PaymentRequest/shippingoptionchange_event)DeprecatedNon-standard

Dispatched whenever the user changes a shipping option.

## [Specifications](#specifications)

Specification
[Payment Request API# paymentrequest-interface](https://w3c.github.io/payment-request/#paymentrequest-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PaymentRequest/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/paymentrequest/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaymentRequest&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpaymentrequest%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPaymentRequest%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpaymentrequest%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8b10fe925e7bdd362ef4c0b88e305c104befa465%0A*+Document+last+modified%3A+2025-08-27T02%3A12%3A45.000Z%0A%0A%3C%2Fdetails%3E)
