# RsaPssParams

The `RsaPssParams` dictionary of the [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API) represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.sign()](/en-US/docs/Web/API/SubtleCrypto/sign) or [SubtleCrypto.verify()](/en-US/docs/Web/API/SubtleCrypto/verify), when using the [RSA-PSS](/en-US/docs/Web/API/SubtleCrypto/sign#rsa-pss) algorithm.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[name](#name)

A string. This should be set to `RSA-PSS`.

[saltLength](#saltlength)

A `long` integer representing the length of the random salt to use, in bytes.

[RFC 3447](https://datatracker.ietf.org/doc/html/rfc3447) says that "Typical salt lengths" are either 0 or the length of the output of the [digest algorithm](/en-US/docs/Web/API/SubtleCrypto#supported_algorithms) that was selected when this key was [generated](/en-US/docs/Web/API/SubtleCrypto/generateKey). For example, if you use [SHA-256](/en-US/docs/Web/API/SubtleCrypto/digest#supported_algorithms) as the digest algorithm, this could be 32.

The maximum size of `saltLength` is given by:

js

```
Math.ceil((keySizeInBits - 1) / 8) - digestSizeInBytes - 2;
```

So for a key length of 2048 bits and a digest output size of 32 bytes, the maximum size would be 222.

## [Examples](#examples)

See the examples for [SubtleCrypto.sign()](/en-US/docs/Web/API/SubtleCrypto/sign) and [SubtleCrypto.verify()](/en-US/docs/Web/API/SubtleCrypto/verify).

## [Specifications](#specifications)

Specification
[Web Cryptography Level 2# dfn-RsaPssParams](https://w3c.github.io/webcrypto/#dfn-RsaPssParams)

## [Browser compatibility](#browser_compatibility)

Browsers that support the "RSA-PSS" algorithm for the [SubtleCrypto.sign()](/en-US/docs/Web/API/SubtleCrypto/sign) and [SubtleCrypto.verify()](/en-US/docs/Web/API/SubtleCrypto/verify) methods will support this type.

## [See also](#see_also)

- [RFC 3447: RSASSA-PSS](https://datatracker.ietf.org/doc/html/rfc3447#section-8.1)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RsaPssParams/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rsapssparams/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRsaPssParams&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frsapssparams%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRsaPssParams%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frsapssparams%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
