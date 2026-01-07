javax.imageio.plugins.jpeg (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

# Package javax.imageio.plugins.jpeg

package javax.imageio.plugins.jpegClasses supporting the built-in JPEG plug-in. 

 This package contains some support classes for the built-in JPEG reader and writer plug-ins. Classes are provided for representing quantization and Huffman tables, and extensions of `ImageReadParam` and `ImageWriteParam` are provided to supply tables during the reading and writing process. For more information about the operation of the built-in JPEG plug-ins, see the [JPEG metadata format
 specification and usage notes](../../metadata/doc-files/jpeg_metadata.html).

Since:1.4

- ClassesClassDescription[JPEGHuffmanTable](JPEGHuffmanTable.html)A class encapsulating a single JPEG Huffman table.[JPEGImageReadParam](JPEGImageReadParam.html)This class adds the ability to set JPEG quantization and Huffman tables when using the built-in JPEG reader plug-in.[JPEGImageWriteParam](JPEGImageWriteParam.html)This class adds the ability to set JPEG quantization and Huffman tables when using the built-in JPEG writer plug-in, and to request that optimized Huffman tables be computed for an image.[JPEGQTable](JPEGQTable.html)A class encapsulating a single JPEG quantization table.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
