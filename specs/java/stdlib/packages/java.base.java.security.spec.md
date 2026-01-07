java.security.spec (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

# Package java.security.spec

package java.security.specProvides classes and interfaces for key specifications and algorithm parameter specifications. 

A key specification is a transparent representation of the key material that constitutes a key. A key may be specified in an algorithm-specific way, or in an algorithm-independent encoding format (such as ASN.1). This package contains key specifications for DSA public and private keys, RSA public and private keys, PKCS #8 private keys in DER-encoded format, and X.509 public and private keys in DER-encoded format. 

An algorithm parameter specification is a transparent representation of the sets of parameters used with an algorithm. This package contains an algorithm parameter specification for parameters used with the DSA algorithm. 

## Package Specification

- PKCS #1: RSA Cryptography Specifications, Version 2.2 (RFC 8017)
- PKCS #8: Private-Key Information Syntax Standard, Version 1.2, November 1993
- Federal Information Processing Standards Publication (FIPS PUB) 186: Digital Signature Standard (DSS)

## Related Documentation

 For documentation that includes information about algorithm parameter and key specifications, please see: 

- [Java Cryptography Architecture (JCA) Reference Guide](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=security_guide_jca)
- [How to Implement a Provider in the Java Cryptography Architecture](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=security_guide_impl_provider)

Since:1.2

- Related PackagesPackageDescription[java.security](../package-summary.html)Provides the classes and interfaces for the security framework.[java.security.cert](../cert/package-summary.html)Provides classes and interfaces for parsing and managing certificates, certificate revocation lists (CRLs), and certification paths.[java.security.interfaces](../interfaces/package-summary.html)Provides interfaces for generating RSA (Rivest, Shamir and Adleman AsymmetricCipher algorithm) keys as defined in the RSA Laboratory Technical Note PKCS#1, and DSA (Digital Signature Algorithm) keys as defined in NIST's FIPS-186.
- All Classes and InterfacesInterfacesClassesException ClassesClassDescription[AlgorithmParameterSpec](AlgorithmParameterSpec.html)A (transparent) specification of cryptographic parameters.[DSAGenParameterSpec](DSAGenParameterSpec.html)This immutable class specifies the set of parameters used for generating DSA parameters as specified in [FIPS 186-3 Digital Signature Standard (DSS)](http://csrc.nist.gov/publications/fips/fips186-3/fips_186-3.pdf).[DSAParameterSpec](DSAParameterSpec.html)This class specifies the set of parameters used with the DSA algorithm.[DSAPrivateKeySpec](DSAPrivateKeySpec.html)This class specifies a DSA private key with its associated parameters.[DSAPublicKeySpec](DSAPublicKeySpec.html)This class specifies a DSA public key with its associated parameters.[ECField](ECField.html)This interface represents an elliptic curve (EC) finite field.[ECFieldF2m](ECFieldF2m.html)This immutable class defines an elliptic curve (EC) characteristic 2 finite field.[ECFieldFp](ECFieldFp.html)This immutable class defines an elliptic curve (EC) prime finite field.[ECGenParameterSpec](ECGenParameterSpec.html)This immutable class specifies the set of parameters used for generating elliptic curve (EC) domain parameters.[ECParameterSpec](ECParameterSpec.html)This immutable class specifies the set of domain parameters used with elliptic curve cryptography (ECC).[ECPoint](ECPoint.html)This immutable class represents a point on an elliptic curve (EC) in affine coordinates.[ECPrivateKeySpec](ECPrivateKeySpec.html)This immutable class specifies an elliptic curve private key with its associated parameters.[ECPublicKeySpec](ECPublicKeySpec.html)This immutable class specifies an elliptic curve public key with its associated parameters.[EdDSAParameterSpec](EdDSAParameterSpec.html)A class used to specify EdDSA signature and verification parameters.[EdECPoint](EdECPoint.html)An elliptic curve point used to specify keys as defined by [RFC 8032: Edwards-Curve
 Digital Signature Algorithm (EdDSA)](https://tools.ietf.org/html/rfc8032).[EdECPrivateKeySpec](EdECPrivateKeySpec.html)A class representing elliptic curve private keys as defined in [RFC 8032: Edwards-Curve
 Digital Signature Algorithm (EdDSA)](https://tools.ietf.org/html/rfc8032), including the curve and other algorithm parameters.[EdECPublicKeySpec](EdECPublicKeySpec.html)A class representing elliptic curve public keys as defined in [RFC 8032: Edwards-Curve
 Digital Signature Algorithm (EdDSA)](https://tools.ietf.org/html/rfc8032), including the curve and other algorithm parameters.[EllipticCurve](EllipticCurve.html)This immutable class holds the necessary values needed to represent an elliptic curve.[EncodedKeySpec](EncodedKeySpec.html)This class represents a public or private key in encoded format.[InvalidKeySpecException](InvalidKeySpecException.html)This is the exception for invalid key specifications.[InvalidParameterSpecException](InvalidParameterSpecException.html)This is the exception for invalid parameter specifications.[KeySpec](KeySpec.html)A (transparent) specification of the key material that constitutes a cryptographic key.[MGF1ParameterSpec](MGF1ParameterSpec.html)This class specifies the set of parameters used with mask generation function MGF1 in OAEP Padding and RSASSA-PSS signature scheme, as defined in the [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard.[NamedParameterSpec](NamedParameterSpec.html)This class is used to specify any algorithm parameters that are determined by a standard name.[PKCS8EncodedKeySpec](PKCS8EncodedKeySpec.html)This class represents the ASN.1 encoding of a private key, encoded according to the ASN.1 type `PrivateKeyInfo`.[PSSParameterSpec](PSSParameterSpec.html)This class specifies a parameter spec for the RSASSA-PSS signature scheme, as defined in the [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard.[RSAKeyGenParameterSpec](RSAKeyGenParameterSpec.html)This class specifies the set of parameters used to generate an RSA key pair.[RSAMultiPrimePrivateCrtKeySpec](RSAMultiPrimePrivateCrtKeySpec.html)This class specifies an RSA multi-prime private key, as defined in the [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard using the Chinese Remainder Theorem (CRT) information values for efficiency.[RSAOtherPrimeInfo](RSAOtherPrimeInfo.html)This class represents the triplet (prime, exponent, and coefficient) inside RSA's OtherPrimeInfo structure, as defined in the [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard.[RSAPrivateCrtKeySpec](RSAPrivateCrtKeySpec.html)This class specifies an RSA private key, as defined in the [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard, using the Chinese Remainder Theorem (CRT) information values for efficiency.[RSAPrivateKeySpec](RSAPrivateKeySpec.html)This class specifies an RSA private key.[RSAPublicKeySpec](RSAPublicKeySpec.html)This class specifies an RSA public key.[X509EncodedKeySpec](X509EncodedKeySpec.html)This class represents the ASN.1 encoding of a public key, encoded according to the ASN.1 type `SubjectPublicKeyInfo`.[XECPrivateKeySpec](XECPrivateKeySpec.html)A class representing elliptic curve private keys as defined in RFC 7748, including the curve and other algorithm parameters.[XECPublicKeySpec](XECPublicKeySpec.html)A class representing elliptic curve public keys as defined in RFC 7748, including the curve and other algorithm parameters.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
