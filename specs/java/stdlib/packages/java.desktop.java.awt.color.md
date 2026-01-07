java.awt.color (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

[SEARCH](../../../../search.html)Module[java.desktop](../../../module-summary.html)

# Package java.awt.color

package java.awt.colorProvides classes for color spaces. It contains an implementation of a color space based on the International Color Consortium (ICC) Profile Format Specification, Version 3.4, August 15, 1997. It also contains color profiles based on the ICC Profile Format Specification.Since:1.2

- Related PackagesPackageDescription[java.awt](../package-summary.html)Contains all of the classes for creating user interfaces and for painting graphics and images.
- All Classes and InterfacesClassesException ClassesClassDescription[CMMException](CMMException.html)This exception is thrown if the native CMM returns an error.[ColorSpace](ColorSpace.html)This abstract class is used to serve as a color space tag to identify the specific color space of a `Color` object or, via a `ColorModel` object, of an `Image`, a `BufferedImage`, or a `GraphicsDevice`.[ICC_ColorSpace](ICC_ColorSpace.html)The `ICC_ColorSpace` class is an implementation of the abstract `ColorSpace` class.[ICC_Profile](ICC_Profile.html)A representation of color profile data for device independent and device dependent color spaces based on the International Color Consortium Specification ICC.1:2001-12, File Format for Color Profiles, (see [http://www.color.org](http://www.color.org)).[ICC_ProfileGray](ICC_ProfileGray.html)The `ICC_ProfileGray` class is a subclass of the `ICC_Profile` class that represents profiles which meet the following criteria: the color space type of the profile is `TYPE_GRAY` and the profile includes the `grayTRCTag` and `mediaWhitePointTag` tags.[ICC_ProfileRGB](ICC_ProfileRGB.html)The `ICC_ProfileRGB` class is a subclass of the `ICC_Profile` class that represents profiles which meet the following criteria: the profile's color space type is RGB, and the profile includes the `redColorantTag`, `greenColorantTag`, `blueColorantTag`, `redTRCTag`, `greenTRCTag`, `blueTRCTag`, `mediaWhitePointTag` tags.[ProfileDataException](ProfileDataException.html)This exception is thrown when an error occurs in accessing or processing an `ICC_Profile` object.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
