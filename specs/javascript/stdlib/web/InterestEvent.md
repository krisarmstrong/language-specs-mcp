# InterestEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInterestEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `InterestEvent` interface represents an event that fires when interest is shown or lost on an [interest invoker](/en-US/docs/Web/API/Popover_API/Using_interest_invokers).

This is the event object for the [interest](/en-US/docs/Web/API/HTMLElement/interest_event) and [loseinterest](/en-US/docs/Web/API/HTMLElement/loseinterest_event) events, which fire on the target element when interest is shown or lost, respectively.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[InterestEvent()](/en-US/docs/Web/API/InterestEvent/InterestEvent)ExperimentalNon-standard

Creates an `InterestEvent` object.

## [Instance properties](#instance_properties)

This interface inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[InterestEvent.source](/en-US/docs/Web/API/InterestEvent/source)Read onlyExperimentalNon-standard

An [Element](/en-US/docs/Web/API/Element) object instance that represents the interest invoker element on which interest was shown or lost to fire the event.

## [Examples](#examples)

See the [Using interest invokers](/en-US/docs/Web/API/Popover_API/Using_interest_invokers) guide and the [interest](/en-US/docs/Web/API/HTMLElement/interest_event) event reference page for examples.

## [Specifications](#specifications)

This feature does not appear to be defined in any specification.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Popover API](/en-US/docs/Web/API/Popover_API)
- [Using interest invokers](/en-US/docs/Web/API/Popover_API/Using_interest_invokers)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 11, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/InterestEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/interestevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInterestEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Finterestevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInterestEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Finterestevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0563b7d83916b234fa637483211889e573df9440%0A*+Document+last+modified%3A+2025-12-11T12%3A09%3A51.000Z%0A%0A%3C%2Fdetails%3E)
