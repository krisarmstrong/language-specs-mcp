Module[java.xml](../../../module-summary.html)

# Package javax.xml.datatype

package javax.xml.datatype

 Defines XML/Java Type Mappings. 

 This API provides XML/Java type mappings. 

 The following XML standards apply: 

- [W3C XML Schema 1.0 Part 2, Section 3.2.7-14](http://www.w3.org/TR/xmlschema-2/#dateTime)
- [XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration](http://www.w3.org/TR/xpath-datamodel#dt-dayTimeDuration)
- [XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration](http://www.w3.org/TR/xpath-datamodel#dt-yearMonthDuration)

 W3C XML Schema/Java Type MappingsW3C XML Schema Data TypeJava Data Typexs:date[XMLGregorianCalendar](XMLGregorianCalendar.html)xs:dateTime[XMLGregorianCalendar](XMLGregorianCalendar.html)xs:duration[Duration](Duration.html)xs:gDay[XMLGregorianCalendar](XMLGregorianCalendar.html)xs:gMonth [XMLGregorianCalendar](XMLGregorianCalendar.html)xs:gMonthDay[XMLGregorianCalendar](XMLGregorianCalendar.html)xs:gYear[XMLGregorianCalendar](XMLGregorianCalendar.html)xs:gYearMonth[XMLGregorianCalendar](XMLGregorianCalendar.html)xs:time[XMLGregorianCalendar](XMLGregorianCalendar.html)XQuery and XPath/Java Type MappingsXQuery 1.0 and XPath 2.0 Data ModelJava Data Typexdt:dayTimeDuration[Duration](Duration.html)xdt:yearMonthDuration[Duration](Duration.html)

 W3C XML Schema data types that have a "natural" mapping to Java types are defined by JSR 31: Java Architecture for XML Binding (JAXB) Specification, Binding XML Schema to Java Representations. JAXB defined mappings for XML Schema built-in data types include: 

- xs:anySimpleType
- xs:base64Binary
- xs:boolean
- xs:byte
- xs:decimal
- xs:double
- xs:float
- xs:hexBinary
- xs:int
- xs:integer
- xs:long
- xs:QName
- xs:short
- xs:string
- xs:unsignedByte
- xs:unsignedInt
- xs:unsignedShort

Since:1.5See Also:

- [W3C XML Schema 1.0 Part 2, Section 3.2.7-14](http://www.w3.org/TR/xmlschema-2/#dateTime)
- [XQuery 1.0 and XPath 2.0 Data Model, xdt:dayTimeDuration](http://www.w3.org/TR/xpath-datamodel#dt-dayTimeDuration)
- [XQuery 1.0 and XPath 2.0 Data Model, xdt:yearMonthDuration](http://www.w3.org/TR/xpath-datamodel#dt-yearMonthDuration)

- Related PackagesPackageDescription[javax.xml](../package-summary.html)Defines constants for XML processing.
- All Classes and InterfacesClassesException ClassesClassDescription[DatatypeConfigurationException](DatatypeConfigurationException.html)Indicates a serious configuration error.[DatatypeConstants](DatatypeConstants.html)Utility class to contain basic Datatype values as constants.[DatatypeConstants.Field](DatatypeConstants.Field.html)Type-safe enum class that represents six fields of the [Duration](Duration.html) class.[DatatypeFactory](DatatypeFactory.html)Factory that creates new `javax.xml.datatype``Object`s that map XML to/from Java `Object`s.[Duration](Duration.html)Immutable representation of a time span as defined in the W3C XML Schema 1.0 specification.[XMLGregorianCalendar](XMLGregorianCalendar.html)Representation for W3C XML Schema 1.0 date/time datatypes.
