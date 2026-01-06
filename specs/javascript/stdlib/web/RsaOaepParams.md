# RsaOaepParams

The `RsaOaepParams` dictionary of the [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API) represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt), [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt), [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey), or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey), when using the [RSA_OAEP](/en-US/docs/Web/API/SubtleCrypto/encrypt#rsa-oaep) algorithm.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[name](#name)

A string. This should be set to `RSA-OAEP`.

[label Optional](#label)

An [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), a [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray), or a [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) — an array of bytes that does not itself need to be encrypted but which should be bound to the ciphertext. A digest of the label is part of the input to the encryption operation.

Unless your application calls for a label, you can just omit this argument and it will not affect the security of the encryption operation.

## [Examples](#examples)

See the examples for [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt) and [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt).

## [Specifications](#specifications)

Specification
[Web Cryptography Level 2# dfn-RsaOaepParams](https://w3c.github.io/webcrypto/#dfn-RsaOaepParams)

## [Browser compatibility](#browser_compatibility)

Browsers that support the "RSA-OAEP" algorithm for the [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt), [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt), [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey), or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey) methods will support this type.

## [See also](#see_also)

- [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt).
- [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt).
- [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey).
- [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RsaOaepParams/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rsaoaepparams/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRsaOaepParams&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frsaoaepparams%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRsaOaepParams%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frsaoaepparams%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
