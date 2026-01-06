# CryptoKeyPair

The `CryptoKeyPair` dictionary of the [Web Crypto API](/en-US/docs/Web/API/Web_Crypto_API) represents a key pair for an asymmetric cryptography algorithm, also known as a public-key algorithm.

A `CryptoKeyPair` object can be obtained using [SubtleCrypto.generateKey()](/en-US/docs/Web/API/SubtleCrypto/generateKey), when the selected algorithm is one of the asymmetric algorithms: RSASSA-PKCS1-v1_5, RSA-PSS, RSA-OAEP, ECDSA, or ECDH.

It contains two properties, which are both [CryptoKey](/en-US/docs/Web/API/CryptoKey) objects: a `privateKey` property containing the private key and a `publicKey` property containing the public key.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[CryptoKeyPair.privateKey](#cryptokeypair.privatekey)

A [CryptoKey](/en-US/docs/Web/API/CryptoKey) object representing the private key. For encryption and decryption algorithms, this key is used to decrypt. For signing and verification algorithms it is used to sign.

[CryptoKeyPair.publicKey](#cryptokeypair.publickey)

A [CryptoKey](/en-US/docs/Web/API/CryptoKey) object representing the public key. For encryption and decryption algorithms, this key is used to encrypt. For signing and verification algorithms it is used to verify signatures.

## [Examples](#examples)

The examples for `SubtleCrypto` methods often use `CryptoKeyPair` objects. For example:

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
[Web Cryptography Level 2# keypair](https://w3c.github.io/webcrypto/#keypair)

## [See also](#see_also)

- [SubtleCrypto.generateKey](/en-US/docs/Web/API/SubtleCrypto/generateKey).
- [SubtleCrypto.sign](/en-US/docs/Web/API/SubtleCrypto/sign) and [SubtleCrypto.verify](/en-US/docs/Web/API/SubtleCrypto/verify).
- [SubtleCrypto.encrypt](/en-US/docs/Web/API/SubtleCrypto/encrypt) and [SubtleCrypto.decrypt](/en-US/docs/Web/API/SubtleCrypto/decrypt).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 19, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/CryptoKeyPair/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cryptokeypair/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCryptoKeyPair&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcryptokeypair%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCryptoKeyPair%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcryptokeypair%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb280ea1234452ff553caa466bf532a66ba51db01%0A*+Document+last+modified%3A+2023-02-19T06%3A34%3A57.000Z%0A%0A%3C%2Fdetails%3E)
