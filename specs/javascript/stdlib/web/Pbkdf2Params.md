# Pbkdf2Params

The `Pbkdf2Params` dictionary of the [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API) represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey), when using the [PBKDF2](/en-US/docs/Web/API/SubtleCrypto/deriveKey#pbkdf2) algorithm.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[name](#name)

A string. This should be set to `PBKDF2`.

[hash](#hash)

A string or an object containing a single property called `name` with a string value. It is an identifier for the [digest algorithm](/en-US/docs/Web/API/SubtleCrypto/digest) to use. This should be one of the following:

- `SHA-256`: selects the [SHA-256](/en-US/docs/Web/API/SubtleCrypto/digest#supported_algorithms) algorithm.
- `SHA-384`: selects the [SHA-384](/en-US/docs/Web/API/SubtleCrypto/digest#supported_algorithms) algorithm.
- `SHA-512`: selects the [SHA-512](/en-US/docs/Web/API/SubtleCrypto/digest#supported_algorithms) algorithm.

Warning:`SHA-1` is considered vulnerable in most cryptographic applications, but is still considered safe in PBKDF2. However, it's advisable to transition away from it everywhere, so unless you need to use `SHA-1`, don't. Use a different digest algorithm instead.

[salt](#salt)

An [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), a [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray), or a [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView). This should be a random or pseudo-random value of at least 16 bytes. Unlike the input key material passed into [deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey), `salt` does not need to be kept secret.

[iterations](#iterations)

A `Number` representing the number of times the hash function will be executed in `deriveKey()`. This determines how computationally expensive (that is, slow) the `deriveKey()` operation will be. In this context, slow is good, since it makes it more expensive for an attacker to run a dictionary attack against the keys. The general guidance here is to use as many iterations as possible, subject to keeping an acceptable level of performance for your application.

## [Examples](#examples)

See the examples for [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey).

## [Specifications](#specifications)

Specification
[Web Cryptography Level 2# dfn-Pbkdf2Params](https://w3c.github.io/webcrypto/#dfn-Pbkdf2Params)

## [Browser compatibility](#browser_compatibility)

Browsers that support the "PBKDF2" algorithm for the [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey) method will support this type.

## [See also](#see_also)

- [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Pbkdf2Params/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/pbkdf2params/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPbkdf2Params&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpbkdf2params%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPbkdf2Params%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpbkdf2params%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa84b606ffd77c40a7306be6c932a74ab9ce6ab96%0A*+Document+last+modified%3A+2025-06-24T06%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
