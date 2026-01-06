Module[java.xml](../../../../module-summary.html)

# Package javax.xml.transform.stream

package javax.xml.transform.streamProvides stream and URI specific transformation classes. 

 The [StreamSource](StreamSource.html) class provides methods for specifying [InputStream](../../../../../java.base/java/io/InputStream.html) input, [Reader](../../../../../java.base/java/io/Reader.html) input, and URL input in the form of strings. Even if an input stream or reader is specified as the source, [StreamSource.setSystemId(java.lang.String)](StreamSource.html#setSystemId(java.lang.String)) should still be called, so that the transformer can know from where it should resolve relative URIs. The public identifier is always optional: if the application writer includes one, it will be provided as part of the [SourceLocator](../SourceLocator.html) information. 

 The [StreamResult](StreamResult.html) class provides methods for specifying [OutputStream](../../../../../java.base/java/io/OutputStream.html), [Writer](../../../../../java.base/java/io/Writer.html), or an output system ID, as the output of the transformation result. 

 Normally streams should be used rather than readers or writers, for both the Source and Result, since readers and writers already have the encoding established to and from the internal Unicode format. However, there are times when it is useful to write to a character stream, such as when using a StringWriter in order to write to a String, or in the case of reading source XML from a StringReader.

Since:1.5

- Related PackagesPackageDescription[javax.xml.transform](../package-summary.html)Defines the generic APIs for processing transformation instructions, and performing a transformation from source to result.[javax.xml.transform.dom](../dom/package-summary.html)Provides DOM specific transformation classes.[javax.xml.transform.sax](../sax/package-summary.html)Provides SAX specific transformation classes.[javax.xml.transform.stax](../stax/package-summary.html)Provides StAX specific transformation classes.
- ClassesClassDescription[StreamResult](StreamResult.html)Acts as an holder for a transformation result, which may be XML, plain Text, HTML, or some other form of markup.[StreamSource](StreamSource.html)Acts as an holder for a transformation Source in the form of a stream of XML markup.
