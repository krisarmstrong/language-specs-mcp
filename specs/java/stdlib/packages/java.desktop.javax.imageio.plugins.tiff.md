javax.imageio.plugins.tiff (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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
  - Related Packages
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- Related Packages | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../../../search.html)Module[java.desktop](../../../../module-summary.html)

# Package javax.imageio.plugins.tiff

package javax.imageio.plugins.tiffPublic classes used by the built-in TIFF plug-ins. 

 This package contains classes supporting the built-in TIFF reader and writer plug-ins. Classes are provided for simplifying interaction with metadata, including Exif metadata common in digital photography, and an extension of [ImageReadParam](../../ImageReadParam.html) which permits specifying which metadata tags are allowed to be read. For more information about the operation of the built-in TIFF plug-ins, see the [TIFF metadata format
 specification and usage notes](../../metadata/doc-files/tiff_metadata.html).

Since:9

- ClassesClassDescription[BaselineTIFFTagSet](BaselineTIFFTagSet.html)A class representing the set of tags found in the baseline TIFF specification as well as some common additional tags.[ExifGPSTagSet](ExifGPSTagSet.html)A class representing the tags found in an Exif GPS Info IFD.[ExifInteroperabilityTagSet](ExifInteroperabilityTagSet.html)A class representing the tags found in an Exif Interoperability IFD.[ExifParentTIFFTagSet](ExifParentTIFFTagSet.html)A class containing the TIFF tags used to reference the Exif and GPS IFDs.[ExifTIFFTagSet](ExifTIFFTagSet.html)A class representing the tags found in an Exif IFD.[FaxTIFFTagSet](FaxTIFFTagSet.html)A class representing the extra tags found in a [TIFF-F](https://tools.ietf.org/html/rfc2306.html) (RFC 2036) file.[GeoTIFFTagSet](GeoTIFFTagSet.html)A class representing the tags found in a GeoTIFF IFD.[TIFFDirectory](TIFFDirectory.html)A convenience class for simplifying interaction with TIFF native image metadata.[TIFFField](TIFFField.html)A class representing a field in a TIFF 6.0 Image File Directory.[TIFFImageReadParam](TIFFImageReadParam.html)A subclass of [ImageReadParam](../../ImageReadParam.html) allowing control over the TIFF reading process.[TIFFTag](TIFFTag.html)A class defining the notion of a TIFF tag.[TIFFTagSet](TIFFTagSet.html)A class representing a set of TIFF tags.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
