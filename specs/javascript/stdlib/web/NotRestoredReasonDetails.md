# NotRestoredReasonDetails

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNotRestoredReasonDetails&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `NotRestoredReasonDetails` interface of the [Performance API](/en-US/docs/Web/API/Performance_API) represents a single reason why a navigated page was blocked from using the back/forward cache ([bfcache](/en-US/docs/Glossary/bfcache)).

An array of `NotRestoredReasonDetails` objects can be accessed via the [NotRestoredReasons.reasons](/en-US/docs/Web/API/NotRestoredReasons/reasons) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[reason](/en-US/docs/Web/API/NotRestoredReasonDetails/reason)Read onlyExperimental

A string describing a reason that the page was blocked from using the back/forward cache.

## [Instance methods](#instance_methods)

[toJSON()](/en-US/docs/Web/API/NotRestoredReasonDetails/toJSON)Experimental

A [serializer](/en-US/docs/Glossary/Serialization); returns a JSON representation of the `NotRestoredReasonDetails` object.

## [Examples](#examples)

See [Monitoring bfcache blocking reasons](/en-US/docs/Web/API/Performance_API/Monitoring_bfcache_blocking_reasons) for examples.

## [Specifications](#specifications)

Specification
[HTML# notrestoredreasondetails](https://html.spec.whatwg.org/multipage/nav-history-apis.html#notrestoredreasondetails)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Monitoring bfcache blocking reasons](/en-US/docs/Web/API/Performance_API/Monitoring_bfcache_blocking_reasons)
- [PerformanceNavigationTiming.notRestoredReasons](/en-US/docs/Web/API/PerformanceNavigationTiming/notRestoredReasons)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 12, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/NotRestoredReasonDetails/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/notrestoredreasondetails/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNotRestoredReasonDetails&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnotrestoredreasondetails%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNotRestoredReasonDetails%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnotrestoredreasondetails%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3148591fa7280daf3e88a5cece3b60dfc9470330%0A*+Document+last+modified%3A+2024-04-12T10%3A05%3A54.000Z%0A%0A%3C%2Fdetails%3E)
