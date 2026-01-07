javax.crypto.interfaces (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
