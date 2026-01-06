# FontFaceSetLoadEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFontFaceSetLoadEvent&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `FontFaceSetLoadEvent` interface of the [CSS Font Loading API](/en-US/docs/Web/API/CSS_Font_Loading_API) represents events fired at a [FontFaceSet](/en-US/docs/Web/API/FontFaceSet) after it starts loading font faces.

Events are fired when font loading starts ([loading](/en-US/docs/Web/API/FontFaceSet/loading_event)), loading completes ([loadingdone](/en-US/docs/Web/API/FontFaceSet/loadingdone_event)) or there is an error loading one of the fonts ([loadingerror](/en-US/docs/Web/API/FontFaceSet/loadingerror_event)).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[FontFaceSetLoadEvent()](/en-US/docs/Web/API/FontFaceSetLoadEvent/FontFaceSetLoadEvent)

Creates a new `FontFaceSetLoadEvent` object.

## [Instance properties](#instance_properties)

Also inherits properties from its parent [Event](/en-US/docs/Web/API/Event).

[FontFaceSetLoadEvent.fontfaces](/en-US/docs/Web/API/FontFaceSetLoadEvent/fontfaces)Read only

Returns an array of [FontFace](/en-US/docs/Web/API/FontFace) instances. Depending on the event, the array will contain font faces that are loading (`loading`), have successfully loaded (`loadingdone`), or have failed to load (`loadingerror`).

## [Instance methods](#instance_methods)

Inherits methods from its parent, [Event](/en-US/docs/Web/API/Event).

## [Specifications](#specifications)

Specification
[CSS Font Loading Module Level 3# fontfacesetloadevent](https://drafts.csswg.org/css-font-loading/#fontfacesetloadevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Document.fonts](/en-US/docs/Web/API/Document/fonts)
- [WorkerGlobalScope.fonts](/en-US/docs/Web/API/WorkerGlobalScope/fonts)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/FontFaceSetLoadEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fontfacesetloadevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFontFaceSetLoadEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffontfacesetloadevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFontFaceSetLoadEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffontfacesetloadevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3b7232826ab98368d06ebf8b021886e4a544de93%0A*+Document+last+modified%3A+2024-10-08T19%3A37%3A19.000Z%0A%0A%3C%2Fdetails%3E)
