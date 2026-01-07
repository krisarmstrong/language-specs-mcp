java.rmi.registry (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

[SEARCH](../../../../search.html)Module[java.rmi](../../../module-summary.html)

# Package java.rmi.registry

package java.rmi.registryProvides a class and two interfaces for the RMI registry. A registry is a remote object that maps names to remote objects. A server registers its remote objects with the registry so that they can be looked up. When an object wants to invoke a method on a remote object, it must first lookup the remote object using its name. The registry returns to the calling object a reference to the remote object, using which a remote method can be invoked.Since:1.1

- Related PackagesPackageDescription[java.rmi](../package-summary.html)Provides the RMI package.[java.rmi.dgc](../dgc/package-summary.html)Provides classes and interface for RMI distributed garbage-collection (DGC).[java.rmi.server](../server/package-summary.html)Provides classes and interfaces for supporting the server side of RMI.
- All Classes and InterfacesInterfacesClassesClassDescription[LocateRegistry](LocateRegistry.html)`LocateRegistry` is used to obtain a reference to a bootstrap remote object registry on a particular host (including the local host), or to create a remote object registry that accepts calls on a specific port.[Registry](Registry.html)`Registry` is a remote interface to a simple remote object registry that provides methods for storing and retrieving remote object references bound with arbitrary string names.[RegistryHandler](RegistryHandler.html)Deprecated. no replacement

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
