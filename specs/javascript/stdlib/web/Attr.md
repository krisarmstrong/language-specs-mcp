# Attr

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAttr&level=high)

The `Attr` interface represents one of an element's attributes as an object. In most situations, you will directly retrieve the attribute value as a string (e.g., [Element.getAttribute()](/en-US/docs/Web/API/Element/getAttribute)), but some cases may require interacting with `Attr` instances (e.g., [Element.getAttributeNode()](/en-US/docs/Web/API/Element/getAttributeNode)).

The core idea of an object of type `Attr` is the association between a name and a value. An attribute may also be part of a namespace and, in this case, it also has a URI identifying the namespace, and a prefix that is an abbreviation for the namespace.

The name is deemed local when it ignores the eventual namespace prefix and deemed qualified when it includes the prefix of the namespace, if any, separated from the local name by a colon (`:`). We have three cases: an attribute outside of a namespace, an attribute inside a namespace without a prefix defined, an attribute inside a namespace with a prefix:

AttributeNamespace nameNamespace prefixAttribute local nameAttribute qualified name`myAttr`nonenone`myAttr``myAttr``myAttr``mynamespace`none`myAttr``myAttr``myAttr``mynamespace``myns``myAttr``myns:myAttr`

Note: This interface represents only attributes present in the tree representation of the [Element](/en-US/docs/Web/API/Element), being a SVG, an HTML or a MathML element. It doesn't represent the property of an interface associated with such element, such as [HTMLTableElement](/en-US/docs/Web/API/HTMLTableElement) for a [<table>](/en-US/docs/Web/HTML/Reference/Elements/table) element. (See [this article](/en-US/docs/Glossary/Attribute) for more information about attributes and how they are reflected into properties.)

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits the properties of its parent interfaces, [Node](/en-US/docs/Web/API/Node) and [EventTarget](/en-US/docs/Web/API/EventTarget).

[localName](/en-US/docs/Web/API/Attr/localName)Read only

A string representing the local part of the qualified name of the attribute.

[name](/en-US/docs/Web/API/Attr/name)Read only

The attribute's qualified name. If the attribute is not in a namespace, it will be the same as [localName](/en-US/docs/Web/API/Attr/localName) property.

[namespaceURI](/en-US/docs/Web/API/Attr/namespaceURI)Read only

A string representing the URI of the namespace of the attribute, or `null` if there is no namespace.

[ownerElement](/en-US/docs/Web/API/Attr/ownerElement)Read only

The [Element](/en-US/docs/Web/API/Element) the attribute belongs to.

[prefix](/en-US/docs/Web/API/Attr/prefix)Read only

A string representing the namespace prefix of the attribute, or `null` if a namespace without prefix or no namespace are specified.

[specified](/en-US/docs/Web/API/Attr/specified)Read onlyDeprecated

This property always returns `true`.

[value](/en-US/docs/Web/API/Attr/value)

The attribute's value, a string that can be set and get using this property.

## [Instance methods](#instance_methods)

This interface has no specific methods, but inherits the methods of its parent interfaces, [Node](/en-US/docs/Web/API/Node) and [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Specifications](#specifications)

Specification
[DOM# interface-attr](https://dom.spec.whatwg.org/#interface-attr)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- Other nodes are [CDATASection](/en-US/docs/Web/API/CDATASection), [CharacterData](/en-US/docs/Web/API/CharacterData), [Comment](/en-US/docs/Web/API/Comment), [Document](/en-US/docs/Web/API/Document), [Element](/en-US/docs/Web/API/Element), [ProcessingInstruction](/en-US/docs/Web/API/ProcessingInstruction), and [Text](/en-US/docs/Web/API/Text).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Attr/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/attr/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAttr&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fattr%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAttr%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fattr%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fec1006afdf68a5808a48ab6301f9ccff3cd7ecc2%0A*+Document+last+modified%3A+2024-07-26T03%3A17%3A12.000Z%0A%0A%3C%2Fdetails%3E)
