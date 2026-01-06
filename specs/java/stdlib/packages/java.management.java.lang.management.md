Module[java.management](../../../module-summary.html)

# Package java.lang.management

package java.lang.managementProvides the management interfaces for monitoring and management of the Java virtual machine and other components in the Java runtime. It allows both local and remote monitoring and management of the running Java virtual machine. 

## Platform MXBean

 A platform MXBean is a managed bean that conforms to the [JMX](../../../javax/management/package-summary.html) Instrumentation Specification and only uses a set of basic data types. Each platform MXBean is a [PlatformManagedObject](PlatformManagedObject.html) with a unique [name](PlatformManagedObject.html#getObjectName()). 

## ManagementFactory

The [ManagementFactory](ManagementFactory.html) class is the management factory class for the Java platform. This class provides a set of static factory methods to obtain the MXBeans for the Java platform to allow an application to access the MXBeans directly. 

A platform MBeanServer can be accessed with the [getPlatformMBeanServer](ManagementFactory.html#getPlatformMBeanServer()) method. On the first call to this method, it creates the platform MBeanServer and registers all platform MXBeans including [platform MXBeans](PlatformManagedObject.html). Each platform MXBean is registered with a unique name defined in the specification of the management interface. This is a single MBeanServer that can be shared by different managed components running within the same Java virtual machine. 

## Interoperability

A management application and a platform MBeanServer of a running virtual machine can interoperate without requiring classes used by the platform MXBean interfaces. The data types being transmitted between the JMX connector server and the connector client are JMX [open types](../../../javax/management/openmbean/OpenType.html) and this allows interoperation across versions. A data type used by the MXBean interfaces are mapped to an open type when being accessed via MBeanServer interface. See the [MXBean](../../../../java.management/javax/management/MXBean.html#MXBean-spec) specification for details. 

## Ways to Access MXBeans

An application can monitor the instrumentation of the Java virtual machine and the runtime in the following ways: 

1. Direct access to an MXBean interface

- Get an MXBean instance locally in the running Java virtual machine: 

```

   RuntimeMXBean mxbean = ManagementFactory.getRuntimeMXBean();

   // Get the standard attribute "VmVendor"
   String vendor = mxbean.getVmVendor();
```

Or by calling the [getPlatformMXBean](ManagementFactory.html#getPlatformMXBean(java.lang.Class)) or [getPlatformMXBeans](ManagementFactory.html#getPlatformMXBeans(java.lang.Class)) method: 

```

   RuntimeMXBean mxbean = ManagementFactory.getPlatformMXBean(RuntimeMXBean.class);

   // Get the standard attribute "VmVendor"
   String vendor = mxbean.getVmVendor();
```

- Construct an MXBean proxy instance that forwards the method calls to a given MBeanServer: 

```

   MBeanServerConnection mbs;

   // Connect to a running JVM (or itself) and get MBeanServerConnection
   // that has the JVM MBeans registered in it
   ...

   // Get a MBean proxy for RuntimeMXBean interface
   RuntimeMXBean proxy =
       ManagementFactory.getPlatformMXBeanManagementFactory.html#getPlatformMXBean(javax.management.MBeanServerConnection,java.lang.Class)(mbs,
                                           RuntimeMXBean.class);
   // Get standard attribute "VmVendor"
   String vendor = proxy.getVmVendor();
```

A proxy is typically used to access an MXBean in a remote Java virtual machine. An alternative way to create an MXBean proxy is: 

```

   RuntimeMXBean proxy =
       ManagementFactory.newPlatformMXBeanProxyManagementFactory.html#newPlatformMXBeanProxy(javax.management.MBeanServerConnection,java.lang.String,java.lang.Class)(mbs,
                                                ManagementFactory.RUNTIME_MXBEAN_NAME,
                                                RuntimeMXBean.class);
```

2. Indirect access to an MXBean interface via MBeanServer

- Go through the [platform MBeanServer](ManagementFactory.html#getPlatformMBeanServer()) to access MXBeans locally or a specific `MBeanServerConnection` to access MXBeans remotely. The attributes and operations of an MXBean use only JMX open types which include basic data types, [CompositeData](../../../javax/management/openmbean/CompositeData.html), and [TabularData](../../../javax/management/openmbean/TabularData.html) defined in [OpenType](../../../javax/management/openmbean/OpenType.html). 

```

   MBeanServerConnection mbs;

   // Connect to a running JVM (or itself) and get MBeanServerConnection
   // that has the JVM MXBeans registered in it
   ...

   try {
       // Assuming the RuntimeMXBean has been registered in mbs
       ObjectName oname = new ObjectName(ManagementFactory.RUNTIME_MXBEAN_NAME);

       // Get standard attribute "VmVendor"
       String vendor = (String) mbs.getAttribute(oname, "VmVendor");
   } catch (....) {
       // Catch the exceptions thrown by ObjectName constructor
       // and MBeanServer.getAttribute method
       ...
   }
```

## Platform Extension

A Java virtual machine implementation may add its platform extension to the management interface by defining platform-dependent interfaces that extend the standard management interfaces to include platform-specific metrics and management operations. The static factory methods in the `ManagementFactory` class will return the MXBeans with the platform extension. 

 It is recommended to name the platform-specific attributes with a vendor-specific prefix such as the vendor's name to avoid collisions of the attribute name between the future extension to the standard management interface and the platform extension. If the future extension to the standard management interface defines a new attribute for a management interface and the attribute name is happened to be same as some vendor-specific attribute's name, the applications accessing that vendor-specific attribute would have to be modified to cope with versioning and compatibility issues. 

Below is an example showing how to access an attribute from the platform extension: 

 1) Direct access to the Oracle-specific MXBean interface 

```

   List<com.sun.management.GarbageCollectorMXBean> mxbeans =
       ManagementFactory.getPlatformMXBeans(com.sun.management.GarbageCollectorMXBean.class);

   for (com.sun.management.GarbageCollectorMXBean gc : mxbeans) {
       // Get the standard attribute "CollectionCount"
       String count = mxbean.getCollectionCount();

       // Get the platform-specific attribute "LastGcInfo"
       GcInfo gcinfo = gc.getLastGcInfo();
       ...
   }
```

 2) Access the Oracle-specific MXBean interface via `MBeanServer` through proxy 

```

   MBeanServerConnection mbs;

   // Connect to a running JVM (or itself) and get MBeanServerConnection
   // that has the JVM MXBeans registered in it
   ...

   List<com.sun.management.GarbageCollectorMXBean> mxbeans =
       ManagementFactory.getPlatformMXBeans(mbs, com.sun.management.GarbageCollectorMXBean.class);

   for (com.sun.management.GarbageCollectorMXBean gc : mxbeans) {
       // Get the standard attribute "CollectionCount"
       String count = mxbean.getCollectionCount();

       // Get the platform-specific attribute "LastGcInfo"
       GcInfo gcinfo = gc.getLastGcInfo();
       ...
   }
```

 Unless otherwise noted, passing a `null` argument to a constructor or method in any class or interface in this package will cause a [NullPointerException](../../../../java.base/java/lang/NullPointerException.html) to be thrown. 

 The java.lang.management API is thread-safe.

Since:1.5See Also:

- [JMX Specification](../../../javax/management/package-summary.html)

- Related PackagesModulePackageDescription[java.base](../../../../java.base/module-summary.html)[java.lang](../../../../java.base/java/lang/package-summary.html)Provides classes that are fundamental to the design of the Java programming language.
- All Classes and InterfacesInterfacesClassesEnum ClassesClassDescription[BufferPoolMXBean](BufferPoolMXBean.html)The management interface for a buffer pool, for example a pool of [direct](../../../../java.base/java/nio/ByteBuffer.html#allocateDirect(int)) or [mapped](../../../../java.base/java/nio/MappedByteBuffer.html) buffers.[ClassLoadingMXBean](ClassLoadingMXBean.html)The management interface for the class loading system of the Java virtual machine.[CompilationMXBean](CompilationMXBean.html)The management interface for the compilation system of the Java virtual machine.[GarbageCollectorMXBean](GarbageCollectorMXBean.html)The management interface for the garbage collection of the Java virtual machine.[LockInfo](LockInfo.html)Information about a lock.[ManagementFactory](ManagementFactory.html)The `ManagementFactory` class is a factory class for getting managed beans for the Java platform.[ManagementPermission](ManagementPermission.html)The permission which the SecurityManager will check when code that is running with a SecurityManager calls methods defined in the management interface for the Java platform.[MemoryManagerMXBean](MemoryManagerMXBean.html)The management interface for a memory manager.[MemoryMXBean](MemoryMXBean.html)The management interface for the memory system of the Java virtual machine.[MemoryNotificationInfo](MemoryNotificationInfo.html)The information about a memory notification.[MemoryPoolMXBean](MemoryPoolMXBean.html)The management interface for a memory pool.[MemoryType](MemoryType.html)Types of [memory pools](MemoryPoolMXBean.html).[MemoryUsage](MemoryUsage.html)A `MemoryUsage` object represents a snapshot of memory usage.[MonitorInfo](MonitorInfo.html)Information about an object monitor lock.[OperatingSystemMXBean](OperatingSystemMXBean.html)The management interface for the operating system on which the Java virtual machine is running.[PlatformLoggingMXBean](PlatformLoggingMXBean.html)The management interface for the [logging](../../../../java.logging/java/util/logging/package-summary.html) facility.[PlatformManagedObject](PlatformManagedObject.html)A platform managed object is a [JMX MXBean](../../../javax/management/MXBean.html) for monitoring and managing a component in the Java platform.[RuntimeMXBean](RuntimeMXBean.html)The management interface for the runtime system of the Java virtual machine.[ThreadInfo](ThreadInfo.html)Thread information.[ThreadMXBean](ThreadMXBean.html)The management interface for the thread system of the Java virtual machine.
