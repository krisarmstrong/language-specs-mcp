# CSSNestedDeclarations

 Baseline  2024 Newly available

 Since ⁨December 2024⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSNestedDeclarations&level=low)

The `CSSNestedDeclarations` interface of the [CSS Rule API](/en-US/docs/Web/API/CSSRule) is used to group nested [CSSRule](/en-US/docs/Web/API/CSSRule)s.

The interface allows the [CSS Object Model (CSSOM](/en-US/docs/Web/API/CSS_Object_Model) to mirror the structure of CSS documents with nested CSS rules, and ensure that rules are parsed and evaluated in the order that they are declared.

Note: Implementations that do not support this interface may parse nested rules in the wrong order. See [Browser compatibility](#browser_compatibility) for more information.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See Also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its ancestor [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSNestedDeclarations.style](/en-US/docs/Web/API/CSSNestedDeclarations/style)Read only

Returns the values of the nested rules.

## [Instance methods](#instance_methods)

No specific methods; inherits methods from its ancestor [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Examples](#examples)

### [CSS](#css)

The CSS below includes a selector `.foo` that contains two declarations and a media query.

css

```
.foo {
  background-color: silver;
  @media screen {
    color: tomato;
  }
  color: black;
}
```

This is represented by a number of JavaScript objects in the [CSS Object Model](/en-US/docs/Web/API/CSS_Object_Model):

- A [CSSStyleRule](/en-US/docs/Web/API/CSSStyleRule) object that represents the `background-color: silver` rule. This can be returned via `document.styleSheets[0].cssRules[0]`.
- A [CSSMediaRule](/en-US/docs/Web/API/CSSMediaRule) object that represents the `@media screen` rule, and which can be returned via `document.styleSheets[0].cssRules[0].cssRules[0]`. 

  - The `CSSMediaRule` object contains a `CSSNestedDeclaration` object which represents the `color: tomato` rule nested by the `@media screen` rule. This can be returned via `document.styleSheets[0].cssRules[0].cssRules[0].cssRules[0]`.

- The final rule is a `CSSNestedDeclaration` object that represents the `color: black` rule in the stylesheet, and which can be returned via `document.styleSheets[0].cssRules[0].cssRules[1]`.

Note: All top-level styles after the first `CSSNestedDeclaration` must also be represented as `CSSNestedDeclaration` objects in order to follow the [CSS nested declarations rule](/en-US/docs/Web/CSS/Guides/Nesting/Using#nested_declarations_rule)

### [CSSOM (CSS Object Model)](#cssom_css_object_model)

```
↳ CSSStyleRule
  .style
    - background-color: silver
  ↳ CSSMediaRule
    ↳ CSSNestedDeclarations
      .style (CSSStyleDeclaration, 1) =
      - color: tomato
  ↳ CSSNestedDeclarations
    .style (CSSStyleDeclaration, 1) =
      - color: black
```

## [Specifications](#specifications)

Specification
[CSS Nesting Module# cssnesteddeclarations](https://drafts.csswg.org/css-nesting-1/#cssnesteddeclarations)

## [Browser compatibility](#browser_compatibility)

## [See Also](#see_also)

- [CSSNestedDeclarations.style](/en-US/docs/Web/API/CSSNestedDeclarations/style)
- [The Nested Declarations Rule](/en-US/docs/Web/CSS/Guides/Nesting/Using#nested_declarations_rule)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSNestedDeclarations/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssnesteddeclarations/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSNestedDeclarations&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssnesteddeclarations%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSNestedDeclarations%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssnesteddeclarations%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
