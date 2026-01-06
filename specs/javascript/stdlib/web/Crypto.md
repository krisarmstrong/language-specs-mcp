# Crypto

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCrypto&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `Crypto` interface represents basic cryptography features available in the current context. It allows access to a cryptographically strong random number generator and to cryptographic primitives.

The `Crypto` is available in windows using the [Window.crypto](/en-US/docs/Web/API/Window/crypto) property and in workers using the [WorkerGlobalScope.crypto](/en-US/docs/Web/API/WorkerGlobalScope/crypto) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[Crypto.subtle](/en-US/docs/Web/API/Crypto/subtle)Read onlySecure context

Returns a [SubtleCrypto](/en-US/docs/Web/API/SubtleCrypto) object providing access to common cryptographic primitives, like hashing, signing, encryption, or decryption.

## [Instance methods](#instance_methods)

[Crypto.getRandomValues()](/en-US/docs/Web/API/Crypto/getRandomValues)

Fills the passed [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray) with cryptographically sound random values.

[Crypto.randomUUID()](/en-US/docs/Web/API/Crypto/randomUUID)Secure context

Returns a randomly generated, 36 character long v4 UUID.

## [Specifications](#specifications)

Specification
[Web Cryptography Level 2# crypto-interface](https://w3c.github.io/webcrypto/#crypto-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web security](/en-US/docs/Web/Security)
- [Secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts)
- [Features restricted to secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts/features_restricted_to_secure_contexts)
- [Transport Layer Security](/en-US/docs/Web/Security/Defenses/Transport_Layer_Security)
- [Strict-Transport-Security](/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Crypto/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/crypto/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCrypto&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcrypto%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCrypto%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcrypto%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
