javax.xml.validation (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

- [Overview](../../../../index.html)
- [Module](../../../module-summary.html)
- Package
- Class
- [Use](package-use.html)
- [Tree](package-tree.html)
- [Preview](../../../../preview-list.html)
- [New](../../../../new-list.html)
- [Deprecated](../../../../deprecated-list.html)
- [Index](../../../../index-files/index-1.html)
- [Help](../../../../help-doc.html#package)

- 

Package:

  - [Description](#package-description)
  - [Related Packages](#related-package-summary)
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- [Related Packages](#related-package-summary) | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../../search.html)Module[java.xml](../../../module-summary.html)

# Package javax.xml.validation

package javax.xml.validation

 Provides an API for validation of XML documents. Validation is the process of verifying that an XML document is an instance of a specified XML schema. An XML schema defines the content model (also called a grammar or vocabulary) that its instance documents will represent. 

 There are a number of popular technologies available for creating an XML schema. Some of the most popular ones include: 

- Document Type Definition (DTD) - XML's built-in schema language. 
- [W3C XML Schema (WXS)](https://www.w3.org/XML/Schema) - an object-oriented XML schema language. WXS also provides a type system for constraining the character data of an XML document. WXS is maintained by the [World Wide Web Consortium (W3C)](https://www.w3.org) and is a W3C Recommendation (that is, a ratified W3C standard specification). 
- [RELAX NG (RNG)](https://relaxng.org/) - a pattern-based, user-friendly XML schema language. RNG schemas may also use types to constrain XML character data. RNG is maintained by the [Organization for the Advancement
         of Structured Information Standards (OASIS)](https://www.oasis-open.org) and is both an OASIS and an [ISO (International Organization
         for Standardization)](https://www.iso.org/home.html) standard. 
- [Schematron](https://standards.iso.org/ittf/PubliclyAvailableStandards/c055982_ISO_IEC_19757-3_2016.zip) - a rules-based XML schema language. Whereas DTD, WXS, and RNG are designed to express the structure of a content model, Schematron is designed to enforce individual rules that are difficult or impossible to express with other schema languages. Schematron is intended to supplement a schema written in structural schema language such as the aforementioned. Schematron is [an ISO standard](https://standards.iso.org/ittf/PubliclyAvailableStandards/index.html). 

 While JAXP supports validation as a feature of an XML parser, represented by either a [SAXParser](../parsers/SAXParser.html) or [DocumentBuilder](../parsers/DocumentBuilder.html) instance, the `Validation` API is preferred. 

 The JAXP validation API decouples the validation of an instance document from the parsing of an XML document. This is advantageous for several reasons, some of which are: 

- Support for additional schema languages. The JAXP parser implementations support only a subset of the available XML schema languages. The Validation API provides a standard mechanism through which applications may take of advantage of specialization validation libraries which support additional schema languages. 
- Easy runtime coupling of an XML instance and schema. Specifying the location of a schema to use for validation with JAXP parsers can be confusing. The Validation API makes this process simple (see [example](#example-1) below). 

Usage example. The following example demonstrates validating an XML document with the Validation API (for readability, some exception handling is not shown): 

```

     // parse an XML document into a DOM tree
     DocumentBuilder parser = DocumentBuilderFactory.newInstance().newDocumentBuilder();
     Document document = parser.parse(new File("instance.xml"));

     // create a SchemaFactory capable of understanding WXS schemas
     SchemaFactory factory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);

     // load a WXS schema, represented by a Schema instance
     Source schemaFile = new StreamSource(new File("mySchema.xsd"));
     Schema schema = factory.newSchema(schemaFile);

     // create a Validator instance, which can be used to validate an instance document
     Validator validator = schema.newValidator();

     // validate the DOM tree
     try {
         validator.validate(new DOMSource(document));
     } catch (SAXException e) {
         // instance document is invalid!
     }
 
```

 The JAXP parsing API has been integrated with the Validation API. Applications may create a [Schema](Schema.html) with the validation API and associate it with a [DocumentBuilderFactory](../parsers/DocumentBuilderFactory.html) or a [SAXParserFactory](../parsers/SAXParserFactory.html) instance by using the [DocumentBuilderFactory.setSchema(Schema)](../parsers/DocumentBuilderFactory.html#setSchema(javax.xml.validation.Schema)) and [SAXParserFactory.setSchema(Schema)](../parsers/SAXParserFactory.html#setSchema(javax.xml.validation.Schema)) methods. You should not both set a schema and call `setValidating(true)` on a parser factory. The former technique will cause parsers to use the new validation API; the latter will cause parsers to use their own internal validation facilities. Turning on both of these options simultaneously will cause either redundant behavior or error conditions.

Since:1.5

- Related PackagesPackageDescription[javax.xml](../package-summary.html)Defines constants for XML processing.
- All Classes and InterfacesClassesException ClassesClassDescription[Schema](Schema.html)Immutable in-memory representation of grammar.[SchemaFactory](SchemaFactory.html)Factory that creates [Schema](Schema.html) objects.[SchemaFactoryConfigurationError](SchemaFactoryConfigurationError.html)Thrown when a problem with configuration with the Schema Factories exists.[SchemaFactoryLoader](SchemaFactoryLoader.html)Factory that creates [SchemaFactory](SchemaFactory.html).[TypeInfoProvider](TypeInfoProvider.html)This class provides access to the type information determined by [ValidatorHandler](ValidatorHandler.html).[Validator](Validator.html)A processor that checks an XML document against [Schema](Schema.html).[ValidatorHandler](ValidatorHandler.html)Streaming validator that works on SAX stream.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
