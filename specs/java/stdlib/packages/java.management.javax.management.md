javax.management (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

- [Overview](../../../index.html)
- [Module](../../module-summary.html)
- Package
- Class
- [Use](package-use.html)
- [Tree](package-tree.html)
- [Preview](../../../preview-list.html)
- [New](../../../new-list.html)
- [Deprecated](../../../deprecated-list.html)
- [Index](../../../index-files/index-1.html)
- [Help](../../../help-doc.html#package)

- 

Package:

  - [Description](#package-description)
  - [Related Packages](#related-package-summary)
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- [Related Packages](#related-package-summary) | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../search.html)Module[java.management](../../module-summary.html)

# Package javax.management

package javax.management

Provides the core classes for the Java Management Extensions.

The Java Management Extensions (JMX) API is a standard API for management and monitoring. Typical uses include:

- consulting and changing application configuration
- accumulating statistics about application behavior and making them available
- notifying of state changes and erroneous conditions.

The JMX API can also be used as part of a solution for managing systems, networks, and so on.

The API includes remote access, so a remote management program can interact with a running application for these purposes.

## MBeans

The fundamental notion of the JMX API is the MBean. An MBean is a named managed object representing a resource. It has a management interface which must be public and consist of:

- named and typed attributes that can be read and/or written
- named and typed operations that can be invoked
- typed notifications that can be emitted by the MBean.

For example, an MBean representing an application's configuration could have attributes representing the different configuration items. Reading the `CacheSize` attribute would return the current value of that item. Writing it would update the item, potentially changing the behavior of the running application. An operation such as `save` could store the current configuration persistently. A notification such as `ConfigurationChangedNotification` could be sent every time the configuration is changed.

In the standard usage of the JMX API, MBeans are implemented as Java objects. However, as explained below, these objects are not usually referenced directly.

### Standard MBeans

To make MBean implementation simple, the JMX API includes the notion of Standard MBeans. A Standard MBean is one whose attributes and operations are deduced from a Java interface using certain naming patterns, similar to those used by JavaBeans. For example, consider an interface like this:

```

    public interface ConfigurationMBean {
         public int getCacheSize();
         public void setCacheSize(int size);
         public long getLastChangedTime();
         public void save();
    }
        
```

The methods `getCacheSize` and `setCacheSize` define a read-write attribute of type `int` called `CacheSize` (with an initial capital, unlike the JavaBeans convention).

The method `getLastChangedTime` defines an attribute of type `long` called `LastChangedTime`. This is a read-only attribute, since there is no method `setLastChangedTime`.

The method `save` defines an operation called `save`. It is not an attribute, since its name does not begin with `get`, `set`, or `is`.

The exact naming patterns for Standard MBeans are detailed in the [JMX Specification](#spec).

There are two ways to make a Java object that is an MBean with this management interface. One is for the object to be of a class that has exactly the same name as the Java interface but without the `MBean` suffix. So in the example the object would be of the class `Configuration`, in the same Java package as `ConfigurationMBean`. The second way is to use the [StandardMBean](StandardMBean.html) class.

### MXBeans

An MXBean is a variant of Standard MBean where complex types are mapped to a standard set of types defined in the [javax.management.openmbean](openmbean/package-summary.html) package. MXBeans are appropriate if you would otherwise need to reference application-specific classes in your MBean interface. They are described in detail in the specification for [MXBean](MXBean.html).

### Dynamic MBeans

A Dynamic MBean is an MBean that defines its management interface at run-time. For example, a configuration MBean could determine the names and types of the attributes it exposes by parsing an XML file.

Any Java object of a class that implements the [DynamicMBean](DynamicMBean.html) interface is a Dynamic MBean.

### Open MBeans

An Open MBean is a kind of Dynamic MBean where the types of attributes and of operation parameters and return values are built using a small set of predefined Java classes. Open MBeans facilitate operation with remote management programs that do not necessarily have access to application-specific types, including non-Java programs. Open MBeans are defined by the package [javax.management.openmbean](openmbean/package-summary.html).

### Model MBeans

A Model MBean is a kind of Dynamic MBean that acts as a bridge between the management interface and the underlying managed resource. Both the management interface and the managed resource are specified as Java objects. The same Model MBean implementation can be reused many times with different management interfaces and managed resources, and it can provide common functionality such as persistence and caching. Model MBeans are defined by the package [javax.management.modelmbean](modelmbean/package-summary.html).

## MBean Server

To be useful, an MBean must be registered in an MBean Server. An MBean Server is a repository of MBeans. Usually the only access to the MBeans is through the MBean Server. In other words, code no longer accesses the Java object implementing the MBean directly, but instead accesses the MBean by name through the MBean Server. Each MBean has a unique name within the MBean Server, defined by the [ObjectName](ObjectName.html) class.

An MBean Server is an object implementing the interface [MBeanServer](MBeanServer.html). The most convenient MBean Server to use is the Platform MBean Server. This is a single MBean Server that can be shared by different managed components running within the same Java Virtual Machine. The Platform MBean Server is accessed with the method [ManagementFactory.getPlatformMBeanServer()](../../java/lang/management/ManagementFactory.html#getPlatformMBeanServer()).

Application code can also create a new MBean Server, or access already-created MBean Servers, using the [MBeanServerFactory](MBeanServerFactory.html) class.

### Creating MBeans in the MBean Server

There are two ways to create an MBean. One is to construct a Java object that will be the MBean, then use the [registerMBean](MBeanServer.html#registerMBean(java.lang.Object,javax.management.ObjectName)) method to register it in the MBean Server. The other is to create and register the MBean in a single operation using one of the [createMBean](MBeanServer.html#createMBean(java.lang.String,javax.management.ObjectName)) methods.

The `registerMBean` method is simpler for local use, but cannot be used remotely. The `createMBean` method can be used remotely, but sometimes requires attention to class loading issues.

An MBean can perform actions when it is registered in or unregistered from an MBean Server if it implements the [MBeanRegistration](MBeanRegistration.html) interface.

### Accessing MBeans in the MBean Server

Given an `ObjectName``name` and an `MBeanServer``mbs`, you can access attributes and operations as in this example:

```

    int cacheSize = mbs.getAttribute(name, "CacheSize");
    AttributeAttribute.html newCacheSize =
         new Attribute("CacheSize", new Integer(2000));
    mbs.setAttribute(name, newCacheSize);
    mbs.invoke(name, "save", new Object[0], new Class[0]);
        
```

Alternatively, if you have a Java interface that corresponds to the management interface for the MBean, you can use an MBean proxy like this:

```

    ConfigurationMBean conf =
        JMX.newMBeanProxyJMX.html#newMBeanProxy(javax.management.MBeanServerConnection,javax.management.ObjectName,java.lang.Class)(mbs, name, ConfigurationMBean.class);
    int cacheSize = conf.getCacheSize();
    conf.setCacheSize(2000);
    conf.save();
        
```

Using an MBean proxy is just a convenience. The second example ends up calling the same `MBeanServer` operations as the first one.

An MBean Server can be queried for MBeans whose names match certain patterns and/or whose attributes meet certain constraints. Name patterns are constructed using the [ObjectName](ObjectName.html) class and constraints are constructed using the [Query](Query.html) class. The methods [queryNames](MBeanServer.html#queryNames(javax.management.ObjectName,javax.management.QueryExp)) and [queryMBeans](MBeanServer.html#queryMBeans(javax.management.ObjectName,javax.management.QueryExp)) then perform the query.

### MBean lifecycle

An MBean can implement the [MBeanRegistration](MBeanRegistration.html) interface in order to be told when it is registered and unregistered in the MBean Server. Additionally, the [preRegister](MBeanRegistration.html#preRegister(javax.management.MBeanServer,javax.management.ObjectName)) method allows the MBean to get a reference to the `MBeanServer` object and to get its `ObjectName` within the MBean Server.

## Notifications

A notification is an instance of the [Notification](Notification.html) class or a subclass. In addition to its Java class, it has a type string that can distinguish it from other notifications of the same class.

An MBean that will emit notifications must implement the [NotificationBroadcaster](NotificationBroadcaster.html) or [NotificationEmitter](NotificationEmitter.html) interface. Usually, it does this by subclassing [NotificationBroadcasterSupport](NotificationBroadcasterSupport.html) or delegating to an instance of that class. Here is an example:

```

    public class Configuration extends NotificationBroadcasterSupport
            implements ConfigurationMBean {
        ...
        private void updated() {
            Notification n = new Notification(...);
            sendNotificationNotificationBroadcasterSupport.html#sendNotification(javax.management.Notification)(n);
        }
    }
        
```

Notifications can be received by a listener, which is an object that implements the [NotificationListener](NotificationListener.html) interface. You can add a listener to an MBean with the method [MBeanServer.addNotificationListener(ObjectName, NotificationListener, NotificationFilter, Object)](MBeanServer.html#addNotificationListener(javax.management.ObjectName,javax.management.NotificationListener,javax.management.NotificationFilter,java.lang.Object)). You can optionally supply a filter to this method, to select only notifications of interest. A filter is an object that implements the [NotificationFilter](NotificationFilter.html) interface.

An MBean can be a listener for notifications emitted by other MBeans in the same MBean Server. In this case, it implements [NotificationListener](NotificationListener.html) and the method [MBeanServer.addNotificationListener(ObjectName, ObjectName, NotificationFilter, Object)](MBeanServer.html#addNotificationListener(javax.management.ObjectName,javax.management.ObjectName,javax.management.NotificationFilter,java.lang.Object)) is used to listen.

## Remote Access to MBeans

An MBean Server can be accessed remotely through a connector. A connector allows a remote Java application to access an MBean Server in essentially the same way as a local one. The package [javax.management.remote](remote/package-summary.html) defines connectors.

The JMX specification also defines the notion of an adaptor. An adaptor translates between requests in a protocol such as SNMP or HTML and accesses to an MBean Server. So for example an SNMP GET operation might result in a `getAttribute` on the MBean Server.

### Interoperability between versions of the JMX specification

When a client connects to a server using the JMX Remote API, it is possible that they do not have the same version of the JMX specification. The version of the JMX specification described here is version 1.4. Previous versions were 1.0, 1.1, and 1.2. (There was no 1.3.) The standard JMX Remote API is defined to work with version 1.2 onwards, so in standards-based deployment the only interoperability questions that arise concern version 1.2 onwards.

Every version of the JMX specification continues to implement the features of previous versions. So when the client is running an earlier version than the server, there should not be any interoperability concerns.

When the client is running a later version than the server, certain newer features may not be available, as detailed in the next sections. The client can determine the server's version by examining the [SpecificationVersion](MBeanServerDelegateMBean.html#getSpecificationVersion()) attribute of the `MBeanServerDelegate`.

#### If the remote MBean Server is 1.2

- 

You cannot use wildcards in a key property of an [ObjectName](ObjectName.html), for example `domain:type=Foo,name=*`. Wildcards that match whole properties are still allowed, for example `*:*` or `*:type=Foo,*`.

- 

You cannot use [Query.isInstanceOf](Query.html#isInstanceOf(javax.management.StringValueExp)) in a query.

- 

You cannot use dot syntax such as `HeapMemoryUsage.used` in the [observed attribute](monitor/Monitor.html#setObservedAttribute(java.lang.String)) of a monitor, as described in the documentation for the [javax.management.monitor](monitor/package-summary.html) package.

Since:1.5See Also:

- [JMX Specification, version 1.4](https://jcp.org/aboutJava/communityprocess/mrel/jsr160/index2.html)

- Related PackagesPackageDescription[javax.management.loading](loading/package-summary.html)Provides the classes which implement advanced dynamic loading.[javax.management.modelmbean](modelmbean/package-summary.html)Provides the definition of the ModelMBean classes.[javax.management.monitor](monitor/package-summary.html)Provides the definition of the monitor classes.[javax.management.openmbean](openmbean/package-summary.html)Provides the open data types and Open MBean descriptor classes.[javax.management.relation](relation/package-summary.html)Provides the definition of the Relation Service.[javax.management.remote](remote/package-summary.html)Interfaces for remote access to JMX MBean servers.[javax.management.timer](timer/package-summary.html)Provides the definition of the Timer MBean.
- All Classes and InterfacesInterfacesClassesException ClassesAnnotation InterfacesClassDescription[Attribute](Attribute.html)Represents an MBean attribute by associating its name with its value.[AttributeChangeNotification](AttributeChangeNotification.html)Provides definitions of the attribute change notifications sent by MBeans.[AttributeChangeNotificationFilter](AttributeChangeNotificationFilter.html)This class implements of the [NotificationFilter](NotificationFilter.html) interface for the [attribute change notification](AttributeChangeNotification.html).[AttributeList](AttributeList.html)Represents a list of values for attributes of an MBean.[AttributeNotFoundException](AttributeNotFoundException.html)The specified attribute does not exist or cannot be retrieved.[AttributeValueExp](AttributeValueExp.html)Represents attributes used as arguments to relational constraints.[BadAttributeValueExpException](BadAttributeValueExpException.html)Thrown when an invalid MBean attribute is passed to a query constructing method.[BadBinaryOpValueExpException](BadBinaryOpValueExpException.html)Thrown when an invalid expression is passed to a method for constructing a query.[BadStringOperationException](BadStringOperationException.html)Thrown when an invalid string operation is passed to a method for constructing a query.[ConstructorParameters](ConstructorParameters.html) An annotation on a constructor that shows how the parameters of that constructor correspond to the constructed object's getter methods.[DefaultLoaderRepository](DefaultLoaderRepository.html)Deprecated. Use [MBeanServer.getClassLoaderRepository()](MBeanServer.html#getClassLoaderRepository()) instead.[Descriptor](Descriptor.html)Additional metadata for a JMX element.[DescriptorAccess](DescriptorAccess.html)This interface is used to gain access to descriptors of the Descriptor class which are associated with a JMX component, i.e.[DescriptorKey](DescriptorKey.html)Meta-annotation that describes how an annotation element relates to a field in a [Descriptor](Descriptor.html).[DescriptorRead](DescriptorRead.html)Interface to read the Descriptor of a management interface element such as an MBeanInfo.[DynamicMBean](DynamicMBean.html)Defines the methods that should be implemented by a Dynamic MBean (MBean that exposes a dynamic management interface).[ImmutableDescriptor](ImmutableDescriptor.html)An immutable descriptor.[InstanceAlreadyExistsException](InstanceAlreadyExistsException.html)The MBean is already registered in the repository.[InstanceNotFoundException](InstanceNotFoundException.html)The specified MBean does not exist in the repository.[IntrospectionException](IntrospectionException.html)An exception occurred during the introspection of an MBean.[InvalidApplicationException](InvalidApplicationException.html)Thrown when an attempt is made to apply either of the following: A subquery expression to an MBean or a qualified attribute expression to an MBean of the wrong class.[InvalidAttributeValueException](InvalidAttributeValueException.html)The value specified is not valid for the attribute.[JMException](JMException.html)Exceptions thrown by JMX implementations.[JMRuntimeException](JMRuntimeException.html)Runtime exceptions emitted by JMX implementations.[JMX](JMX.html)Static methods from the JMX API.[ListenerNotFoundException](ListenerNotFoundException.html)The specified MBean listener does not exist in the repository.[MalformedObjectNameException](MalformedObjectNameException.html)The format of the string does not correspond to a valid ObjectName.[MBeanAttributeInfo](MBeanAttributeInfo.html)Describes an MBean attribute exposed for management.[MBeanConstructorInfo](MBeanConstructorInfo.html)Describes a constructor exposed by an MBean.[MBeanException](MBeanException.html)Represents "user defined" exceptions thrown by MBean methods in the agent.[MBeanFeatureInfo](MBeanFeatureInfo.html)Provides general information for an MBean descriptor object.[MBeanInfo](MBeanInfo.html)Describes the management interface exposed by an MBean; that is, the set of attributes and operations which are available for management operations.[MBeanNotificationInfo](MBeanNotificationInfo.html)The `MBeanNotificationInfo` class is used to describe the characteristics of the different notification instances emitted by an MBean, for a given Java class of notification.[MBeanOperationInfo](MBeanOperationInfo.html)Describes a management operation exposed by an MBean.[MBeanParameterInfo](MBeanParameterInfo.html)Describes an argument of an operation exposed by an MBean.[MBeanPermission](MBeanPermission.html)Permission controlling access to MBeanServer operations.[MBeanRegistration](MBeanRegistration.html)Can be implemented by an MBean in order to carry out operations before and after being registered or unregistered from the MBean Server.[MBeanRegistrationException](MBeanRegistrationException.html)Wraps exceptions thrown by the preRegister(), preDeregister() methods of the `MBeanRegistration` interface.[MBeanServer](MBeanServer.html)This is the interface for MBean manipulation on the agent side.[MBeanServerBuilder](MBeanServerBuilder.html)This class represents a builder that creates a default [MBeanServer](MBeanServer.html) implementation.[MBeanServerConnection](MBeanServerConnection.html)This interface represents a way to talk to an MBean server, whether local or remote.[MBeanServerDelegate](MBeanServerDelegate.html)Represents the MBean server from the management point of view.[MBeanServerDelegateMBean](MBeanServerDelegateMBean.html)Defines the management interface of an object of class MBeanServerDelegate.[MBeanServerFactory](MBeanServerFactory.html)Provides MBean server references.[MBeanServerInvocationHandler](MBeanServerInvocationHandler.html)[InvocationHandler](../../../java.base/java/lang/reflect/InvocationHandler.html) that forwards methods in an MBean's management interface through the MBean server to the MBean.[MBeanServerNotification](MBeanServerNotification.html)Represents a notification emitted by the MBean Server through the MBeanServerDelegate MBean.[MBeanServerPermission](MBeanServerPermission.html)A Permission to perform actions related to MBeanServers.[MBeanTrustPermission](MBeanTrustPermission.html)This permission represents "trust" in a signer or codebase.[MXBean](MXBean.html)Annotation to mark an interface explicitly as being an MXBean interface, or as not being an MXBean interface.[NotCompliantMBeanException](NotCompliantMBeanException.html)Exception which occurs when trying to register an object in the MBean server that is not a JMX compliant MBean.[Notification](Notification.html)The Notification class represents a notification emitted by an MBean.[NotificationBroadcaster](NotificationBroadcaster.html)Interface implemented by an MBean that emits Notifications.[NotificationBroadcasterSupport](NotificationBroadcasterSupport.html)Provides an implementation of [NotificationEmitter](NotificationEmitter.html) interface.[NotificationEmitter](NotificationEmitter.html)Interface implemented by an MBean that emits Notifications.[NotificationFilter](NotificationFilter.html)To be implemented by a any class acting as a notification filter.[NotificationFilterSupport](NotificationFilterSupport.html)Provides an implementation of the [NotificationFilter](NotificationFilter.html) interface.[NotificationListener](NotificationListener.html)Should be implemented by an object that wants to receive notifications.[ObjectInstance](ObjectInstance.html)Used to represent the object name of an MBean and its class name.[ObjectName](ObjectName.html)Represents the object name of an MBean, or a pattern that can match the names of several MBeans.[OperationsException](OperationsException.html)Represents exceptions thrown in the MBean server when performing operations on MBeans.[PersistentMBean](PersistentMBean.html)This class is the interface to be implemented by MBeans that are meant to be persistent.[Query](Query.html)Constructs query object constraints.[QueryEval](QueryEval.html)Allows a query to be performed in the context of a specific MBean server.[QueryExp](QueryExp.html)Represents relational constraints similar to database query "where clauses".[ReflectionException](ReflectionException.html)Represents exceptions thrown in the MBean server when using the java.lang.reflect classes to invoke methods on MBeans.[RuntimeErrorException](RuntimeErrorException.html)When a `java.lang.Error` occurs in the agent it should be caught and re-thrown as a `RuntimeErrorException`.[RuntimeMBeanException](RuntimeMBeanException.html)Represents runtime exceptions thrown by MBean methods in the agent.[RuntimeOperationsException](RuntimeOperationsException.html)Represents runtime exceptions thrown in the agent when performing operations on MBeans.[ServiceNotFoundException](ServiceNotFoundException.html)Represents exceptions raised when a requested service is not supported.[StandardEmitterMBean](StandardEmitterMBean.html)An MBean whose management interface is determined by reflection on a Java interface, and that emits notifications.[StandardMBean](StandardMBean.html)An MBean whose management interface is determined by reflection on a Java interface.[StringValueExp](StringValueExp.html)Represents strings that are arguments to relational constraints.[ValueExp](ValueExp.html)Represents values that can be passed as arguments to relational expressions.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
