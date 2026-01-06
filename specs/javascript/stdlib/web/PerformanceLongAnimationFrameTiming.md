# PerformanceLongAnimationFrameTiming

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceLongAnimationFrameTiming&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `PerformanceLongAnimationFrameTiming` interface is specified in the Long Animation Frames API and provides metrics on long animation frames (LoAFs) that occupy rendering and block other tasks from being executed.

## In this article

- [Description](#description)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Description](#description)

Long animation frames (LoAFs) are rendering updates that are delayed beyond 50ms. LoAFs can result in slow user interface (UI) updates, making controls appear unresponsive and causing [janky](/en-US/docs/Glossary/Jank) (non-smooth) animated effects and scrolling. This often leads to user frustration.

The `PerformanceLongAnimationFrameTiming` interface provides the following granular set of information on LoAFs, allowing developers to narrow down their root causes:

- A detailed set of timestamps for each LoAF.
- Detailed information on each script that contributed to creating the LoAF, via the [PerformanceLongAnimationFrameTiming.scripts](/en-US/docs/Web/API/PerformanceLongAnimationFrameTiming/scripts) property. This returns an array of [PerformanceScriptTiming](/en-US/docs/Web/API/PerformanceScriptTiming) objects, one for each script.

`PerformanceLongAnimationFrameTiming` inherits from [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry).

## [Instance properties](#instance_properties)

This interface extends the following [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) properties for long animation frame performance entries:

[PerformanceEntry.duration](/en-US/docs/Web/API/PerformanceEntry/duration)Read onlyExperimental

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time taken in milliseconds to process the LoAF in its entirety.

[PerformanceEntry.entryType](/en-US/docs/Web/API/PerformanceEntry/entryType)Read onlyExperimental

Returns the entry type, which is always `"long-animation-frame"`.

[PerformanceEntry.name](/en-US/docs/Web/API/PerformanceEntry/name)Read onlyExperimental

Returns the entry name, which is always `"long-animation-frame"`.

[PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime)Read onlyExperimental

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time when the animation frame started.

This interface also supports the following properties:

[PerformanceLongAnimationFrameTiming.blockingDuration](/en-US/docs/Web/API/PerformanceLongAnimationFrameTiming/blockingDuration)Read onlyExperimental

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) indicating the total time in milliseconds that the main thread was blocked from responding to high priority tasks, such as user input. This is calculated by taking all the [long tasks](/en-US/docs/Web/API/PerformanceLongTaskTiming#description) within the LoAF that have a `duration` of more than `50ms`, subtracting `50ms` from each, adding the rendering time to the longest task time, and summing the results.

[PerformanceLongAnimationFrameTiming.firstUIEventTimestamp](/en-US/docs/Web/API/PerformanceLongAnimationFrameTiming/firstUIEventTimestamp)Read onlyExperimental

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) indicating the time of the first UI event — such as a mouse or keyboard event — to be queued during the current animation frame.

[PerformanceLongAnimationFrameTiming.renderStart](/en-US/docs/Web/API/PerformanceLongAnimationFrameTiming/renderStart)Read onlyExperimental

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) indicating the start time of the rendering cycle, which includes [Window.requestAnimationFrame()](/en-US/docs/Web/API/Window/requestAnimationFrame) callbacks, style and layout calculation, [ResizeObserver](/en-US/docs/Web/API/ResizeObserver) callbacks, and [IntersectionObserver](/en-US/docs/Web/API/IntersectionObserver) callbacks.

[PerformanceLongAnimationFrameTiming.scripts](/en-US/docs/Web/API/PerformanceLongAnimationFrameTiming/scripts)Read onlyExperimental

Returns an array of [PerformanceScriptTiming](/en-US/docs/Web/API/PerformanceScriptTiming) instances.

[PerformanceLongAnimationFrameTiming.styleAndLayoutStart](/en-US/docs/Web/API/PerformanceLongAnimationFrameTiming/styleAndLayoutStart)Read onlyExperimental

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) indicating the beginning of the time period spent in style and layout calculations for the current animation frame.

## [Instance methods](#instance_methods)

[PerformanceLongAnimationFrameTiming.toJSON()](/en-US/docs/Web/API/PerformanceLongAnimationFrameTiming/toJSON)Experimental

Returns a JSON representation of the `PerformanceLongAnimationFrameTiming` object.

## [Examples](#examples)

See [Long animation frame timing](/en-US/docs/Web/API/Performance_API/Long_animation_frame_timing#examples) for examples related to the Long Animation Frames API.

## [Specifications](#specifications)

Specification
[Long Animation Frames API# sec-PerformanceLongAnimationFrameTiming](https://w3c.github.io/long-animation-frames/#sec-PerformanceLongAnimationFrameTiming)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Long animation frame timing](/en-US/docs/Web/API/Performance_API/Long_animation_frame_timing)
- [PerformanceScriptTiming](/en-US/docs/Web/API/PerformanceScriptTiming)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PerformanceLongAnimationFrameTiming/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performancelonganimationframetiming/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceLongAnimationFrameTiming&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformancelonganimationframetiming%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceLongAnimationFrameTiming%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformancelonganimationframetiming%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F04301fa08caba25ce0fc17ea80e35383aa3361c0%0A*+Document+last+modified%3A+2024-10-08T19%3A44%3A13.000Z%0A%0A%3C%2Fdetails%3E)
