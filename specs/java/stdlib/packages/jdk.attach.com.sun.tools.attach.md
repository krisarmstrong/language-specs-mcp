Module[jdk.attach](../../../../module-summary.html)

# Package com.sun.tools.attach

package com.sun.tools.attachProvides the API to attach to a Java virtual machine. 

 A tool, written in the Java Language, uses this API to attach to a target virtual machine (VM) and load its tool agent into the target VM. For example, a management console might have a management agent which it uses to obtain management information from instrumented objects in a Java virtual machine. If the management console is required to manage an application that is running in a virtual machine that does not include the management agent, then this API can be used to attach to the target VM and load the agent.

Since:1.6

- Related PackagesPackageDescription[com.sun.tools.attach.spi](spi/package-summary.html)Only developers who are defining new attach providers should need to make direct use of this package.
- All Classes and InterfacesClassesException ClassesClassDescription[AgentInitializationException](AgentInitializationException.html)The exception thrown when an agent fails to initialize in the target Java virtual machine.[AgentLoadException](AgentLoadException.html)The exception thrown when an agent cannot be loaded into the target Java virtual machine.[AttachNotSupportedException](AttachNotSupportedException.html)Thrown by [VirtualMachine.attach](VirtualMachine.html#attach(java.lang.String)) when attempting to attach to a Java virtual machine for which a compatible [AttachProvider](spi/AttachProvider.html) does not exist.[AttachOperationFailedException](AttachOperationFailedException.html)Exception type to signal that an attach operation failed in the target VM.[AttachPermission](AttachPermission.html)When a [SecurityManager](../../../../../java.base/java/lang/SecurityManager.html) set, this is the permission which will be checked when code invokes [VirtualMachine.attach](VirtualMachine.html#attach(java.lang.String)) to attach to a target virtual machine.[VirtualMachine](VirtualMachine.html)A Java virtual machine.[VirtualMachineDescriptor](VirtualMachineDescriptor.html)Describes a Java virtual machine.
