javax.imageio.metadata (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

# Package javax.imageio.metadata

package javax.imageio.metadataA package of the Java Image I/O API dealing with reading and writing metadata. 

 When reading an image, its per-stream and per-image metadata is made available as an `IIOMetadata` object. The internals of this object are specific to the plug-in that created it. Its contents may be accessed in the form of an XML `Document`, which is implemented as a tree of `IIOMetadataNode` objects. 

 When writing an image, its metadata may be set by defining or modifying an `IIOMetadata` object. Such an object may be obtained from an `ImageWriter` or `ImageTranscoder` (from the `javax.imageio` package). Once such an object has been obtained, its contents may be set of modified via a `Document` consisting of `IIOMetadataNode`s. The document format may optionally be described using an `IIOMetadataFormat` object. 

 The format of the metadata contained in the XML `Document` is identified by a string which appears as the root node of the tree of `IIOMetadataNode` objects. This string contains a version number, e.g. "javax_imageio_jpeg_image_1.0". Readers and writers may support multiple versions of the same basic format and the Image I/O API has methods that allow specifying which version to use by passing the string to the method/constructor used to obtain an `IIOMetadata` object. In some cases, a more recent version may not be strictly compatible with a program written expecting an older version (for an example, see the Native Metadata Format section of the JPEG Metadata Usage Notes below). 

 Plug-ins may choose to support a [standard (plug-in neutral) format](doc-files/standard_metadata.html). This format does not provide lossless encoding of metadata, but allows a portion of the metadata to be accessed in a generic manner. 

 Each of the standard plug-ins supports a so-called "native" metadata format, which encodes its metadata losslessly: 

- [BMP metadata](doc-files/bmp_metadata.html)
- [GIF metadata](doc-files/gif_metadata.html)
- [JPEG metadata](doc-files/jpeg_metadata.html)
- [PNG metadata](doc-files/png_metadata.html)
- [TIFF metadata](doc-files/tiff_metadata.html#StreamMetadata)
- [WBMP metadata](doc-files/wbmp_metadata.html)

Since:1.4

- Related PackagesPackageDescription[javax.imageio](../package-summary.html)The main package of the Java Image I/O API.[javax.imageio.event](../event/package-summary.html)A package of the Java Image I/O API dealing with synchronous notification of events during the reading and writing of images.[javax.imageio.spi](../spi/package-summary.html)A package of the Java Image I/O API containing the plug-in interfaces for readers, writers, transcoders, and streams, and a runtime registry.[javax.imageio.stream](../stream/package-summary.html)A package of the Java Image I/O API dealing with low-level I/O from files and streams.
- All Classes and InterfacesInterfacesClassesException ClassesClassDescription[IIOInvalidTreeException](IIOInvalidTreeException.html)An `IIOInvalidTreeException` is thrown when an attempt by an `IIOMetadata` object to parse a tree of `IIOMetadataNode`s fails.[IIOMetadata](IIOMetadata.html)An abstract class to be extended by objects that represent metadata (non-image data) associated with images and streams.[IIOMetadataController](IIOMetadataController.html)An interface to be implemented by objects that can determine the settings of an `IIOMetadata` object, either by putting up a GUI to obtain values from a user, or by other means.[IIOMetadataFormat](IIOMetadataFormat.html)An object describing the structure of metadata documents returned from `IIOMetadata.getAsTree` and passed to `IIOMetadata.setFromTree` and `mergeTree`.[IIOMetadataFormatImpl](IIOMetadataFormatImpl.html)A concrete class providing a reusable implementation of the `IIOMetadataFormat` interface.[IIOMetadataNode](IIOMetadataNode.html)A class representing a node in a meta-data tree, which implements the [org.w3c.dom.Element](../../../../java.xml/org/w3c/dom/Element.html) interface and additionally allows for the storage of non-textual objects via the `getUserObject` and `setUserObject` methods.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
