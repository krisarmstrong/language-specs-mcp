# SecurePaymentConfirmationRequest

The `SecurePaymentConfirmationRequest` dictionary describes input to the [Payment Request API](/en-US/docs/Web/API/Payment_Request_API) when used to authenticate a user during an e-commerce transaction [using SPC with Payment Request API](/en-US/docs/Web/API/Payment_Request_API/Using_secure_payment_confirmation).

An instance of this dictionary must be passed into the [PaymentRequest()](/en-US/docs/Web/API/PaymentRequest/PaymentRequest) constructor as the value of the [data](/en-US/docs/Web/API/PaymentRequest/PaymentRequest#data) field corresponding to a [supportedMethods](/en-US/docs/Web/API/PaymentRequest/PaymentRequest#supportedmethods) value of `"secure-payment-confirmation"`.

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)

## [Instance properties](#instance_properties)

[challenge](#challenge)

An [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray), or [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) provided by the relying party's server and used as a [cryptographic challenge](https://en.wikipedia.org/wiki/Challenge%E2%80%93response_authentication). This value will be signed by the authenticator and the signature will be sent back as part of [AuthenticatorAttestationResponse.attestationObject](/en-US/docs/Web/API/AuthenticatorAttestationResponse/attestationObject). This helps prevent replay attacks.

[credentialIds](#credentialids)

A list of [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray), or [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView). These [Credential IDs](https://w3c.github.io/webauthn/#credential-id) represent Web Authentication credentials that have been registered with the relying party for authenticating during a payment with the associated `instrument`.

[extensions Optional](#extensions)

Any [WebAuthn extensions](/en-US/docs/Web/API/Web_Authentication_API/WebAuthn_extensions) that should be used for the passed credential(s). The caller does not need to specify the [payment extension](/en-US/docs/Web/API/Web_Authentication_API/WebAuthn_extensions#payment); this is added automatically.

[instrument](#instrument)

The description of the instrument name and icon to display during registration and to be signed along with the transaction details. This is an object with the following properties:

[displayName](#displayname)

A string containing the payment instrument's name, which will be displayed to the user.

[icon](#icon)

A string containing the URL of the payment instrument's icon.

[iconMustBeShown Optional](#iconmustbeshown)

A boolean value indicating whether the icon must be successfully fetched and shown for the request to succeed. Defaults to `true`.

[locale Optional](#locale)

An optional list of well-formed [BCP 47 language tags](/en-US/docs/Glossary/BCP_47_language_tag), in descending order of priority, that identify the local preferences of the website. That is, this represents a language priority list [RFC 4647: Matching of Language Tags](https://datatracker.ietf.org/doc/html/rfc4647), which the user agent can use to perform [language negotiation](/en-US/docs/Web/HTTP/Guides/Content_negotiation) and locale-affected formatting with the caller.

Note: The locale is distinct from language or direction metadata associated with specific input members, in that it represents the caller's requested localized experience rather than assertion about a specific string value. See [SPC internationalization Considerations](https://w3c.github.io/secure-payment-confirmation/#sctn-i18n-considerations) for more discussion.

[payeeName Optional](#payeename)

A string that serves as the display name of the payee that this SPC call is for (e.g., the merchant). Optional, may be provided alongside or instead of `payeeOrigin`.

[payeeOrigin Optional](#payeeorigin)

A string that is the origin of the payee that this SPC call is for (e.g., the merchant). Optional, may be provided alongside or instead of `payeeName`.

[rpId](#rpid)

A string that specifies the relying party's identifier (for example "login.example.org").

[showOptOut Optional](#showoptout)

A boolean indicating whether the user should be given a chance to opt-out during the [transaction dialog UX](/en-US/docs/Web/API/Payment_Request_API/Using_secure_payment_confirmation#authenticating_a_payment). Defaults to `false`.

[timeout Optional](#timeout)

The number of milliseconds before the request to sign the transaction details times out. At most 1 hour.

## [Specifications](#specifications)

Specification
[Secure Payment Confirmation# sctn-securepaymentconfirmationrequest-dictionary](https://w3c.github.io/secure-payment-confirmation/#sctn-securepaymentconfirmationrequest-dictionary)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SecurePaymentConfirmationRequest/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/securepaymentconfirmationrequest/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSecurePaymentConfirmationRequest&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsecurepaymentconfirmationrequest%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSecurePaymentConfirmationRequest%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsecurepaymentconfirmationrequest%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe7bc0ed5466f5834641d75d416fa81886cf6b37e%0A*+Document+last+modified%3A+2025-09-24T12%3A28%3A15.000Z%0A%0A%3C%2Fdetails%3E)
