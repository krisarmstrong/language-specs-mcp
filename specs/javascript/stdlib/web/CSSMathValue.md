# CSSMathValue

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSMathValue&level=not)

The `CSSMathValue` interface of the [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Object_Model) a base class for classes representing complex numeric values.

## In this article

- [Interfaces based on CSSMathValue](#interfaces_based_on_cssmathvalue)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Interfaces based on CSSMathValue](#interfaces_based_on_cssmathvalue)

Below is a list of interfaces based on the CSSMathValue interface.

- [CSSMathInvert](/en-US/docs/Web/API/CSSMathInvert)
- [CSSMathMax](/en-US/docs/Web/API/CSSMathMax)
- [CSSMathMin](/en-US/docs/Web/API/CSSMathMin)
- [CSSMathNegate](/en-US/docs/Web/API/CSSMathNegate)
- [CSSMathProduct](/en-US/docs/Web/API/CSSMathProduct)
- [CSSMathSum](/en-US/docs/Web/API/CSSMathSum)

## [Instance properties](#instance_properties)

[CSSMathValue.operator](/en-US/docs/Web/API/CSSMathValue/operator)

Indicates the operator that the current subtype represents.

## [Static methods](#static_methods)

The interface may also inherit methods from its parent interface, [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue).

## [Instance methods](#instance_methods)

The interface may also inherit methods from its parent interface, [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue).

## [Examples](#examples)

We create an element with a [width](/en-US/docs/Web/CSS/Reference/Properties/width) determined using a [calc()](/en-US/docs/Web/CSS/Reference/Values/calc) function, then [console.log()](/en-US/docs/Web/API/console/log_static) the `operator`.

html

```
<div>has width</div>
```

We assign a `width` with a calculation

css

```
div {
  width: calc(30% - 20px);
}
```

We add the JavaScript

js

```
const styleMap = document.querySelector("div").computedStyleMap();

console.log(styleMap.get("width")); // CSSMathSum {values: CSSNumericArray, operator: "sum"}
console.log(styleMap.get("width").operator); // 'sum'
console.log(styleMap.get("width").values[1].value); // -20
```

The `CSSMathValue.operator` returns `"sum"` because `styleMap.get("width").values[1].value );` is `-20`: adding a negative number.

## [Specifications](#specifications)

Specification
[CSS Typed OM Level 1# complex-numeric](https://drafts.css-houdini.org/css-typed-om/#complex-numeric)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSMathValue/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssmathvalue/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSMathValue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssmathvalue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSMathValue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssmathvalue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0c13af55e869cbc54830fd1a601fd05f60717375%0A*+Document+last+modified%3A+2025-12-17T16%3A01%3A14.000Z%0A%0A%3C%2Fdetails%3E)
