# CSSFunctionRule

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSFunctionRule&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `CSSFunctionRule` interface of the [CSS Object Model](/en-US/docs/Web/API/CSS_Object_Model) represents CSS [@function](/en-US/docs/Web/CSS/Reference/At-rules/@function) (custom function) [at-rules](/en-US/docs/Web/CSS/Guides/Syntax/At-rules).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule).

[CSSFunctionRule.name](/en-US/docs/Web/API/CSSFunctionRule/name)Read onlyExperimental

Returns a string representing the custom function's name.

[CSSFunctionRule.returnType](/en-US/docs/Web/API/CSSFunctionRule/returnType)Read onlyExperimental

Returns a string representing the custom function's return type.

## [Instance methods](#instance_methods)

This interface also inherits methods from [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule).

[CSSFunctionRule.getParameters()](/en-US/docs/Web/API/CSSFunctionRule/getParameters)Experimental

Returns an array of objects representing the custom function's parameters.

## [Examples](#examples)

### [Basic CSSFunctionRule usage](#basic_cssfunctionrule_usage)

In this example, we define a CSS custom function and then access it using the CSSOM.

#### CSS

Our CSS defines a custom function using the [@function](/en-US/docs/Web/CSS/Reference/At-rules/@function) at-rule. The function is called `--lighter()`, and outputs a lightened version of an input color. `--lighter()` accepts two parameters, a [<color>](/en-US/docs/Web/CSS/Reference/Properties/color) and a [<number>](/en-US/docs/Web/CSS/Reference/Values/number). It returns an [oklch()](/en-US/docs/Web/CSS/Reference/Values/color_value/oklch) color created using [relative color syntax](/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors); the input color is transformed into an `oklch()` color and its lightness channel is increased by the input number.

css

```
@function --lighter(--color <color>, --lightness-adjust <number>: 0.2) returns
  <color> {
  result: oklch(from var(--color) calc(l + var(--lightness-adjust)) c h);
}
```

#### JavaScript

Our script starts by getting a reference to the stylesheet attached to our document using [HTMLStyleElement.sheet](/en-US/docs/Web/API/HTMLStyleElement/sheet), then getting a reference to the only rule in the stylesheet, the `CSSFunctionRule` — via [CSSStylesheet.cssRules](/en-US/docs/Web/API/CSSStyleSheet/cssRules). We then log each of the `CSSFunctionRule` members to the console.

js

```
// Get a CSSFunctionRule
const cssFunc = document.getElementById("css-output").sheet.cssRules[0];

// Accessing CSSFunctionRule members
console.log(cssFunc.name);
console.log(cssFunc.returnType);
console.log(cssFunc.getParameters());
```

- The `name` property is equal to `--lighter`.
- The `returnType` property is equal to `<color>`.
- The `getParameters()` method returns an array that looks like so: js

```
[
  { name: "--color", type: "<color>" },
  { defaultValue: "0.2", name: "--lightness-adjust", type: "<number>" },
];
```

## [Specifications](#specifications)

Specification
[CSS Functions and Mixins Module# the-function-interface](https://drafts.csswg.org/css-mixins/#the-function-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [@function](/en-US/docs/Web/CSS/Reference/At-rules/@function)
- [CSSFunctionDescriptors](/en-US/docs/Web/API/CSSFunctionDescriptors)
- [CSSFunctionDeclarations](/en-US/docs/Web/API/CSSFunctionDeclarations)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSFunctionRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssfunctionrule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSFunctionRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssfunctionrule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSFunctionRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssfunctionrule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0c13af55e869cbc54830fd1a601fd05f60717375%0A*+Document+last+modified%3A+2025-12-17T16%3A01%3A14.000Z%0A%0A%3C%2Fdetails%3E)
