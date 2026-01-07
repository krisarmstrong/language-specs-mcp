javax.xml.stream (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

- [Overview](../../../../index.html)
- [Module](../../../module-summary.html)
- Package
- Class
- [Use](package-use.html)
- [Tree](package-tree.html)
- [Preview](../../../../preview-list.html)
- [New](../../../../new-list.html)
- [Deprecated](../../../../deprecated-list.html)
- [Index](../../../../index-files/index-1.html)
- [Help](../../../../help-doc.html#package)

- 

Package:

  - [Description](#package-description)
  - [Related Packages](#related-package-summary)
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- [Related Packages](#related-package-summary) | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../../search.html)Module[java.xml](../../../module-summary.html)

# Package javax.xml.stream

package javax.xml.stream

 Defines interfaces and classes for the Streaming API for XML (StAX). 

 StAX provides two basic functions: the cursor API allowing users to read and write XML efficiently, and the event iterator API promoting ease of use that is event based, easy to extend and pipeline. The event iterator API is intended to layer on top of the cursor API. 

 The cursor API defines two interfaces: [XMLStreamReader](XMLStreamReader.html) and [XMLStreamWriter](XMLStreamWriter.html), while the event iterator API defines: [XMLEventReader](XMLEventReader.html) and [XMLEventWriter](XMLEventWriter.html). 

 StAX supports plugability with [XMLInputFactory](XMLInputFactory.html) and [XMLOutputFactory](XMLOutputFactory.html) that define how an implementation is located through a process as described in the `newFactory` methods.

Since:1.6

- Related PackagesPackageDescription[javax.xml](../package-summary.html)Defines constants for XML processing.[javax.xml.stream.events](events/package-summary.html)Defines event interfaces for the Streaming API for XML (StAX).[javax.xml.stream.util](util/package-summary.html)Provides utility classes for the Streaming API for XML (StAX).
- All Classes and InterfacesInterfacesClassesException ClassesClassDescription[EventFilter](EventFilter.html)This interface declares a simple filter interface that one can create to filter XMLEventReaders[FactoryConfigurationError](FactoryConfigurationError.html)An error class for reporting factory configuration errors.[Location](Location.html)Provides information on the location of an event.[StreamFilter](StreamFilter.html)This interface declares a simple filter interface that one can create to filter XMLStreamReaders[XMLEventFactory](XMLEventFactory.html)This interface defines a utility class for creating instances of XMLEvents[XMLEventReader](XMLEventReader.html)This is the top level interface for parsing XML Events.[XMLEventWriter](XMLEventWriter.html)This is the top level interface for writing XML documents.[XMLInputFactory](XMLInputFactory.html)Defines an abstract implementation of a factory for getting streams.[XMLOutputFactory](XMLOutputFactory.html)Defines an abstract implementation of a factory for getting XMLEventWriters and XMLStreamWriters.[XMLReporter](XMLReporter.html)This interface is used to report non-fatal errors.[XMLResolver](XMLResolver.html)This interface is used to resolve resources during an XML parse.[XMLStreamConstants](XMLStreamConstants.html)This interface declares the constants used in this API.[XMLStreamException](XMLStreamException.html)The base exception for unexpected processing errors.[XMLStreamReader](XMLStreamReader.html)The XMLStreamReader interface allows forward, read-only access to XML.[XMLStreamWriter](XMLStreamWriter.html)The XMLStreamWriter interface specifies how to write XML.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
