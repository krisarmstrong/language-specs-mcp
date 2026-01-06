# Private State Token API

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Private State Token API provides a mechanism for conveying trust in a user's authenticity from one browsing context to another, without sharing the user's identity or allowing their activity across websites to be tracked.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [HTML elements](#html_elements)
- [HTTP headers](#http_headers)
- [Security considerations](#security_considerations)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Concepts and usage](#concepts_and_usage)

To prevent fraud on the web, websites and services need to establish and convey trust signals that prove a user is who they say they are, and is not a bot pretending to be a human or a malicious third party defrauding a real person or service.

- Trust is established using mechanisms such as [CAPTCHAs](https://en.wikipedia.org/wiki/CAPTCHA), verifying email addresses, or making purchases.
- Trust is traditionally conveyed between different origins using mechanisms such as [third-party cookies](/en-US/docs/Web/Privacy/Guides/Third-party_cookies).

Unfortunately, current cookie-based techniques for conveying such information are not secure and can be used for [fingerprinting](/en-US/docs/Glossary/Fingerprinting) and tracking users, which is problematic for user privacy.

Private state tokens solve this problem, allowing trust signals to be conveyed across origins without passive tracking using the [Privacy Pass protocol](https://privacypass.github.io/) in the background.

Note: Private state tokens are not a replacement for CAPTCHAs or other trust-establishing mechanisms. Private state tokens provide a way to convey trust in a user, not establish trust in a user.

### [How do private state tokens work?](#how_do_private_state_tokens_work)

1. When a website has established trust in a user (for example via a CAPTCHA), it can issue a cryptographic token that is stored securely by the user's browser. This website is called an issuer.
2. Another website can then verify that the same user is trustworthy by checking if their browser has a token stored that was issued by an issuer that the website trusts. If so, they can redeem that token to get a redemption record. This website is called a redeemer.
3. The redemption record is then used to give the user access to services as if they were authenticated directly with that site, and can also be forwarded onto other parties to convey trust.

Private state tokens are encrypted, so it isn't possible to identify an individual or connect trusted and untrusted instances to discover user identity.

See [Using the Private State Token API](/en-US/docs/Web/API/Private_State_Token_API/Using) for a guide to using private state tokens.

## [Interfaces](#interfaces)

The Private State Token API has no distinct interfaces of its own.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Document.hasPrivateToken()](/en-US/docs/Web/API/Document/hasPrivateToken)

Returns a promise that fulfills with a boolean indicating whether the browser has a private state token stored from a particular issuer.

[Document.hasRedemptionRecord()](/en-US/docs/Web/API/Document/hasRedemptionRecord)

Returns a promise that fulfills with a boolean indicating whether the browser has a redemption record originating from a particular issuer.

[HTMLIFrameElement.privateToken](/en-US/docs/Web/API/HTMLIFrameElement/privateToken)

Mirrors the value of the `<iframe>``privateToken` attribute.

[fetch()](/en-US/docs/Web/API/Window/fetch) / [Request()](/en-US/docs/Web/API/Request/Request), the [privateToken](/en-US/docs/Web/API/RequestInit#privatetoken) option

An object representing a private state token operation. Fetch calls with the `privateToken` option specified initiate operations such as issuing or redeeming tokens.

[XMLHttpRequest.setPrivateToken()](/en-US/docs/Web/API/XMLHttpRequest/setPrivateToken)

Adds private state token information to an `XMLHttpRequest` call, to initiate private state token operations.

## [HTML elements](#html_elements)

[<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe), the [privateToken](/en-US/docs/Web/HTML/Reference/Elements/iframe#privatetoken) attribute

Contains a string representation of an options object representing a private state token operation. IFrames containing this attribute can be used to initiate operations such as issuing or redeeming tokens.

## [HTTP headers](#http_headers)

[Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy); the [private-state-token-issuance](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/private-state-token-issuance) directive

Controls usage of `token-request` operations.

[Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy); the [private-state-token-redemption](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/private-state-token-redemption) directive

Controls usage of `token-redemption` and `send-redemption-record` operations.

[Sec-Redemption-Record](/en-US/docs/Web/HTTP/Reference/Headers/Sec-Redemption-Record)

A request header that forwards a redemption record to another party to convey trust when a `send-redemption-record` fetch request is made.

[Sec-Private-State-Token](/en-US/docs/Web/HTTP/Reference/Headers/Sec-Private-State-Token)

Exists both as a request and a response header, used during issuance and redemption requests to transmit request data (such as blinded nonces used to generate tokens) and response data (such as tokens and redemption records).

[Sec-Private-State-Token-Crypto-Version](/en-US/docs/Web/HTTP/Reference/Headers/Sec-Private-State-Token-Crypto-Version)

A request header sent to an issuer server that states which cryptographic protocol version should be used to sign blinded nonces when generating tokens.

[Sec-Private-State-Token-Lifetime](/en-US/docs/Web/HTTP/Reference/Headers/Sec-Private-State-Token-Lifetime)

A response header, sent by the redeemer server, to indicate to the browser how long it should cache a particular redemption record for.

## [Security considerations](#security_considerations)

Private state token `token-request` operations are controlled by the [private-state-token-issuance](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/private-state-token-issuance)[Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy) directive, whereas `token-redemption` and `send-redemption-record` operations are controlled by the [private-state-token-redemption](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/private-state-token-redemption) directive.

Specifically, where a defined policy blocks usage, any attempts to initiate private state token operations via fetch requests will fail.

## [Examples](#examples)

See the [Private State Token Demo Issuer](https://privatetokens.dev/) for an example implementation.

## [Specifications](#specifications)

Specification[Private State Token API](https://wicg.github.io/trust-token-api/)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 16, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Private_State_Token_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/private_state_token_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPrivate_State_Token_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fprivate_state_token_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPrivate_State_Token_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fprivate_state_token_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff6e66d18205c93fcaeb2ea9ad51541b5b4d7d2b1%0A*+Document+last+modified%3A+2025-12-16T10%3A03%3A04.000Z%0A%0A%3C%2Fdetails%3E)
