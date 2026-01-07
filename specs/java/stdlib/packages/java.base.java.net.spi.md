java.net.spi (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

# Package java.net.spi

package java.net.spiService-provider classes for the [java.net](../package-summary.html) package. 

 Only developers who are defining new URL stream handler providers or implementing a custom resolver provider should need to make direct use of this package.

Since:9

- Related PackagesModulePackageDescription[java.base](../../../module-summary.html)[java.net](../package-summary.html)Provides the classes for implementing networking applications.[java.net.http](../../../../java.net.http/module-summary.html)[java.net.http](../../../../java.net.http/java/net/http/package-summary.html)HTTP Client and WebSocket APIs
- All Classes and InterfacesInterfacesClassesClassDescription[InetAddressResolver](InetAddressResolver.html)This interface defines operations for looking up host names and IP addresses.[InetAddressResolver.LookupPolicy](InetAddressResolver.LookupPolicy.html)A `LookupPolicy` object describes characteristics that can be applied to a lookup operation.[InetAddressResolverProvider](InetAddressResolverProvider.html)Service-provider class for [InetAddress resolvers](InetAddressResolver.html).[InetAddressResolverProvider.Configuration](InetAddressResolverProvider.Configuration.html)A `Configuration` object is supplied to the [InetAddressResolverProvider.get(Configuration)](InetAddressResolverProvider.html#get(java.net.spi.InetAddressResolverProvider.Configuration)) method when setting the system-wide resolver.[URLStreamHandlerProvider](URLStreamHandlerProvider.html)URL stream handler service-provider class.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
