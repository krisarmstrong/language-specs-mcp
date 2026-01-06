Module[java.base](../../../../module-summary.html)

# Package java.nio.channels.spi

package java.nio.channels.spiService-provider classes for the [java.nio.channels](../package-summary.html) package. 

 Only developers who are defining new selector providers or asynchronous channel providers should need to make direct use of this package. 

 Unless otherwise noted, passing a `null` argument to a constructor or method in any class or interface in this package will cause a [NullPointerException](../../../lang/NullPointerException.html) to be thrown.

Since:1.4

- Related PackagesPackageDescription[java.nio.channels](../package-summary.html)Defines channels, which represent connections to entities that are capable of performing I/O operations, such as files and sockets; defines selectors, for multiplexed, non-blocking I/O operations.
- ClassesClassDescription[AbstractInterruptibleChannel](AbstractInterruptibleChannel.html)Base implementation class for interruptible channels.[AbstractSelectableChannel](AbstractSelectableChannel.html)Base implementation class for selectable channels.[AbstractSelectionKey](AbstractSelectionKey.html)Base implementation class for selection keys.[AbstractSelector](AbstractSelector.html)Base implementation class for selectors.[AsynchronousChannelProvider](AsynchronousChannelProvider.html)Service-provider class for asynchronous channels.[SelectorProvider](SelectorProvider.html)Service-provider class for selectors and selectable channels.
