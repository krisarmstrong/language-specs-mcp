# TaskAttributionTiming

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTaskAttributionTiming&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `TaskAttributionTiming` interface returns information about the work involved in a long task and its associate frame context. The frame context, also called the container, is the iframe, embed or object that is being implicated, on the whole, for a long task.

You usually work with `TaskAttributionTiming` objects when observing [long tasks](/en-US/docs/Web/API/PerformanceLongTaskTiming).

`TaskAttributionTiming` inherits from [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface extends the following [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) properties for event timing performance entry types by qualifying them as follows:

[PerformanceEntry.duration](/en-US/docs/Web/API/PerformanceEntry/duration)Read onlyExperimental

Always returns `0`, as `duration` is not applicable for this interface.

[PerformanceEntry.entryType](/en-US/docs/Web/API/PerformanceEntry/entryType)Read onlyExperimental

Always returns `taskattribution`.

[PerformanceEntry.name](/en-US/docs/Web/API/PerformanceEntry/name)Read onlyExperimental

Always returns `"unknown"`.

[PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime)Read onlyExperimental

Always returns `0`.

This interface also supports the following properties:

[TaskAttributionTiming.containerType](/en-US/docs/Web/API/TaskAttributionTiming/containerType)Read onlyExperimental

Returns the type of frame container, one of `iframe`, `embed`, or `object`.

[TaskAttributionTiming.containerSrc](/en-US/docs/Web/API/TaskAttributionTiming/containerSrc)Read onlyExperimental

Returns the container's `src` attribute.

[TaskAttributionTiming.containerId](/en-US/docs/Web/API/TaskAttributionTiming/containerId)Read onlyExperimental

Returns the container's `id` attribute.

[TaskAttributionTiming.containerName](/en-US/docs/Web/API/TaskAttributionTiming/containerName)Read onlyExperimental

Returns the container's `name` attribute.

## [Instance methods](#instance_methods)

[TaskAttributionTiming.toJSON()](/en-US/docs/Web/API/TaskAttributionTiming/toJSON)Experimental

Returns a JSON representation of the `TaskAttributionTiming` object.

## [Specifications](#specifications)

Specification
[Long Tasks API# sec-TaskAttributionTiming](https://w3c.github.io/longtasks/#sec-TaskAttributionTiming)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [PerformanceLongTaskTiming](/en-US/docs/Web/API/PerformanceLongTaskTiming)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 19, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/TaskAttributionTiming/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/taskattributiontiming/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTaskAttributionTiming&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftaskattributiontiming%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTaskAttributionTiming%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftaskattributiontiming%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd414c502f3cc1c08d2fb043e98cda4a65621ff08%0A*+Document+last+modified%3A+2023-02-19T08%3A44%3A56.000Z%0A%0A%3C%2Fdetails%3E)
