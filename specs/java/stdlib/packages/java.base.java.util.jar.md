Module[java.base](../../../module-summary.html)

# Package java.util.jar

package java.util.jarProvides classes for reading and writing the JAR (Java ARchive) file format, which is based on the standard ZIP file format with an optional manifest file. The manifest stores meta-information about the JAR file contents and is also used for signing JAR files. 

## Package Specification

 The `java.util.jar` package is based on the following specifications: 

- Info-ZIP file format - The JAR format is based on the Info-ZIP file format. See [java.util.zip
       package description.](../zip/package-summary.html#package-description)

 In JAR files, all file names must be encoded in the UTF-8 encoding. 
- [Manifest and Signature Specification](../../../../../specs/jar/jar.html) - The manifest format specification. 

Since:1.2External Specifications

- [JAR File Specification](../../../../../specs/jar/jar.html)

- Related PackagesPackageDescription[java.util](../package-summary.html)Contains the collections framework, some internationalization support classes, a service loader, properties, random number generation, string parsing and scanning classes, base64 encoding and decoding, a bit array, and several miscellaneous utility classes.
- All Classes and InterfacesClassesException ClassesClassDescription[Attributes](Attributes.html)The Attributes class maps Manifest attribute names to associated string values.[Attributes.Name](Attributes.Name.html)The Attributes.Name class represents an attribute name stored in this Map.[JarEntry](JarEntry.html)This class is used to represent a JAR file entry.[JarException](JarException.html)Signals that an error of some sort has occurred while reading from or writing to a JAR file.[JarFile](JarFile.html)The `JarFile` class is used to read the contents of a jar file from any file that can be opened with `java.io.RandomAccessFile`.[JarInputStream](JarInputStream.html)The `JarInputStream` class, which extends [ZipInputStream](../zip/ZipInputStream.html), is used to read the contents of a JAR file from an input stream.[JarOutputStream](JarOutputStream.html)The `JarOutputStream` class is used to write the contents of a JAR file to any output stream.[Manifest](Manifest.html)The Manifest class is used to maintain Manifest entry names and their associated Attributes.
