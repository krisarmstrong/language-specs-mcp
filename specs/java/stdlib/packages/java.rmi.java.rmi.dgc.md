Module[java.rmi](../../../module-summary.html)

# Package java.rmi.dgc

package java.rmi.dgcProvides classes and interface for RMI distributed garbage-collection (DGC). When the RMI server returns an object to its client (caller of the remote method), it tracks the remote object's usage in the client. When there are no more references to the remote object on the client, or if the reference's ``lease'' expires and not renewed, the server garbage-collects the remote object.Since:1.1

- Related PackagesPackageDescription[java.rmi](../package-summary.html)Provides the RMI package.[java.rmi.registry](../registry/package-summary.html)Provides a class and two interfaces for the RMI registry.[java.rmi.server](../server/package-summary.html)Provides classes and interfaces for supporting the server side of RMI.
- All Classes and InterfacesInterfacesClassesClassDescription[DGC](DGC.html)The DGC abstraction is used for the server side of the distributed garbage collection algorithm.[Lease](Lease.html)A lease contains a unique VM identifier and a lease duration.[VMID](VMID.html)A VMID is a identifier that is unique across all Java virtual machines.
