java.util.spi (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

[SEARCH](../../../../search.html)Module[java.base](../../../module-summary.html)

# Package java.util.spi

package java.util.spiService provider classes for the classes in the java.util package.Since:1.6

- Related PackagesPackageDescription[java.util](../package-summary.html)Contains the collections framework, some internationalization support classes, a service loader, properties, random number generation, string parsing and scanning classes, base64 encoding and decoding, a bit array, and several miscellaneous utility classes.
- All Classes and InterfacesInterfacesClassesClassDescription[AbstractResourceBundleProvider](AbstractResourceBundleProvider.html)`AbstractResourceBundleProvider` is an abstract class that provides the basic support for a provider implementation class for [ResourceBundleProvider](ResourceBundleProvider.html).[CalendarDataProvider](CalendarDataProvider.html)An abstract class for service providers that provide locale-dependent [Calendar](../Calendar.html) parameters.[CalendarNameProvider](CalendarNameProvider.html)An abstract class for service providers that provide localized string representations (display names) of `Calendar` field values.[CurrencyNameProvider](CurrencyNameProvider.html)An abstract class for service providers that provide localized currency symbols and display names for the [Currency](../Currency.html) class.[LocaleNameProvider](LocaleNameProvider.html)An abstract class for service providers that provide localized names for the [Locale](../Locale.html) class.[LocaleServiceProvider](LocaleServiceProvider.html) This is the super class of all the locale sensitive service provider interfaces (SPIs).[ResourceBundleControlProvider](ResourceBundleControlProvider.html)An interface for service providers that provide implementations of [ResourceBundle.Control](../ResourceBundle.Control.html).[ResourceBundleProvider](ResourceBundleProvider.html)`ResourceBundleProvider` is a service provider interface for resource bundles.[TimeZoneNameProvider](TimeZoneNameProvider.html)An abstract class for service providers that provide localized time zone names for the [TimeZone](../TimeZone.html) class.[ToolProvider](ToolProvider.html)An interface for command-line tools to provide a way to be invoked without necessarily starting a new VM.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
