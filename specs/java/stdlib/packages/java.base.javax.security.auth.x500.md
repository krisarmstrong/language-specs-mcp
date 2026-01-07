javax.security.auth.x500 (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

- [Overview](../../../../../index.html)
- [Module](../../../../module-summary.html)
- Package
- Class
- [Use](package-use.html)
- [Tree](package-tree.html)
- [Preview](../../../../../preview-list.html)
- [New](../../../../../new-list.html)
- [Deprecated](../../../../../deprecated-list.html)
- [Index](../../../../../index-files/index-1.html)
- [Help](../../../../../help-doc.html#package)

- 

Package:

  - [Description](#package-description)
  - [Related Packages](#related-package-summary)
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- [Related Packages](#related-package-summary) | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../../../search.html)Module[java.base](../../../../module-summary.html)

# Package javax.security.auth.x500

package javax.security.auth.x500This package contains the classes that should be used to store X500 Principal and X500 Private Credentials in a Subject. 

## Package Specification

- [RFC 1779: A String Representation of Distinguished Names](https://tools.ietf.org/html/rfc1779)
- [RFC 2253: Lightweight Directory Access Protocol (v3):
     UTF-8 String Representation of Distinguished Names](https://tools.ietf.org/html/rfc2253)
- [RFC 5280: Internet X.509 Public Key Infrastructure
     Certificate and Certificate Revocation List (CRL) Profile](https://tools.ietf.org/html/rfc5280)
- [RFC 4512: Lightweight Directory Access Protocol (LDAP):
     Directory Information Models](https://tools.ietf.org/html/rfc4512)

Since:1.4

- Related PackagesModulePackageDescription[java.base](../../../../module-summary.html)[javax.security.auth](../package-summary.html)This package provides a framework for authentication and authorization.[java.base](../../../../module-summary.html)[javax.security.auth.callback](../callback/package-summary.html)This package provides the classes necessary for services to interact with applications in order to retrieve information (authentication data including usernames or passwords, for example) or to display information (error and warning messages, for example).[java.security.jgss](../../../../../java.security.jgss/module-summary.html)[javax.security.auth.kerberos](../../../../../java.security.jgss/javax/security/auth/kerberos/package-summary.html)This package contains utility classes related to the Kerberos network authentication protocol.[java.base](../../../../module-summary.html)[javax.security.auth.login](../login/package-summary.html)This package provides a pluggable authentication framework.[java.base](../../../../module-summary.html)[javax.security.auth.spi](../spi/package-summary.html)This package provides the interface to be used for implementing pluggable authentication modules.
- ClassesClassDescription[X500Principal](X500Principal.html) This class represents an X.500 `Principal`.[X500PrivateCredential](X500PrivateCredential.html) This class represents an `X500PrivateCredential`.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
