# CSSStyleSheet

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSStyleSheet&level=high)

The `CSSStyleSheet` interface represents a single [CSS](/en-US/docs/Web/CSS) stylesheet, and lets you inspect and modify the list of rules contained in the stylesheet. It inherits properties and methods from its parent, [StyleSheet](/en-US/docs/Web/API/StyleSheet).

A stylesheet consists of a collection of [CSSRule](/en-US/docs/Web/API/CSSRule) objects representing each of the rules in the stylesheet. The rules are contained in a [CSSRuleList](/en-US/docs/Web/API/CSSRuleList), which can be obtained from the stylesheet's [cssRules](/en-US/docs/Web/API/CSSStyleSheet/cssRules) property.

For example, one rule might be a [CSSStyleRule](/en-US/docs/Web/API/CSSStyleRule) object containing a style such as:

css

```
h1,
h2 {
  font-size: 16pt;
}
```

Another rule might be an at-rule such as [@import](/en-US/docs/Web/CSS/Reference/At-rules/@import) or [@media](/en-US/docs/Web/CSS/Reference/At-rules/@media), and so forth.

See the [Obtaining a StyleSheet](#obtaining_a_stylesheet) section for the various ways a `CSSStyleSheet` object can be obtained. A `CSSStyleSheet` object can also be directly constructed. The constructor, and the [CSSStyleSheet.replace()](/en-US/docs/Web/API/CSSStyleSheet/replace), and [CSSStyleSheet.replaceSync()](/en-US/docs/Web/API/CSSStyleSheet/replaceSync) methods are newer additions to the specification, enabling Constructable Stylesheets.

To apply a `CSSStyleSheet` to a document or shadow root, assign it to the [Document.adoptedStyleSheets](/en-US/docs/Web/API/Document/adoptedStyleSheets) or [ShadowRoot.adoptedStyleSheets](/en-US/docs/Web/API/ShadowRoot/adoptedStyleSheets) property, respectively.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Legacy properties](#legacy_properties)
- [Legacy methods](#legacy_methods)
- [Obtaining a StyleSheet](#obtaining_a_stylesheet)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[CSSStyleSheet()](/en-US/docs/Web/API/CSSStyleSheet/CSSStyleSheet)

Creates a new `CSSStyleSheet` object.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [StyleSheet](/en-US/docs/Web/API/StyleSheet).

[CSSStyleSheet.cssRules](/en-US/docs/Web/API/CSSStyleSheet/cssRules)Read only

Returns a live [CSSRuleList](/en-US/docs/Web/API/CSSRuleList) which maintains an up-to-date list of the [CSSRule](/en-US/docs/Web/API/CSSRule) objects that comprise the stylesheet.

Note: In some browsers, if a stylesheet is loaded from a different domain, accessing `cssRules` results in a `SecurityError`.

[CSSStyleSheet.ownerRule](/en-US/docs/Web/API/CSSStyleSheet/ownerRule)Read only

If this stylesheet is imported into the document using an [@import](/en-US/docs/Web/CSS/Reference/At-rules/@import) rule, the `ownerRule` property returns the corresponding [CSSImportRule](/en-US/docs/Web/API/CSSImportRule); otherwise, this property's value is `null`.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [StyleSheet](/en-US/docs/Web/API/StyleSheet).

[CSSStyleSheet.deleteRule()](/en-US/docs/Web/API/CSSStyleSheet/deleteRule)

Deletes the rule at the specified index into the stylesheet's rule list.

[CSSStyleSheet.insertRule()](/en-US/docs/Web/API/CSSStyleSheet/insertRule)

Inserts a new rule at the specified position in the stylesheet, given the textual representation of the rule.

[CSSStyleSheet.replace()](/en-US/docs/Web/API/CSSStyleSheet/replace)

Asynchronously replaces the content of the stylesheet and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with the updated `CSSStyleSheet`.

[CSSStyleSheet.replaceSync()](/en-US/docs/Web/API/CSSStyleSheet/replaceSync)

Synchronously replaces the content of the stylesheet.

## [Legacy properties](#legacy_properties)

These properties are legacy properties as introduced by Microsoft; these are maintained for compatibility with existing sites.

[rules](/en-US/docs/Web/API/CSSStyleSheet/rules)Read onlyDeprecated

The `rules` property is functionally identical to the standard [cssRules](/en-US/docs/Web/API/CSSStyleSheet/cssRules) property; it returns a live [CSSRuleList](/en-US/docs/Web/API/CSSRuleList) which maintains an up-to-date list of all of the rules in the style sheet.

## [Legacy methods](#legacy_methods)

These methods are legacy methods as introduced by Microsoft; these are maintained for compatibility with existing sites.

[addRule()](/en-US/docs/Web/API/CSSStyleSheet/addRule)Deprecated

Adds a new rule to the stylesheet given the selector to which the style applies and the style block to apply to the matching elements.

This differs from [insertRule()](/en-US/docs/Web/API/CSSStyleSheet/insertRule), which takes the textual representation of the entire rule as a single string.

[removeRule()](/en-US/docs/Web/API/CSSStyleSheet/removeRule)Deprecated

Functionally identical to [deleteRule()](/en-US/docs/Web/API/CSSStyleSheet/deleteRule); removes the rule at the specified index from the stylesheet's rule list.

## [Obtaining a StyleSheet](#obtaining_a_stylesheet)

A stylesheet is associated with at most one [Document](/en-US/docs/Web/API/Document), which it applies to (unless [disabled](/en-US/docs/Web/API/StyleSheet/disabled)). A list of `CSSStyleSheet` objects for a given document can be obtained using the [Document.styleSheets](/en-US/docs/Web/API/Document/styleSheets) property. A specific style sheet can also be accessed from its owner object (`Node` or `CSSImportRule`), if any.

A `CSSStyleSheet` object is created and inserted into the document's [Document.styleSheets](/en-US/docs/Web/API/Document/styleSheets) list automatically by the browser, when a stylesheet is loaded for a document.

A (possibly incomplete) list of ways a stylesheet can be associated with a document follows:

 Reason for the style sheet to be associated with the document  Appears in 
`document.styleSheets` list  Getting the owner element/rule given the style sheet object The interface for the owner objectGetting the CSSStyleSheet object from the owner[<style>](/en-US/docs/Web/HTML/Reference/Elements/style) and [<link>](/en-US/docs/Web/HTML/Reference/Elements/link) elements in the document Yes[.ownerNode](/en-US/docs/Web/API/StyleSheet/ownerNode)[HTMLLinkElement](/en-US/docs/Web/API/HTMLLinkElement),
[HTMLStyleElement](/en-US/docs/Web/API/HTMLStyleElement),
or [SVGStyleElement](/en-US/docs/Web/API/SVGStyleElement)[HTMLLinkElement.sheet](/en-US/docs/Web/API/HTMLLinkElement/sheet),
[HTMLStyleElement.sheet](/en-US/docs/Web/API/HTMLStyleElement/sheet),
or [SVGStyleElement.sheet](/en-US/docs/Web/API/SVGStyleElement/sheet) CSS [@import](/en-US/docs/Web/CSS/Reference/At-rules/@import) rule in other style sheets applied to the document Yes[.ownerRule](/en-US/docs/Web/API/CSSStyleSheet/ownerRule)[CSSImportRule](/en-US/docs/Web/API/CSSImportRule)[.styleSheet](/en-US/docs/Web/API/CSSImportRule/styleSheet)`<?xml-stylesheet ?>` processing instruction in the (non-HTML) document Yes[.ownerNode](/en-US/docs/Web/API/StyleSheet/ownerNode)[ProcessingInstruction](/en-US/docs/Web/API/ProcessingInstruction)[.sheet](/en-US/docs/Web/API/ProcessingInstruction/sheet) JavaScript [import ... with { type: "css" }](/en-US/docs/Web/JavaScript/Reference/Statements/import/with)NoN/AN/AN/AHTTP Link HeaderYesN/AN/AN/AUser agent (default) style sheetsNoN/AN/AN/A

## [Specifications](#specifications)

Specification
[CSS Object Model (CSSOM)# the-cssstylesheet-interface](https://drafts.csswg.org/cssom/#the-cssstylesheet-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CSS Object Model](/en-US/docs/Web/API/CSS_Object_Model)
- [Using dynamic styling information](/en-US/docs/Web/API/CSS_Object_Model/Using_dynamic_styling_information)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSStyleSheet/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssstylesheet/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSStyleSheet&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssstylesheet%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSStyleSheet%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssstylesheet%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdfc2f2fe483e5aaac785cc8d32064b925667aed2%0A*+Document+last+modified%3A+2025-12-19T01%3A30%3A26.000Z%0A%0A%3C%2Fdetails%3E)
