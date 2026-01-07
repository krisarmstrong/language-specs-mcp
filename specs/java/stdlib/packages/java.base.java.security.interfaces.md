java.security.interfaces (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

- [Overview](../../../../index.html)
- [Module](../../../module-summary.html)
- Package
- Class
- [Use](package-use.html)
- [Tree](package-tree.html)
- [Preview](../../../../preview-list.html)
- [New](../../../../new-list.html)
- [Deprecated](../../../../deprecated-list.html)
- [Index](../../../../index-files/index-1.html)
- [Help](../../../../help-doc.html#package)

- 

Package:

  - [Description](#package-description)
  - [Related Packages](#related-package-summary)
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- [Related Packages](#related-package-summary) | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../../search.html)Module[java.base](../../../module-summary.html)

# Package java.security.interfaces

package java.security.interfacesProvides interfaces for generating RSA (Rivest, Shamir and Adleman AsymmetricCipher algorithm) keys as defined in the RSA Laboratory Technical Note PKCS#1, and DSA (Digital Signature Algorithm) keys as defined in NIST's FIPS-186. 

 Note that these interfaces are intended only for key implementations whose key material is accessible and available. These interfaces are not intended for key implementations whose key material resides in inaccessible, protected storage (such as in a hardware device). 

 For more developer information on how to use these interfaces, including information on how to design `Key` classes for hardware devices, please refer to these cryptographic provider developer guides: 

- [How to Implement a Provider in the Java Cryptography Architecture](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=security_guide_impl_provider)

## Package Specification

- PKCS #1: RSA Cryptography Specifications, Version 2.2 (RFC 8017)
- Federal Information Processing Standards Publication (FIPS PUB) 186: Digital Signature Standard (DSS) 

## Related Documentation

 For further documentation, please see: 

- [Java Cryptography Architecture Reference Guide](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=security_guide_jca)

Since:1.1

- Related PackagesPackageDescription[java.security](../package-summary.html)Provides the classes and interfaces for the security framework.[java.security.cert](../cert/package-summary.html)Provides classes and interfaces for parsing and managing certificates, certificate revocation lists (CRLs), and certification paths.[java.security.spec](../spec/package-summary.html)Provides classes and interfaces for key specifications and algorithm parameter specifications.
- InterfacesClassDescription[DSAKey](DSAKey.html)The interface to a DSA public or private key.[DSAKeyPairGenerator](DSAKeyPairGenerator.html)An interface to an object capable of generating DSA key pairs.[DSAParams](DSAParams.html)Interface to a DSA-specific set of key parameters, which defines a DSA key family.[DSAPrivateKey](DSAPrivateKey.html)The standard interface to a DSA private key.[DSAPublicKey](DSAPublicKey.html)The interface to a DSA public key.[ECKey](ECKey.html)The interface to an elliptic curve (EC) key.[ECPrivateKey](ECPrivateKey.html)The interface to an elliptic curve (EC) private key.[ECPublicKey](ECPublicKey.html)The interface to an elliptic curve (EC) public key.[EdECKey](EdECKey.html)An interface for an elliptic curve public/private key as defined by [RFC 8032: Edwards-Curve
 Digital Signature Algorithm (EdDSA)](https://tools.ietf.org/html/rfc8032).[EdECPrivateKey](EdECPrivateKey.html)An interface for an elliptic curve private key as defined by [RFC 8032: Edwards-Curve
 Digital Signature Algorithm (EdDSA)](https://tools.ietf.org/html/rfc8032).[EdECPublicKey](EdECPublicKey.html)An interface for an elliptic curve public key as defined by [RFC 8032: Edwards-Curve
 Digital Signature Algorithm (EdDSA)](https://tools.ietf.org/html/rfc8032).[RSAKey](RSAKey.html)The interface to a public or private key in [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard, such as those for RSA, or RSASSA-PSS algorithms.[RSAMultiPrimePrivateCrtKey](RSAMultiPrimePrivateCrtKey.html)The interface to an RSA multi-prime private key, as defined in the [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard, using the Chinese Remainder Theorem (CRT) information values.[RSAPrivateCrtKey](RSAPrivateCrtKey.html)The interface to an RSA private key, as defined in the [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard, using the Chinese Remainder Theorem (CRT) information values.[RSAPrivateKey](RSAPrivateKey.html)The interface to an RSA private key.[RSAPublicKey](RSAPublicKey.html)The interface to an RSA public key.[XECKey](XECKey.html)An interface for an elliptic curve public/private key as defined by RFC 7748.[XECPrivateKey](XECPrivateKey.html)An interface for an elliptic curve private key as defined by RFC 7748.[XECPublicKey](XECPublicKey.html)An interface for an elliptic curve public key as defined by RFC 7748.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
