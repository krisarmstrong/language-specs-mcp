# AesCtrParams

The `AesCtrParams` dictionary of the [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API) represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt), [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt), [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey), or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey), when using the [AES-CTR](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-ctr) algorithm.

AES is a block cipher, meaning that it splits the message into blocks and encrypts it a block at a time. In CTR mode, every time a block of the message is encrypted, an extra block of data is mixed in. This extra block is called the "counter block".

A given counter block value must never be used more than once with the same key:

- Given a message n blocks long, a different counter block must be used for every block.
- If the same key is used to encrypt more than one message, a different counter block must be used for all blocks across all messages.

Typically this is achieved by splitting the initial counter block value into two concatenated parts:

- A [nonce](/en-US/docs/Glossary/Nonce) (that is, a number that may only be used once). The nonce part of the block stays the same for every block in the message. Each time a new message is to be encrypted, a new nonce is chosen. Nonces don't have to be secret, but they must not be reused with the same key.
- A counter. This part of the block gets incremented each time a block is encrypted.

Essentially: the nonce should ensure that counter blocks are not reused from one message to the next, while the counter should ensure that counter blocks are not reused within a single message.

Note: See [Appendix B of the NIST SP800-38A standard](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf#%5B%7B%22num%22%3A70%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22Fit%22%7D%5D) for more information.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[name](#name)

A string. This should be set to `AES-CTR`.

[counter](#counter)

An [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), a [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray), or a [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) — the initial value of the counter block. This must be 16 bytes long (the AES block size). The rightmost `length` bits of this block are used for the counter, and the rest is used for the nonce. For example, if `length` is set to 64, then the first half of `counter` is the nonce and the second half is used for the counter.

[length](#length)

A `Number` — the number of bits in the counter block that are used for the actual counter. The counter must be big enough that it doesn't wrap: if the message is `n` blocks and the counter is `m` bits long, then the following must be true: `n <= 2^m`. The [NIST SP800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) standard, which defines CTR, suggests that the counter should occupy half of the counter block (see [Appendix B.2](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf#%5B%7B%22num%22%3A73%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22Fit%22%7D%5D)), so for AES it would be 64.

## [Examples](#examples)

See the examples for [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt) and [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt).

## [Specifications](#specifications)

Specification
[Web Cryptography Level 2# dfn-AesCtrParams](https://w3c.github.io/webcrypto/#dfn-AesCtrParams)

## [Browser compatibility](#browser_compatibility)

Browsers that support the "AES-CTR" algorithm for the [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt), [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt), [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey), or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey) methods will support this type.

## [See also](#see_also)

- CTR mode is defined in section 6.5 of the [NIST SP800-38A standard](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf#%5B%7B%22num%22%3A70%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22Fit%22%7D%5D).
- [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt).
- [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt).
- [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey).
- [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AesCtrParams/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/aesctrparams/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAesCtrParams&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faesctrparams%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAesCtrParams%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faesctrparams%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdc788bf0ea36cb1ebe809c82aaae2c77cb3e18c0%0A*+Document+last+modified%3A+2025-12-15T07%3A46%3A57.000Z%0A%0A%3C%2Fdetails%3E)
