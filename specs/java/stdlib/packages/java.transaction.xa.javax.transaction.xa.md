Module[java.transaction.xa](../../../module-summary.html)

# Package javax.transaction.xa

package javax.transaction.xaProvides the API that defines the contract between the transaction manager and the resource manager, which allows the transaction manager to enlist and delist resource objects (supplied by the resource manager driver) in JTA transactions. The driver vendor for a specific resource manager provides the implementation of this API.Since:1.4

- All Classes and InterfacesInterfacesException ClassesClassDescription[XAException](XAException.html)The XAException is thrown by the Resource Manager (RM) to inform the Transaction Manager of an error encountered by the involved transaction.[XAResource](XAResource.html)The XAResource interface is a Java mapping of the industry standard XA interface based on the X/Open CAE Specification (Distributed Transaction Processing: The XA Specification).[Xid](Xid.html)The Xid interface is a Java mapping of the X/Open transaction identifier XID structure.
