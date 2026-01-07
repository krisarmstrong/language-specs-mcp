javax.xml.transform.stream (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

- [Overview](../../../../../index.html)
- [Module](../../../../module-summary.html)
- Package
- Class
- [Use](package-use.html)
- [Tree](package-tree.html)
- [Preview](../../../../../preview-list.html)
- [New](../../../../../new-list.html)
- [Deprecated](../../../../../deprecated-list.html)
- [Index](../../../../../index-files/index-1.html)
- [Help](../../../../../help-doc.html#package)

- 

Package:

  - [Description](#package-description)
  - [Related Packages](#related-package-summary)
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- [Related Packages](#related-package-summary) | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../../../search.html)Module[java.xml](../../../../module-summary.html)

# Package javax.xml.transform.stream

package javax.xml.transform.streamProvides stream and URI specific transformation classes. 

 The [StreamSource](StreamSource.html) class provides methods for specifying [InputStream](../../../../../java.base/java/io/InputStream.html) input, [Reader](../../../../../java.base/java/io/Reader.html) input, and URL input in the form of strings. Even if an input stream or reader is specified as the source, [StreamSource.setSystemId(java.lang.String)](StreamSource.html#setSystemId(java.lang.String)) should still be called, so that the transformer can know from where it should resolve relative URIs. The public identifier is always optional: if the application writer includes one, it will be provided as part of the [SourceLocator](../SourceLocator.html) information. 

 The [StreamResult](StreamResult.html) class provides methods for specifying [OutputStream](../../../../../java.base/java/io/OutputStream.html), [Writer](../../../../../java.base/java/io/Writer.html), or an output system ID, as the output of the transformation result. 

 Normally streams should be used rather than readers or writers, for both the Source and Result, since readers and writers already have the encoding established to and from the internal Unicode format. However, there are times when it is useful to write to a character stream, such as when using a StringWriter in order to write to a String, or in the case of reading source XML from a StringReader.

Since:1.5

- Related PackagesPackageDescription[javax.xml.transform](../package-summary.html)Defines the generic APIs for processing transformation instructions, and performing a transformation from source to result.[javax.xml.transform.dom](../dom/package-summary.html)Provides DOM specific transformation classes.[javax.xml.transform.sax](../sax/package-summary.html)Provides SAX specific transformation classes.[javax.xml.transform.stax](../stax/package-summary.html)Provides StAX specific transformation classes.
- ClassesClassDescription[StreamResult](StreamResult.html)Acts as an holder for a transformation result, which may be XML, plain Text, HTML, or some other form of markup.[StreamSource](StreamSource.html)Acts as an holder for a transformation Source in the form of a stream of XML markup.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
