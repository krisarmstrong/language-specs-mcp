# QuotaExceededError

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `QuotaExceededError` interface represents an error when a requested operation would exceed a system-imposed storage quota.

Note: In browser versions before this interface was implemented, it was a regular `DOMException`. The subclassing allows for extra information like `quota` and `requested` to be included.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[QuotaExceededError()](/en-US/docs/Web/API/QuotaExceededError/QuotaExceededError)Experimental

Creates a `QuotaExceededError` object.

## [Instance properties](#instance_properties)

Also inherits properties from its ancestor [DOMException](/en-US/docs/Web/API/DOMException).

[QuotaExceededError.quota](/en-US/docs/Web/API/QuotaExceededError/quota)Read onlyExperimental

Returns the system-defined storage limit (in bytes) that was exceeded.

[requested](/en-US/docs/Web/API/QuotaExceededError/requested)Read onlyExperimental

Returns the amount of storage (in bytes) that was requested during the operation.

## [Specifications](#specifications)

Specification
[Web IDL# quotaexceedederror](https://webidl.spec.whatwg.org/#quotaexceedederror)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [DOMException](/en-US/docs/Web/API/DOMException)
- [StorageManager.estimate()](/en-US/docs/Web/API/StorageManager/estimate)
- [Storage quotas and eviction criteria](/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 20, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/QuotaExceededError/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/quotaexceedederror/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FQuotaExceededError&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fquotaexceedederror%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FQuotaExceededError%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fquotaexceedederror%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F886f2641ae90a70858c5e7d0d20959c70ee44d9d%0A*+Document+last+modified%3A+2025-08-20T01%3A23%3A27.000Z%0A%0A%3C%2Fdetails%3E)
