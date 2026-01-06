Module[java.xml](../../../module-summary.html)

# Package javax.xml.stream

package javax.xml.stream

 Defines interfaces and classes for the Streaming API for XML (StAX). 

 StAX provides two basic functions: the cursor API allowing users to read and write XML efficiently, and the event iterator API promoting ease of use that is event based, easy to extend and pipeline. The event iterator API is intended to layer on top of the cursor API. 

 The cursor API defines two interfaces: [XMLStreamReader](XMLStreamReader.html) and [XMLStreamWriter](XMLStreamWriter.html), while the event iterator API defines: [XMLEventReader](XMLEventReader.html) and [XMLEventWriter](XMLEventWriter.html). 

 StAX supports plugability with [XMLInputFactory](XMLInputFactory.html) and [XMLOutputFactory](XMLOutputFactory.html) that define how an implementation is located through a process as described in the `newFactory` methods.

Since:1.6

- Related PackagesPackageDescription[javax.xml](../package-summary.html)Defines constants for XML processing.[javax.xml.stream.events](events/package-summary.html)Defines event interfaces for the Streaming API for XML (StAX).[javax.xml.stream.util](util/package-summary.html)Provides utility classes for the Streaming API for XML (StAX).
- All Classes and InterfacesInterfacesClassesException ClassesClassDescription[EventFilter](EventFilter.html)This interface declares a simple filter interface that one can create to filter XMLEventReaders[FactoryConfigurationError](FactoryConfigurationError.html)An error class for reporting factory configuration errors.[Location](Location.html)Provides information on the location of an event.[StreamFilter](StreamFilter.html)This interface declares a simple filter interface that one can create to filter XMLStreamReaders[XMLEventFactory](XMLEventFactory.html)This interface defines a utility class for creating instances of XMLEvents[XMLEventReader](XMLEventReader.html)This is the top level interface for parsing XML Events.[XMLEventWriter](XMLEventWriter.html)This is the top level interface for writing XML documents.[XMLInputFactory](XMLInputFactory.html)Defines an abstract implementation of a factory for getting streams.[XMLOutputFactory](XMLOutputFactory.html)Defines an abstract implementation of a factory for getting XMLEventWriters and XMLStreamWriters.[XMLReporter](XMLReporter.html)This interface is used to report non-fatal errors.[XMLResolver](XMLResolver.html)This interface is used to resolve resources during an XML parse.[XMLStreamConstants](XMLStreamConstants.html)This interface declares the constants used in this API.[XMLStreamException](XMLStreamException.html)The base exception for unexpected processing errors.[XMLStreamReader](XMLStreamReader.html)The XMLStreamReader interface allows forward, read-only access to XML.[XMLStreamWriter](XMLStreamWriter.html)The XMLStreamWriter interface specifies how to write XML.
