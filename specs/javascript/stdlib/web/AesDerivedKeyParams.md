# AesDerivedKeyParams

The `AesDerivedKeyParams` dictionary of the [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API) represents the object that should be passed as the `derivedKeyType` parameter into [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey), when deriving an AES key: that is, when the algorithm is identified as any of [AES-CBC](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-cbc), [AES-CTR](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-ctr), [AES-GCM](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-gcm), or [AES-KW](/en-US/docs/Web/API/SubtleCrypto/wrapKey#aes-kw).

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[name](#name)

A string. This should be set to `AES-CBC`, `AES-CTR`, `AES-GCM`, or `AES-KW`, depending on the algorithm you want to use.

[length](#length)

A `Number` — the length in bits of the key to generate. This must be one of: 128, 192, or 256.

## [Examples](#examples)

See the examples for [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey).

## [Specifications](#specifications)

Specification
[Web Cryptography Level 2# dfn-AesDerivedKeyParams](https://w3c.github.io/webcrypto/#dfn-AesDerivedKeyParams)

## [Browser compatibility](#browser_compatibility)

Browsers that support any of the AES-based algorithms for the [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey) method will support this type.

## [See also](#see_also)

- [SubtleCrypto.generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AesDerivedKeyParams/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/aesderivedkeyparams/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAesDerivedKeyParams&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faesderivedkeyparams%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAesDerivedKeyParams%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faesderivedkeyparams%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F63774786a6abccda8e70ad62429aa39571aba878%0A*+Document+last+modified%3A+2025-09-17T00%3A31%3A06.000Z%0A%0A%3C%2Fdetails%3E)
