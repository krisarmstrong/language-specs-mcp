java.nio.file.spi (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

[SEARCH](../../../../../search.html)Module[java.base](../../../../module-summary.html)

# Package java.nio.file.spi

package java.nio.file.spiService-provider classes for the [java.nio.file](../package-summary.html) package. 

 Only developers who are defining new file system providers or file type detectors should need to make direct use of this package. 

 Unless otherwise noted, passing a `null` argument to a constructor or method in any class or interface in this package will cause a [NullPointerException](../../../lang/NullPointerException.html) to be thrown. In some cases methods which are specified to throw an `IOException` may throw a more specific [optional
 specific exception](../package-summary.html#optspecex).

Since:1.7

- Related PackagesPackageDescription[java.nio.file](../package-summary.html)Defines interfaces and classes for the Java virtual machine to access files, file attributes, and file systems.[java.nio.file.attribute](../attribute/package-summary.html)Interfaces and classes providing access to file and file system attributes.
- ClassesClassDescription[FileSystemProvider](FileSystemProvider.html)Service-provider class for file systems.[FileTypeDetector](FileTypeDetector.html)A file type detector for probing a file to guess its file type.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
