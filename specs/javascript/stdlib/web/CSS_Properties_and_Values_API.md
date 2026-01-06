# CSS Properties and Values API

The CSS Properties and Values API — part of the [CSS Houdini](/en-US/docs/Web/API/Houdini_APIs) umbrella of APIs — allows developers to explicitly define their [CSS custom properties](/en-US/docs/Web/CSS/Reference/Properties/--*), allowing for property type checking, default values, and properties that do or do not inherit their value.

## In this article

- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces](#interfaces)

[CSS.registerProperty](/en-US/docs/Web/API/CSS/registerProperty_static)

Defines how a browser should parse [CSS custom properties](/en-US/docs/Web/CSS/Reference/Properties/--*). Access this interface through [CSS.registerProperty](/en-US/docs/Web/API/CSS/registerProperty_static) in [JavaScript](/en-US/docs/Web/JavaScript).

[@property](/en-US/docs/Web/CSS/Reference/At-rules/@property)

Defines how a browser should parse [CSS custom properties](/en-US/docs/Web/CSS/Reference/Properties/--*). Access this interface through [@property](/en-US/docs/Web/CSS/Reference/At-rules/@property)[at-rule](/en-US/docs/Web/CSS/Guides/Syntax/At-rules) in [CSS](/en-US/docs/Web/CSS).

## [Examples](#examples)

The following will register a [custom property](/en-US/docs/Web/CSS/Reference/Properties/--*) named `--my-color` using [CSS.registerProperty](/en-US/docs/Web/API/CSS/registerProperty_static) in [JavaScript](/en-US/docs/Web/JavaScript). `--my-color` will use the CSS color syntax, it will have a default value of `#c0ffee`, and it will not inherit its value:

js

```
window.CSS.registerProperty({
  name: "--my-color",
  syntax: "<color>",
  inherits: false,
  initialValue: "#c0ffee",
});
```

The same registration can take place in [CSS](/en-US/docs/Web/CSS) using the [@property](/en-US/docs/Web/CSS/Reference/At-rules/@property)[at-rule](/en-US/docs/Web/CSS/Guides/Syntax/At-rules):

css

```
@property --my-color {
  syntax: "<color>";
  inherits: false;
  initial-value: #c0ffee;
}
```

## [Specifications](#specifications)

Specification
[CSS Properties and Values API Level 1# the-css-property-rule-interface](https://drafts.css-houdini.org/css-properties-values-api/#the-css-property-rule-interface)
[CSS Properties and Values API Level 1# the-registerproperty-function](https://drafts.css-houdini.org/css-properties-values-api/#the-registerproperty-function)

## [Browser compatibility](#browser_compatibility)

### [api.CSSPropertyRule](#api.CSSPropertyRule)

### [api.CSS.registerProperty_static](#api.CSS.registerProperty_static)

## [See also](#see_also)

- [Using the CSS properties and values API](/en-US/docs/Web/API/CSS_Properties_and_Values_API/guide)
- [CSS Painting API](/en-US/docs/Web/API/CSS_Painting_API)
- [CSS Typed Object Model](/en-US/docs/Web/API/CSS_Typed_OM_API)
- [Houdini APIs](/en-US/docs/Web/API/Houdini_APIs)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSS_Properties_and_Values_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/css_properties_and_values_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSS_Properties_and_Values_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcss_properties_and_values_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSS_Properties_and_Values_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcss_properties_and_values_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
