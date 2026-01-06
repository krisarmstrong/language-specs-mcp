Module[java.xml](../../../module-summary.html)

# Package javax.xml.xpath

package javax.xml.xpathProvides an object-model neutral API for the evaluation of XPath expressions and access to the evaluation environment. 

 The XPath API supports [XML Path Language (XPath) Version 1.0](http://www.w3.org/TR/xpath)

- [1. XPath Overview](#XPath.Overview)
- [2. XPath Expressions](#XPath.Expressions)
- [3. XPath Data Types](#XPath.Datatypes)

  - [3.1 QName Types](#XPath.Datatypes.QName)
  - [3.2 Class Types](#XPath.Datatypes.Class)
  - [3.3 Enum Types](#XPath.Datatypes.Enum)

- [4. XPath Context](#XPath.Context)
- [5. Using the XPath API](#XPath.Use)

## 1. XPath Overview

 The XPath language provides a simple, concise syntax for selecting nodes from an XML document. XPath also provides rules for converting a node in an XML document object model (DOM) tree to a boolean, double, or string value. XPath is a W3C-defined language and an official W3C recommendation; the W3C hosts the XML Path Language (XPath) Version 1.0 specification. 

 XPath started in life in 1999 as a supplement to the XSLT and XPointer languages, but has more recently become popular as a stand-alone language, as a single XPath expression can be used to replace many lines of DOM API code. 

## 2. XPath Expressions

 An XPath expression is composed of a location path and one or more optional predicates. Expressions may also include XPath variables. 

 The following is an example of a simple XPath expression: 

```

     /foo/bar
 
```

 This example would select the `<bar>` element in an XML document such as the following: 

```

     <foo>
         <bar/>
     </foo>
 
```

The expression `/foo/bar` is an example of a location path. While XPath location paths resemble Unix-style file system paths, an important distinction is that XPath expressions return all nodes that match the expression. Thus, all three `<bar>` elements in the following document would be selected by the `/foo/bar` expression: 

```

     <foo>
         <bar/>
         <bar/>
         <bar/>
     </foo>
 
```

 A special location path operator, `//`, selects nodes at any depth in an XML document. The following example selects all `<bar>` elements regardless of their location in a document: 

```

     //bar
 
```

 A wildcard operator, *, causes all element nodes to be selected. The following example selects all children elements of a `<foo>` element: 

```

     /foo/*
 
```

 In addition to element nodes, XPath location paths may also address attribute nodes, text nodes, comment nodes, and processing instruction nodes. The following table gives examples of location paths for each of these node types: Examples of Location PathLocation PathDescription`/foo/bar/@id` Selects the attribute `id` of the `<bar>` element `/foo/bar/text()` Selects the text nodes of the `<bar>` element. No distinction is made between escaped and non-escaped character data. `/foo/bar/comment()` Selects all comment nodes contained in the `<bar>` element. `/foo/bar/processing-instruction()` Selects all processing-instruction nodes contained in the `<bar>` element. 

 Predicates allow for refining the nodes selected by an XPath location path. Predicates are of the form `[expression]`. The following example selects all `<foo>` elements that contain an `include` attribute with the value of `true`: 

```

     //foo[@include='true']
 
```

 Predicates may be appended to each other to further refine an expression, such as: 

```

     //foo[@include='true'][@mode='bar']
 
```

## 3. XPath Data Types

 While XPath expressions select nodes in the XML document, the XPath API allows the selected nodes to be coalesced into one of the following data types: 

- `Boolean`
- `Number`
- `String`

## 3.1 QName types

 The XPath API defines the following [QName](../namespace/QName.html) types to represent return types of an XPath evaluation: 

- [XPathConstants.NODESET](XPathConstants.html#NODESET)
- [XPathConstants.NODE](XPathConstants.html#NODE)
- [XPathConstants.STRING](XPathConstants.html#STRING)
- [XPathConstants.BOOLEAN](XPathConstants.html#BOOLEAN)
- [XPathConstants.NUMBER](XPathConstants.html#NUMBER)

 The return type is specified by a [QName](../namespace/QName.html) parameter in method call used to evaluate the expression, which is either a call to `XPathExpression.evaluate(...)` or `XPath.evaluate(...)` methods. 

 When a `Boolean` return type is requested, `Boolean.TRUE` is returned if one or more nodes were selected; otherwise, `Boolean.FALSE` is returned. 

 The `String` return type is a convenience for retrieving the character data from a text node, attribute node, comment node, or processing-instruction node. When used on an element node, the value of the child text nodes is returned. 

 The `Number` return type attempts to coalesce the text of a node to a `double` data type. 

## 3.2 Class types

 In addition to the QName types, the XPath API supports the use of Class types through the `XPathExpression.evaluateExpression(...)` or `XPath.evaluateExpression(...)` methods. The XPath data types are mapped to Class types as follows: 

- `Boolean` -- `Boolean.class`
- `Number` -- `Number.class`
- `String` -- `String.class`
- `Nodeset` -- `XPathNodes.class`
- `Node` -- `Node.class`

 Of the subtypes of `Number`, only `Double, Integer` and `Long` are supported. 

## 3.3 Enum types

 Enum types are defined in [XPathEvaluationResult.XPathResultType](XPathEvaluationResult.XPathResultType.html) that provide mappings between the QName and Class types above. The result of evaluating an expression using the `XPathExpression.evaluateExpression(...)` or `XPath.evaluateExpression(...)` methods will be of one of these types. 

 Note the differences between the Enum and [QName](#XPath.Datatypes.QName) mappings: 

- [NUMBER](XPathConstants.html#NUMBER)
 The Enum mapping for [NUMBER](XPathConstants.html#NUMBER) supports `Double, Integer` and `Long`.

- [NODESET](XPathConstants.html#NODESET)
 The Enum mapping for [NODESET](XPathConstants.html#NODESET) is [XPathNodes](XPathNodes.html) instead of [NodeList](../../../org/w3c/dom/NodeList.html) in the [QName](#XPath.Datatypes.QName) mapping. 

## 4. XPath Context

 XPath location paths may be relative to a particular node in the document, known as the `context`. A context consists of: 

- a node (the context node)
- a pair of non-zero positive integers (the context position and the context size)
- a set of variable bindings
- a function library
- the set of namespace declarations in scope for the expression

 It is an XML document tree represented as a hierarchy of nodes, a [Node](../../../org/w3c/dom/Node.html) for example, in the JDK implementation. 

## 5. Using the XPath API

 Consider the following XML document: 

```

 <widgets>
 <widget>
 <manufacturer/>
 <dimensions/>
 </widget>
 </widgets>
 
```

 The `<widget>` element can be selected with the following process: 

```

     // parse the XML as a W3C Document
     DocumentBuilder builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();
     Document document = builder.parse(new File("/widgets.xml"));

     //Get an XPath object and evaluate the expression
     XPath xpath = XPathFactory.newInstance().newXPath();
     String expression = "/widgets/widget";
     Node widgetNode = (Node) xpath.evaluate(expression, document, XPathConstants.NODE);

     //or using the evaluateExpression method
     Node widgetNode = xpath.evaluateExpression(expression, document, Node.class);
 
```

 With a reference to the `<widget>` element, a relative XPath expression can be written to select the `<manufacturer>` child element: 

```

     XPath xpath = XPathFactory.newInstance().newXPath();
     String expression = "manufacturer";
     Node manufacturerNode = (Node) xpath.evaluate(expression, widgetNode, XPathConstants.NODE);

     //or using the evaluateExpression method
     Node manufacturerNode = xpath.evaluateExpression(expression, widgetNode, Node.class);
 
```

 In the above example, the XML file is read into a DOM Document before being passed to the XPath API. The following code demonstrates the use of InputSource to leave it to the XPath implementation to process it: 

```

     XPath xpath = XPathFactory.newInstance().newXPath();
     String expression = "/widgets/widget";
     InputSource inputSource = new InputSource("widgets.xml");
     NodeList nodes = (NodeList) xpath.evaluate(expression, inputSource, XPathConstants.NODESET);

     //or using the evaluateExpression method
     XPathNodes nodes = xpath.evaluateExpression(expression, inputSource, XPathNodes.class);
 
```

 In the above cases, the type of the expected results are known. In case where the result type is unknown or any type, the [XPathEvaluationResult](XPathEvaluationResult.html) may be used to determine the return type. The following code demonstrates the usage: 

```

     XPathEvaluationResult<?> result = xpath.evaluateExpression(expression, document);
     switch (result.type()) {
         case NODESET:
             XPathNodes nodes = (XPathNodes)result.value();
             ...
             break;
     }
 
```

 The XPath 1.0 Number data type is defined as a double. However, the XPath specification also provides functions that returns Integer type. To facilitate such operations, the XPath API allows Integer and Long to be used in `evaluateExpression` method such as the following code: 

```

     int count = xpath.evaluateExpression("count(/widgets/widget)", document, Integer.class);
 
```

Since:1.5

- Related PackagesPackageDescription[javax.xml](../package-summary.html)Defines constants for XML processing.
- All Classes and InterfacesInterfacesClassesEnum ClassesException ClassesClassDescription[XPath](XPath.html)`XPath` provides access to the XPath evaluation environment and expressions.[XPathConstants](XPathConstants.html)XPath constants.[XPathEvaluationResult](XPathEvaluationResult.html)<T>The `XPathEvaluationResult` interface represents the result of the evaluation of an XPath expression within the context of a particular node.[XPathEvaluationResult.XPathResultType](XPathEvaluationResult.XPathResultType.html)XPathResultType represents possible return types of an XPath evaluation.[XPathException](XPathException.html)`XPathException` represents a generic XPath exception.[XPathExpression](XPathExpression.html)`XPathExpression` provides access to compiled XPath expressions.[XPathExpressionException](XPathExpressionException.html)`XPathExpressionException` represents an error in an XPath expression.[XPathFactory](XPathFactory.html)An `XPathFactory` instance can be used to create [XPath](XPath.html) objects.[XPathFactoryConfigurationException](XPathFactoryConfigurationException.html)`XPathFactoryConfigurationException` represents a configuration error in a `XPathFactory` environment.[XPathFunction](XPathFunction.html)`XPathFunction` provides access to XPath functions.[XPathFunctionException](XPathFunctionException.html)`XPathFunctionException` represents an error with an XPath function.[XPathFunctionResolver](XPathFunctionResolver.html)`XPathFunctionResolver` provides access to the set of user defined `XPathFunction`s.[XPathNodes](XPathNodes.html)XPathNodes represents a set of nodes selected by a location path as specified in [XML Path Language (XPath)
 Version 1.0, 3.3 Node-sets](http://www.w3.org/TR/xpath/#node-sets).[XPathVariableResolver](XPathVariableResolver.html)`XPathVariableResolver` provides access to the set of user defined XPath variables.
