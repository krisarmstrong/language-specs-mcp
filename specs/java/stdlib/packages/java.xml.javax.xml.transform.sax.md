Module[java.xml](../../../../module-summary.html)

# Package javax.xml.transform.sax

package javax.xml.transform.saxProvides SAX specific transformation classes. 

 The [SAXSource](SAXSource.html) class allows the setting of an [XMLReader](../../../../org/xml/sax/XMLReader.html) to be used for pulling parse events, and an [InputSource](../../../../org/xml/sax/InputSource.html) that may be used to specify the SAX source. 

 The [SAXResult](SAXResult.html) class allows the setting of a [ContentHandler](../../../../org/xml/sax/ContentHandler.html) to be the receiver of SAX2 events from the transformation. 

 The [SAXTransformerFactory](SAXTransformerFactory.html) extends [TransformerFactory](../TransformerFactory.html) to provide factory methods for creating [TemplatesHandler](TemplatesHandler.html), [TransformerHandler](TransformerHandler.html), and [XMLReader](../../../../org/xml/sax/XMLReader.html) instances. 

 To obtain a [SAXTransformerFactory](SAXTransformerFactory.html), the caller must cast the [TransformerFactory](../TransformerFactory.html) instance returned from [TransformerFactory.newInstance()](../TransformerFactory.html#newInstance()). 

 The [TransformerHandler](TransformerHandler.html) interface allows a transformation to be created from SAX2 parse events, which is a "push" model rather than the "pull" model that normally occurs for a transformation. Normal parse events are received through the [ContentHandler](../../../../org/xml/sax/ContentHandler.html) interface, lexical events such as startCDATA and endCDATA are received through the [LexicalHandler](../../../../org/xml/sax/ext/LexicalHandler.html) interface, and events that signal the start or end of disabling output escaping are received via [ContentHandler.processingInstruction(java.lang.String, java.lang.String)](../../../../org/xml/sax/ContentHandler.html#processingInstruction(java.lang.String,java.lang.String)), with the target parameter being [Result.PI_DISABLE_OUTPUT_ESCAPING](../Result.html#PI_DISABLE_OUTPUT_ESCAPING) and [Result.PI_ENABLE_OUTPUT_ESCAPING](../Result.html#PI_ENABLE_OUTPUT_ESCAPING). If parameters, output properties, or other features need to be set on the Transformer handler, a [Transformer](../Transformer.html) reference will need to be obtained from [TransformerHandler.getTransformer()](TransformerHandler.html#getTransformer()), and the methods invoked from that reference. 

 The [TemplatesHandler](TemplatesHandler.html) interface allows the creation of [Templates](../Templates.html) objects from SAX2 parse events. Once the [ContentHandler](../../../../org/xml/sax/ContentHandler.html) events are complete, the Templates object may be obtained from [TemplatesHandler.getTemplates()](TemplatesHandler.html#getTemplates()). Note that [TemplatesHandler.setSystemId(java.lang.String)](TemplatesHandler.html#setSystemId(java.lang.String)) should normally be called in order to establish a base system ID from which relative URLs may be resolved. 

 The [SAXTransformerFactory.newXMLFilter(javax.xml.transform.Source)](SAXTransformerFactory.html#newXMLFilter(javax.xml.transform.Source)) method allows the creation of a [XMLFilter](../../../../org/xml/sax/XMLFilter.html), which encapsulates the SAX2 notion of a "pull" transformation. The resulting `XMLFilters` can be chained together so that a series of transformations can happen with one's output becoming another's input.

Since:1.5

- Related PackagesPackageDescription[javax.xml.transform](../package-summary.html)Defines the generic APIs for processing transformation instructions, and performing a transformation from source to result.[javax.xml.transform.dom](../dom/package-summary.html)Provides DOM specific transformation classes.[javax.xml.transform.stax](../stax/package-summary.html)Provides StAX specific transformation classes.[javax.xml.transform.stream](../stream/package-summary.html)Provides stream and URI specific transformation classes.
- All Classes and InterfacesInterfacesClassesClassDescription[SAXResult](SAXResult.html)Acts as an holder for a transformation Result.[SAXSource](SAXSource.html)Acts as an holder for SAX-style Source.[SAXTransformerFactory](SAXTransformerFactory.html)This class extends TransformerFactory to provide SAX-specific factory methods.[TemplatesHandler](TemplatesHandler.html)A SAX ContentHandler that may be used to process SAX parse events (parsing transformation instructions) into a Templates object.[TransformerHandler](TransformerHandler.html)A TransformerHandler listens for SAX ContentHandler parse events and transforms them to a Result.
