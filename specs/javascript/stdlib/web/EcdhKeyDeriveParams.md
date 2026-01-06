# EcdhKeyDeriveParams

The `EcdhKeyDeriveParams` dictionary of the [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API) represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey) and [SubtleCrypto.deriveBits()](/en-US/docs/Web/API/SubtleCrypto/deriveBits), when using the [ECDH](/en-US/docs/Web/API/SubtleCrypto/deriveKey#ecdh) or [X25519](/en-US/docs/Web/API/SubtleCrypto/deriveKey#x25519) algorithms.

ECDH enables two people who each have a key pair consisting of a public and a private key to derive a shared secret. They exchange public keys and use the combination of their private key and the other entity's public key to derive a secret key that they — and no one else — share.

The parameters for ECDH `deriveKey()` therefore include the other entity's public key, which is combined with this entity's private key to derive the shared secret.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[name](#name)

A string. This should be set to `ECDH` or `X25519`, depending on the algorithm used.

[public](#public)

A [CryptoKey](/en-US/docs/Web/API/CryptoKey) object representing the public key of the other entity.

## [Examples](#examples)

See the examples for [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey) and [SubtleCrypto.deriveBits()](/en-US/docs/Web/API/SubtleCrypto/deriveBits).

## [Specifications](#specifications)

Specification
[Web Cryptography Level 2# dfn-EcdhKeyDeriveParams](https://w3c.github.io/webcrypto/#dfn-EcdhKeyDeriveParams)

## [Browser compatibility](#browser_compatibility)

Browsers that support the "ECDH" or "X25519" algorithm for the [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey) method will support this type.

## [See also](#see_also)

- [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey).
- [SubtleCrypto.deriveBits()](/en-US/docs/Web/API/SubtleCrypto/deriveBits)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 6, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/EcdhKeyDeriveParams/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/ecdhkeyderiveparams/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEcdhKeyDeriveParams&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fecdhkeyderiveparams%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEcdhKeyDeriveParams%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fecdhkeyderiveparams%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F223d903a52fb6a381b7c14f10e956822af38930c%0A*+Document+last+modified%3A+2024-08-06T02%3A48%3A45.000Z%0A%0A%3C%2Fdetails%3E)
