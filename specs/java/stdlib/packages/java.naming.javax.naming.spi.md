Module[java.naming](../../../module-summary.html)

# Package javax.naming.spi

package javax.naming.spiProvides the means for dynamically plugging in support for accessing naming and directory services through the `javax.naming` and related packages. 

 This package defines the service provider interface (SPI) of the Java Naming and Directory Interface (JNDI). JNDI provides naming and directory functionality to applications written in the Java programming language. It is designed to be independent of any specific naming or directory service implementation. Thus a variety of services--new, emerging, and already deployed ones--can be accessed in a common way. 

 The JNDI SPI provides the means for creating JNDI service providers, through which JNDI applications access different naming and directory services. 

## Plug-in Architecture

 The service provider package allows different implementations to be plugged in dynamically. These different implementations include those for the initial context, and implementations for contexts that can be reached from the initial context. 

## Java Object Support

 The service provider package provides support for implementors of the `javax.naming.Context.lookup()` method and related methods to return Java objects that are natural and intuitive for the Java programmer. For example, when looking up a printer name from the directory, it is natural for you to expect to get back a printer object on which to operate. 

## Multiple Naming Systems (Federation)

 JNDI operations allow applications to supply names that span multiple naming systems. So in the process of completing an operation, one service provider might need to interact with another service provider, for example, to pass on the operation to be continued in the next naming system. The service provider package provides support for different providers to cooperate to complete JNDI operations. 

## Package Specification

 The JNDI SPI Specification and related documents can be found in the [JNDI documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=jndi_overview).Since:1.3

- Related PackagesPackageDescription[javax.naming](../package-summary.html)Provides the classes and interfaces for accessing naming services.[javax.naming.directory](../directory/package-summary.html)Extends the `javax.naming` package to provide functionality for accessing directory services.[javax.naming.event](../event/package-summary.html)Provides support for event notification when accessing naming and directory services.[javax.naming.ldap](../ldap/package-summary.html)Provides support for LDAPv3 extended operations and controls.
- All Classes and InterfacesInterfacesClassesClassDescription[DirectoryManager](DirectoryManager.html)This class contains methods for supporting `DirContext` implementations.[DirObjectFactory](DirObjectFactory.html)This interface represents a factory for creating an object given an object and attributes about the object.[DirStateFactory](DirStateFactory.html)This interface represents a factory for obtaining the state of an object and corresponding attributes for binding.[DirStateFactory.Result](DirStateFactory.Result.html)An object/attributes pair for returning the result of DirStateFactory.getStateToBind().[InitialContextFactory](InitialContextFactory.html)This interface represents a factory that creates an initial context.[InitialContextFactoryBuilder](InitialContextFactoryBuilder.html)This interface represents a builder that creates initial context factories.[NamingManager](NamingManager.html)This class contains methods for creating context objects and objects referred to by location information in the naming or directory service.[ObjectFactory](ObjectFactory.html)This interface represents a factory for creating an object.[ObjectFactoryBuilder](ObjectFactoryBuilder.html)This interface represents a builder that creates object factories.[Resolver](Resolver.html)This interface represents an "intermediate context" for name resolution.[ResolveResult](ResolveResult.html)This class represents the result of resolution of a name.[StateFactory](StateFactory.html)This interface represents a factory for obtaining the state of an object for binding.
