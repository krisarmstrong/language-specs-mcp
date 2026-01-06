# HTMLFencedFrameElement

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLFencedFrameElement&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `HTMLFencedFrameElement` interface represents a [<fencedframe>](/en-US/docs/Web/HTML/Reference/Elements/fencedframe) element in JavaScript and provides configuration properties.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLFencedFrameElement.allow](/en-US/docs/Web/API/HTMLFencedFrameElement/allow)Experimental

Gets and sets the value of the corresponding `<fencedframe>``allow` attribute, which represents a [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) applied to the content when it is first embedded.

[HTMLFencedFrameElement.config](/en-US/docs/Web/API/HTMLFencedFrameElement/config)Experimental

a [FencedFrameConfig](/en-US/docs/Web/API/FencedFrameConfig) object, which represents the navigation of a [<fencedframe>](/en-US/docs/Web/HTML/Reference/Elements/fencedframe), i.e., what content will be displayed in it. A `FencedFrameConfig` is returned from a source such as the [Protected Audience API](https://privacysandbox.google.com/private-advertising/protected-audience).

[HTMLFencedFrameElement.height](/en-US/docs/Web/API/HTMLFencedFrameElement/height)Experimental

Gets and sets the value of the corresponding `<fencedframe>``height` attribute, which specifies the height of the element.

[HTMLFencedFrameElement.width](/en-US/docs/Web/API/HTMLFencedFrameElement/width)Experimental

Gets and sets the value of the corresponding `<fencedframe>``width` attribute, which specifies the width of the element.

## [Examples](#examples)

To set what content will be shown in a `<fencedframe>`, a utilizing API (such as [Protected Audience](https://privacysandbox.google.com/private-advertising/protected-audience) or [Shared Storage](https://privacysandbox.google.com/private-advertising/shared-storage)) generates a [FencedFrameConfig](/en-US/docs/Web/API/FencedFrameConfig) object, which is then set as the value of the `<fencedframe>`'s `config` property.

The following example gets a `FencedFrameConfig` from a Protected Audience API's ad auction, which is then used to display the winning ad in a `<fencedframe>`:

js

```
const frameConfig = await navigator.runAdAuction({
  // … auction configuration
  resolveToConfig: true,
});

const frame = document.createElement("fencedframe");
frame.config = frameConfig;
```

Note:`resolveToConfig: true` must be passed in to the `runAdAuction()` call to obtain a `FencedFrameConfig` object. If it is not set, the resulting [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) will resolve to a URN that can only be used in an [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe).

## [Specifications](#specifications)

Specification
[Fenced Frame# htmlfencedframeelement](https://wicg.github.io/fenced-frame/#htmlfencedframeelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Fenced frames](https://privacysandbox.google.com/private-advertising/fenced-frame) on privacysandbox.google.com
- [The Privacy Sandbox](https://privacysandbox.google.com/) on privacysandbox.google.com

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLFencedFrameElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlfencedframeelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLFencedFrameElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlfencedframeelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLFencedFrameElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlfencedframeelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa84b606ffd77c40a7306be6c932a74ab9ce6ab96%0A*+Document+last+modified%3A+2025-06-24T06%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
