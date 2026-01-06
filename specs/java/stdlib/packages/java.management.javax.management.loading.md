Module[java.management](../../../module-summary.html)

# Package javax.management.loading

package javax.management.loading

Provides the classes which implement advanced dynamic loading. See the chapter Advanced Dynamic Loading in the [JMX Specification](#spec).

An MBean that is of a subclass of [ClassLoader](../../../../java.base/java/lang/ClassLoader.html) can be used as a class loader to create other MBeans via the method [MBeanServer.createMBean(String, ObjectName, ObjectName, Object[], String[])](../MBeanServer.html#createMBean(java.lang.String,javax.management.ObjectName,javax.management.ObjectName,java.lang.Object%5B%5D,java.lang.String%5B%5D)), and to instantiate arbitrary objects via the method [MBeanServer.instantiate(String, ObjectName, Object[], String[])](../MBeanServer.html#instantiate(java.lang.String,javax.management.ObjectName,java.lang.Object%5B%5D,java.lang.String%5B%5D)). The [MLet](MLet.html) class is an example of such an MBean. It is a [URLClassLoader](../../../../java.base/java/net/URLClassLoader.html), so the list of URLs to load classes from can be configured.

Additionally, an `MLet` can read a configuration file that specifies a set of MBeans to be registered in the same MBean Server as the `MLet`.

Every MBean Server has a class loader repository containing all MBeans registered in that MBean Server that are of a subclass of [ClassLoader](../../../../java.base/java/lang/ClassLoader.html). The class loader repository is used by the forms of the `createMBean` and `instantiate` methods in the [MBeanServer](../MBeanServer.html) interface that do not have an explicit loader parameter. It is also used by the `MLet` class when it does not find a class in its own set of URLs.

If an MBean implements the interface [PrivateClassLoader](PrivateClassLoader.html), then it is not added to the class loader repository. The class [PrivateMLet](PrivateMLet.html) is a subclass of `MLet` that implements `PrivateClassLoader`.

Since:1.5See Also:

- [JMX Specification, version 1.4](https://jcp.org/aboutJava/communityprocess/mrel/jsr160/index2.html)

- Related PackagesPackageDescription[javax.management](../package-summary.html)Provides the core classes for the Java Management Extensions.
- All Classes and InterfacesInterfacesClassesClassDescription[ClassLoaderRepository](ClassLoaderRepository.html)Instances of this interface are used to keep the list of ClassLoaders registered in an MBean Server.[DefaultLoaderRepository](DefaultLoaderRepository.html)Deprecated. Use [MBeanServer.getClassLoaderRepository()](../MBeanServer.html#getClassLoaderRepository()) instead.[MLet](MLet.html)Deprecated, for removal: This API element is subject to removal in a future version. This API is part of Management Applets (m-lets), which is a legacy feature that allows loading of remote MBeans.[MLetContent](MLetContent.html)Deprecated, for removal: This API element is subject to removal in a future version. This API is part of Management Applets (m-lets), which is a legacy feature that allows loading of remote MBeans.[MLetMBean](MLetMBean.html)Deprecated, for removal: This API element is subject to removal in a future version. This API is part of Management Applets (m-lets), which is a legacy feature that allows loading of remote MBeans.[PrivateClassLoader](PrivateClassLoader.html)Marker interface indicating that a ClassLoader should not be added to the [ClassLoaderRepository](ClassLoaderRepository.html).[PrivateMLet](PrivateMLet.html)Deprecated, for removal: This API element is subject to removal in a future version. This API is part of Management Applets (m-lets), which is a legacy feature that allows loading of remote MBeans.
