Module[jdk.xml.dom](../../../../module-summary.html)

# Package org.w3c.dom.xpath

package org.w3c.dom.xpathProvides interfaces for DOM Level 3 XPath Specification. The XPath module provides simple functionalities to access a DOM tree using [XPath 1.0](https://www.w3.org/TR/1999/REC-xpath-19991116/). 

 The interfaces and classes in this package came from Document Object Model (DOM) Level 3 XPath Specification, Working Draft 20 August 2002. Refer to [Document Object Model (DOM) Level 3 XPath Specification, Version 1.0,
 W3C Working Group Note 26 February 2004](https://www.w3.org/TR/DOM-Level-3-XPath/) except that the values of [XPathException.INVALID_EXPRESSION_ERR](XPathException.html#INVALID_EXPRESSION_ERR) and [XPathException.TYPE_ERR](XPathException.html#TYPE_ERR) are 1 and 2 respectively (instead of 51 and 52).

Since:1.4

- Related PackagesModulePackageDescription[java.xml](../../../../../java.xml/module-summary.html)[org.w3c.dom](../../../../../java.xml/org/w3c/dom/package-summary.html)Provides the interfaces for the Document Object Model (DOM).
- All Classes and InterfacesInterfacesException ClassesClassDescription[XPathEvaluator](XPathEvaluator.html)The evaluation of XPath expressions is provided by `XPathEvaluator`.[XPathException](XPathException.html)A new exception has been created for exceptions specific to these XPath interfaces.[XPathExpression](XPathExpression.html)The `XPathExpression` interface represents a parsed and resolved XPath expression.[XPathNamespace](XPathNamespace.html)The `XPathNamespace` interface is returned by `XPathResult` interfaces to represent the XPath namespace node type that DOM lacks.[XPathNSResolver](XPathNSResolver.html)The `XPathNSResolver` interface permit `prefix` strings in the expression to be properly bound to `namespaceURI` strings.[XPathResult](XPathResult.html)The `XPathResult` interface represents the result of the evaluation of an XPath 1.0 expression within the context of a particular node.
