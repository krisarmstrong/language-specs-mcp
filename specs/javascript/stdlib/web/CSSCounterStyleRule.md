# CSSCounterStyleRule

 Baseline  2023 Newly available

 Since ⁨September 2023⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSCounterStyleRule&level=low)

The `CSSCounterStyleRule` interface represents an [@counter-style](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)[at-rule](/en-US/docs/Web/CSS/Guides/Syntax/At-rules).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent [CSSRule](/en-US/docs/Web/API/CSSRule).

[CSSCounterStyleRule.name](/en-US/docs/Web/API/CSSCounterStyleRule/name)

A string that contains the serialization of the [<custom-ident>](/en-US/docs/Web/CSS/Reference/Values/custom-ident) defined as the `name` for the associated rule.

[CSSCounterStyleRule.system](/en-US/docs/Web/API/CSSCounterStyleRule/system)

A string that contains the serialization of the [system](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system) descriptor defined for the associated rule. If the descriptor was not specified in the associated rule, the attribute returns an empty string.

[CSSCounterStyleRule.symbols](/en-US/docs/Web/API/CSSCounterStyleRule/symbols)

A string that contains the serialization of the [symbols](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/symbols) descriptor defined for the associated rule. If the descriptor was not specified in the associated rule, the attribute returns an empty string.

[CSSCounterStyleRule.additiveSymbols](/en-US/docs/Web/API/CSSCounterStyleRule/additiveSymbols)

A string that contains the serialization of the [additive-symbols](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/additive-symbols) descriptor defined for the associated rule. If the descriptor was not specified in the associated rule, the attribute returns an empty string.

[CSSCounterStyleRule.negative](/en-US/docs/Web/API/CSSCounterStyleRule/negative)

A string that contains the serialization of the [negative](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/negative) descriptor defined for the associated rule. If the descriptor was not specified in the associated rule, the attribute returns an empty string.

[CSSCounterStyleRule.prefix](/en-US/docs/Web/API/CSSCounterStyleRule/prefix)

A string that contains the serialization of the [prefix](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/prefix) descriptor defined for the associated rule. If the descriptor was not specified in the associated rule, the attribute returns an empty string.

[CSSCounterStyleRule.suffix](/en-US/docs/Web/API/CSSCounterStyleRule/suffix)

A string that contains the serialization of the [suffix](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/suffix) descriptor defined for the associated rule. If the descriptor was not specified in the associated rule, the attribute returns an empty string.

[CSSCounterStyleRule.range](/en-US/docs/Web/API/CSSCounterStyleRule/range)

A string that contains the serialization of the [range](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range) descriptor defined for the associated rule. If the descriptor was not specified in the associated rule, the attribute returns an empty string.

[CSSCounterStyleRule.pad](/en-US/docs/Web/API/CSSCounterStyleRule/pad)

A string that contains the serialization of the [pad](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad) descriptor defined for the associated rule. If the descriptor was not specified in the associated rule, the attribute returns an empty string.

[CSSCounterStyleRule.speakAs](/en-US/docs/Web/API/CSSCounterStyleRule/speakAs)

A string that contains the serialization of the [speak-as](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as) descriptor defined for the associated rule. If the descriptor was not specified in the associated rule, the attribute returns an empty string.

[CSSCounterStyleRule.fallback](/en-US/docs/Web/API/CSSCounterStyleRule/fallback)

A string that contains the serialization of the [fallback](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/fallback) descriptor defined for the associated rule. If the descriptor was not specified in the associated rule, the attribute returns an empty string.

## [Instance methods](#instance_methods)

This interface doesn't implement any specific method but inherits methods from its parent [CSSRule](/en-US/docs/Web/API/CSSRule).

## [Specifications](#specifications)

Specification
[CSS Counter Styles Level 3# the-csscounterstylerule-interface](https://drafts.csswg.org/css-counter-styles/#the-csscounterstylerule-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [@counter-style](/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
- [CSS counter styles](/en-US/docs/Web/CSS/Guides/Counter_styles) module
- [Using CSS counters](/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters) guide

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSCounterStyleRule/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csscounterstylerule/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSCounterStyleRule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsscounterstylerule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSCounterStyleRule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsscounterstylerule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
