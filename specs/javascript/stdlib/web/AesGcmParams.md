# AesGcmParams

The `AesGcmParams` dictionary of the [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API) represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt), [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt), [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey), or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey), when using the [AES-GCM](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-gcm) algorithm.

For details of how to supply appropriate values for this parameter, see the specification for AES-GCM: [NIST SP800-38D](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf), in particular section 5.2.1.1 on Input Data.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[name](#name)

A string. This should be set to `AES-GCM`.

[iv](#iv)

An [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), a [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray), or a [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) with the initialization vector. This must be unique for every encryption operation carried out with a given key. Put another way: never reuse an IV with the same key. The AES-GCM specification recommends that the IV should be 96 bits long, and typically contains bits from a random number generator. [Section 8.2 of the specification](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf#%5B%7B%22num%22%3A65%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C0%2C792%2Cnull%5D) outlines methods for constructing IVs. Note that the IV does not have to be secret, just unique: so it is OK, for example, to transmit it in the clear alongside the encrypted message.

[additionalData Optional](#additionaldata)

An [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), a [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray), or a [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView). This contains additional data that will not be encrypted but will be authenticated along with the encrypted data. If `additionalData` is given here then the same data must be given in the corresponding call to [decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt): if the data given to the `decrypt()` call does not match the original data, the decryption will throw an exception. This gives you a way to authenticate associated data without having to encrypt it.

The bit length of `additionalData` must be smaller than `2^64 - 1`.

The `additionalData` property is optional and may be omitted without compromising the security of the encryption operation.

[tagLength Optional](#taglength)

A `Number`. This determines the size in bits of the authentication tag generated in the encryption operation and used for authentication in the corresponding decryption.

The [Web Crypto API specification](https://w3c.github.io/webcrypto/#aes-gcm-operations-encrypt) requires this to have one of the following values: 32, 64, 96, 104, 112, 120, or 128. On the other hand, the AES-GCM specification recommends that it should be 96, 104, 112, 120, or 128, although 32 or 64 bits may be acceptable in some applications. For additional guidance, see [Appendix C](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf#%5B%7B%22num%22%3A92%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C0%2C792%2Cnull%5D) of the NIST Publication on "Recommendation for Block Cipher Modes of Operation".

`tagLength` is optional and defaults to 128 if it is not specified.

## [Examples](#examples)

See the examples for [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt) and [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt).

## [Specifications](#specifications)

Specification
[Web Cryptography Level 2# dfn-AesGcmParams](https://w3c.github.io/webcrypto/#dfn-AesGcmParams)

## [Browser compatibility](#browser_compatibility)

Browsers that support the "AES-GCM" algorithm for the [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt), [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt), [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey), or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey) methods will support this type.

## [See also](#see_also)

- [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt).
- [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt).
- [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey).
- [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AesGcmParams/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/aesgcmparams/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAesGcmParams&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faesgcmparams%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAesGcmParams%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faesgcmparams%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
