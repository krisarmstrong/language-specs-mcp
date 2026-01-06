# SyncEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSyncEvent&level=not)

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `SyncEvent` interface of the [Background Synchronization API](/en-US/docs/Web/API/Background_Synchronization_API) represents a sync action that is dispatched on the [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) of a ServiceWorker.

This interface inherits from the [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent) interface.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[SyncEvent()](/en-US/docs/Web/API/SyncEvent/SyncEvent)

Creates a new `SyncEvent` object.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent) and [Event](/en-US/docs/Web/API/Event).

[SyncEvent.tag](/en-US/docs/Web/API/SyncEvent/tag)Read only

Returns the developer-defined identifier for this `SyncEvent`.

[SyncEvent.lastChance](/en-US/docs/Web/API/SyncEvent/lastChance)Read only

Returns `true` if the user agent will not make further synchronization attempts after the current attempt.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent) and [Event](/en-US/docs/Web/API/Event).

None.

## [Specifications](#specifications)

Specification
[Web Background Synchronization# sync-event](https://wicg.github.io/background-sync/spec/#sync-event)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 19, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/SyncEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/syncevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSyncEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsyncevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSyncEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsyncevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Faa38aff31533096459caed61424a6f20f9807a15%0A*+Document+last+modified%3A+2024-04-19T15%3A40%3A01.000Z%0A%0A%3C%2Fdetails%3E)
