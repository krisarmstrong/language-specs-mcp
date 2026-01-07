java.rmi.dgc (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

# Package java.rmi.dgc

package java.rmi.dgcProvides classes and interface for RMI distributed garbage-collection (DGC). When the RMI server returns an object to its client (caller of the remote method), it tracks the remote object's usage in the client. When there are no more references to the remote object on the client, or if the reference's ``lease'' expires and not renewed, the server garbage-collects the remote object.Since:1.1

- Related PackagesPackageDescription[java.rmi](../package-summary.html)Provides the RMI package.[java.rmi.registry](../registry/package-summary.html)Provides a class and two interfaces for the RMI registry.[java.rmi.server](../server/package-summary.html)Provides classes and interfaces for supporting the server side of RMI.
- All Classes and InterfacesInterfacesClassesClassDescription[DGC](DGC.html)The DGC abstraction is used for the server side of the distributed garbage collection algorithm.[Lease](Lease.html)A lease contains a unique VM identifier and a lease duration.[VMID](VMID.html)A VMID is a identifier that is unique across all Java virtual machines.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
