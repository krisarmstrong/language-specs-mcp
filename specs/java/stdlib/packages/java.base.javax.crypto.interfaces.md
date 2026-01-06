Module[java.base](../../../module-summary.html)

# Package javax.crypto.interfaces

package javax.crypto.interfacesProvides interfaces for Diffie-Hellman keys as defined in RSA Laboratories' PKCS #3. 

Note that these interfaces are intended only for key implementations whose key material is accessible and available. These interfaces are not intended for key implementations whose key material resides in inaccessible, protected storage (such as in a hardware device). 

For more developer information on how to use these interfaces, including information on how to design `Key` classes for hardware devices, please refer to the cryptographic provider developer guide: 

- [How to Implement a Provider in the Java Cryptography Architecture](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=security_guide_impl_provider)

## Package Specification

- PKCS #3: Diffie-Hellman Key-Agreement Standard, Version 1.4, November 1993.

## Related Documentation

 For further documentation, please see: 

- [Java Cryptography Architecture (JCA) Reference Guide](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=security_guide_jca)

Since:1.4

- Related PackagesPackageDescription[javax.crypto](../package-summary.html)Provides the classes and interfaces for cryptographic operations.[javax.crypto.spec](../spec/package-summary.html)Provides classes and interfaces for key specifications and algorithm parameter specifications.
- InterfacesClassDescription[DHKey](DHKey.html)The interface to a Diffie-Hellman key.[DHPrivateKey](DHPrivateKey.html)The interface to a Diffie-Hellman private key.[DHPublicKey](DHPublicKey.html)The interface to a Diffie-Hellman public key.[PBEKey](PBEKey.html)The interface to a PBE key.
