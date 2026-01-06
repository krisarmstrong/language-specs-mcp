# CryptoKey

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCryptoKey&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `CryptoKey` interface of the [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API) represents a cryptographic [key](/en-US/docs/Glossary/Key) obtained from one of the [SubtleCrypto](/en-US/docs/Web/API/SubtleCrypto) methods [generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey), [deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey), [importKey()](/en-US/docs/Web/API/SubtleCrypto/importKey), or [unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey).

For security reasons, the `CryptoKey` interface can only be used in a [secure context](/en-US/docs/Web/Security/Defenses/Secure_Contexts).

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[CryptoKey.type](/en-US/docs/Web/API/CryptoKey/type)Read only

The type of key the object represents. It may take one of the following values: `"secret"`, `"private"` or `"public"`.

[CryptoKey.extractable](/en-US/docs/Web/API/CryptoKey/extractable)Read only

A boolean value indicating whether or not the key may be extracted using [SubtleCrypto.exportKey()](/en-US/docs/Web/API/SubtleCrypto/exportKey) or [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey).

[CryptoKey.algorithm](/en-US/docs/Web/API/CryptoKey/algorithm)Read only

An object describing the algorithm for which this key can be used and any associated extra parameters.

[CryptoKey.usages](/en-US/docs/Web/API/CryptoKey/usages)Read only

An [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of strings, indicating what can be done with the key. Possible values for array elements are `"encrypt"`, `"decrypt"`, `"sign"`, `"verify"`, `"deriveKey"`, `"deriveBits"`, `"wrapKey"`, and `"unwrapKey"`.

## [Examples](#examples)

The examples for `SubtleCrypto` methods often use `CryptoKey` objects. For example:

- [SubtleCrypto.generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey)
- [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey)
- [SubtleCrypto.importKey()](/en-US/docs/Web/API/SubtleCrypto/importKey)
- [SubtleCrypto.exportKey()](/en-US/docs/Web/API/SubtleCrypto/exportKey)
- [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey)
- [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey)
- [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt)
- [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt)
- [SubtleCrypto.sign()](/en-US/docs/Web/API/SubtleCrypto/sign)
- [SubtleCrypto.verify()](/en-US/docs/Web/API/SubtleCrypto/verify)

## [Specifications](#specifications)

Specification
[Web Cryptography Level 2# cryptokey-interface](https://w3c.github.io/webcrypto/#cryptokey-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API)
- [Web security](/en-US/docs/Web/Security)
- [Privacy, permissions, and information security](/en-US/docs/Web/Privacy)
- [Crypto](/en-US/docs/Web/API/Crypto) and [Crypto.subtle](/en-US/docs/Web/API/Crypto/subtle).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CryptoKey/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cryptokey/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCryptoKey&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcryptokey%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCryptoKey%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcryptokey%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
