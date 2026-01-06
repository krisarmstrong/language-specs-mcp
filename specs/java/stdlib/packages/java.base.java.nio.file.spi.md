Module[java.base](../../../../module-summary.html)

# Package java.nio.file.spi

package java.nio.file.spiService-provider classes for the [java.nio.file](../package-summary.html) package. 

 Only developers who are defining new file system providers or file type detectors should need to make direct use of this package. 

 Unless otherwise noted, passing a `null` argument to a constructor or method in any class or interface in this package will cause a [NullPointerException](../../../lang/NullPointerException.html) to be thrown. In some cases methods which are specified to throw an `IOException` may throw a more specific [optional
 specific exception](../package-summary.html#optspecex).

Since:1.7

- Related PackagesPackageDescription[java.nio.file](../package-summary.html)Defines interfaces and classes for the Java virtual machine to access files, file attributes, and file systems.[java.nio.file.attribute](../attribute/package-summary.html)Interfaces and classes providing access to file and file system attributes.
- ClassesClassDescription[FileSystemProvider](FileSystemProvider.html)Service-provider class for file systems.[FileTypeDetector](FileTypeDetector.html)A file type detector for probing a file to guess its file type.
