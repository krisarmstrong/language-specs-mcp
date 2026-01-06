# CSSUnitValue

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSUnitValue&level=not)

The `CSSUnitValue` interface of the [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Object_Model#css_typed_object_model) represents values that contain a single unit type. For example, "42px" would be represented by a `CSSNumericValue`.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[CSSUnitValue()](/en-US/docs/Web/API/CSSUnitValue/CSSUnitValue)

Creates a new `CSSUnitValue` object.

## [Instance properties](#instance_properties)

[CSSUnitValue.value](/en-US/docs/Web/API/CSSUnitValue/value)

Returns a double indicating the number of units.

[CSSUnitValue.unit](/en-US/docs/Web/API/CSSUnitValue/unit)

Returns a string indicating the type of unit.

## [Static methods](#static_methods)

The interface may also inherit methods from its parent interface, [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue).

## [Instance methods](#instance_methods)

The interface may also inherit methods from its parent interface, [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue).

## [Examples](#examples)

The following shows a method of creating a [CSSPositionValue](/en-US/docs/Web/API/CSSPositionValue) from individual `CSSUnitValue` constructors.

js

```
let pos = new CSSPositionValue(
  new CSSUnitValue(5, "px"),
  new CSSUnitValue(10, "px"),
);
```

## [Specifications](#specifications)

Specification
[CSS Typed OM Level 1# simple-numeric](https://drafts.css-houdini.org/css-typed-om/#simple-numeric)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 14, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/CSSUnitValue/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssunitvalue/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSUnitValue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssunitvalue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSUnitValue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssunitvalue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F23d4eb925c7394922e271e733421716e4055b095%0A*+Document+last+modified%3A+2024-05-14T17%3A40%3A37.000Z%0A%0A%3C%2Fdetails%3E)
