# CSSMediaRule

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSMediaRule&level=high)

The `CSSMediaRule` interface represents a single CSS [@media](/en-US/docs/Web/CSS/Reference/At-rules/@media) rule.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

Inherits properties from its ancestors [CSSConditionRule](/en-US/docs/Web/API/CSSConditionRule), [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule), and [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSMediaRule.media](/en-US/docs/Web/API/CSSMediaRule/media)Read only

Returns a [MediaList](/en-US/docs/Web/API/MediaList) representing the intended destination medium for style information.

## [Instance methods](#instance_methods)

No specific methods; inherits methods from its ancestors [CSSConditionRule](/en-US/docs/Web/API/CSSConditionRule), [CSSGroupingRule](/en-US/docs/Web/API/CSSGroupingRule), and [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Examples](#examples)

The CSS below includes a media query with one style rule. The MDN [live sample](/en-US/docs/MDN/Writing_guidelines/Page_structures/Live_samples) infrastructure combines all the CSS blocks in the example into a single inline style with the id `css-output`, so we first use [document.getElementById()](/en-US/docs/Web/API/Document/getElementById) to find that sheet. `myRules[0]` returns a `CSSMediaRule` object, from which we can get the `mediaText`.

html

```
<p id="log"></p>
```

css

```
@media (width >= 500px) {
  body {
    color: blue;
  }
}
```

js

```
const log = document.getElementById("log");
const myRules = document.getElementById("css-output").sheet.cssRules;
const mediaList = myRules[0]; // a CSSMediaRule representing the media query.
log.textContent += ` ${mediaList.media.mediaText}`;
```

## [Specifications](#specifications)

Specification
[CSS Conditional Rules Module Level 3# the-cssmediarule-interface](https://drafts.csswg.org/css-conditional-3/#the-cssmediarule-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSMediaRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssmediarule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSMediaRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssmediarule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSMediaRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssmediarule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F56bbf59f4ea2566d64ad2e5c669a7a597626b7f3%0A*+Document+last+modified%3A+2025-10-17T17%3A02%3A52.000Z%0A%0A%3C%2Fdetails%3E)
