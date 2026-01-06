# CSSMathSum

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSMathSum&level=not)

The `CSSMathSum` interface of the [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Object_Model) represents the result obtained by calling [add()](/en-US/docs/Web/API/CSSNumericValue/add), [sub()](/en-US/docs/Web/API/CSSNumericValue/sub), or [toSum()](/en-US/docs/Web/API/CSSNumericValue/toSum) on [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue).

A CSSMathSum is the object type returned when the [StylePropertyMapReadOnly.get()](/en-US/docs/Web/API/StylePropertyMapReadOnly/get) method is used on a CSS property whose value is created with a [calc()](/en-US/docs/Web/CSS/Reference/Values/calc) function.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[CSSMathSum()](/en-US/docs/Web/API/CSSMathSum/CSSMathSum)Experimental

Creates a new `CSSMathSum` object.

## [Instance properties](#instance_properties)

[CSSMathSum.values](/en-US/docs/Web/API/CSSMathSum/values)

Returns a [CSSNumericArray](/en-US/docs/Web/API/CSSNumericArray) object which contains one or more [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue) objects.

## [Static methods](#static_methods)

The interface may also inherit methods from its parent interface, [CSSMathValue](/en-US/docs/Web/API/CSSMathValue).

## [Instance methods](#instance_methods)

The interface may also inherit methods from its parent interface, [CSSMathValue](/en-US/docs/Web/API/CSSMathValue).

## [Examples](#examples)

We create an element with a [width](/en-US/docs/Web/CSS/Reference/Properties/width) determined using a [calc()](/en-US/docs/Web/CSS/Reference/Values/calc) function, then [console.log()](/en-US/docs/Web/API/console/log_static) the `operator` and `values`, and dig into the values a bit.

html

```
<div>has width</div>
```

We assign a `width`

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
console.log(styleMap.get("width").values); // CSSNumericArray {0: CSSUnitValue, 1: CSSUnitValue, length: 2}
console.log(styleMap.get("width").values[0]); // CSSUnitValue {value: 30, unit: "percent"}
console.log(styleMap.get("width").values[0].value); // 30
console.log(styleMap.get("width").values[0].unit); // 'percent'
console.log(styleMap.get("width").values[1]); // CSSUnitValue {value: -20, unit: "px"}
console.log(styleMap.get("width").values[1].value); //  -20
console.log(styleMap.get("width").values[1].unit); // 'px'
```

The specification is still evolving. In the future we may write the last three lines as:

js

```
console.log(styleMap.get("width").values[1]); // CSSMathNegate {value: CSSUnitValue, operator: "negate"}
console.log(styleMap.get("width").values[1].value); // CSSUnitValue {value: 20, unit: "px"}
console.log(styleMap.get("width").values[1].value.unit); // 'px'
```

## [Specifications](#specifications)

Specification
[CSS Typed OM Level 1# cssmathsum](https://drafts.css-houdini.org/css-typed-om/#cssmathsum)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSMathSum/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssmathsum/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSMathSum&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssmathsum%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSMathSum%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssmathsum%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0c13af55e869cbc54830fd1a601fd05f60717375%0A*+Document+last+modified%3A+2025-12-17T16%3A01%3A14.000Z%0A%0A%3C%2Fdetails%3E)
