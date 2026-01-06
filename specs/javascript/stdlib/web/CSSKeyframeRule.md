# CSSKeyframeRule

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨August 2016⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSKeyframeRule&level=high)

The `CSSKeyframeRule` interface describes an object representing a set of styles for a given keyframe. It corresponds to the contents of a single keyframe of a [@keyframes](/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)[at-rule](/en-US/docs/Web/CSS/Guides/Syntax/At-rules).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its ancestor [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSKeyframeRule.keyText](/en-US/docs/Web/API/CSSKeyframeRule/keyText)

Represents the key of the keyframe, like `'10%'`, `'75%'`. The `from` keyword maps to `'0%'` and the `to` keyword maps to `'100%'`.

[CSSKeyframeRule.style](/en-US/docs/Web/API/CSSKeyframeRule/style)Read only

Returns a [CSSStyleDeclaration](/en-US/docs/Web/API/CSSStyleDeclaration) of the CSS style associated with the keyframe.

## [Instance methods](#instance_methods)

No specific methods; inherits methods from its ancestor [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Examples](#examples)

The CSS includes a keyframes at-rule. This will be the first [CSSRule](/en-US/docs/Web/API/CSSRule) returned by `document.styleSheets[0].cssRules`. `myRules[0]` returns a [CSSKeyframesRule](/en-US/docs/Web/API/CSSKeyframesRule) object, which will contain individual `CSSKeyFrameRule` objects for each keyframe.

css

```
@keyframes slide-in {
  from {
    transform: translateX(0%);
  }

  to {
    transform: translateX(100%);
  }
}
```

js

```
let myRules = document.styleSheets[0].cssRules;
let keyframes = myRules[0]; // a CSSKeyframesRule
console.log(keyframes[0]); // a CSSKeyframeRule representing an individual keyframe.
```

## [Specifications](#specifications)

Specification
[CSS Animations Level 1# interface-csskeyframerule](https://drafts.csswg.org/css-animations/#interface-csskeyframerule)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [@keyframes](/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
- [CSSKeyFramesRule](/en-US/docs/Web/API/CSSKeyframesRule)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSKeyframeRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csskeyframerule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSKeyframeRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsskeyframerule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSKeyframeRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsskeyframerule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
