# MediaList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaList&level=high)

The `MediaList` interface represents the media queries of a stylesheet, e.g., those set using a [<link>](/en-US/docs/Web/HTML/Reference/Elements/link) element's `media` attribute.

Note:`MediaList` is a live list; updating the list using properties or methods listed below will immediately update the behavior of the document.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[MediaList.mediaText](/en-US/docs/Web/API/MediaList/mediaText)

A [stringifier](/en-US/docs/Glossary/Stringifier) that returns a string representing the `MediaList` as text, and also allows you to set a new `MediaList`.

[MediaList.length](/en-US/docs/Web/API/MediaList/length)Read only

Returns the number of media queries in the `MediaList`.

## [Instance methods](#instance_methods)

[MediaList.appendMedium()](/en-US/docs/Web/API/MediaList/appendMedium)

Adds a media query to the `MediaList`.

[MediaList.deleteMedium()](/en-US/docs/Web/API/MediaList/deleteMedium)

Removes a media query from the `MediaList`.

[MediaList.item()](/en-US/docs/Web/API/MediaList/item)

A getter that returns a string representing a media query as text, given the media query's index value inside the `MediaList`. This method can also be called using the bracket (`[]`) syntax.

[MediaList.toString()](/en-US/docs/Web/API/MediaList/toString)

Returns a string representation of this media list in the same format as the object's [MediaList.mediaText](/en-US/docs/Web/API/MediaList/mediaText) property.

## [Examples](#examples)

The following would log to the console a textual representation of the `MediaList` of the first stylesheet applied to the current document.

js

```
const stylesheets = document.styleSheets;
let stylesheet = stylesheets[0];
console.log(stylesheet.media.mediaText);
```

## [Specifications](#specifications)

Specification
[CSS Object Model (CSSOM)# the-medialist-interface](https://drafts.csswg.org/cssom/#the-medialist-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MediaList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/medialist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmedialist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmedialist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa84b606ffd77c40a7306be6c932a74ab9ce6ab96%0A*+Document+last+modified%3A+2025-06-24T06%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
