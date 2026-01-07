javax.xml.crypto.dsig.keyinfo (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

- [Overview](../../../../../../index.html)
- [Module](../../../../../module-summary.html)
- Package
- Class
- [Use](package-use.html)
- [Tree](package-tree.html)
- [Preview](../../../../../../preview-list.html)
- [New](../../../../../../new-list.html)
- [Deprecated](../../../../../../deprecated-list.html)
- [Index](../../../../../../index-files/index-1.html)
- [Help](../../../../../../help-doc.html#package)

- 

Package:

  - [Description](#package-description)
  - [Related Packages](#related-package-summary)
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- [Related Packages](#related-package-summary) | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../../../../search.html)Module[java.xml.crypto](../../../../../module-summary.html)

# Package javax.xml.crypto.dsig.keyinfo

package javax.xml.crypto.dsig.keyinfoClasses for parsing and processing [KeyInfo](KeyInfo.html) elements and structures. `KeyInfo` is an optional element that enables the recipient(s) to obtain the key needed to validate an [XMLSignature](../XMLSignature.html). `KeyInfo` may contain keys, names, certificates and other public key management information, such as in-band key distribution or key agreement data. This package contains classes representing types defined in the W3C specification for XML Signatures, such as [KeyName](KeyName.html), [KeyValue](KeyValue.html), [RetrievalMethod](RetrievalMethod.html), [X509Data](X509Data.html), [X509IssuerSerial](X509IssuerSerial.html), and [PGPData](PGPData.html). [KeyInfoFactory](KeyInfoFactory.html) is an abstract factory that creates `KeyInfo` objects from scratch. 

## Package Specification

- [XML-Signature Syntax and Processing: W3C Recommendation](http://www.w3.org/TR/xmldsig-core/)
- [RFC 3275: XML-Signature Syntax and Processing](http://www.ietf.org/rfc/rfc3275.txt)

Since:1.6

- Related PackagesPackageDescription[javax.xml.crypto.dsig](../package-summary.html)Classes for generating and validating XML digital signatures.[javax.xml.crypto.dsig.dom](../dom/package-summary.html)DOM-specific classes for the [javax.xml.crypto.dsig](../package-summary.html) package.[javax.xml.crypto.dsig.spec](../spec/package-summary.html)Parameter classes for XML digital signatures.
- All Classes and InterfacesInterfacesClassesClassDescription[KeyInfo](KeyInfo.html)A representation of the XML `KeyInfo` element as defined in the [W3C Recommendation for XML-Signature Syntax and Processing](http://www.w3.org/TR/xmldsig-core/).[KeyInfoFactory](KeyInfoFactory.html)A factory for creating [KeyInfo](KeyInfo.html) objects from scratch or for unmarshalling a `KeyInfo` object from a corresponding XML representation.[KeyName](KeyName.html)A representation of the XML `KeyName` element as defined in the [W3C Recommendation for XML-Signature Syntax and Processing](http://www.w3.org/TR/xmldsig-core/).[KeyValue](KeyValue.html)A representation of the XML `KeyValue` element as defined in the [W3C Recommendation for XML-Signature Syntax and Processing](http://www.w3.org/TR/xmldsig-core/).[PGPData](PGPData.html)A representation of the XML `PGPData` element as defined in the [W3C Recommendation for XML-Signature Syntax and Processing](http://www.w3.org/TR/xmldsig-core/).[RetrievalMethod](RetrievalMethod.html)A representation of the XML `RetrievalMethod` element as defined in the [W3C Recommendation for XML-Signature Syntax and Processing](http://www.w3.org/TR/xmldsig-core/).[X509Data](X509Data.html)A representation of the XML `X509Data` element as defined in the [W3C Recommendation for XML-Signature Syntax and Processing](http://www.w3.org/TR/xmldsig-core/).[X509IssuerSerial](X509IssuerSerial.html)A representation of the XML `X509IssuerSerial` element as defined in the [W3C Recommendation for XML-Signature Syntax and Processing](http://www.w3.org/TR/xmldsig-core/).

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
