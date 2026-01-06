# Web Crypto API

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Crypto_API&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Web Crypto API is an interface allowing a script to use cryptographic primitives in order to build systems using cryptography.

Some browsers implemented an interface called [Crypto](/en-US/docs/Web/API/Crypto) without having it well defined or being cryptographically sound. In order to avoid confusion, methods and properties of this interface have been removed from browsers implementing the Web Crypto API, and all Web Crypto API methods are available on a new interface: [SubtleCrypto](/en-US/docs/Web/API/SubtleCrypto). The [Crypto.subtle](/en-US/docs/Web/API/Crypto/subtle) property gives access to an object implementing it.

Warning: The Web Crypto API provides a number of low-level cryptographic primitives. It's very easy to misuse them, and the pitfalls involved can be very subtle.

Even assuming you use the basic cryptographic functions correctly, secure key management and overall security system design are extremely hard to get right, and are generally the domain of specialist security experts.

Errors in security system design and implementation can make the security of the system completely ineffective.

Please learn and experiment, but don't guarantee or imply the security of your work before an individual knowledgeable in this subject matter thoroughly reviews it. The [Crypto 101 Course](https://www.crypto101.io/) can be a great place to start learning about the design and implementation of secure systems.

## In this article

- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Interfaces](#interfaces)

[Crypto](/en-US/docs/Web/API/Crypto)

Provides basic cryptography features, such as a cryptographically strong random number generator, and access to cryptographic primitives via a [SubtleCrypto](/en-US/docs/Web/API/SubtleCrypto) object. An object of this type can be accessed in the global scope using [Window.crypto](/en-US/docs/Web/API/Window/crypto) or [WorkerGlobalScope.crypto](/en-US/docs/Web/API/WorkerGlobalScope/crypto).

[SubtleCrypto](/en-US/docs/Web/API/SubtleCrypto)

Represents an object that provides low-level cryptographic functions for key generation, encryption, decryption, key wrapping and unwrapping, and so on.

[CryptoKey](/en-US/docs/Web/API/CryptoKey)

Represents a cryptographic [key](/en-US/docs/Glossary/Key) obtained from one of the [SubtleCrypto](/en-US/docs/Web/API/SubtleCrypto) methods [generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey), [deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey), [importKey()](/en-US/docs/Web/API/SubtleCrypto/importKey), or [unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey).

### [Dictionaries](#dictionaries)

[AesCbcParams](/en-US/docs/Web/API/AesCbcParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt), [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt), [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey), or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey), when using the [AES-CBC](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-cbc) algorithm.

[AesCtrParams](/en-US/docs/Web/API/AesCtrParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt), [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt), [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey), or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey), when using the [AES-CTR](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-ctr) algorithm.

[AesGcmParams](/en-US/docs/Web/API/AesGcmParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt), [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt), [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey), or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey), when using the [AES-GCM](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-gcm) algorithm.

[AesKeyGenParams](/en-US/docs/Web/API/AesKeyGenParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey), when generating an AES key: that is, when the algorithm is identified as any of [AES-CBC](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-cbc), [AES-CTR](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-ctr), [AES-GCM](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-gcm), or [AES-KW](/en-US/docs/Web/API/SubtleCrypto/wrapKey#aes-kw).

[CryptoKeyPair](/en-US/docs/Web/API/CryptoKeyPair)

Represents a public and private key pair used for an asymmetric cryptography algorithm.

[EcKeyGenParams](/en-US/docs/Web/API/EcKeyGenParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey), when generating any elliptic-curve-based key pair: that is, when the algorithm is identified as either of [ECDSA](/en-US/docs/Web/API/SubtleCrypto/sign#ecdsa) or [ECDH](/en-US/docs/Web/API/SubtleCrypto/deriveKey#ecdh).

[EcKeyImportParams](/en-US/docs/Web/API/EcKeyImportParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.importKey()](/en-US/docs/Web/API/SubtleCrypto/importKey) or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey), when generating any elliptic-curve-based key pair: that is, when the algorithm is identified as either of [ECDSA](/en-US/docs/Web/API/SubtleCrypto/sign#ecdsa) or [ECDH](/en-US/docs/Web/API/SubtleCrypto/deriveKey#ecdh).

[EcdhKeyDeriveParams](/en-US/docs/Web/API/EcdhKeyDeriveParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey), when using the [ECDH](/en-US/docs/Web/API/SubtleCrypto/deriveKey#ecdh) algorithm.

[EcdsaParams](/en-US/docs/Web/API/EcdsaParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.sign()](/en-US/docs/Web/API/SubtleCrypto/sign) or [SubtleCrypto.verify()](/en-US/docs/Web/API/SubtleCrypto/verify) when using the [ECDSA](/en-US/docs/Web/API/SubtleCrypto/sign#ecdsa) algorithm.

[HkdfParams](/en-US/docs/Web/API/HkdfParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey), when using the [HKDF](/en-US/docs/Web/API/SubtleCrypto/deriveKey#hkdf) algorithm.

[HmacImportParams](/en-US/docs/Web/API/HmacImportParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.importKey()](/en-US/docs/Web/API/SubtleCrypto/importKey) or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey), when generating a key for the [HMAC](/en-US/docs/Web/API/SubtleCrypto/sign#hmac) algorithm.

[HmacKeyGenParams](/en-US/docs/Web/API/HmacKeyGenParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey), when generating a key for the [HMAC](/en-US/docs/Web/API/SubtleCrypto/sign#hmac) algorithm.

[Pbkdf2Params](/en-US/docs/Web/API/Pbkdf2Params)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey), when using the [PBKDF2](/en-US/docs/Web/API/SubtleCrypto/deriveKey#pbkdf2) algorithm.

[RsaHashedImportParams](/en-US/docs/Web/API/RsaHashedImportParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.importKey()](/en-US/docs/Web/API/SubtleCrypto/importKey) or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey), when importing any RSA-based key pair: that is, when the algorithm is identified as any of [RSASSA-PKCS1-v1_5](/en-US/docs/Web/API/SubtleCrypto/sign#rsassa-pkcs1-v1_5), [RSA-PSS](/en-US/docs/Web/API/SubtleCrypto/sign#rsa-pss), or [RSA-OAEP](/en-US/docs/Web/API/SubtleCrypto/encrypt#rsa-oaep).

[RsaHashedKeyGenParams](/en-US/docs/Web/API/RsaHashedKeyGenParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey), when generating any RSA-based key pair: that is, when the algorithm is identified as any of [RSASSA-PKCS1-v1_5](/en-US/docs/Web/API/SubtleCrypto/sign#rsassa-pkcs1-v1_5), [RSA-PSS](/en-US/docs/Web/API/SubtleCrypto/sign#rsa-pss), or [RSA-OAEP](/en-US/docs/Web/API/SubtleCrypto/encrypt#rsa-oaep).

[RsaOaepParams](/en-US/docs/Web/API/RsaOaepParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt), [SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt), [SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey), or [SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey), when using the [RSA_OAEP](/en-US/docs/Web/API/SubtleCrypto/encrypt#rsa-oaep) algorithm.

[RsaPssParams](/en-US/docs/Web/API/RsaPssParams)

Represents the object that should be passed as the `algorithm` parameter into [SubtleCrypto.sign()](/en-US/docs/Web/API/SubtleCrypto/sign) or [SubtleCrypto.verify()](/en-US/docs/Web/API/SubtleCrypto/verify), when using the [RSA-PSS](/en-US/docs/Web/API/SubtleCrypto/sign#rsa-pss) algorithm.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Window.crypto](/en-US/docs/Web/API/Window/crypto)

Represents the [Crypto](/en-US/docs/Web/API/Crypto) object associated with the global object in the main thread scope.

[WorkerGlobalScope.crypto](/en-US/docs/Web/API/WorkerGlobalScope/crypto)

Represents [Crypto](/en-US/docs/Web/API/Crypto) object associated with the global object in worker scope.

## [Specifications](#specifications)

Specification
[Web Cryptography Level 2# crypto-interface](https://w3c.github.io/webcrypto/#crypto-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 2, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Web_Crypto_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/web_crypto_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Crypto_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fweb_crypto_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Crypto_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fweb_crypto_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff430d277573ba0b06b1ac33ae8017fd90f170bef%0A*+Document+last+modified%3A+2024-09-02T01%3A14%3A47.000Z%0A%0A%3C%2Fdetails%3E)
