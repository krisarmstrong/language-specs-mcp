Module[java.xml](../../../module-summary.html)

# Package javax.xml.transform

package javax.xml.transformDefines the generic APIs for processing transformation instructions, and performing a transformation from source to result. These interfaces have no dependencies on SAX or the DOM standard, and try to make as few assumptions as possible about the details of the source and result of a transformation. It achieves this by defining [Source](Source.html) and [Result](Result.html) interfaces. 

 To provide concrete classes for the user, the API defines specializations of the interfaces found at the root level. These interfaces are found in [javax.xml.transform.sax](sax/package-summary.html), [javax.xml.transform.dom](dom/package-summary.html), [javax.xml.transform.stax](stax/package-summary.html), and [javax.xml.transform.stream](stream/package-summary.html). 

## Creating Objects

 The API allows a concrete [TransformerFactory](TransformerFactory.html) object to be created from the static function [TransformerFactory.newInstance()](TransformerFactory.html#newInstance()). 

## Specification of Inputs and Outputs

 This API defines two interface objects called [Source](Source.html) and [Result](Result.html). In order to pass Source and Result objects to the interfaces, concrete classes must be used. The following concrete representations are defined for each of these objects: [StreamSource](stream/StreamSource.html) and [StreamResult](stream/StreamResult.html), [StAXSource](stax/StAXSource.html) and [StAXResult](stax/StAXResult.html), and [SAXSource](sax/SAXSource.html) and [SAXResult](sax/SAXResult.html), and [DOMSource](dom/DOMSource.html) and [DOMResult](dom/DOMResult.html). Each of these objects defines a FEATURE string (which is in the form of a URL), which can be passed into [TransformerFactory.getFeature(java.lang.String)](TransformerFactory.html#getFeature(java.lang.String)) to see if the given type of Source or Result object is supported. For instance, to test if a DOMSource and a StreamResult is supported, you can apply the following test. 

```

 
 TransformerFactory tfactory = TransformerFactory.newInstance();
 if (tfactory.getFeature(DOMSource.FEATURE) &&
     tfactory.getFeature(StreamResult.FEATURE)) {
     ...
 }
 
 
```

## Qualified Name Representation

[Namespaces](http://www.w3.org/TR/REC-xml-names) present something of a problem area when dealing with XML objects. Qualified Names appear in XML markup as prefixed names. But the prefixes themselves do not hold identity. Rather, it is the URIs that they contextually map to that hold the identity. Therefore, when passing a Qualified Name like "xyz:foo" among Java programs, one must provide a means to map "xyz" to a namespace. 

 One solution has been to create a "QName" object that holds the namespace URI, as well as the prefix and local name, but this is not always an optimal solution, as when, for example, you want to use unique strings as keys in a dictionary object. Not having a string representation also makes it difficult to specify a namespaced identity outside the context of an XML document. 

 In order to pass namespaced values to transformations, for instance when setting a property or a parameter on a [Transformer](Transformer.html) object, this specification defines that a String "qname" object parameter be passed as two-part string, the namespace URI enclosed in curly braces ({}), followed by the local name. If the qname has a null URI, then the String object only contains the local name. An application can safely check for a non-null URI by testing to see if the first character of the name is a '{' character. 

 For example, if a URI and local name were obtained from an element defined with <xyz:foo xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>, then the Qualified Name would be "{http://xyz.foo.com/yada/baz.html}foo". Note that the prefix is lost. 

## Result Tree Serialization

 Serialization of the result tree to a stream can be controlled with the [Transformer.setOutputProperties(java.util.Properties)](Transformer.html#setOutputProperties(java.util.Properties)) and the [Transformer.setOutputProperty(java.lang.String, java.lang.String)](Transformer.html#setOutputProperty(java.lang.String,java.lang.String)) methods. These properties only apply to stream results, they have no effect when the result is a DOM tree or SAX event stream. 

 Strings that match the [XSLT
 specification for xsl:output attributes](http://www.w3.org/TR/xslt#output) can be referenced from the [OutputKeys](OutputKeys.html) class. Other strings can be specified as well. If the transformer does not recognize an output key, a [IllegalArgumentException](../../../../java.base/java/lang/IllegalArgumentException.html) is thrown, unless the key name is [namespace qualified](#qname-delimiter). Output key names that are namespace qualified are always allowed, although they may be ignored by some implementations. 

 If all that is desired is the simple identity transformation of a source to a result, then [TransformerFactory](TransformerFactory.html) provides a [TransformerFactory.newTransformer()](TransformerFactory.html#newTransformer()) method with no arguments. This method creates a Transformer that effectively copies the source to the result. This method may be used to create a DOM from SAX events or to create an XML or HTML stream from a DOM or SAX events. 

## Exceptions and Error Reporting

 The transformation API throw three types of specialized exceptions. A [TransformerFactoryConfigurationError](TransformerFactoryConfigurationError.html) is parallel to the [FactoryConfigurationError](../parsers/FactoryConfigurationError.html), and is thrown when a configuration problem with the TransformerFactory exists. This error will typically be thrown when the transformation factory class specified with the "javax.xml.transform.TransformerFactory" system property cannot be found or instantiated. 

 A [TransformerConfigurationException](TransformerConfigurationException.html) may be thrown if for any reason a Transformer can not be created. A TransformerConfigurationException may be thrown if there is a syntax error in the transformation instructions, for example when [TransformerFactory.newTransformer(javax.xml.transform.Source)](TransformerFactory.html#newTransformer(javax.xml.transform.Source)) is called. 

[TransformerException](TransformerException.html) is a general exception that occurs during the course of a transformation. A transformer exception may wrap another exception, and if any of the [TransformerException.printStackTrace()](TransformerException.html#printStackTrace()) methods are called on it, it will produce a list of stack dumps, starting from the most recent. The transformer exception also provides a [SourceLocator](SourceLocator.html) object which indicates where in the source tree or transformation instructions the error occurred. [TransformerException.getMessageAndLocation()](TransformerException.html#getMessageAndLocation()) may be called to get an error message with location info, and [TransformerException.getLocationAsString()](TransformerException.html#getLocationAsString()) may be called to get just the location string. 

 Transformation warnings and errors are sent to an [ErrorListener](ErrorListener.html), at which point the application may decide to report the error or warning, and may decide to throw an `Exception` for a non-fatal error. The `ErrorListener` may be set via [TransformerFactory.setErrorListener(javax.xml.transform.ErrorListener)](TransformerFactory.html#setErrorListener(javax.xml.transform.ErrorListener)) for reporting errors that have to do with syntax errors in the transformation instructions, or via [Transformer.setErrorListener(javax.xml.transform.ErrorListener)](Transformer.html#setErrorListener(javax.xml.transform.ErrorListener)) to report errors that occur during the transformation. The `ErrorListener` on both objects will always be valid and non-`null`, whether set by the application or a default implementation provided by the processor. 

## Resolution of URIs within a transformation

 The API provides a way for URIs referenced from within the stylesheet instructions or within the transformation to be resolved by the calling application. This can be done by creating a class that implements the [URIResolver](URIResolver.html) interface, with its one method, [URIResolver.resolve(java.lang.String, java.lang.String)](URIResolver.html#resolve(java.lang.String,java.lang.String)), and use this class to set the URI resolution for the transformation instructions or transformation with [TransformerFactory.setURIResolver(javax.xml.transform.URIResolver)](TransformerFactory.html#setURIResolver(javax.xml.transform.URIResolver)) or [Transformer.setURIResolver(javax.xml.transform.URIResolver)](Transformer.html#setURIResolver(javax.xml.transform.URIResolver)). The `URIResolver.resolve` method takes two String arguments, the URI found in the stylesheet instructions or built as part of the transformation process, and the base URI against which the first argument will be made absolute if the absolute URI is required. The returned [Source](Source.html) object must be usable by the transformer, as specified in its implemented features.

Since:1.5

- Related PackagesPackageDescription[javax.xml](../package-summary.html)Defines constants for XML processing.[javax.xml.transform.dom](dom/package-summary.html)Provides DOM specific transformation classes.[javax.xml.transform.sax](sax/package-summary.html)Provides SAX specific transformation classes.[javax.xml.transform.stax](stax/package-summary.html)Provides StAX specific transformation classes.[javax.xml.transform.stream](stream/package-summary.html)Provides stream and URI specific transformation classes.
- All Classes and InterfacesInterfacesClassesException ClassesClassDescription[ErrorListener](ErrorListener.html)The listener interface used by a [TransformerFactory](TransformerFactory.html) or [Transformer](Transformer.html) to notify callers of error messages that occur during a transformation process.[OutputKeys](OutputKeys.html)Provides string constants that can be used to set output properties for a Transformer, or to retrieve output properties from a Transformer or Templates object.[Result](Result.html)An object that implements this interface contains the information needed to build a transformation result tree.[Source](Source.html)An object that implements this interface contains the information needed to act as source input (XML source or transformation instructions).[SourceLocator](SourceLocator.html)This interface is primarily for the purposes of reporting where an error occurred in the XML source or transformation instructions.[Templates](Templates.html)An object that implements this interface is the runtime representation of processed transformation instructions.[Transformer](Transformer.html)An instance of this abstract class can transform a source tree into a result tree.[TransformerConfigurationException](TransformerConfigurationException.html)Indicates a serious configuration error.[TransformerException](TransformerException.html)This class specifies an exceptional condition that occurred during the transformation process.[TransformerFactory](TransformerFactory.html)A TransformerFactory instance can be used to create [Transformer](Transformer.html) and [Templates](Templates.html) objects.[TransformerFactoryConfigurationError](TransformerFactoryConfigurationError.html)Thrown when a problem with configuration with the Transformer Factories exists.[URIResolver](URIResolver.html)An object that implements this interface that can be called by the processor to turn a URI used in document(), xsl:import, or xsl:include into a Source object.
