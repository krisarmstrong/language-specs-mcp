# EcdsaParams

The `EcdsaParams` dictionary of the [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API) represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.sign()](/en-US/docs/Web/API/SubtleCrypto/sign) or [SubtleCrypto.verify()](/en-US/docs/Web/API/SubtleCrypto/verify) when using the [ECDSA](/en-US/docs/Web/API/SubtleCrypto/sign#ecdsa) algorithm.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[name](#name)

A string. This should be set to `ECDSA`.

[hash](#hash)

A string or an object containing a single property called `name` with a string value. It is an identifier for the [digest algorithm](/en-US/docs/Web/API/SubtleCrypto/digest) to use. This should be one of the following:

- `SHA-256`: selects the [SHA-256](/en-US/docs/Web/API/SubtleCrypto/digest#supported_algorithms) algorithm.
- `SHA-384`: selects the [SHA-384](/en-US/docs/Web/API/SubtleCrypto/digest#supported_algorithms) algorithm.
- `SHA-512`: selects the [SHA-512](/en-US/docs/Web/API/SubtleCrypto/digest#supported_algorithms) algorithm.

Warning:`SHA-1` is also supported here but the [SHA-1](/en-US/docs/Web/API/SubtleCrypto/digest#supported_algorithms) algorithm is considered vulnerable and should no longer be used.

## [Examples](#examples)

See the examples for [SubtleCrypto.sign()](/en-US/docs/Web/API/SubtleCrypto/sign) or [SubtleCrypto.verify()](/en-US/docs/Web/API/SubtleCrypto/verify).

## [Specifications](#specifications)

Specification
[Web Cryptography Level 2# SubtleCrypto-method-sign](https://w3c.github.io/webcrypto/#SubtleCrypto-method-sign)
[Web Cryptography Level 2# SubtleCrypto-method-verify](https://w3c.github.io/webcrypto/#SubtleCrypto-method-verify)

## [Browser compatibility](#browser_compatibility)

Browsers that support the "ECDSA" algorithm for the [SubtleCrypto.sign()](/en-US/docs/Web/API/SubtleCrypto/sign) and [SubtleCrypto.verify()](/en-US/docs/Web/API/SubtleCrypto/verify) methods will support this type.

### [api.SubtleCrypto.sign](#api.SubtleCrypto.sign)

### [api.SubtleCrypto.verify](#api.SubtleCrypto.verify)

## [See also](#see_also)

- [SubtleCrypto.sign()](/en-US/docs/Web/API/SubtleCrypto/sign) and [SubtleCrypto.verify()](/en-US/docs/Web/API/SubtleCrypto/verify).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/EcdsaParams/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/ecdsaparams/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEcdsaParams&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fecdsaparams%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEcdsaParams%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fecdsaparams%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa84b606ffd77c40a7306be6c932a74ab9ce6ab96%0A*+Document+last+modified%3A+2025-06-24T06%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
