# CSSFontFeatureValuesRule

 Baseline  2025  * Newly available

 Since ⁨March 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSFontFeatureValuesRule&level=low)

The `CSSFontFeatureValuesRule` interface represents an [@font-feature-values](/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values)[at-rule](/en-US/docs/Web/CSS/Guides/Syntax/At-rules), letting developers assign for each font face a common name to specify features indices to be used in [font-variant-alternates](/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its ancestor [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSFontFeatureValuesRule.fontFamily](/en-US/docs/Web/API/CSSFontFeatureValuesRule/fontFamily)

A string that identifies the font family this rule applies to.

## [Instance methods](#instance_methods)

Inherits methods from its ancestor [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Examples](#examples)

### [Read font family](#read_font_family)

In this example, we declare two [@font-feature-values](/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values) one for the Font One font family, and the other for Font Two. We then use the CSSOM to read these font families, displaying them into the log.

#### HTML

html

```
<pre id="log"></pre>
```

#### CSS

css

```
/* At-rule for "nice-style" in Font One */
@font-feature-values Font One {
  @styleset {
    nice-style: 12;
  }
}

/* At-rule for "nice-style" in Font Two */
@font-feature-values Font Two {
  @styleset {
    nice-style: 4;
  }
}

/* Apply the at-rules with a single declaration */
.nice-look {
  font-variant-alternates: styleset(nice-style);
}
```

#### JavaScript

js

```
const log = document.getElementById("log");
const rules = document.getElementById("css-output").sheet.cssRules;

const fontOne = rules[0]; // A CSSFontFeatureValuesRule
log.textContent = `The 1st '@font-feature-values' family: "${fontOne.fontFamily}".\n`;

const fontTwo = rules[1]; // Another CSSFontFeatureValuesRule
log.textContent += `The 2nd '@font-feature-values' family: "${fontTwo.fontFamily}".`;
```

## [Specifications](#specifications)

Specification
[CSS Fonts Module Level 4# cssfontfeaturevaluesrule](https://drafts.csswg.org/css-fonts/#cssfontfeaturevaluesrule)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [@font-feature-values](/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSFontFeatureValuesRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssfontfeaturevaluesrule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSFontFeatureValuesRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssfontfeaturevaluesrule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSFontFeatureValuesRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssfontfeaturevaluesrule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
