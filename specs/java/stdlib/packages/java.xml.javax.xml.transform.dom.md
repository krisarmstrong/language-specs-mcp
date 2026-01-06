Module[java.xml](../../../../module-summary.html)

# Package javax.xml.transform.dom

package javax.xml.transform.domProvides DOM specific transformation classes. 

 The [DOMSource](DOMSource.html) class allows the client of the implementation of this API to specify a DOM [Node](../../../../org/w3c/dom/Node.html) as the source of the input tree. The model of how the Transformer deals with the DOM tree in terms of mismatches with the [XSLT data model](http://www.w3.org/TR/xslt#data-model) or other data models is beyond the scope of this document. Any of the nodes derived from [Node](../../../../org/w3c/dom/Node.html) are legal input. 

 The [DOMResult](DOMResult.html) class allows a [Node](../../../../org/w3c/dom/Node.html) to be specified to which result DOM nodes will be appended. If an output node is not specified, the transformer will use [DocumentBuilder.newDocument()](../../parsers/DocumentBuilder.html#newDocument()) to create an output [Document](../../../../org/w3c/dom/Document.html) node. If a node is specified, it should be one of the following: [Document](../../../../org/w3c/dom/Document.html), [Element](../../../../org/w3c/dom/Element.html), or [DocumentFragment](../../../../org/w3c/dom/DocumentFragment.html). Specification of any other node type is implementation dependent and undefined by this API. If the result is a [Document](../../../../org/w3c/dom/Document.html), the output of the transformation must have a single element root to set as the document element. 

 The [DOMLocator](DOMLocator.html) node may be passed to [TransformerException](../TransformerException.html) objects, and retrieved by trying to cast the result of the [TransformerException.getLocator()](../TransformerException.html#getLocator()) method. The implementation has no responsibility to use a DOMLocator instead of a [SourceLocator](../SourceLocator.html) (though line numbers and the like do not make much sense for a DOM), so the result of getLocator must always be tested with an instanceof.

Since:1.5

- Related PackagesPackageDescription[javax.xml.transform](../package-summary.html)Defines the generic APIs for processing transformation instructions, and performing a transformation from source to result.[javax.xml.transform.sax](../sax/package-summary.html)Provides SAX specific transformation classes.[javax.xml.transform.stax](../stax/package-summary.html)Provides StAX specific transformation classes.[javax.xml.transform.stream](../stream/package-summary.html)Provides stream and URI specific transformation classes.
- All Classes and InterfacesInterfacesClassesClassDescription[DOMLocator](DOMLocator.html)Indicates the position of a node in a source DOM, intended primarily for error reporting.[DOMResult](DOMResult.html)Acts as a holder for a transformation result tree in the form of a Document Object Model (DOM) tree.[DOMSource](DOMSource.html)Acts as a holder for a transformation Source tree in the form of a Document Object Model (DOM) tree.
