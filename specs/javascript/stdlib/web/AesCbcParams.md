# AesCbcParams

The `AesCbcParams` dictionary of the [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API) represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt), [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt), [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey), or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey), when using the [AES-CBC](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-cbc) algorithm.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[name](#name)

A string. This should be set to `AES-CBC`.

[iv](#iv)

An [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), a [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray), or a [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView). The initialization vector. Must be 16 bytes, unpredictable, and preferably cryptographically random. However, it need not be secret (for example, it may be transmitted unencrypted along with the ciphertext).

## [Examples](#examples)

See the examples for [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt) and [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt).

## [Specifications](#specifications)

Specification
[Web Cryptography Level 2# dfn-AesCbcParams](https://w3c.github.io/webcrypto/#dfn-AesCbcParams)

## [Browser compatibility](#browser_compatibility)

Browsers that support the "AES-CBC" algorithm for the [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt), [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt), [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey), or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey) methods will support this type.

## [See also](#see_also)

- CBC mode is defined in section 6.2 of the [NIST SP800-38A standard](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf#%5B%7B%22num%22%3A70%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22Fit%22%7D%5D).
- [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt).
- [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt).
- [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey).
- [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 18, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/AesCbcParams/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/aescbcparams/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAesCbcParams&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faescbcparams%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAesCbcParams%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faescbcparams%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbca8d1ab2bc4f5a1ef6b39c454b0229539178e98%0A*+Document+last+modified%3A+2023-02-18T07%3A09%3A59.000Z%0A%0A%3C%2Fdetails%3E)
