java.nio.charset (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

# Package java.nio.charset

package java.nio.charsetDefines charsets, decoders, and encoders, for translating between bytes and Unicode characters. Summary of charsets, decoders, and encoders in this packageClass nameDescription [Charset](Charset.html)A named mapping between characters and bytes[CharsetDecoder](CharsetDecoder.html)Decodes bytes into characters[CharsetEncoder](CharsetEncoder.html)Encodes characters into bytes[CoderResult](CoderResult.html)Describes coder results[CodingErrorAction](CodingErrorAction.html)Describes actions to take when coding errors are detected

 A charset is named mapping between sequences of sixteen-bit Unicode characters and sequences of bytes, in the sense defined in [RFC 2278](http://www.ietf.org/rfc/rfc2278.txt). A decoder is an engine which transforms bytes in a specific charset into characters, and an encoder is an engine which transforms characters into bytes. Encoders and decoders operate on byte and character buffers. They are collectively referred to as coders. 

 The [Charset](Charset.html) class defines methods for creating coders for a given charset and for retrieving the various names associated with a charset. It also defines static methods for testing whether a particular charset is supported, for locating charset instances by name, and for constructing a map that contains every charset for which support is available in the current Java virtual machine. 

 Most users will not use these classes directly; instead they will use the existing charset-related constructors and methods in the [String](../../lang/String.html) class, together with the existing [InputStreamReader](../../io/InputStreamReader.html) and [OutputStreamWriter](../../io/OutputStreamWriter.html) classes, all of whose implementations have been reworked to make use of the charset facilities defined in this package. A small number of changes have been made to the [InputStreamReader](../../io/InputStreamReader.html) and [OutputStreamWriter](../../io/OutputStreamWriter.html) classes in order to allow explicit charset objects to be specified in the construction of instances of those classes. 

 Support for new charsets can be made available via the interface defined in the [CharsetProvider](spi/CharsetProvider.html) class in the [java.nio.charset.spi](spi/package-summary.html) package. 

 Unless otherwise noted, passing a `null` argument to a constructor or method in any class or interface in this package will cause a [NullPointerException](../../lang/NullPointerException.html) to be thrown.

Since:1.4External Specifications

- [RFC 2278: IANA Charset Registration Procedures](https://www.rfc-editor.org/info/rfc2278)

- Related PackagesPackageDescription[java.nio](../package-summary.html)Defines buffers, which are containers for data, and provides an overview of the other NIO packages.[java.nio.charset.spi](spi/package-summary.html)Service-provider classes for the [java.nio.charset](package-summary.html) package.[java.nio.channels](../channels/package-summary.html)Defines channels, which represent connections to entities that are capable of performing I/O operations, such as files and sockets; defines selectors, for multiplexed, non-blocking I/O operations.[java.nio.file](../file/package-summary.html)Defines interfaces and classes for the Java virtual machine to access files, file attributes, and file systems.
- All Classes and InterfacesClassesException ClassesClassDescription[CharacterCodingException](CharacterCodingException.html)Checked exception thrown when a character encoding or decoding error occurs.[Charset](Charset.html)A named mapping between sequences of sixteen-bit Unicode [code units](../../lang/Character.html#unicode) and sequences of bytes.[CharsetDecoder](CharsetDecoder.html)An engine that can transform a sequence of bytes in a specific charset into a sequence of sixteen-bit Unicode characters.[CharsetEncoder](CharsetEncoder.html)An engine that can transform a sequence of sixteen-bit Unicode characters into a sequence of bytes in a specific charset.[CoderMalfunctionError](CoderMalfunctionError.html)Error thrown when the [decodeLoop](CharsetDecoder.html#decodeLoop(java.nio.ByteBuffer,java.nio.CharBuffer)) method of a [CharsetDecoder](CharsetDecoder.html), or the [encodeLoop](CharsetEncoder.html#encodeLoop(java.nio.CharBuffer,java.nio.ByteBuffer)) method of a [CharsetEncoder](CharsetEncoder.html), throws an unexpected exception.[CoderResult](CoderResult.html)A description of the result state of a coder.[CodingErrorAction](CodingErrorAction.html)A typesafe enumeration for coding-error actions.[IllegalCharsetNameException](IllegalCharsetNameException.html)Unchecked exception thrown when a string that is not a [legal charset name](Charset.html#names) is used as such.[MalformedInputException](MalformedInputException.html)Checked exception thrown when an input byte sequence is not legal for given charset, or an input character sequence is not a legal sixteen-bit Unicode sequence.[StandardCharsets](StandardCharsets.html)Constant definitions for the standard [charsets](Charset.html).[UnmappableCharacterException](UnmappableCharacterException.html)Checked exception thrown when an input character (or byte) sequence is valid but cannot be mapped to an output byte (or character) sequence.[UnsupportedCharsetException](UnsupportedCharsetException.html)Unchecked exception thrown when no support is available for a requested charset.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
