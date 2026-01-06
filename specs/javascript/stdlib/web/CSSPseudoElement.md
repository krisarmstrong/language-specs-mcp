# CSSPseudoElement

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPseudoElement&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `CSSPseudoElement` interface represents a pseudo-element that may be the target of an event or animated using the [Web Animations API](/en-US/docs/Web/API/Web_Animations_API). Instances of this interface may be obtained by calling `Element.pseudo()`.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[CSSPseudoElement.element](/en-US/docs/Web/API/CSSPseudoElement/element)ExperimentalRead only

Returns the originating/parent [Element](/en-US/docs/Web/API/Element) of the pseudo-element.

[CSSPseudoElement.type](/en-US/docs/Web/API/CSSPseudoElement/type)ExperimentalRead only

Returns the pseudo-element selector as a string.

## [Instance methods](#instance_methods)

`CSSPseudoElement` extends [EventTarget](/en-US/docs/Web/API/EventTarget), so it inherits the following methods:

## [Examples](#examples)

### [Basic example using Element.pseudo](#basic_example_using_element.pseudo)

Using pseudo-elements, most modern browsers will automatically add quotation marks around text inside a [<q>](/en-US/docs/Web/HTML/Reference/Elements/q) element. (A style rule may be needed to add quotation marks in older browsers.) The example below demonstrates the basic properties of the `CSSPseudoElement` object representing the opening quotation mark.

js

```
const element = document.querySelector("q");
const cssPseudoElement = element.pseudo("::before");
console.log(cssPseudoElement.element); // Outputs [object HTMLQuoteElement]
console.log(cssPseudoElement.type); // Outputs '::before'
```

## [Specifications](#specifications)

Specification
[CSS Pseudo-Elements Module Level 4# CSSPseudoElement-interface](https://drafts.csswg.org/css-pseudo/#CSSPseudoElement-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- `Element.pseudo()`
- [Web Animations API](/en-US/docs/Web/API/Web_Animations_API)
- [Element.animate()](/en-US/docs/Web/API/Element/animate)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 22, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/CSSPseudoElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csspseudoelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPseudoElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsspseudoelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPseudoElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsspseudoelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F47cff57ce02950e9137634e7923042d156f04081%0A*+Document+last+modified%3A+2023-11-22T07%3A58%3A59.000Z%0A%0A%3C%2Fdetails%3E)
