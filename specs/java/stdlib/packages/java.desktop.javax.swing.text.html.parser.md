Module[java.desktop](../../../../../module-summary.html)

# Package javax.swing.text.html.parser

package javax.swing.text.html.parserProvides the default HTML parser, along with support classes. As the stream is parsed, the parser notifies a delegate, which must implement the `HTMLEditorKit.ParserCallback` interface. 

Note: Most of the Swing API is not thread safe. For details, see [Concurrency in Swing](https://docs.oracle.com/javase/tutorial/uiswing/concurrency/index.html), a section in [The Java Tutorial](https://docs.oracle.com/javase/tutorial/).

Since:1.2See Also:

- [HTMLEditorKit.ParserCallback](../HTMLEditorKit.ParserCallback.html)

- Related PackagesPackageDescription[javax.swing.text.html](../package-summary.html)Provides the class `HTMLEditorKit` and supporting classes for creating HTML text editors.
- All Classes and InterfacesInterfacesClassesClassDescription[AttributeList](AttributeList.html)This class defines the attributes of an SGML element as described in a DTD using the ATTLIST construct.[ContentModel](ContentModel.html)A representation of a content model.[DocumentParser](DocumentParser.html)A Parser for HTML Documents (actually, you can specify a DTD, but you should really only use this class with the html dtd in swing).[DTD](DTD.html)The representation of an SGML DTD.[DTDConstants](DTDConstants.html)SGML constants used in a DTD.[Element](Element.html)An element as described in a DTD using the ELEMENT construct.[Entity](Entity.html)An entity is described in a DTD using the ENTITY construct.[Parser](Parser.html)A simple DTD-driven HTML parser.[ParserDelegator](ParserDelegator.html)Responsible for starting up a new DocumentParser each time its parse method is invoked.[TagElement](TagElement.html)A generic HTML TagElement class.
