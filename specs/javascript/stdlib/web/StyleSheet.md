# StyleSheet

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStyleSheet&level=high)

An object implementing the `StyleSheet` interface represents a single style sheet. CSS style sheets will further implement the more specialized [CSSStyleSheet](/en-US/docs/Web/API/CSSStyleSheet) interface.

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[StyleSheet.disabled](/en-US/docs/Web/API/StyleSheet/disabled)

A boolean value representing whether the current stylesheet has been applied or not.

[StyleSheet.href](/en-US/docs/Web/API/StyleSheet/href)Read only

Returns a string representing the location of the stylesheet.

[StyleSheet.media](/en-US/docs/Web/API/StyleSheet/media)Read only

Returns a [MediaList](/en-US/docs/Web/API/MediaList) representing the intended destination medium for style information.

[StyleSheet.ownerNode](/en-US/docs/Web/API/StyleSheet/ownerNode)Read only

Returns a [Node](/en-US/docs/Web/API/Node) associating this style sheet with the current document.

[StyleSheet.parentStyleSheet](/en-US/docs/Web/API/StyleSheet/parentStyleSheet)Read only

Returns a `StyleSheet` including this one, if any; returns `null` if there aren't any.

[StyleSheet.title](/en-US/docs/Web/API/StyleSheet/title)Read only

Returns a string representing the advisory title of the current style sheet.

[StyleSheet.type](/en-US/docs/Web/API/StyleSheet/type)Read only

Returns a string representing the style sheet language for this style sheet.

## [Specifications](#specifications)

Specification
[CSS Object Model (CSSOM)# the-stylesheet-interface](https://drafts.csswg.org/cssom/#the-stylesheet-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CSSStyleSheet](/en-US/docs/Web/API/CSSStyleSheet)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/StyleSheet/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/stylesheet/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStyleSheet&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fstylesheet%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStyleSheet%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fstylesheet%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32305cc3cf274fbfdcc73a296bbd400a26f38296%0A*+Document+last+modified%3A+2024-07-24T20%3A47%3A46.000Z%0A%0A%3C%2Fdetails%3E)
