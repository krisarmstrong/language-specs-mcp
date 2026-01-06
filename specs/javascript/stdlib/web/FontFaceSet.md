# FontFaceSet

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFontFaceSet&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `FontFaceSet` interface of the [CSS Font Loading API](/en-US/docs/Web/API/CSS_Font_Loading_API) manages the loading of font-faces and querying of their download status.

A `FontFaceSet` instance is a [Set-like object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set-like_browser_apis) that can hold an ordered set of [FontFace](/en-US/docs/Web/API/FontFace) objects.

This property is available as [Document.fonts](/en-US/docs/Web/API/Document/fonts), or `self.fonts` in [web workers](/en-US/docs/Web/API/Web_Workers_API).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[FontFaceSet.status](/en-US/docs/Web/API/FontFaceSet/status)Read only

Indicates the font-face's loading status. It will be one of `'loading'` or `'loaded'`.

[FontFaceSet.ready](/en-US/docs/Web/API/FontFaceSet/ready)Read only

[Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves once font loading and layout operations have completed.

[FontFaceSet.size](/en-US/docs/Web/API/FontFaceSet/size)Read only

Returns the number of values in the `FontFaceSet`.

### [Events](#events)

[loading](/en-US/docs/Web/API/FontFaceSet/loading_event)

Fires when a font-face set has started loading.

[loadingdone](/en-US/docs/Web/API/FontFaceSet/loadingdone_event)

Fires when a font face set has finished loading.

[loadingerror](/en-US/docs/Web/API/FontFaceSet/loadingerror_event)

Fires when an error occurred whilst loading a font-face set.

## [Instance methods](#instance_methods)

[FontFaceSet.add()](/en-US/docs/Web/API/FontFaceSet/add)

Adds a font to the font set.

[FontFaceSet.check()](/en-US/docs/Web/API/FontFaceSet/check)

A boolean value that indicates whether a font is loaded, but doesn't initiate a load when it isn't.

[FontFaceSet.clear()](/en-US/docs/Web/API/FontFaceSet/clear)

Removes all manually-added fonts from the font set. [CSS-connected](https://drafts.csswg.org/css-font-loading-3/#css-connected) fonts are unaffected.

[FontFaceSet.delete()](/en-US/docs/Web/API/FontFaceSet/delete)

Removes a manually-added font from the font set. [CSS-connected](https://drafts.csswg.org/css-font-loading-3/#css-connected) fonts are unaffected.

[FontFaceSet.entries()](/en-US/docs/Web/API/FontFaceSet/entries)

Returns a new iterator with the values for each element in the `FontFaceSet` in insertion order.

[FontFaceSet.forEach()](/en-US/docs/Web/API/FontFaceSet/forEach)

Executes a provided function for each value in the `FontFaceSet` object.

[FontFaceSet.has()](/en-US/docs/Web/API/FontFaceSet/has)

Returns a [Boolean](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean) asserting whether an element is present with the given value.

[FontFaceSet.keys()](/en-US/docs/Web/API/FontFaceSet/keys)

An alias for [FontFaceSet.values()](/en-US/docs/Web/API/FontFaceSet/values).

[FontFaceSet.load()](/en-US/docs/Web/API/FontFaceSet/load)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves to a list of font-faces for a requested font.

[FontFaceSet.values()](/en-US/docs/Web/API/FontFaceSet/values)

Returns a new iterator object that yields the values for each element in the `FontFaceSet` object in insertion order.

## [Specifications](#specifications)

Specification
[CSS Font Loading Module Level 3# FontFaceSet-interface](https://drafts.csswg.org/css-font-loading/#FontFaceSet-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FontFaceSet/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fontfaceset/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFontFaceSet&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffontfaceset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFontFaceSet%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffontfaceset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F636b90011532e3fd2cf9333aaf1754fdc8de7938%0A*+Document+last+modified%3A+2025-06-10T14%3A48%3A09.000Z%0A%0A%3C%2Fdetails%3E)
