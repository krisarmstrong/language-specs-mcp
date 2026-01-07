org.w3c.dom.ls (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

# Package org.w3c.dom.ls

package org.w3c.dom.ls

 Provides interfaces for DOM Level 3 Load and Save. Refer to the [Document Object Model (DOM) Level 3 Load and Save Specification](http://www.w3.org/TR/2004/REC-DOM-Level-3-LS-20040407), the Load and Save interface allows programs and scripts to dynamically load the content of an XML document into a DOM document and serialize a DOM document into an XML document.

Since:1.5

- Related PackagesPackageDescription[org.w3c.dom](../package-summary.html)Provides the interfaces for the Document Object Model (DOM).
- All Classes and InterfacesInterfacesException ClassesClassDescription[DOMImplementationLS](DOMImplementationLS.html)`DOMImplementationLS` contains the factory methods for creating Load and Save objects.[LSException](LSException.html)Parser or write operations may throw an `LSException` if the processing is stopped.[LSInput](LSInput.html)This interface represents an input source for data.[LSLoadEvent](LSLoadEvent.html)This interface represents a load event object that signals the completion of a document load.[LSOutput](LSOutput.html)This interface represents an output destination for data.[LSParser](LSParser.html)An interface to an object that is able to build, or augment, a DOM tree from various input sources.[LSParserFilter](LSParserFilter.html)`LSParserFilter`s provide applications the ability to examine nodes as they are being constructed while parsing.[LSProgressEvent](LSProgressEvent.html)This interface represents a progress event object that notifies the application about progress as a document is parsed.[LSResourceResolver](LSResourceResolver.html)`LSResourceResolver` provides a way for applications to redirect references to external resources.[LSSerializer](LSSerializer.html)A `LSSerializer` provides an API for serializing (writing) a DOM document out into XML.[LSSerializerFilter](LSSerializerFilter.html)`LSSerializerFilter`s provide applications the ability to examine nodes as they are being serialized and decide what nodes should be serialized or not.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
