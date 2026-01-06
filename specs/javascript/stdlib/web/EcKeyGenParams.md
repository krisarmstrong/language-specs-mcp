# EcKeyGenParams

The `EcKeyGenParams` dictionary of the [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API) represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey), when generating any elliptic-curve-based key pair: that is, when the algorithm is identified as either of [ECDSA](/en-US/docs/Web/API/SubtleCrypto/sign#ecdsa) or [ECDH](/en-US/docs/Web/API/SubtleCrypto/deriveKey#ecdh).

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[name](#name)

A string. This should be set to `ECDSA` or `ECDH`, depending on the algorithm you want to use.

[namedCurve](#namedcurve)

A string representing the name of the elliptic curve to use. This may be any of the following names for [NIST](https://www.nist.gov/)-approved curves:

- `P-256`
- `P-384`
- `P-521`

## [Examples](#examples)

See the examples for [SubtleCrypto.generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey).

## [Specifications](#specifications)

Specification
[Web Cryptography Level 2# dfn-EcKeyGenParams](https://w3c.github.io/webcrypto/#dfn-EcKeyGenParams)

## [Browser compatibility](#browser_compatibility)

Browsers that support the "ECDH" or "ECDSA" algorithms for the [SubtleCrypto.generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey) method will support this type.

## [See also](#see_also)

- [SubtleCrypto.generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/EcKeyGenParams/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/eckeygenparams/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEcKeyGenParams&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Feckeygenparams%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEcKeyGenParams%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Feckeygenparams%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
