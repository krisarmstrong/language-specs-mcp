Module[jdk.management](../../../module-summary.html)

# Package com.sun.management

package com.sun.managementThis package contains the JDK's extension to the standard implementation of the [java.lang.management](../../../../java.management/java/lang/management/package-summary.html) API and also defines the management interface for some other components of the platform. 

 All platform MBeans are registered in the platform MBeanServer which can be obtained via the [ManagementFactory.getPlatformMBeanServer()](../../../../java.management/java/lang/management/ManagementFactory.html#getPlatformMBeanServer())

Since:1.5

- All Classes and InterfacesInterfacesClassesEnum ClassesClassDescription[DiagnosticCommandMBean](DiagnosticCommandMBean.html)Management interface for the diagnostic commands for the HotSpot Virtual Machine.[GarbageCollectionNotificationInfo](GarbageCollectionNotificationInfo.html)The information about a garbage collection[GarbageCollectorMXBean](GarbageCollectorMXBean.html)Platform-specific management interface for a garbage collector which performs collections in cycles.[GcInfo](GcInfo.html)Garbage collection information.[HotSpotDiagnosticMXBean](HotSpotDiagnosticMXBean.html)Diagnostic management interface for the HotSpot Virtual Machine.[HotSpotDiagnosticMXBean.ThreadDumpFormat](HotSpotDiagnosticMXBean.ThreadDumpFormat.html)Thread dump format.[OperatingSystemMXBean](OperatingSystemMXBean.html)Platform-specific management interface for the operating system on which the Java virtual machine is running.[ThreadMXBean](ThreadMXBean.html)Platform-specific management interface for the thread system of the Java virtual machine.[UnixOperatingSystemMXBean](UnixOperatingSystemMXBean.html)Platform-specific management interface for the Unix operating system on which the Java virtual machine is running.[VMOption](VMOption.html)Information about a VM option including its value and where the value came from which is referred as its [origin](VMOption.Origin.html).[VMOption.Origin](VMOption.Origin.html)Origin of the value of a VM option.
