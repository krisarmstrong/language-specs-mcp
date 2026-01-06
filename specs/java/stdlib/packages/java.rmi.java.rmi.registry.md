Module[java.rmi](../../../module-summary.html)

# Package java.rmi.registry

package java.rmi.registryProvides a class and two interfaces for the RMI registry. A registry is a remote object that maps names to remote objects. A server registers its remote objects with the registry so that they can be looked up. When an object wants to invoke a method on a remote object, it must first lookup the remote object using its name. The registry returns to the calling object a reference to the remote object, using which a remote method can be invoked.Since:1.1

- Related PackagesPackageDescription[java.rmi](../package-summary.html)Provides the RMI package.[java.rmi.dgc](../dgc/package-summary.html)Provides classes and interface for RMI distributed garbage-collection (DGC).[java.rmi.server](../server/package-summary.html)Provides classes and interfaces for supporting the server side of RMI.
- All Classes and InterfacesInterfacesClassesClassDescription[LocateRegistry](LocateRegistry.html)`LocateRegistry` is used to obtain a reference to a bootstrap remote object registry on a particular host (including the local host), or to create a remote object registry that accepts calls on a specific port.[Registry](Registry.html)`Registry` is a remote interface to a simple remote object registry that provides methods for storing and retrieving remote object references bound with arbitrary string names.[RegistryHandler](RegistryHandler.html)Deprecated. no replacement
