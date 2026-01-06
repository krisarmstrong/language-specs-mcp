Module[java.xml](../../../module-summary.html)

# Package javax.xml.catalog

package javax.xml.catalogProvides the classes for implementing [XML Catalogs OASIS Standard V1.1, 7 October 2005](https://www.oasis-open.org/committees/download.php/14809/xml-catalogs.html). 

 The Catalog API defines a standard solution for resolving external resources referenced by XML documents. It is fully supported by the XML Processors allowing application developers to configure a catalog through an XML processor or system property or the configuration file to take advantage of the feature. 

 The XML Catalog API defines the following interfaces: 

- [Catalog](Catalog.html) -- The [Catalog](Catalog.html) interface represents an entity catalog as defined by the Catalog standard. A [Catalog](Catalog.html) object is immutable. Once created, it can be used to find matches in a `system`, `public` or `uri` entry. A custom resolver implementation may find it useful for locating local resources through a catalog. 
- [CatalogFeatures](CatalogFeatures.html) -- The [CatalogFeatures](CatalogFeatures.html) class holds all of the features and properties the Catalog API supports, including `javax.xml.catalog.files`, `javax.xml.catalog.defer`, `javax.xml.catalog.prefer`, and `javax.xml.catalog.resolve`. 
- [CatalogManager](CatalogManager.html) -- The [CatalogManager](CatalogManager.html) class manages the creation of XML catalogs and catalog resolvers. 
- [CatalogResolver](CatalogResolver.html) -- The [CatalogResolver](CatalogResolver.html) class is a `Catalog` resolver that implements [EntityResolver](../../../org/xml/sax/EntityResolver.html), [XMLResolver](../stream/XMLResolver.html), [LSResourceResolver](../../../org/w3c/dom/ls/LSResourceResolver.html), and [URIResolver](../transform/URIResolver.html), and resolves external references using catalogs. 

 Unless otherwise noted, passing a null argument to a constructor or method in any class or interface in this package will cause a `NullPointerException` to be thrown.

Since:9

- Related PackagesPackageDescription[javax.xml](../package-summary.html)Defines constants for XML processing.
- All Classes and InterfacesInterfacesClassesEnum ClassesException ClassesClassDescription[Catalog](Catalog.html)The Catalog class represents an entity Catalog as defined by [XML Catalogs, OASIS Standard V1.1, 7 October 2005](https://www.oasis-open.org/committees/download.php/14809/xml-catalogs.html).[CatalogException](CatalogException.html)The exception class handles errors that may happen while processing or using a catalog.[CatalogFeatures](CatalogFeatures.html)The CatalogFeatures holds a collection of features and properties.[CatalogFeatures.Builder](CatalogFeatures.Builder.html)The Builder class for building the CatalogFeatures object.[CatalogFeatures.Feature](CatalogFeatures.Feature.html)A Feature type as defined in the [Catalog Features table](CatalogFeatures.html#CatalogFeatures).[CatalogManager](CatalogManager.html)The Catalog Manager manages the creation of XML Catalogs and Catalog Resolvers.[CatalogResolver](CatalogResolver.html)A Catalog Resolver that implements SAX [EntityResolver](../../../org/xml/sax/EntityResolver.html), StAX [XMLResolver](../stream/XMLResolver.html), DOM LS [LSResourceResolver](../../../org/w3c/dom/ls/LSResourceResolver.html) used by Schema Validation, and Transform [URIResolver](../transform/URIResolver.html), and resolves external references using catalogs.
