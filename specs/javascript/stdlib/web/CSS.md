# CSS

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSS&level=high)

The `CSS` interface holds useful CSS-related methods. No objects with this interface are implemented: it contains only static methods and is therefore a utilitarian interface.

## In this article

- [Static properties](#static_properties)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Static properties](#static_properties)

[CSS.highlights](/en-US/docs/Web/API/CSS/highlights_static)

Provides access to the `HighlightRegistry` used to style arbitrary text ranges using the [CSS Custom Highlight API](/en-US/docs/Web/API/CSS_Custom_Highlight_API).

[CSS.paintWorklet](/en-US/docs/Web/API/CSS/paintWorklet_static)ExperimentalSecure context

Provides access to the Worklet responsible for all the classes related to painting.

## [Instance properties](#instance_properties)

The CSS interface is a utility interface and no object of this type can be created: only static properties are defined on it.

## [Static methods](#static_methods)

No inherited static methods.

[CSS.registerProperty()](/en-US/docs/Web/API/CSS/registerProperty_static)

Registers [custom properties](/en-US/docs/Web/CSS/Reference/Properties/--*), allowing for property type checking, default values, and properties that do or do not inherit their value.

[CSS.supports()](/en-US/docs/Web/API/CSS/supports_static)

Returns a boolean value indicating if the pair property-value, or the condition, given in parameter is supported.

[CSS.escape()](/en-US/docs/Web/API/CSS/escape_static)

Can be used to escape a string mostly for use as part of a CSS selector.

[CSS factory functions](/en-US/docs/Web/API/CSS/factory_functions_static)

Can be used to return a new [CSSUnitValue](/en-US/docs/Web/API/CSSUnitValue) with a value of the parameter number of the units of the name of the factory function method used.

js

```
CSS.em(3); // CSSUnitValue {value: 3, unit: "em"}
```

## [Instance methods](#instance_methods)

The CSS interface is a utility interface and no object of this type can be created: only static methods are defined on it.

## [Specifications](#specifications)

Specification
[CSS Object Model (CSSOM)# namespacedef-css](https://drafts.csswg.org/cssom/#namespacedef-css)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 31, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSS/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/css/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSS&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcss%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSS%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcss%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F55326f330a6ae829494c7606b1bd47b2c0f9d888%0A*+Document+last+modified%3A+2025-10-31T00%3A41%3A06.000Z%0A%0A%3C%2Fdetails%3E)
