Module[jdk.dynalink](../../../module-summary.html)

# Package jdk.dynalink.support

package jdk.dynalink.support

Contains classes that make using Dynalink more convenient by providing basic implementations of some classes as well as various utilities. 

Since:9

- Related PackagesPackageDescription[jdk.dynalink](../package-summary.html)Contains interfaces and classes that are used to link an `invokedynamic` call site.[jdk.dynalink.beans](../beans/package-summary.html)Contains the linker for ordinary Java objects.[jdk.dynalink.linker](../linker/package-summary.html) Contains interfaces and classes needed by language runtimes to implement their own language-specific object models and type conversions.
- ClassesClassDescription[AbstractRelinkableCallSite](AbstractRelinkableCallSite.html)A basic implementation of the [RelinkableCallSite](../RelinkableCallSite.html) as a [MutableCallSite](../../../../java.base/java/lang/invoke/MutableCallSite.html).[ChainedCallSite](ChainedCallSite.html)A relinkable call site that implements a polymorphic inline caching strategy.[SimpleRelinkableCallSite](SimpleRelinkableCallSite.html)A relinkable call site that implements monomorphic inline caching strategy, only being linked to a single [GuardedInvocation](../linker/GuardedInvocation.html) at any given time.
