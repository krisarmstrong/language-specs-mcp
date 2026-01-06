# MerchantValidationEvent

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `MerchantValidationEvent` interface of the [Payment Request API](/en-US/docs/Web/API/Payment_Request_API) enables a merchant to verify themselves as allowed to use a particular payment handler.

Learn more about [merchant validation](/en-US/docs/Web/API/Payment_Request_API/Concepts#merchant_validation).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[MerchantValidationEvent()](/en-US/docs/Web/API/MerchantValidationEvent/MerchantValidationEvent)Deprecated

Creates a new `MerchantValidationEvent` object describing a [merchantvalidation](/en-US/docs/Web/API/PaymentRequest/merchantvalidation_event) event that will be sent to the payment handler to request that it validate the merchant.

## [Instance properties](#instance_properties)

[MerchantValidationEvent.methodName](/en-US/docs/Web/API/MerchantValidationEvent/methodName)Deprecated

A string providing a unique payment method identifier for the payment handler that's requiring validation. This may be either one of the standard payment method identifier strings or a URL that both identifies and handles requests for the payment handler, such as `https://apple.com/apple-pay`.

[MerchantValidationEvent.validationURL](/en-US/docs/Web/API/MerchantValidationEvent/validationURL)Deprecated

A string specifying a URL from which the site or app can fetch payment handler specific validation information. Once this data is retrieved, the data (or a promise resolving to the validation data) should be passed into [complete()](/en-US/docs/Web/API/MerchantValidationEvent/complete) to validate that the payment request is coming from an authorized merchant.

## [Instance methods](#instance_methods)

[MerchantValidationEvent.complete()](/en-US/docs/Web/API/MerchantValidationEvent/complete)Deprecated

Pass the data retrieved from the URL specified by [validationURL](/en-US/docs/Web/API/MerchantValidationEvent/validationURL) into `complete()` to complete the validation process for the [PaymentRequest](/en-US/docs/Web/API/PaymentRequest).

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 26, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/MerchantValidationEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/merchantvalidationevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMerchantValidationEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmerchantvalidationevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMerchantValidationEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmerchantvalidationevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F89c7b111d380e607e94b58abbd0d37951cf395c4%0A*+Document+last+modified%3A+2023-12-26T18%3A54%3A26.000Z%0A%0A%3C%2Fdetails%3E)
