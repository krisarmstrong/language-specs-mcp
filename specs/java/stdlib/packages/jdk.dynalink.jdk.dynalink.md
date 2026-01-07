jdk.dynalink (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

- [Overview](../../../index.html)
- [Module](../../module-summary.html)
- Package
- Class
- [Use](package-use.html)
- [Tree](package-tree.html)
- [Preview](../../../preview-list.html)
- [New](../../../new-list.html)
- [Deprecated](../../../deprecated-list.html)
- [Index](../../../index-files/index-1.html)
- [Help](../../../help-doc.html#package)

- 

Package:

  - [Description](#package-description)
  - [Related Packages](#related-package-summary)
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- [Related Packages](#related-package-summary) | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../search.html)Module[jdk.dynalink](../../module-summary.html)

# Package jdk.dynalink

package jdk.dynalinkContains interfaces and classes that are used to link an `invokedynamic` call site.

- Related PackagesPackageDescription[jdk.dynalink.beans](beans/package-summary.html)Contains the linker for ordinary Java objects.[jdk.dynalink.linker](linker/package-summary.html) Contains interfaces and classes needed by language runtimes to implement their own language-specific object models and type conversions.[jdk.dynalink.support](support/package-summary.html)Contains classes that make using Dynalink more convenient by providing basic implementations of some classes as well as various utilities.
- All Classes and InterfacesInterfacesClassesEnum ClassesException ClassesClassDescription[CallSiteDescriptor](CallSiteDescriptor.html)Call site descriptors contain all the information necessary for linking a call site.[DynamicLinker](DynamicLinker.html)The linker for [RelinkableCallSite](RelinkableCallSite.html) objects.[DynamicLinkerFactory](DynamicLinkerFactory.html)A factory class for creating [DynamicLinker](DynamicLinker.html) objects.[NamedOperation](NamedOperation.html)Operation that associates a name with another operation.[Namespace](Namespace.html)An object that describes a namespace that is the target of a dynamic operation on an object.[NamespaceOperation](NamespaceOperation.html)Describes an operation that operates on at least one [Namespace](Namespace.html) of an object.[NoSuchDynamicMethodException](NoSuchDynamicMethodException.html)Thrown at the invocation if the call site can not be linked by any available [GuardingDynamicLinker](linker/GuardingDynamicLinker.html).[Operation](Operation.html)An object that describes a dynamic operation.[RelinkableCallSite](RelinkableCallSite.html)Interface for call sites managed by a [DynamicLinker](DynamicLinker.html).[SecureLookupSupplier](SecureLookupSupplier.html)Provides security-checked access to a `MethodHandles.Lookup` object.[StandardNamespace](StandardNamespace.html)An enumeration of standard namespaces defined by Dynalink.[StandardOperation](StandardOperation.html)Defines the standard dynamic operations.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
