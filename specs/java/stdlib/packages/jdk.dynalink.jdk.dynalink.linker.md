jdk.dynalink.linker (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

[SEARCH](../../../../search.html)Module[jdk.dynalink](../../../module-summary.html)

# Package jdk.dynalink.linker

package jdk.dynalink.linker

 Contains interfaces and classes needed by language runtimes to implement their own language-specific object models and type conversions. The main entry point is the [GuardingDynamicLinker](GuardingDynamicLinker.html) interface. It needs to be implemented in order to provide linking for the runtime's own object model. A language runtime can have more than one guarding dynamic linker implementation. When a runtime is configuring Dynalink for itself, it will normally set these guarding linkers as the prioritized linkers in its [DynamicLinkerFactory](../DynamicLinkerFactory.html) (and maybe some of them as fallback linkers, for e.g. handling "method not found" and similar errors in a language-specific manner if no other linker managed to handle the operation.) 

 A language runtime that wishes to make at least some of its linkers available to other language runtimes for interoperability will need to use a [GuardingDynamicLinkerExporter](GuardingDynamicLinkerExporter.html). 

 Most language runtimes will be able to implement their own linking logic by implementing [TypeBasedGuardingDynamicLinker](TypeBasedGuardingDynamicLinker.html) instead of [GuardingDynamicLinker](GuardingDynamicLinker.html); it allows for faster type-based linking dispatch. 

 Language runtimes that allow type conversions other than those provided by Java will need to have their guarding dynamic linker (or linkers) also implement the [GuardingTypeConverterFactory](GuardingTypeConverterFactory.html) interface to provide the logic for these conversions. 

Since:9

- Related PackagesPackageDescription[jdk.dynalink](../package-summary.html)Contains interfaces and classes that are used to link an `invokedynamic` call site.[jdk.dynalink.linker.support](support/package-summary.html)Contains classes that make it more convenient for language runtimes to implement their own language-specific object models and type conversions by providing basic implementations of some classes as well as various utilities.[jdk.dynalink.beans](../beans/package-summary.html)Contains the linker for ordinary Java objects.[jdk.dynalink.support](../support/package-summary.html)Contains classes that make using Dynalink more convenient by providing basic implementations of some classes as well as various utilities.
- All Classes and InterfacesInterfacesClassesEnum ClassesClassDescription[ConversionComparator](ConversionComparator.html)Optional interface to be implemented by [GuardingTypeConverterFactory](GuardingTypeConverterFactory.html) implementers.[ConversionComparator.Comparison](ConversionComparator.Comparison.html)Enumeration of possible outcomes of comparing one conversion to another.[GuardedInvocation](GuardedInvocation.html)Represents a conditionally valid method handle.[GuardedInvocationTransformer](GuardedInvocationTransformer.html)Interface for objects that are used to transform one guarded invocation into another one.[GuardingDynamicLinker](GuardingDynamicLinker.html)The base interface for language-specific dynamic linkers.[GuardingDynamicLinkerExporter](GuardingDynamicLinkerExporter.html)A class acting as a supplier of guarding dynamic linkers that can be automatically loaded by other language runtimes.[GuardingTypeConverterFactory](GuardingTypeConverterFactory.html)Optional interface that can be implemented by [GuardingDynamicLinker](GuardingDynamicLinker.html) implementations to provide language-specific type conversion capabilities.[LinkerServices](LinkerServices.html)Interface for services provided to [GuardingDynamicLinker](GuardingDynamicLinker.html) instances by the [DynamicLinker](../DynamicLinker.html) that owns them.[LinkRequest](LinkRequest.html)Represents a request to link a particular invocation at a particular call site.[MethodHandleTransformer](MethodHandleTransformer.html)A generic interface describing operations that transform method handles.[MethodTypeConversionStrategy](MethodTypeConversionStrategy.html)Interface for objects representing a strategy for converting a method handle to a new type.[TypeBasedGuardingDynamicLinker](TypeBasedGuardingDynamicLinker.html)A guarding dynamic linker that can determine whether it can link the call site solely based on the type of the first argument at linking invocation time.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
