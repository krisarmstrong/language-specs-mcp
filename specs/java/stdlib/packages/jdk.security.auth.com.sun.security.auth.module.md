com.sun.security.auth.module (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

- [Overview](../../../../../../index.html)
- [Module](../../../../../module-summary.html)
- Package
- Class
- [Use](package-use.html)
- [Tree](package-tree.html)
- [Preview](../../../../../../preview-list.html)
- [New](../../../../../../new-list.html)
- [Deprecated](../../../../../../deprecated-list.html)
- [Index](../../../../../../index-files/index-1.html)
- [Help](../../../../../../help-doc.html#package)

- 

Package:

  - [Description](#package-description)
  - [Related Packages](#related-package-summary)
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- [Related Packages](#related-package-summary) | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../../../../search.html)Module[jdk.security.auth](../../../../../module-summary.html)

# Package com.sun.security.auth.module

package com.sun.security.auth.moduleProvides implementations of [LoginModule](../../../../../../java.base/javax/security/auth/spi/LoginModule.html).Since:1.4

- Related PackagesPackageDescription[com.sun.security.auth](../package-summary.html)Provides implementations of [Principal](../../../../../../java.base/java/security/Principal.html).[com.sun.security.auth.callback](../callback/package-summary.html)Provides an implementation of [CallbackHandler](../../../../../../java.base/javax/security/auth/callback/CallbackHandler.html).[com.sun.security.auth.login](../login/package-summary.html)Provides an implementation of [Configuration](../../../../../../java.base/javax/security/auth/login/Configuration.html).
- ClassesClassDescription[JndiLoginModule](JndiLoginModule.html)The module prompts for a username and password and then verifies the password against the password stored in a directory service configured under JNDI.[KeyStoreLoginModule](KeyStoreLoginModule.html)Provides a JAAS login module that prompts for a key store alias and populates the subject with the alias's principal and credentials.[Krb5LoginModule](Krb5LoginModule.html)This `LoginModule` authenticates users using Kerberos protocols.[LdapLoginModule](LdapLoginModule.html)This [LoginModule](../../../../../../java.base/javax/security/auth/spi/LoginModule.html) performs LDAP-based authentication.[NTLoginModule](NTLoginModule.html)This `LoginModule` renders a user's NT security information as some number of `Principal`s and associates them with a `Subject`.[NTSystem](NTSystem.html)This class implementation retrieves and makes available NT security information for the current user.[UnixLoginModule](UnixLoginModule.html)This `LoginModule` imports a user's Unix `Principal` information (`UnixPrincipal`, `UnixNumericUserPrincipal`, and `UnixNumericGroupPrincipal`) and associates them with the current `Subject`.[UnixSystem](UnixSystem.html)This class implementation retrieves and makes available Unix UID/GID/groups information for the current user.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
