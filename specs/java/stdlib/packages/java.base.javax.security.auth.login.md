javax.security.auth.login (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

# Package javax.security.auth.login

package javax.security.auth.loginThis package provides a pluggable authentication framework. 

## Package Specification

- [Java Security Standard Algorithm Names Specification](../../../../../../specs/security/standard-names.html)

Since:1.4

- Related PackagesModulePackageDescription[java.base](../../../../module-summary.html)[javax.security.auth](../package-summary.html)This package provides a framework for authentication and authorization.[java.base](../../../../module-summary.html)[javax.security.auth.callback](../callback/package-summary.html)This package provides the classes necessary for services to interact with applications in order to retrieve information (authentication data including usernames or passwords, for example) or to display information (error and warning messages, for example).[java.security.jgss](../../../../../java.security.jgss/module-summary.html)[javax.security.auth.kerberos](../../../../../java.security.jgss/javax/security/auth/kerberos/package-summary.html)This package contains utility classes related to the Kerberos network authentication protocol.[java.base](../../../../module-summary.html)[javax.security.auth.spi](../spi/package-summary.html)This package provides the interface to be used for implementing pluggable authentication modules.[java.base](../../../../module-summary.html)[javax.security.auth.x500](../x500/package-summary.html)This package contains the classes that should be used to store X500 Principal and X500 Private Credentials in a Subject.
- All Classes and InterfacesInterfacesClassesException ClassesClassDescription[AccountException](AccountException.html)A generic account exception.[AccountExpiredException](AccountExpiredException.html)Signals that a user account has expired.[AccountLockedException](AccountLockedException.html)Signals that an account was locked.[AccountNotFoundException](AccountNotFoundException.html)Signals that an account was not found.[AppConfigurationEntry](AppConfigurationEntry.html)This class represents a single `LoginModule` entry configured for the application specified in the `getAppConfigurationEntry(String appName)` method in the `Configuration` class.[AppConfigurationEntry.LoginModuleControlFlag](AppConfigurationEntry.LoginModuleControlFlag.html)This class represents whether a `LoginModule` is REQUIRED, REQUISITE, SUFFICIENT or OPTIONAL.[Configuration](Configuration.html)A Configuration object is responsible for specifying which LoginModules should be used for a particular application, and in what order the LoginModules should be invoked.[Configuration.Parameters](Configuration.Parameters.html)This represents a marker interface for Configuration parameters.[ConfigurationSpi](ConfigurationSpi.html)This class defines the Service Provider Interface (SPI) for the `Configuration` class.[CredentialException](CredentialException.html)A generic credential exception.[CredentialExpiredException](CredentialExpiredException.html)Signals that a `Credential` has expired.[CredentialNotFoundException](CredentialNotFoundException.html)Signals that a credential was not found.[FailedLoginException](FailedLoginException.html)Signals that user authentication failed.[LoginContext](LoginContext.html) The `LoginContext` class describes the basic methods used to authenticate Subjects and provides a way to develop an application independent of the underlying authentication technology.[LoginException](LoginException.html)This is the basic login exception.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
