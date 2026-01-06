# CSSScopeRule

 Baseline  2025 Newly available

 Since ⁨December 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSScopeRule&level=low)

The `CSSScopeRule` interface of the [CSS Object Model](/en-US/docs/Web/API/CSS_Object_Model) represents a CSS [@scope](/en-US/docs/Web/CSS/Reference/At-rules/@scope) at-rule.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its ancestors [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule) and [CSSRule](/en-US/docs/Web/API/CSSRule).

[end](/en-US/docs/Web/API/CSSScopeRule/end)

Returns a string containing the value of the `@scope` at-rule's scope limit.

[start](/en-US/docs/Web/API/CSSScopeRule/start)

Returns a string containing the value of the `@scope` at-rule's scope root.

## [Instance methods](#instance_methods)

Inherits methods from its ancestors [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule) and [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Examples](#examples)

### [Accessing @scope information in JavaScript](#accessing_scope_information_in_javascript)

Assuming the following is the only stylesheet attached to a document:

css

```
@scope (.outer) to (.inner) {
  :scope {
    background: yellow;
  }
}
```

The following JavaScript could be used to access information about the contained `@scope` block:

js

```
const scopeBlock = document.styleSheets[0].cssRules[0];

console.log(scopeBlock.start); // Returns ".outer"
console.log(scopeBlock.end); // Returns ".inner"
```

## [Specifications](#specifications)

Specification
[CSS Cascading and Inheritance Level 6# cssscoperule](https://drafts.csswg.org/css-cascade-6/#cssscoperule)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [@scope](/en-US/docs/Web/CSS/Reference/At-rules/@scope)
- [:scope](/en-US/docs/Web/CSS/Reference/Selectors/:scope)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 11, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/CSSScopeRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssscoperule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSScopeRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssscoperule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSScopeRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssscoperule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Faa1c6876fb3cea003dda92f02c9bac93fd3370b2%0A*+Document+last+modified%3A+2024-07-11T23%3A51%3A23.000Z%0A%0A%3C%2Fdetails%3E)
