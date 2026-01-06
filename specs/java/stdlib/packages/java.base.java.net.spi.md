Module[java.base](../../../module-summary.html)

# Package java.net.spi

package java.net.spiService-provider classes for the [java.net](../package-summary.html) package. 

 Only developers who are defining new URL stream handler providers or implementing a custom resolver provider should need to make direct use of this package.

Since:9

- Related PackagesModulePackageDescription[java.base](../../../module-summary.html)[java.net](../package-summary.html)Provides the classes for implementing networking applications.[java.net.http](../../../../java.net.http/module-summary.html)[java.net.http](../../../../java.net.http/java/net/http/package-summary.html)HTTP Client and WebSocket APIs
- All Classes and InterfacesInterfacesClassesClassDescription[InetAddressResolver](InetAddressResolver.html)This interface defines operations for looking up host names and IP addresses.[InetAddressResolver.LookupPolicy](InetAddressResolver.LookupPolicy.html)A `LookupPolicy` object describes characteristics that can be applied to a lookup operation.[InetAddressResolverProvider](InetAddressResolverProvider.html)Service-provider class for [InetAddress resolvers](InetAddressResolver.html).[InetAddressResolverProvider.Configuration](InetAddressResolverProvider.Configuration.html)A `Configuration` object is supplied to the [InetAddressResolverProvider.get(Configuration)](InetAddressResolverProvider.html#get(java.net.spi.InetAddressResolverProvider.Configuration)) method when setting the system-wide resolver.[URLStreamHandlerProvider](URLStreamHandlerProvider.html)URL stream handler service-provider class.
