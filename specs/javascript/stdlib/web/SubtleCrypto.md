# SubtleCrypto

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2017⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSubtleCrypto&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `SubtleCrypto` interface of the [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API) provides a number of low-level cryptographic functions.

The interface name includes the term "subtle" to indicate that many of its algorithms have subtle usage requirements, and hence that it must be used carefully in order to provide suitable security guarantees.

An instance of `SubtleCrypto` is available as the [subtle](/en-US/docs/Web/API/Crypto/subtle) property of the [Crypto](/en-US/docs/Web/API/Crypto) interface, which in turn is available in windows through the [Window.crypto](/en-US/docs/Web/API/Window/crypto) property and in workers through the [WorkerGlobalScope.crypto](/en-US/docs/Web/API/WorkerGlobalScope/crypto) property.

Warning: This API provides a number of low-level cryptographic primitives. It's very easy to misuse them, and the pitfalls involved can be very subtle.

Even assuming you use the basic cryptographic functions correctly, secure key management and overall security system design are extremely hard to get right, and are generally the domain of specialist security experts.

Errors in security system design and implementation can make the security of the system completely ineffective.

Please learn and experiment, but don't guarantee or imply the security of your work before an individual knowledgeable in this subject matter thoroughly reviews it. The [Crypto 101 Course](https://www.crypto101.io/) can be a great place to start learning about the design and implementation of secure systems.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Using SubtleCrypto](#using_subtlecrypto)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface doesn't inherit any properties, as it has no parent interface.

## [Instance methods](#instance_methods)

This interface doesn't inherit any methods, as it has no parent interface.

[SubtleCrypto.encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with the encrypted data corresponding to the clear text, algorithm, and key given as parameters.

[SubtleCrypto.decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with the clear data corresponding to the encrypted text, algorithm, and key given as parameters.

[SubtleCrypto.sign()](/en-US/docs/Web/API/SubtleCrypto/sign)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with the signature corresponding to the text, algorithm, and key given as parameters.

[SubtleCrypto.verify()](/en-US/docs/Web/API/SubtleCrypto/verify)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a boolean value indicating if the signature given as a parameter matches the text, algorithm, and key that are also given as parameters.

[SubtleCrypto.digest()](/en-US/docs/Web/API/SubtleCrypto/digest)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a digest generated from the algorithm and text given as parameters.

[SubtleCrypto.generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a newly-generated [CryptoKey](/en-US/docs/Web/API/CryptoKey), for symmetrical algorithms, or a [CryptoKeyPair](/en-US/docs/Web/API/CryptoKeyPair), containing two newly generated keys, for asymmetrical algorithms. These will match the algorithm, usages, and extractability given as parameters.

[SubtleCrypto.deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a newly generated [CryptoKey](/en-US/docs/Web/API/CryptoKey) derived from the master key and specific algorithm given as parameters.

[SubtleCrypto.deriveBits()](/en-US/docs/Web/API/SubtleCrypto/deriveBits)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a newly generated buffer of pseudo-random bits derived from the master key and specific algorithm given as parameters.

[SubtleCrypto.importKey()](/en-US/docs/Web/API/SubtleCrypto/importKey)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [CryptoKey](/en-US/docs/Web/API/CryptoKey) corresponding to the format, the algorithm, raw key data, usages, and extractability given as parameters.

[SubtleCrypto.exportKey()](/en-US/docs/Web/API/SubtleCrypto/exportKey)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with the raw key data containing the key in the requested format.

[SubtleCrypto.wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a wrapped symmetric key for usage (transfer and storage) in insecure environments. The wrapped key matches the format specified in the given parameters, and wrapping is done by the given wrapping key, using the specified algorithm.

[SubtleCrypto.unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [CryptoKey](/en-US/docs/Web/API/CryptoKey) corresponding to the wrapped key given in the parameter.

## [Using SubtleCrypto](#using_subtlecrypto)

We can split the functions implemented by this API into two groups: cryptography functions and key management functions.

### [Cryptography functions](#cryptography_functions)

These are the functions you can use to implement security features such as privacy and authentication in a system. The `SubtleCrypto` API provides the following cryptography functions:

- [sign()](/en-US/docs/Web/API/SubtleCrypto/sign) and [verify()](/en-US/docs/Web/API/SubtleCrypto/verify): create and verify digital signatures.
- [encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt) and [decrypt()](/en-US/docs/Web/API/SubtleCrypto/decrypt): encrypt and decrypt data.
- [digest()](/en-US/docs/Web/API/SubtleCrypto/digest): create a fixed-length, collision-resistant digest of some data.

### [Key management functions](#key_management_functions)

Except for [digest()](/en-US/docs/Web/API/SubtleCrypto/digest), all the cryptography functions in the API use cryptographic keys. In the `SubtleCrypto` API a cryptographic key is represented using a [CryptoKey](/en-US/docs/Web/API/CryptoKey) object. To perform operations like signing and encrypting, you pass a [CryptoKey](/en-US/docs/Web/API/CryptoKey) object into the [sign()](/en-US/docs/Web/API/SubtleCrypto/sign) or [encrypt()](/en-US/docs/Web/API/SubtleCrypto/encrypt) function.

#### Generating and deriving keys

The [generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey) and [deriveKey()](/en-US/docs/Web/API/SubtleCrypto/deriveKey) functions both create a new [CryptoKey](/en-US/docs/Web/API/CryptoKey) object.

The difference is that `generateKey()` will generate a new distinct key value each time you call it, while `deriveKey()` derives a key from some initial keying material. If you provide the same keying material to two separate calls to `deriveKey()`, you will get two `CryptoKey` objects that have the same underlying value. This is useful if, for example, you want to derive an encryption key from a password and later derive the same key from the same password to decrypt the data.

#### Importing and exporting keys

To make keys available outside your app, you need to export the key, and that's what [exportKey()](/en-US/docs/Web/API/SubtleCrypto/exportKey) is for. You can choose one of a number of export formats.

The inverse of `exportKey()` is [importKey()](/en-US/docs/Web/API/SubtleCrypto/importKey). You can import keys from other systems, and support for standard formats like [PKCS #8](https://datatracker.ietf.org/doc/html/rfc5208) and [JSON Web Key](https://datatracker.ietf.org/doc/html/rfc7517) helps you do this. The `exportKey()` function exports the key in an unencrypted format.

If the key is sensitive you should use [wrapKey()](/en-US/docs/Web/API/SubtleCrypto/wrapKey), which exports the key and then encrypts it using another key; the API calls a "key-wrapping key".

The inverse of `wrapKey()` is [unwrapKey()](/en-US/docs/Web/API/SubtleCrypto/unwrapKey), which decrypts then imports the key.

#### Storing keys

`CryptoKey` is a [serializable object](/en-US/docs/Glossary/Serializable_object), which allows keys to be stored and retrieved using standard web storage APIs.

The specification expects that most developers will use the [IndexedDB API](/en-US/docs/Web/API/IndexedDB_API), storing `CryptoKey` objects against some key string identifier that is meaningful to the application, along with any other metadata it finds useful. This allows the storage and retrieval of the `CryptoKey` without having to expose its underlying key material to the application or the JavaScript environment.

### [Supported algorithms](#supported_algorithms)

The cryptographic functions provided by the Web Crypto API can be performed by one or more different cryptographic algorithms: the `algorithm` argument to the function indicates which algorithm to use. Some algorithms need extra parameters: in these cases the `algorithm` argument is a dictionary object that includes the extra parameters.

The table below summarizes which algorithms are suitable for which cryptographic operations:

[sign](/en-US/docs/Web/API/SubtleCrypto/sign)
[verify](/en-US/docs/Web/API/SubtleCrypto/verify)[encrypt](/en-US/docs/Web/API/SubtleCrypto/encrypt)
[decrypt](/en-US/docs/Web/API/SubtleCrypto/decrypt)[digest](/en-US/docs/Web/API/SubtleCrypto/digest)[deriveBits](/en-US/docs/Web/API/SubtleCrypto/deriveBits)
[deriveKey](/en-US/docs/Web/API/SubtleCrypto/deriveKey)[wrapKey](/en-US/docs/Web/API/SubtleCrypto/wrapKey)
[unwrapKey](/en-US/docs/Web/API/SubtleCrypto/unwrapKey)[generateKey](/en-US/docs/Web/API/SubtleCrypto/generateKey)
[exportKey](/en-US/docs/Web/API/SubtleCrypto/exportKey)[importKey](/en-US/docs/Web/API/SubtleCrypto/importKey)[RSASSA-PKCS1-v1_5](/en-US/docs/Web/API/SubtleCrypto/sign#rsassa-pkcs1-v1_5)✓✓✓[RSA-PSS](/en-US/docs/Web/API/SubtleCrypto/sign#rsa-pss)✓✓✓[ECDSA](/en-US/docs/Web/API/SubtleCrypto/sign#ecdsa)✓✓✓[Ed25519](/en-US/docs/Web/API/SubtleCrypto/sign#ed25519)✓✓✓[HMAC](/en-US/docs/Web/API/SubtleCrypto/sign#hmac)✓✓✓[RSA-OAEP](/en-US/docs/Web/API/SubtleCrypto/encrypt#rsa-oaep)✓✓✓✓[AES-CTR](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-ctr)✓✓✓✓[AES-CBC](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-cbc)✓✓✓✓[AES-GCM](/en-US/docs/Web/API/SubtleCrypto/encrypt#aes-gcm)✓✓✓✓[AES-KW](/en-US/docs/Web/API/SubtleCrypto/wrapKey#aes-kw)✓✓✓[SHA-1](/en-US/docs/Web/API/SubtleCrypto/digest#supported_algorithms)✓[SHA-256](/en-US/docs/Web/API/SubtleCrypto/digest#supported_algorithms)✓[SHA-384](/en-US/docs/Web/API/SubtleCrypto/digest#supported_algorithms)✓[SHA-512](/en-US/docs/Web/API/SubtleCrypto/digest#supported_algorithms)✓[ECDH](/en-US/docs/Web/API/SubtleCrypto/deriveKey#ecdh)✓✓✓[X25519](/en-US/docs/Web/API/SubtleCrypto/deriveKey#x25519)✓✓✓[HKDF](/en-US/docs/Web/API/SubtleCrypto/deriveKey#hkdf)✓✓[PBKDF2](/en-US/docs/Web/API/SubtleCrypto/deriveKey#pbkdf2)✓✓

## [Specifications](#specifications)

Specification
[Web Cryptography Level 2# subtlecrypto-interface](https://w3c.github.io/webcrypto/#subtlecrypto-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API)
- [Non-cryptographic uses of SubtleCrypto](/en-US/docs/Web/API/Web_Crypto_API/Non-cryptographic_uses_of_subtle_crypto)
- [Web security](/en-US/docs/Web/Security)
- [Privacy, permissions, and information security](/en-US/docs/Web/Privacy)
- [Crypto](/en-US/docs/Web/API/Crypto) and [Crypto.subtle](/en-US/docs/Web/API/Crypto/subtle).
- [Crypto 101](https://www.crypto101.io/): an introductory course on cryptography.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 12, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SubtleCrypto/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/subtlecrypto/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSubtleCrypto&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsubtlecrypto%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSubtleCrypto%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsubtlecrypto%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F44b15fff6c156ec81c2290e252e20c4519089688%0A*+Document+last+modified%3A+2025-09-12T01%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E)
