Module[java.base](../../../module-summary.html)

# Package javax.crypto.spec

package javax.crypto.specProvides classes and interfaces for key specifications and algorithm parameter specifications. 

A key specification is a transparent representation of the key material that constitutes a key. A key may be specified in an algorithm-specific way, or in an algorithm-independent encoding format (such as ASN.1). This package contains key specifications for Diffie-Hellman public and private keys, as well as key specifications for DES, Triple DES, and PBE secret keys. 

An algorithm parameter specification is a transparent representation of the sets of parameters used with an algorithm. This package contains algorithm parameter specifications for parameters used with the Diffie-Hellman, DES, Triple DES, PBE, RC2 and RC5 algorithms. 

- PKCS #1: RSA Cryptography Specifications, Version 2.2 (RFC 8017)
- PKCS #3: Diffie-Hellman Key-Agreement Standard, Version 1.4, November 1993.
- PKCS #5: Password-Based Encryption Standard, Version 1.5, November 1993.
- Federal Information Processing Standards Publication (FIPS PUB) 46-2: Data Encryption Standard (DES) 

## Related Documentation

 For documentation that includes information about algorithm parameter and key specifications, please see: 

- [Java Cryptography Architecture (JCA) Reference Guide](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=security_guide_jca)
- [How to Implement a Provider in the Java Cryptography Architecture](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=security_guide_impl_provider)

Since:1.4

- Related PackagesPackageDescription[javax.crypto](../package-summary.html)Provides the classes and interfaces for cryptographic operations.[javax.crypto.interfaces](../interfaces/package-summary.html)Provides interfaces for Diffie-Hellman keys as defined in RSA Laboratories' PKCS #3.
- ClassesClassDescription[ChaCha20ParameterSpec](ChaCha20ParameterSpec.html)This class specifies the parameters used with the [ChaCha20](https://tools.ietf.org/html/rfc7539) algorithm.[DESedeKeySpec](DESedeKeySpec.html)This class specifies a DES-EDE ("triple-DES") key.[DESKeySpec](DESKeySpec.html)This class specifies a DES key.[DHGenParameterSpec](DHGenParameterSpec.html)This class specifies the set of parameters used for generating Diffie-Hellman (system) parameters for use in Diffie-Hellman key agreement.[DHParameterSpec](DHParameterSpec.html)This class specifies the set of parameters used with the Diffie-Hellman algorithm, as specified in PKCS #3: Diffie-Hellman Key-Agreement Standard.[DHPrivateKeySpec](DHPrivateKeySpec.html)This class specifies a Diffie-Hellman private key with its associated parameters.[DHPublicKeySpec](DHPublicKeySpec.html)This class specifies a Diffie-Hellman public key with its associated parameters.[GCMParameterSpec](GCMParameterSpec.html)Specifies the set of parameters required by a [Cipher](../Cipher.html) using the Galois/Counter Mode (GCM) mode.[IvParameterSpec](IvParameterSpec.html)This class specifies an initialization vector (IV).[OAEPParameterSpec](OAEPParameterSpec.html)This class specifies the set of parameters used with OAEP Padding, as defined in the [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard.[PBEKeySpec](PBEKeySpec.html)A user-chosen password that can be used with password-based encryption (PBE).[PBEParameterSpec](PBEParameterSpec.html)This class specifies the set of parameters used with password-based encryption (PBE), as defined in the [PKCS #5](http://www.ietf.org/rfc/rfc2898.txt) standard.[PSource](PSource.html)This class specifies the source for encoding input P in OAEP Padding, as defined in the [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard.[PSource.PSpecified](PSource.PSpecified.html)This class is used to explicitly specify the value for encoding input P in OAEP Padding.[RC2ParameterSpec](RC2ParameterSpec.html)This class specifies the parameters used with the [RC2](http://www.ietf.org/rfc/rfc2268.txt) algorithm.[RC5ParameterSpec](RC5ParameterSpec.html)This class specifies the parameters used with the [RC5](https://tools.ietf.org/html/rfc2040) algorithm.[SecretKeySpec](SecretKeySpec.html)This class specifies a secret key in a provider-independent fashion.
