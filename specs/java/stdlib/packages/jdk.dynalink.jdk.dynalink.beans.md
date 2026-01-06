Module[jdk.dynalink](../../../module-summary.html)

# Package jdk.dynalink.beans

package jdk.dynalink.beansContains the linker for ordinary Java objects.Since:9

- Related PackagesPackageDescription[jdk.dynalink](../package-summary.html)Contains interfaces and classes that are used to link an `invokedynamic` call site.[jdk.dynalink.linker](../linker/package-summary.html) Contains interfaces and classes needed by language runtimes to implement their own language-specific object models and type conversions.[jdk.dynalink.support](../support/package-summary.html)Contains classes that make using Dynalink more convenient by providing basic implementations of some classes as well as various utilities.
- All Classes and InterfacesInterfacesClassesClassDescription[BeansLinker](BeansLinker.html)A linker for ordinary Java objects.[MissingMemberHandlerFactory](MissingMemberHandlerFactory.html)A factory for creating method handles for linking missing member behavior in [BeansLinker](BeansLinker.html).[StaticClass](StaticClass.html)Object that allows access to the static members of a class (its static methods, properties, and fields), as well as construction of instances using [StandardOperation.NEW](../StandardOperation.html#NEW) operation.
