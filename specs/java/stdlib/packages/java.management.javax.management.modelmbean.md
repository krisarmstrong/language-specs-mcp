Module[java.management](../../../module-summary.html)

# Package javax.management.modelmbean

package javax.management.modelmbean

Provides the definition of the ModelMBean classes. A Model MBean is an MBean that acts as a bridge between the management interface and the underlying managed resource. Both the management interface and the managed resource are specified as Java objects. The same Model MBean implementation can be reused many times with different management interfaces and managed resources, and it can provide common functionality such as persistence and caching.

A Model MBean implements the [ModelMBean](ModelMBean.html) interface. It is a [DynamicMBean](../DynamicMBean.html) whose [getMBeanInfo](../DynamicMBean.html#getMBeanInfo()) method returns an object implementing [ModelMBeanInfo](ModelMBeanInfo.html).

Every MBean has an [MBeanInfo](../MBeanInfo.html) with information about the MBean itself, and its attributes, operations, constructors, and notifications. A Model MBean augments this `MBeanInfo` with [Descriptor](../Descriptor.html)s that encode additional information in the form of (key,value) pairs. Usually, `Descriptor`s are instances of [DescriptorSupport](DescriptorSupport.html).

The class [RequiredModelMBean](RequiredModelMBean.html) provides a standard Model MBean implementation.

The following example shows a Model MBean being used to make the `get` method of a `HashMap` available for management through an MBean server. No other methods are available through the MBean server. There is nothing special about `HashMap` here. Public methods from any public class can be exposed for management in the same way.

```

import java.lang.reflect.Method;
import java.util.HashMap;
import javax.management.*;
import javax.management.modelmbean.*;

// ...

MBeanServer mbs = MBeanServerFactory.createMBeanServer();
// The MBean Server

HashMap map = new HashMap();
// The resource that will be managed

// Construct the management interface for the Model MBean
Method getMethod = HashMap.class.getMethod("get", new Class[] {Object.class});
ModelMBeanOperationInfo getInfo =
    new ModelMBeanOperationInfo("Get value for key", getMethod);
ModelMBeanInfo mmbi =
    new ModelMBeanInfoSupport(HashMap.class.getName(),
                              "Map of keys and values",
                              null,  // no attributes
                              null,  // no constructors
                              new ModelMBeanOperationInfo[] {getInfo},
                              null); // no notifications

// Make the Model MBean and link it to the resource
ModelMBean mmb = new RequiredModelMBean(mmbi);
mmb.setManagedResource(map, "ObjectReference");

// Register the Model MBean in the MBean Server
ObjectName mapName = new ObjectName(":type=Map,name=whatever");
mbs.registerMBean(mmb, mapName);

// Resource can evolve independently of the MBean
map.put("key", "value");

// Can access the "get" method through the MBean Server
mbs.invoke(mapName, "get", new Object[] {"key"}, new String[] {Object.class.getName()});
// returns "value"
    
```

## Package Specification

- See the JMX 1.4 Specification[JMX Specification, version 1.4](https://jcp.org/aboutJava/communityprocess/mrel/jsr160/index2.html)

Since:1.5

- Related PackagesPackageDescription[javax.management](../package-summary.html)Provides the core classes for the Java Management Extensions.
- All Classes and InterfacesInterfacesClassesException ClassesClassDescription[DescriptorSupport](DescriptorSupport.html)This class represents the metadata set for a ModelMBean element.[InvalidTargetObjectTypeException](InvalidTargetObjectTypeException.html)Exception thrown when an invalid target object type is specified.[ModelMBean](ModelMBean.html)This interface must be implemented by the ModelMBeans.[ModelMBeanAttributeInfo](ModelMBeanAttributeInfo.html)The ModelMBeanAttributeInfo object describes an attribute of the ModelMBean.[ModelMBeanConstructorInfo](ModelMBeanConstructorInfo.html)The ModelMBeanConstructorInfo object describes a constructor of the ModelMBean.[ModelMBeanInfo](ModelMBeanInfo.html)This interface is implemented by the ModelMBeanInfo for every ModelMBean.[ModelMBeanInfoSupport](ModelMBeanInfoSupport.html)This class represents the meta data for ModelMBeans.[ModelMBeanNotificationBroadcaster](ModelMBeanNotificationBroadcaster.html)This interface must be implemented by the ModelMBeans.[ModelMBeanNotificationInfo](ModelMBeanNotificationInfo.html)The ModelMBeanNotificationInfo object describes a notification emitted by a ModelMBean.[ModelMBeanOperationInfo](ModelMBeanOperationInfo.html)The ModelMBeanOperationInfo object describes a management operation of the ModelMBean.[RequiredModelMBean](RequiredModelMBean.html)This class is the implementation of a ModelMBean.[XMLParseException](XMLParseException.html)This exception is thrown when an XML formatted string is being parsed into ModelMBean objects or when XML formatted strings are being created from ModelMBean objects.
