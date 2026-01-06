Module[jdk.dynalink](../../../../module-summary.html)

# Package jdk.dynalink.linker.support

package jdk.dynalink.linker.support

Contains classes that make it more convenient for language runtimes to implement their own language-specific object models and type conversions by providing basic implementations of some classes as well as various utilities. 

Since:9

- Related PackagesPackageDescription[jdk.dynalink.linker](../package-summary.html) Contains interfaces and classes needed by language runtimes to implement their own language-specific object models and type conversions.
- ClassesClassDescription[CompositeGuardingDynamicLinker](CompositeGuardingDynamicLinker.html)A [GuardingDynamicLinker](../GuardingDynamicLinker.html) that delegates sequentially to a list of other guarding dynamic linkers in its [CompositeGuardingDynamicLinker.getGuardedInvocation(LinkRequest, LinkerServices)](CompositeGuardingDynamicLinker.html#getGuardedInvocation(jdk.dynalink.linker.LinkRequest,jdk.dynalink.linker.LinkerServices)).[CompositeTypeBasedGuardingDynamicLinker](CompositeTypeBasedGuardingDynamicLinker.html)A composite type-based guarding dynamic linker.[DefaultInternalObjectFilter](DefaultInternalObjectFilter.html)Default implementation for a [DynamicLinkerFactory.setInternalObjectsFilter(MethodHandleTransformer)](../../DynamicLinkerFactory.html#setInternalObjectsFilter(jdk.dynalink.linker.MethodHandleTransformer)) that delegates to a pair of filtering method handles.[Guards](Guards.html)Utility methods for creating typical guards for [MethodHandles.guardWithTest(MethodHandle, MethodHandle, MethodHandle)](../../../../../java.base/java/lang/invoke/MethodHandles.html#guardWithTest(java.lang.invoke.MethodHandle,java.lang.invoke.MethodHandle,java.lang.invoke.MethodHandle)) and for adjusting their method types.[Lookup](Lookup.html)A wrapper around [MethodHandles.Lookup](../../../../../java.base/java/lang/invoke/MethodHandles.Lookup.html) that masks checked exceptions.[SimpleLinkRequest](SimpleLinkRequest.html)Default simple implementation of [LinkRequest](../LinkRequest.html).[TypeUtilities](TypeUtilities.html)Various static utility methods for working with Java types.
