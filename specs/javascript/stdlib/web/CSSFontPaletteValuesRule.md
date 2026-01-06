# CSSFontPaletteValuesRule

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨November 2022⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSFontPaletteValuesRule&level=high)

The `CSSFontPaletteValuesRule` interface represents an [@font-palette-values](/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)[at-rule](/en-US/docs/Web/CSS/Guides/Syntax/At-rules).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its ancestor [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSFontPaletteValuesRule.name](/en-US/docs/Web/API/CSSFontPaletteValuesRule/name)Read only

A string with the name of the font palette.

[CSSFontPaletteValuesRule.fontFamily](/en-US/docs/Web/API/CSSFontPaletteValuesRule/fontFamily)Read only

A string indicating the font families on which the rule has to be applied.

[CSSFontPaletteValuesRule.basePalette](/en-US/docs/Web/API/CSSFontPaletteValuesRule/basePalette)Read only

A string indicating the base palette associated with the rule.

[CSSFontPaletteValuesRule.overrideColors](/en-US/docs/Web/API/CSSFontPaletteValuesRule/overrideColors)Read only

A string indicating the colors of the base palette that are overwritten and the new colors.

## [Instance methods](#instance_methods)

Inherits methods from its ancestor [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Examples](#examples)

### [Read associated font family using CSSOM](#read_associated_font_family_using_cssom)

This example first defines an [@import](/en-US/docs/Web/CSS/Reference/At-rules/@import) and an [@font-palette-values](/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values) at-rule. Then it reads the [@font-palette-values](/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values) rule and displays its name. The MDN [live sample](/en-US/docs/MDN/Writing_guidelines/Page_structures/Live_samples) infrastructure combines all the CSS blocks in the example into a single inline style with the id `css-output`, so we first use [document.getElementById()](/en-US/docs/Web/API/Document/getElementById) to find that sheet. The palette will be the second [CSSRule](/en-US/docs/Web/API/CSSRule) in that stylesheet. So, `rules[1]` returns a `CSSFontPaletteValuesRule` object, from which we can access `fontFamily`.

#### HTML

html

```
<pre id="log">The @font-palette-values at-rule font families:</pre>
```

#### CSS

css

```
@import "https://fonts.googleapis.com/css2?family=Bungee+Spice";

@font-palette-values --Alternate {
  font-family: "Bungee Spice";
  override-colors:
    0 #00ffbb,
    1 #007744;
}

.alternate {
  font-palette: --Alternate;
}
```

#### JavaScript

js

```
const log = document.getElementById("log");

const rules = document.getElementById("css-output").sheet.cssRules;
const fontPaletteValuesRule = rules[1]; // aA CSSFontPaletteValuesRule interface
log.textContent += ` ${fontPaletteValuesRule.fontFamily}`;
```

#### Result

## [Specifications](#specifications)

Specification
[CSS Fonts Module Level 4# om-fontpalettevalues](https://drafts.csswg.org/css-fonts/#om-fontpalettevalues)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [@font-palette-values](/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSFontPaletteValuesRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssfontpalettevaluesrule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSFontPaletteValuesRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssfontpalettevaluesrule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSFontPaletteValuesRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssfontpalettevaluesrule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
