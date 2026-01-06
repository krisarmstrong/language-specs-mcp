Module[java.management](../../../module-summary.html)

# Package javax.management.remote

package javax.management.remote

Interfaces for remote access to JMX MBean servers. This package defines the essential interfaces for making a JMX MBean server manageable remotely. 

JMX defines the notion of connectors. A connector is attached to a JMX API MBean server and makes it accessible to remote Java clients. The client end of a connector exports essentially the same interface as the MBean server, specifically the [MBeanServerConnection](../MBeanServerConnection.html) interface.

A connector makes an MBean server remotely accessible through a given protocol. 

- The JMX Remote API defines a standard connector, the RMI Connector, which provides remote access to an MBeanServer through RMI. 
- Other connector protocols are also possible using the [JMXConnectorFactory](JMXConnectorFactory.html). 

## Connector addresses

Typically, a connector server has an address, represented by the class [JMXServiceURL](JMXServiceURL.html). An address for the RMI Connector can look like this:

```

      service:jmx:rmi:///jndi/rmi://myhost:1099/myname
      
```

In this `JMXServiceURL`, the first `rmi:` specifies the RMI connector, while the second `rmi:` specifies the RMI registry into which the RMI connector server has stored its stub. 

The example above shows only one form of address. An address for the RMI Connector can take several forms, as detailed in the documentation for the package [javax.management.remote.rmi](../../../../java.management.rmi/javax/management/remote/rmi/package-summary.html).

## Creating a connector server

A connector server is created by constructing an instance of a subclass of [JMXConnectorServer](JMXConnectorServer.html). Usually, this instance is created using the method [JMXConnectorServerFactory.newJMXConnectorServer](JMXConnectorServerFactory.html#newJMXConnectorServer(javax.management.remote.JMXServiceURL,java.util.Map,javax.management.MBeanServer)).

Typically, a connector server is associated with an MBean server either by registering it in that MBean server, or by supplying the MBean server as a parameter when creating the connector server.

## Creating a connector client

A connector client is usually created by supplying the `JMXServiceURL` of the connector server to connect to to the [JMXConnectorFactory.connect](JMXConnectorFactory.html#connect(javax.management.remote.JMXServiceURL)) method.

For more specialized uses, a connector client can be created by directly instantiating a class that implements the [JMXConnector](JMXConnector.html) interface, for example the class [RMIConnector](../../../../java.management.rmi/javax/management/remote/rmi/RMIConnector.html).

## Additional client or server parameters

When creating a connector client or server, it is possible to supply an object of type [Map](../../../../java.base/java/util/Map.html) that defines additional parameters. Each entry in this Map has a key that is a string and an associated value whose type is appropriate for that key. The standard keys defined by the JMX Remote API all begin with the string "`jmx.remote.`". The document JMX Remote API lists these standard keys.

## Connection identifiers

Every connection opened by a connector server has a string identifier, called its connection id. This identifier appears in the [JMXConnectionNotification](JMXConnectionNotification.html) events emitted by the connector server, in the list returned by [getConnectionIds()](JMXConnectorServerMBean.html#getConnectionIds()), and in the value returned by the client's [getConnectionId()](JMXConnector.html#getConnectionId()) method.

As an example, a connection ID can look something like this:

```

rmi://192.18.1.9 username 1
      
```

The formal grammar for connection ids that follow this convention is as follows (using the grammar notation from section 2.4 of The Java Language Specification):

```

ConnectionId:
    Protocol : ClientAddressopt Space ClientIdopt Space ArbitraryText

ClientAddress:
    // HostAddress ClientPortopt

ClientPort
    : HostPort
      
```

The `Protocol` is a protocol that would be recognized by [JMXConnectorFactory](JMXConnectorFactory.html).

The `ClientAddress` is the address and port of the connecting client, if these can be determined, otherwise nothing. The `HostAddress` is the Internet address of the host that the client is connecting from, in numeric or DNS form. Numeric IPv6 addresses are enclosed in square brackets `[]`. The `HostPort` is the decimal port number that the client is connecting from.

The `ClientId` is the identity of the client entity, typically a string returned by [JMXPrincipal.getName()](JMXPrincipal.html#getName()). This string must not contain spaces.

The `ArbitraryText` is any additional text that the connector server adds when creating the client id. At a minimum, it must be enough to distinguish this connection ID from the ID of any other connection currently opened by this connector server.

Since:1.5See Also:

- [JMX Specification, version 1.4](https://jcp.org/aboutJava/communityprocess/mrel/jsr160/index2.html)

- Related PackagesModulePackageDescription[java.management](../../../module-summary.html)[javax.management](../package-summary.html)Provides the core classes for the Java Management Extensions.[java.management.rmi](../../../../java.management.rmi/module-summary.html)[javax.management.remote.rmi](../../../../java.management.rmi/javax/management/remote/rmi/package-summary.html)The RMI connector is a connector for the JMX Remote API that uses RMI to transmit client requests to a remote MBean server.
- All Classes and InterfacesInterfacesClassesException ClassesClassDescription[JMXAddressable](JMXAddressable.html)Implemented by objects that can have a `JMXServiceURL` address.[JMXAuthenticator](JMXAuthenticator.html)Interface to define how remote credentials are converted into a JAAS Subject.[JMXConnectionNotification](JMXConnectionNotification.html)Notification emitted when a client connection is opened or closed or when notifications are lost.[JMXConnector](JMXConnector.html)The client end of a JMX API connector.[JMXConnectorFactory](JMXConnectorFactory.html)Factory to create JMX API connector clients.[JMXConnectorProvider](JMXConnectorProvider.html)A provider for creating JMX API connector clients using a given protocol.[JMXConnectorServer](JMXConnectorServer.html)Superclass of every connector server.[JMXConnectorServerFactory](JMXConnectorServerFactory.html)Factory to create JMX API connector servers.[JMXConnectorServerMBean](JMXConnectorServerMBean.html)MBean interface for connector servers.[JMXConnectorServerProvider](JMXConnectorServerProvider.html)A provider for creating JMX API connector servers using a given protocol.[JMXPrincipal](JMXPrincipal.html)The identity of a remote client of the JMX Remote API.[JMXProviderException](JMXProviderException.html)Exception thrown by [JMXConnectorFactory](JMXConnectorFactory.html) and [JMXConnectorServerFactory](JMXConnectorServerFactory.html) when a provider exists for the required protocol but cannot be used for some reason.[JMXServerErrorException](JMXServerErrorException.html)Exception thrown as the result of a remote [MBeanServer](../MBeanServer.html) method invocation when an `Error` is thrown while processing the invocation in the remote MBean server.[JMXServiceURL](JMXServiceURL.html)The address of a JMX API connector server.[MBeanServerForwarder](MBeanServerForwarder.html)An object of this class implements the MBeanServer interface and wraps another object that also implements that interface.[NotificationResult](NotificationResult.html)Result of a query for buffered notifications.[SubjectDelegationPermission](SubjectDelegationPermission.html)Permission required by an authentication identity to perform operations on behalf of an authorization identity.[TargetedNotification](TargetedNotification.html)A (Notification, Listener ID) pair.
