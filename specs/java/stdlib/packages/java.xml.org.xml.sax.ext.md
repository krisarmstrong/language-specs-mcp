org.xml.sax.ext (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

# Package org.xml.sax.ext

package org.xml.sax.extProvides interfaces to SAX2 facilities that conformant SAX drivers won't necessarily support. 

 This package is independent of the SAX2 core, though the functionality exposed generally needs to be implemented within a parser core. That independence has several consequences: 

- SAX2 drivers are not required to recognize these handlers. 
- You cannot assume that the class files will be present in every SAX2 installation.
- This package may be updated independently of SAX2 (i.e. new handlers and classes may be added without updating SAX2 itself).
- The new handlers are not implemented by the SAX2 `org.xml.sax.helpers.DefaultHandler` or `org.xml.sax.helpers.XMLFilterImpl` classes. You can subclass these if you need such behavior, or use the helper classes found here.
- The handlers need to be registered differently than core SAX2 handlers.

This package, SAX2-ext, is a standardized extension to SAX2. It is designed both to allow SAX parsers to pass certain types of information to applications, and to serve as a simple model for other SAX2 parser extension packages. Not all such extension packages should need to be recognized directly by parsers, however. As an example, most validation systems can be cleanly layered on top of parsers supporting the standardized SAX2 interfaces.

API Note:The SAX API, originally developed at [the SAX Project](http://www.saxproject.org), has been defined by Java SE since 1.4.Since:1.4

- Related PackagesPackageDescription[org.xml.sax](../package-summary.html)Provides the interfaces for the Simple API for XML (SAX).[org.xml.sax.helpers](../helpers/package-summary.html)Provides helper classes, including support for bootstrapping SAX-based applications.
- All Classes and InterfacesInterfacesClassesClassDescription[Attributes2](Attributes2.html)SAX2 extension to augment the per-attribute information provided through [Attributes](../Attributes.html).[Attributes2Impl](Attributes2Impl.html)SAX2 extension helper for additional Attributes information, implementing the [Attributes2](Attributes2.html) interface.[DeclHandler](DeclHandler.html)SAX2 extension handler for DTD declaration events.[DefaultHandler2](DefaultHandler2.html)This class extends the SAX2 base handler class to support the SAX2 [LexicalHandler](LexicalHandler.html), [DeclHandler](DeclHandler.html), and [EntityResolver2](EntityResolver2.html) extensions.[EntityResolver2](EntityResolver2.html)Extended interface for mapping external entity references to input sources, or providing a missing external subset.[LexicalHandler](LexicalHandler.html)SAX2 extension handler for lexical events.[Locator2](Locator2.html)SAX2 extension to augment the entity information provided through a [Locator](../Locator.html).[Locator2Impl](Locator2Impl.html)SAX2 extension helper for holding additional Entity information, implementing the [Locator2](Locator2.html) interface.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
