java.util.prefs (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

[SEARCH](../../../../search.html)Module[java.prefs](../../../module-summary.html)

# Package java.util.prefs

package java.util.prefsThis package allows applications to store and retrieve user and system preference and configuration data. This data is stored persistently in an implementation-dependent backing store. There are two separate trees of preference nodes, one for user preferences and one for system preferences.Since:1.4

- Related PackagesModulePackageDescription[java.base](../../../../java.base/module-summary.html)[java.util](../../../../java.base/java/util/package-summary.html)Contains the collections framework, some internationalization support classes, a service loader, properties, random number generation, string parsing and scanning classes, base64 encoding and decoding, a bit array, and several miscellaneous utility classes.
- All Classes and InterfacesInterfacesClassesException ClassesClassDescription[AbstractPreferences](AbstractPreferences.html)This class provides a skeletal implementation of the [Preferences](Preferences.html) class, greatly easing the task of implementing it.[BackingStoreException](BackingStoreException.html)Thrown to indicate that a preferences operation could not complete because of a failure in the backing store, or a failure to contact the backing store.[InvalidPreferencesFormatException](InvalidPreferencesFormatException.html)Thrown to indicate that an operation could not complete because the input did not conform to the appropriate XML document type for a collection of preferences, as per the [Preferences](Preferences.html) specification.[NodeChangeEvent](NodeChangeEvent.html)An event emitted by a `Preferences` node to indicate that a child of that node has been added or removed.[NodeChangeListener](NodeChangeListener.html)A listener for receiving preference node change events.[PreferenceChangeEvent](PreferenceChangeEvent.html)An event emitted by a `Preferences` node to indicate that a preference has been added, removed or has had its value changed.[PreferenceChangeListener](PreferenceChangeListener.html)A listener for receiving preference change events.[Preferences](Preferences.html)A node in a hierarchical collection of preference data.[PreferencesFactory](PreferencesFactory.html)A factory object that generates Preferences objects.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
