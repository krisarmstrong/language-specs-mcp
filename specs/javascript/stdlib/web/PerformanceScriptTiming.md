# PerformanceScriptTiming

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceScriptTiming&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `PerformanceScriptTiming` interface is specified in the Long Animation Frames API and provides metrics on individual scripts that contribute to long animation frames (LoAFs).

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

The `PerformanceScriptTiming` interface (instances of which are accessed via the [PerformanceLongAnimationFrameTiming.scripts](/en-US/docs/Web/API/PerformanceLongAnimationFrameTiming/scripts) property) provides the following granular set of information on individual scripts that contribute to LoAFs, allowing developers to narrow down their root causes:

- A detailed set of timestamps for each script.
- The identity and type of the invoker, i.e., the feature that, when invoked, ran the script.
- Detailed information on each script source file, including the URL, and the function name and character position that contributed to the LoAF.

`PerformanceScriptTiming` inherits from [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry).

## [Instance properties](#instance_properties)

This interface extends the following [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) properties for long animation frame performance entries:

[PerformanceEntry.duration](/en-US/docs/Web/API/PerformanceEntry/duration)Read onlyExperimental

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the elapsed time in milliseconds between the start and end of the script's execution.

[PerformanceEntry.entryType](/en-US/docs/Web/API/PerformanceEntry/entryType)Read onlyExperimental

Returns the entry type, which is always `"script"`.

[PerformanceEntry.name](/en-US/docs/Web/API/PerformanceEntry/name)Read onlyExperimental

Returns the entry name, which is always `"script"`.

[PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime)Read onlyExperimental

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time when the script execution started, in milliseconds.

This interface also supports the following properties:

[PerformanceScriptTiming.executionStart](/en-US/docs/Web/API/PerformanceScriptTiming/executionStart)Read onlyExperimental

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) indicating the time when the script compilation finished and execution started.

[PerformanceScriptTiming.forcedStyleAndLayoutDuration](/en-US/docs/Web/API/PerformanceScriptTiming/forcedStyleAndLayoutDuration)Read onlyExperimental

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) indicating the total time spent, in milliseconds, by the script processing forced layout/style. See [Avoid layout thrashing](https://web.dev/articles/avoid-large-complex-layouts-and-layout-thrashing#avoid_layout_thrashing) to understand what causes this.

[PerformanceScriptTiming.invoker](/en-US/docs/Web/API/PerformanceScriptTiming/invoker)Read onlyExperimental

Returns a string value indicating the identity of the feature that, when invoked, ran the script.

[PerformanceScriptTiming.invokerType](/en-US/docs/Web/API/PerformanceScriptTiming/invokerType)Read onlyExperimental

Returns a string value indicating the type of feature that, when invoked, ran the script.

[PerformanceScriptTiming.pauseDuration](/en-US/docs/Web/API/PerformanceScriptTiming/pauseDuration)Read onlyExperimental

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) indicating the total time, in milliseconds, spent by the script on "pausing" synchronous operations (for example, [Window.alert()](/en-US/docs/Web/API/Window/alert) calls or synchronous [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest)s).

[PerformanceScriptTiming.sourceCharPosition](/en-US/docs/Web/API/PerformanceScriptTiming/sourceCharPosition)Read onlyExperimental

Returns a number representing the script character position of the script feature that contributed to the LoAF.

[PerformanceScriptTiming.sourceFunctionName](/en-US/docs/Web/API/PerformanceScriptTiming/sourceFunctionName)Read onlyExperimental

Returns a string representing the name of the function that contributed to the LoAF.

[PerformanceScriptTiming.sourceURL](/en-US/docs/Web/API/PerformanceScriptTiming/sourceURL)Read onlyExperimental

Returns a string representing the URL of the script.

[PerformanceScriptTiming.window](/en-US/docs/Web/API/PerformanceScriptTiming/window)Read onlyExperimental

Returns a reference to a [Window](/en-US/docs/Web/API/Window) object representing the `window` of the container (i.e., either the top-level document or an [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe)) in which the LoAF-causing script was executed.

[PerformanceScriptTiming.windowAttribution](/en-US/docs/Web/API/PerformanceScriptTiming/windowAttribution)Read onlyExperimental

Returns an enumerated value describing the relationship of the container (i.e., either the top-level document or an [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe)) in which the LoAF-causing script was executed, relative to the window running the current document.

## [Instance methods](#instance_methods)

[PerformanceScriptTiming.toJSON()](/en-US/docs/Web/API/PerformanceScriptTiming/toJSON)Experimental

Returns a JSON representation of the `PerformanceScriptTiming` object.

## [Examples](#examples)

See [Long animation frame timing](/en-US/docs/Web/API/Performance_API/Long_animation_frame_timing#examples) for examples related to the Long Animation Frames API.

## [Specifications](#specifications)

Specification
[Long Animation Frames API# sec-PerformanceScriptTiming](https://w3c.github.io/long-animation-frames/#sec-PerformanceScriptTiming)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Long animation frame timing](/en-US/docs/Web/API/Performance_API/Long_animation_frame_timing)
- [PerformanceLongAnimationFrameTiming](/en-US/docs/Web/API/PerformanceLongAnimationFrameTiming)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PerformanceScriptTiming/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performancescripttiming/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceScriptTiming&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformancescripttiming%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceScriptTiming%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformancescripttiming%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
