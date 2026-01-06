Module[java.desktop](../../../module-summary.html)

# Package javax.imageio.event

package javax.imageio.eventA package of the Java Image I/O API dealing with synchronous notification of events during the reading and writing of images. 

 The `IIOReadProgressListener` interface allows for notification of the percentage of an image that has been read successfully. 

 The `IIOReadUpdateListener` interface allows for notification of the portions of an image that have been read. This is useful, for example, for implementing dynamic display of an image as it is loaded. 

 The `IIOReadWarningListener` interface allows for notification of non-fatal errors during reading. 

 The `IIOWriteWarningListener` and `IIOWriteProgressListener` interfaces perform analogous functions for writers.

Since:1.4

- Related PackagesPackageDescription[javax.imageio](../package-summary.html)The main package of the Java Image I/O API.[javax.imageio.metadata](../metadata/package-summary.html)A package of the Java Image I/O API dealing with reading and writing metadata.[javax.imageio.spi](../spi/package-summary.html)A package of the Java Image I/O API containing the plug-in interfaces for readers, writers, transcoders, and streams, and a runtime registry.[javax.imageio.stream](../stream/package-summary.html)A package of the Java Image I/O API dealing with low-level I/O from files and streams.
- InterfacesClassDescription[IIOReadProgressListener](IIOReadProgressListener.html)An interface used by `ImageReader` implementations to notify callers of their image and thumbnail reading methods of progress.[IIOReadUpdateListener](IIOReadUpdateListener.html)An interface used by `ImageReader` implementations to notify callers of their image and thumbnail reading methods of pixel updates.[IIOReadWarningListener](IIOReadWarningListener.html)An interface used by `ImageReader` implementations to notify callers of their image and thumbnail reading methods of warnings (non-fatal errors).[IIOWriteProgressListener](IIOWriteProgressListener.html)An interface used by `ImageWriter` implementations to notify callers of their image writing methods of progress.[IIOWriteWarningListener](IIOWriteWarningListener.html)An interface used by `ImageWriter` implementations to notify callers of their image and thumbnail reading methods of warnings (non-fatal errors).
