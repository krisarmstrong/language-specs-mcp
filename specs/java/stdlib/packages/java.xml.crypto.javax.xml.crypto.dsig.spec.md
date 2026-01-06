Module[java.xml.crypto](../../../../../module-summary.html)

# Package javax.xml.crypto.dsig.spec

package javax.xml.crypto.dsig.specParameter classes for XML digital signatures. This package contains interfaces and classes representing input parameters for the digest, signature, transform, or canonicalization algorithms used in the processing of XML signatures. 

## Package Specification

- [XML-Signature Syntax and Processing: W3C Recommendation](http://www.w3.org/TR/xmldsig-core/)
- [RFC 3275: XML-Signature Syntax and Processing](http://www.ietf.org/rfc/rfc3275.txt)
- [Exclusive XML Canonicalization algorithm: W3C Recommendation](http://www.w3.org/TR/xml-exc-c14n/)
- [XPath Filter 2.0 Transform Algorithm: W3C Recommendation](http://www.w3.org/TR/xmldsig-filter2/)

Since:1.6

- Related PackagesPackageDescription[javax.xml.crypto.dsig](../package-summary.html)Classes for generating and validating XML digital signatures.[javax.xml.crypto.dsig.dom](../dom/package-summary.html)DOM-specific classes for the [javax.xml.crypto.dsig](../package-summary.html) package.[javax.xml.crypto.dsig.keyinfo](../keyinfo/package-summary.html)Classes for parsing and processing [KeyInfo](../keyinfo/KeyInfo.html) elements and structures.
- All Classes and InterfacesInterfacesClassesClassDescription[C14NMethodParameterSpec](C14NMethodParameterSpec.html)A specification of algorithm parameters for a [CanonicalizationMethod](../CanonicalizationMethod.html) Algorithm.[DigestMethodParameterSpec](DigestMethodParameterSpec.html)A specification of algorithm parameters for a [DigestMethod](../DigestMethod.html) algorithm.[ExcC14NParameterSpec](ExcC14NParameterSpec.html)Parameters for the W3C Recommendation: [Exclusive XML Canonicalization (C14N) algorithm](http://www.w3.org/TR/xml-exc-c14n/).[HMACParameterSpec](HMACParameterSpec.html)Parameters for the [XML Signature HMAC Algorithm](http://www.w3.org/TR/xmldsig-core/#sec-MACs).[RSAPSSParameterSpec](RSAPSSParameterSpec.html)Parameters for the [XML Signature RSASSA-PSS Algorithm](http://www.w3.org/2007/05/xmldsig-more#rsa-pss).[SignatureMethodParameterSpec](SignatureMethodParameterSpec.html)A specification of algorithm parameters for an XML [SignatureMethod](../SignatureMethod.html) algorithm.[TransformParameterSpec](TransformParameterSpec.html)A specification of algorithm parameters for a [Transform](../Transform.html) algorithm.[XPathFilter2ParameterSpec](XPathFilter2ParameterSpec.html)Parameters for the W3C Recommendation [XPath Filter 2.0 Transform Algorithm](http://www.w3.org/TR/xmldsig-filter2/).[XPathFilterParameterSpec](XPathFilterParameterSpec.html)Parameters for the [XPath Filtering Transform Algorithm](http://www.w3.org/TR/xmldsig-core/#sec-XPath).[XPathType](XPathType.html)The XML Schema Definition of the `XPath` element as defined in the [W3C Recommendation for XML-Signature XPath Filter 2.0](http://www.w3.org/TR/xmldsig-filter2):[XPathType.Filter](XPathType.Filter.html)Represents the filter set operation.[XSLTTransformParameterSpec](XSLTTransformParameterSpec.html)Parameters for the [XSLT Transform Algorithm](http://www.w3.org/TR/1999/REC-xslt-19991116).
