# CSSViewTransitionRule

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSViewTransitionRule&level=not)

The `CSSViewTransitionRule` interface represents a CSS [@view-transition](/en-US/docs/Web/CSS/Reference/At-rules/@view-transition)[at-rule](/en-US/docs/Web/CSS/Guides/Syntax/At-rules).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its ancestor, [CSSRule](/en-US/docs/Web/API/CSSRule).

[navigation](/en-US/docs/Web/API/CSSViewTransitionRule/navigation)Read only

Returns the `@view-transition` at-rule's `navigation` descriptor value.

[types](/en-US/docs/Web/API/CSSViewTransitionRule/types)Read only

Returns an array containing the `@view-transition` at-rule's `types` descriptor values.

## [Instance methods](#instance_methods)

Inherits methods from its ancestor, [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Examples](#examples)

### [Basic usage](#basic_usage)

A stylesheet includes a [@view-transition](/en-US/docs/Web/CSS/Reference/At-rules/@view-transition)[at-rule](/en-US/docs/Web/CSS/Guides/Syntax/At-rules), with `navigation` and `types` descriptors set:

css

```
@view-transition {
  navigation: auto;
  types: slide, rotate;
}
```

In script, we grab a reference to the `@view-transition` at-rule using `document.styleSheets[0].cssRules`, then log the corresponding `CSSViewTransitionRule` object and its `navigation` and `types` properties to the console. The `types` property returns an array containing the values set for the `types` descriptor.

js

```
let myRule = document.styleSheets[0].cssRules;
console.log(myRule[0]); // a CSSViewTransitionRule representing the @view-transition at-rule
console.log(myRule[0].navigation); // "auto"
console.log(myRule[0].types); // ["slide", "rotate"]
```

## [Specifications](#specifications)

Specification
[CSS View Transitions Module Level 2# cssviewtransitionrule](https://drafts.csswg.org/css-view-transitions-2/#cssviewtransitionrule)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [@view-transition](/en-US/docs/Web/CSS/Reference/At-rules/@view-transition)
- [View Transition API](/en-US/docs/Web/API/View_Transition_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 9, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSViewTransitionRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssviewtransitionrule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSViewTransitionRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssviewtransitionrule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSViewTransitionRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssviewtransitionrule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbaf0cb6bfe8bf2418122300d3f93e3aa94f72dca%0A*+Document+last+modified%3A+2025-12-09T12%3A19%3A47.000Z%0A%0A%3C%2Fdetails%3E)
