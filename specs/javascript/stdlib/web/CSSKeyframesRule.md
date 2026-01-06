# CSSKeyframesRule

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨August 2016⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSKeyframesRule&level=high)

The `CSSKeyframesRule` interface describes an object representing a complete set of keyframes for a CSS animation. It corresponds to the contents of a whole [@keyframes](/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)[at-rule](/en-US/docs/Web/CSS/Guides/Syntax/At-rules).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its ancestor [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSKeyframesRule.name](/en-US/docs/Web/API/CSSKeyframesRule/name)

Represents the name of the keyframes, used by the [animation-name](/en-US/docs/Web/CSS/Reference/Properties/animation-name) property.

[CSSKeyframesRule.cssRules](/en-US/docs/Web/API/CSSKeyframesRule/cssRules)Read only

Returns a [CSSRuleList](/en-US/docs/Web/API/CSSRuleList) of the keyframes in the list.

[CSSKeyframesRule.length](/en-US/docs/Web/API/CSSKeyframesRule/length)Read only

Returns the number of keyframes in the list.

## [Instance methods](#instance_methods)

Inherits methods from its ancestor [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSKeyframesRule.appendRule()](/en-US/docs/Web/API/CSSKeyframesRule/appendRule)

Inserts a new keyframe rule into the current CSSKeyframesRule. The parameter is a string containing a keyframe in the same format as an entry of a [@keyframes](/en-US/docs/Web/CSS/Reference/At-rules/@keyframes) at-rule. If it contains more than one keyframe rule, a [DOMException](/en-US/docs/Web/API/DOMException) with a `SYNTAX_ERR` is thrown.

[CSSKeyframesRule.deleteRule()](/en-US/docs/Web/API/CSSKeyframesRule/deleteRule)

Deletes a keyframe rule from the current CSSKeyframesRule. The parameter is the index of the keyframe to be deleted, expressed as a string resolving as a number between `0%` and `100%`.

[CSSKeyframesRule.findRule()](/en-US/docs/Web/API/CSSKeyframesRule/findRule)

Returns a keyframe rule corresponding to the given key. The key is a string containing an index of the keyframe to be returned, resolving to a percentage between `0%` and `100%`. If no such keyframe exists, `findRule` returns `null`.

## [Example](#example)

### [Using CSSKeyframesRule](#using_csskeyframesrule)

The CSS includes a keyframes at-rule. This will be the first [CSSRule](/en-US/docs/Web/API/CSSRule) returned by `document.styleSheets[0].cssRules`. `myRules[0]` returns a `CSSKeyframesRule` object.

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
const myRules = document.styleSheets[0].cssRules;
const keyframes = myRules[0]; // a CSSKeyframesRule
```

### [Accessing indexes](#accessing_indexes)

`CSSKeyframesRule` can be indexed like an array, and functions similar to its [cssRules](/en-US/docs/Web/API/CSSKeyframesRule/cssRules) property.

js

```
const keyframes = document.styleSheets[0].cssRules[0];

for (let i = 0; i < keyframes.length; i++) {
  console.log(keyframes[i].keyText);
}

// Output:
// 0%
// 100%
```

## [Specifications](#specifications)

Specification
[CSS Animations Level 1# interface-csskeyframesrule](https://drafts.csswg.org/css-animations/#interface-csskeyframesrule)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [@keyframes](/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
- [CSSKeyFrameRule](/en-US/docs/Web/API/CSSKeyframeRule)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSKeyframesRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csskeyframesrule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSKeyframesRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsskeyframesrule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSKeyframesRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsskeyframesrule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
