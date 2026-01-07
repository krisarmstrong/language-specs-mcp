javax.imageio.spi (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

[SEARCH](../../../../search.html)Module[java.desktop](../../../module-summary.html)

# Package javax.imageio.spi

package javax.imageio.spiA package of the Java Image I/O API containing the plug-in interfaces for readers, writers, transcoders, and streams, and a runtime registry. 

 The `javax.imageio.spi` package contains service provider interfaces for reading, writing, and transcoding images, and obtaining image input and output streams, as well as a run-time registry that discovers installed instances of Image I/O service providers and allows new instances to be registered dynamically.

Since:1.4

- Related PackagesPackageDescription[javax.imageio](../package-summary.html)The main package of the Java Image I/O API.[javax.imageio.event](../event/package-summary.html)A package of the Java Image I/O API dealing with synchronous notification of events during the reading and writing of images.[javax.imageio.metadata](../metadata/package-summary.html)A package of the Java Image I/O API dealing with reading and writing metadata.[javax.imageio.stream](../stream/package-summary.html)A package of the Java Image I/O API dealing with low-level I/O from files and streams.
- All Classes and InterfacesInterfacesClassesClassDescription[IIORegistry](IIORegistry.html)A registry for Image I/O service provider instances.[IIOServiceProvider](IIOServiceProvider.html)A superinterface for functionality common to all Image I/O service provider interfaces (SPIs).[ImageInputStreamSpi](ImageInputStreamSpi.html)The service provider interface (SPI) for `ImageInputStream`s.[ImageOutputStreamSpi](ImageOutputStreamSpi.html)The service provider interface (SPI) for `ImageOutputStream`s.[ImageReaderSpi](ImageReaderSpi.html)The service provider interface (SPI) for `ImageReader`s.[ImageReaderWriterSpi](ImageReaderWriterSpi.html)A superclass containing instance variables and methods common to `ImageReaderSpi` and `ImageWriterSpi`.[ImageTranscoderSpi](ImageTranscoderSpi.html)The service provider interface (SPI) for `ImageTranscoder`s.[ImageWriterSpi](ImageWriterSpi.html)The service provider interface (SPI) for `ImageWriter`s.[RegisterableService](RegisterableService.html)An optional interface that may be provided by service provider objects that will be registered with a `ServiceRegistry`.[ServiceRegistry](ServiceRegistry.html)A registry for service provider instances for Image I/O service types.[ServiceRegistry.Filter](ServiceRegistry.Filter.html)A simple filter interface used by `ServiceRegistry.getServiceProviders` to select providers matching an arbitrary criterion.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
