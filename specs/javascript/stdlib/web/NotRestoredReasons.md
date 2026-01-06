# NotRestoredReasons

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNotRestoredReasons&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `NotRestoredReasons` interface of the [Performance API](/en-US/docs/Web/API/Performance_API) provides report data containing reasons why the current document was blocked from using the back/forward cache ([bfcache](/en-US/docs/Glossary/bfcache)) on navigation.

These objects are accessed via the [PerformanceNavigationTiming.notRestoredReasons](/en-US/docs/Web/API/PerformanceNavigationTiming/notRestoredReasons) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[children](/en-US/docs/Web/API/NotRestoredReasons/children)Read onlyExperimental

An array of `NotRestoredReasons` objects, one for each child [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe) embedded in the current document, which may contain reasons why the top-level frame was blocked relating to the child frames. Each object has the same structure as the parent object — this way, any number of levels of embedded `<iframe>`s can be represented inside the object recursively. If the frame has no children, the array will be empty; if the document is in a cross-origin `<iframe>`, `children` will return `null`.

[id](/en-US/docs/Web/API/NotRestoredReasons/id)Read onlyExperimental

A string representing the `id` attribute value of the `<iframe>` the document is contained in (for example `<iframe id="foo" src="...">`). If the document is not in an `<iframe>` or the `<iframe>` has no `id` set, `id` will return `null`.

[name](/en-US/docs/Web/API/NotRestoredReasons/name)Read onlyExperimental

A string representing the `name` attribute value of the `<iframe>` the document is contained in (for example `<iframe name="bar" src="...">`). If the document is not in an `<iframe>` or the `<iframe>` has no `name` set, `name` will return `null`.

[reasons](/en-US/docs/Web/API/NotRestoredReasons/reasons)Read onlyExperimental

An array of [NotRestoredReasonDetails](/en-US/docs/Web/API/NotRestoredReasonDetails) objects, each representing a reason why the navigated page was blocked from using the bfcache. If the document is in a cross-origin `<iframe>`, `reasons` will return `null`, but the parent document may show a `reason` of `"masked"` if any `<iframe>`s blocked bfcache usage for the top-level frame.

[src](/en-US/docs/Web/API/NotRestoredReasons/src)Read onlyExperimental

A string representing the path to the source of the `<iframe>` the document is contained in (for example `<iframe src="exampleframe.html">`). If the document is not in an `<iframe>`, `src` will return `null`.

[url](/en-US/docs/Web/API/NotRestoredReasons/url)Read onlyExperimental

A string representing the URL of the navigated page or `<iframe>`. If the document is in a cross-origin `<iframe>`, `url` will return `null`.

## [Instance methods](#instance_methods)

[toJSON()](/en-US/docs/Web/API/NotRestoredReasons/toJSON)Experimental

A [serializer](/en-US/docs/Glossary/Serialization); returns a JSON representation of the `NotRestoredReasons` object.

## [Examples](#examples)

See [Monitoring bfcache blocking reasons](/en-US/docs/Web/API/Performance_API/Monitoring_bfcache_blocking_reasons) for examples.

## [Specifications](#specifications)

Specification
[HTML# notrestoredreasons](https://html.spec.whatwg.org/multipage/nav-history-apis.html#notrestoredreasons)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Monitoring bfcache blocking reasons](/en-US/docs/Web/API/Performance_API/Monitoring_bfcache_blocking_reasons)
- [PerformanceNavigationTiming.notRestoredReasons](/en-US/docs/Web/API/PerformanceNavigationTiming/notRestoredReasons)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 12, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/NotRestoredReasons/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/notrestoredreasons/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNotRestoredReasons&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnotrestoredreasons%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNotRestoredReasons%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnotrestoredreasons%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3148591fa7280daf3e88a5cece3b60dfc9470330%0A*+Document+last+modified%3A+2024-04-12T10%3A05%3A54.000Z%0A%0A%3C%2Fdetails%3E)
