Module[java.naming](../../../module-summary.html)

# Package javax.naming.directory

package javax.naming.directoryExtends the `javax.naming` package to provide functionality for accessing directory services. 

 This package defines the directory operations of the Java Naming and Directory Interface (JNDI). JNDI provides naming and directory functionality to applications written in the Java programming language. It is designed to be independent of any specific naming or directory service implementation. Thus a variety of services--new, emerging, and already deployed ones--can be accessed in a common way. 

 This package allows applications to retrieve and update attributes associated with objects stored in a directory, and to search for objects using specified attributes. 

## The Directory Context

 The `DirContext` interface represents a directory context. It defines methods for examining and updating attributes associated with a directory object, or directory entry as it is sometimes called. 

 You use `getAttributes()` to retrieve the attributes associated with a directory object (for which you supply the name). Attributes are modified using `modifyAttributes()`. You can add, replace, or remove attributes and/or attribute values using this operation. 

`DirContext` also behaves as a naming context by extending the `Context` interface in the `javax.naming` package. This means that any directory object can also provide a naming context. For example, the directory object for a person might contain the attributes of that person, and at the same time provide a context for naming objects relative to that person such as his printers and home directory. 

### Searches

`DirContext` contains methods for performing content-based searching of the directory. In the simplest and most common form of usage, the application specifies a set of attributes--possibly with specific values--to match, and submits this attribute set, to the `search()` method. There are other overloaded forms of `search()` that support more sophisticated search filters. 

## Package Specification

 The JNDI API Specification and related documents can be found in the [JNDI documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=jndi_overview).Since:1.3

- Related PackagesPackageDescription[javax.naming](../package-summary.html)Provides the classes and interfaces for accessing naming services.[javax.naming.event](../event/package-summary.html)Provides support for event notification when accessing naming and directory services.[javax.naming.ldap](../ldap/package-summary.html)Provides support for LDAPv3 extended operations and controls.[javax.naming.spi](../spi/package-summary.html)Provides the means for dynamically plugging in support for accessing naming and directory services through the `javax.naming` and related packages.
- All Classes and InterfacesInterfacesClassesException ClassesClassDescription[Attribute](Attribute.html)This interface represents an attribute associated with a named object.[AttributeInUseException](AttributeInUseException.html)This exception is thrown when an operation attempts to add an attribute that already exists.[AttributeModificationException](AttributeModificationException.html)This exception is thrown when an attempt is made to add, or remove, or modify an attribute, its identifier, or its values that conflicts with the attribute's (schema) definition or the attribute's state.[Attributes](Attributes.html)This interface represents a collection of attributes.[BasicAttribute](BasicAttribute.html)This class provides a basic implementation of the `Attribute` interface.[BasicAttributes](BasicAttributes.html)This class provides a basic implementation of the Attributes interface.[DirContext](DirContext.html)The directory service interface, containing methods for examining and updating attributes associated with objects, and for searching the directory.[InitialDirContext](InitialDirContext.html)This class is the starting context for performing directory operations.[InvalidAttributeIdentifierException](InvalidAttributeIdentifierException.html)This exception is thrown when an attempt is made to add to create an attribute with an invalid attribute identifier.[InvalidAttributesException](InvalidAttributesException.html)This exception is thrown when an attempt is made to add or modify an attribute set that has been specified incompletely or incorrectly.[InvalidAttributeValueException](InvalidAttributeValueException.html)This class is thrown when an attempt is made to add to an attribute a value that conflicts with the attribute's schema definition.[InvalidSearchControlsException](InvalidSearchControlsException.html)This exception is thrown when the specification of the SearchControls for a search operation is invalid.[InvalidSearchFilterException](InvalidSearchFilterException.html)This exception is thrown when the specification of a search filter is invalid.[ModificationItem](ModificationItem.html)This class represents a modification item.[NoSuchAttributeException](NoSuchAttributeException.html)This exception is thrown when attempting to access an attribute that does not exist.[SchemaViolationException](SchemaViolationException.html)This exception is thrown when a method in some ways violates the schema.[SearchControls](SearchControls.html)This class encapsulates factors that determine scope of search and what gets returned as a result of the search.[SearchResult](SearchResult.html)This class represents an item in the NamingEnumeration returned as a result of the DirContext.search() methods.
