# CSSFunctionDeclarations

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSFunctionDeclarations&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `CSSFunctionDeclarations` interface of the [CSS Object Model](/en-US/docs/Web/API/CSS_Object_Model) represents a consecutive run of CSS declarations included within a [@function](/en-US/docs/Web/CSS/Reference/At-rules/@function) body.

This can include [CSS custom properties](/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties), and the value of the `results` descriptor inside the `@function` body, but it doesn't include blocks such as [@media](/en-US/docs/Web/CSS/Reference/At-rules/@media) at-rules that may be included. Such a block, included in the middle of a set of declarations, would cause the body contents to be broken up into separate `CSSFunctionDeclarations` objects, as seen in our [Multiple CSSFunctionDeclarations](#multiple_cssfunctiondeclarations) demo.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSFunctionDeclarations.style](/en-US/docs/Web/API/CSSFunctionDeclarations/style)Read onlyExperimental

Returns a [CSSFunctionDescriptors](/en-US/docs/Web/API/CSSFunctionDescriptors) object representing the descriptors available in a [@function](/en-US/docs/Web/CSS/Reference/At-rules/@function) body.

## [Examples](#examples)

### [Basic CSSFunctionDeclarations usage](#basic_cssfunctiondeclarations_usage)

In this example, we define a CSS custom function and then access its declarations using the CSSOM.

#### CSS

Our CSS defines a custom function using the [@function](/en-US/docs/Web/CSS/Reference/At-rules/@function) at-rule. The function is called `--lighter()`, and outputs a lightened version of an input color. `--lighter()` accepts two parameters, a [<color>](/en-US/docs/Web/CSS/Reference/Properties/color) and a [<number>](/en-US/docs/Web/CSS/Reference/Values/number). It returns an [oklch()](/en-US/docs/Web/CSS/Reference/Values/color_value/oklch) color created using [relative color syntax](/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors); the input color is transformed into an `oklch()` color and its lightness channel is increased by the input number.

css

```
@function --lighter(--color <color>, --lightness-adjust <number>: 0.2) returns
  <color> {
  --someVar: 100;
  result: oklch(from var(--color) calc(l + var(--lightness-adjust)) c h);
}
```

We've also included a local [custom property](/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties) inside the function, `--someVar`, which isn't used, but illustrates what happens when multiple declarations are available continuously inside the `@function` body.

#### JavaScript

Our script starts by getting a reference to the stylesheet attached to our document using [HTMLStyleElement.sheet](/en-US/docs/Web/API/HTMLStyleElement/sheet), then getting a reference to the only rule in the stylesheet, the `CSSFunctionRule` — via [CSSStylesheet.cssRules](/en-US/docs/Web/API/CSSStyleSheet/cssRules).

We then access the `CSSFunctionDeclarations` object representing the only continuous run of declarations inside the function using [cssRules[0]](/en-US/docs/Web/API/CSSGroupingRule/cssRules), access its descriptor's information using [CSSFunctionDeclarations.style](/en-US/docs/Web/API/CSSFunctionDeclarations/style), and then access the descriptor length and style information. All of this information is logged to the console.

js

```
// Get a CSSFunctionRule
const cssFunc = document.getElementById("css-output").sheet.cssRules[0];

// Accessing CSSFunctionDeclarations and CSSFunctionDescriptors
console.log(cssFunc.cssRules[0]); // CSSFunctionDeclarations
console.log(cssFunc.cssRules[0].style); // CSSFunctionDescriptors
console.log(cssFunc.cssRules[0].style.length);
console.log(cssFunc.cssRules[0].style.result);
```

Most notably:

- The `length` property is equal to `2`, as there are two parts to the descriptor's text (`--someVar: 100;` and `result: oklch(from var(--color) calc(l + var(--lightness-adjust)) c h);`).
- The `result` property is equal to the `@function` body's `result` descriptor, which is `oklch(from var(--color) calc(l + var(--lightness-adjust)) c h)`.

### [Multiple CSSFunctionDeclarations](#multiple_cssfunctiondeclarations)

In this example, we show how a `@media` at-rule inserted in the middle of a set of declarations causes two `CSSFunctionDeclarations` objects to be generated.

#### CSS

Our CSS shows a `@function` example taken from the specification, `--bar()`, which doesn't do much, but features a set of declarations separated by a `@media` block.

css

```
@function --bar() {
  --x: 42;
  result: var(--y);
  @media (width > 1000px) {
    /* ... */
  }
  --y: var(--x);
}
```

#### JavaScript

Our script starts by getting a reference to the stylesheet attached to our document via [HTMLStyleElement.sheet](/en-US/docs/Web/API/HTMLStyleElement/sheet), then getting a reference to the only rule in the stylesheet, the `CSSFunctionRule` — via [CSSStylesheet.cssRules](/en-US/docs/Web/API/CSSStyleSheet/cssRules).

We then access the [CSSGroupingRule.cssRules](/en-US/docs/Web/API/CSSGroupingRule/cssRules), logging its value to the console. This returns a [CSSRuleList](/en-US/docs/Web/API/CSSRuleList) object containing three objects:

- A `CSSFunctionDeclarations` object representing the `--x: 42;result: var(--y);` portion.
- A [CSSMediaRule](/en-US/docs/Web/API/CSSMediaRule) object representing the `@media` at-rule.
- A second `CSSFunctionDeclarations` object representing the `--y: var(--x);` portion.

js

```
// Get a CSSFunctionRule
const cssFunc = document.getElementById("css-output").sheet.cssRules[0];

// Accessing both CSSFunctionDeclarations
console.log(cssFunc.cssRules);
```

We then log a few details of each `CSSFunctionDeclarations` object to the console — the object itself, the [CSSFunctionDescriptors](/en-US/docs/Web/API/CSSFunctionDescriptors) object contained in its `style` property, and the [CSSFunctionDescriptors.result](/en-US/docs/Web/API/CSSFunctionDescriptors/result) property.

js

```
console.log(cssFunc.cssRules[0]); // First CSSFunctionDeclarations
console.log(cssFunc.cssRules[0].style); // CSSFunctionDescriptors
console.log(cssFunc.cssRules[0].style.result);

console.log(cssFunc.cssRules[2]); // Second CSSFunctionDeclarations
console.log(cssFunc.cssRules[2].style); // CSSFunctionDescriptors
console.log(cssFunc.cssRules[2].style.result);
```

In the second case, `result` returns an empty string, because the second declarations portion does not contain a `result` descriptor.

## [Specifications](#specifications)

Specification
[CSS Functions and Mixins Module# the-function-declarations-interface](https://drafts.csswg.org/css-mixins/#the-function-declarations-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [@function](/en-US/docs/Web/CSS/Reference/At-rules/@function)
- [CSSFunctionRule](/en-US/docs/Web/API/CSSFunctionRule)
- [CSSFunctionDescriptors](/en-US/docs/Web/API/CSSFunctionDescriptors)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSFunctionDeclarations/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssfunctiondeclarations/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSFunctionDeclarations&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssfunctiondeclarations%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSFunctionDeclarations%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssfunctiondeclarations%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0c13af55e869cbc54830fd1a601fd05f60717375%0A*+Document+last+modified%3A+2025-12-17T16%3A01%3A14.000Z%0A%0A%3C%2Fdetails%3E)
