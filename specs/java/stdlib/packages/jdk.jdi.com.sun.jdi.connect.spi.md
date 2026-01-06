Module[jdk.jdi](../../../../../module-summary.html)

# Package com.sun.jdi.connect.spi

package com.sun.jdi.connect.spiThis package comprises the interfaces and classes used to develop new [TransportService](TransportService.html) implementations.

- Related PackagesPackageDescription[com.sun.jdi.connect](../package-summary.html)This package defines connections between the virtual machine using the JDI and the target virtual machine.
- All Classes and InterfacesClassesException ClassesClassDescription[ClosedConnectionException](ClosedConnectionException.html)This exception may be thrown as a result of an asynchronous close of a [Connection](Connection.html) while an I/O operation is in progress.[Connection](Connection.html)A connection between a debugger and a target VM which it debugs.[TransportService](TransportService.html)A transport service for connections between a debugger and a target VM.[TransportService.Capabilities](TransportService.Capabilities.html)The transport service capabilities.[TransportService.ListenKey](TransportService.ListenKey.html)A listen key.
