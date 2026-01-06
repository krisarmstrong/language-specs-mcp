# Performance APIs

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Performance API is a group of standards used to measure the performance of web applications.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Reference](#reference)
- [Guides](#guides)
- [Specifications](#specifications)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

To ensure web applications are fast, it's important to measure and analyze various performance metrics. The Performance API provides important built-in metrics and the ability to add your own measurements to the browser's performance timeline. The performance timeline contains high precision timestamps and can be displayed in developer tools. You can also send its data to analytics end points to record performance metrics over time.

Each performance metric is represented by a single [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry). A performance entry has a `name`, a `duration`, a `startTime`, and a `type`. All performance metrics extend the `PerformanceEntry` interface and qualify it further.

Most of the performance entries are recorded for you without you having to do anything, and are then accessible either through [Performance.getEntries()](/en-US/docs/Web/API/Performance/getEntries) or (preferably) through [PerformanceObserver](/en-US/docs/Web/API/PerformanceObserver). For example, [PerformanceEventTiming](/en-US/docs/Web/API/PerformanceEventTiming) entries are recorded for events that take longer than a set threshold. But the Performance API also enables you to define and record your own custom events, using the [PerformanceMark](/en-US/docs/Web/API/PerformanceMark) and [PerformanceMeasure](/en-US/docs/Web/API/PerformanceMeasure) interfaces.

The main [Performance](/en-US/docs/Web/API/Performance) interface is available in both [Window](/en-US/docs/Web/API/Window/performance) and [Worker](/en-US/docs/Web/API/WorkerGlobalScope/performance) global scopes, and enables you to add custom performance entries, to clear performance entries, and to retrieve performance entries.

The [PerformanceObserver](/en-US/docs/Web/API/PerformanceObserver) interface enables you to listen for various types of performance entry as they are recorded.

For more conceptual information, see the [Performance API guides](#guides) below.

## [Reference](#reference)

The following interfaces are present in the Performance API:

[EventCounts](/en-US/docs/Web/API/EventCounts)

A read-only map returned by [performance.eventCounts](/en-US/docs/Web/API/Performance/eventCounts) containing the number of events which have been dispatched per event type.

[LargestContentfulPaint](/en-US/docs/Web/API/LargestContentfulPaint)

Measures the render time of the largest image or text block visible within the viewport, recorded from when the page first begins to load.

[LayoutShift](/en-US/docs/Web/API/LayoutShift)

Provides insights into the layout stability of web pages based on movements of the elements on the page.

[LayoutShiftAttribution](/en-US/docs/Web/API/LayoutShiftAttribution)

Provides debugging information about elements which have shifted.

[NotRestoredReasonDetails](/en-US/docs/Web/API/NotRestoredReasonDetails)

Represents a single reason why a navigated page was blocked from using the back/forward cache ([bfcache](/en-US/docs/Glossary/bfcache)).

[NotRestoredReasons](/en-US/docs/Web/API/NotRestoredReasons)

Provides report data containing reasons why the current document was blocked from using the back/forward cache ([bfcache](/en-US/docs/Glossary/bfcache)) on navigation.

[Performance](/en-US/docs/Web/API/Performance)

Main interface to access performance measurements. Available to window and worker contexts using [Window.performance](/en-US/docs/Web/API/Window/performance) or [WorkerGlobalScope.performance](/en-US/docs/Web/API/WorkerGlobalScope/performance).

[PerformanceElementTiming](/en-US/docs/Web/API/PerformanceElementTiming)

Measures rendering timestamps of specific elements.

[PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry)

An entry on the performance timeline encapsulating a single performance metric. All performance metrics inherit from this interface.

[PerformanceEventTiming](/en-US/docs/Web/API/PerformanceEventTiming)

Measures latency of events and [Interaction to Next Paint](/en-US/docs/Glossary/Interaction_to_next_paint) (INP).

[PerformanceLongAnimationFrameTiming](/en-US/docs/Web/API/PerformanceLongAnimationFrameTiming)

Provides metrics on [long animation frames (LoAFs)](/en-US/docs/Web/API/Performance_API/Long_animation_frame_timing#what_is_a_long_animation_frame) that occupy rendering and block other tasks from being executed.

[PerformanceLongTaskTiming](/en-US/docs/Web/API/PerformanceLongTaskTiming)

Provides metrics on [long tasks](/en-US/docs/Glossary/Long_task) that occupy rendering and block other tasks from being executed.

[PerformanceMark](/en-US/docs/Web/API/PerformanceMark)

Custom marker for your own entry on the performance timeline.

[PerformanceMeasure](/en-US/docs/Web/API/PerformanceMeasure)

Custom time measurement between two performance entries.

[PerformanceNavigationTiming](/en-US/docs/Web/API/PerformanceNavigationTiming)

Measures document navigation events, like how much time it takes to load a document.

[PerformanceObserver](/en-US/docs/Web/API/PerformanceObserver)

Listens for new performance entries as they are recorded in the performance timeline.

[PerformanceObserverEntryList](/en-US/docs/Web/API/PerformanceObserverEntryList)

List of entries that were observed in a performance observer.

[PerformancePaintTiming](/en-US/docs/Web/API/PerformancePaintTiming)

Measures render operations during web page construction.

[PerformanceResourceTiming](/en-US/docs/Web/API/PerformanceResourceTiming)

Measures network loading metrics such as redirect start and end times, fetch start, DNS lookup start and end times, response start and end times for resources such as images, scripts, fetch calls, etc.

[PerformanceScriptTiming](/en-US/docs/Web/API/PerformanceScriptTiming)

Provides metrics on individual scripts causing [long animation frames (LoAFs)](/en-US/docs/Web/API/Performance_API/Long_animation_frame_timing#what_is_a_long_animation_frame).

[PerformanceServerTiming](/en-US/docs/Web/API/PerformanceServerTiming)

Surfaces server metrics that are sent with the response in the [Server-Timing](/en-US/docs/Web/HTTP/Reference/Headers/Server-Timing) HTTP header.

[TaskAttributionTiming](/en-US/docs/Web/API/TaskAttributionTiming)

Identifies the type of task and the container that is responsible for the long task.

[VisibilityStateEntry](/en-US/docs/Web/API/VisibilityStateEntry)

Measures the timing of page visibility state changes, i.e., when a tab changes from the foreground to the background or vice versa.

## [Guides](#guides)

The following guides help you to understand key concepts of the Performance API and provide an overview about its abilities:

- [Performance data](/en-US/docs/Web/API/Performance_API/Performance_data): Collecting, accessing, and working with performance data.
- [High precision timing](/en-US/docs/Web/API/Performance_API/High_precision_timing): Measuring with high precision time and monotonic clocks.
- [Resource timing](/en-US/docs/Web/API/Performance_API/Resource_timing): Measuring network timing for fetched resources, such as images, CSS, and JavaScript.
- [Navigation timing](/en-US/docs/Web/API/Performance_API/Navigation_timing): Measuring navigation timing of a document.
- [User timing](/en-US/docs/Web/API/Performance_API/User_timing): Measuring and recording performance data custom to your application.
- [Server timing](/en-US/docs/Web/API/Performance_API/Server_timing): Collecting server-side metrics.
- [Long animation frame timing](/en-US/docs/Web/API/Performance_API/Long_animation_frame_timing): Collecting metrics on long animation frames (LoAFs) and their causes.
- [Monitoring bfcache blocking reasons](/en-US/docs/Web/API/Performance_API/Monitoring_bfcache_blocking_reasons): Reporting on why the current document was blocked from using the back/forward cache ([bfcache](/en-US/docs/Glossary/bfcache)).

## [Specifications](#specifications)

Specification[Element Timing API](https://wicg.github.io/element-timing/)[Event Timing API](https://w3c.github.io/event-timing/)[High Resolution Time](https://w3c.github.io/hr-time/)[Largest Contentful Paint](https://w3c.github.io/largest-contentful-paint/)[Layout Instability API](https://wicg.github.io/layout-instability/)[Long Tasks API](https://w3c.github.io/longtasks/)[Navigation Timing Level 2](https://w3c.github.io/navigation-timing/)[Paint Timing](https://w3c.github.io/paint-timing/)[Performance Timeline](https://w3c.github.io/performance-timeline/)[Resource Timing](https://w3c.github.io/resource-timing/)[Server Timing](https://w3c.github.io/server-timing/)[User Timing](https://w3c.github.io/user-timing/)[Long Animation Frames API](https://w3c.github.io/long-animation-frames/)[Measure Memory API](https://wicg.github.io/performance-measure-memory/)
[HTML# the-visibilitystateentry-interface](https://html.spec.whatwg.org/multipage/interaction.html#the-visibilitystateentry-interface)
[HTML# the-notrestoredreasons-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-notrestoredreasons-interface)

## [See also](#see_also)

- [Web performance](/en-US/docs/Web/Performance)
- [Learn: Web performance](/en-US/docs/Learn_web_development/Extensions/Performance)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 19, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Performance_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performance_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformance_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformance_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformance_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformance_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5b20f5f4265f988f80f513db0e4b35c7e0cd70dc%0A*+Document+last+modified%3A+2024-12-19T15%3A37%3A45.000Z%0A%0A%3C%2Fdetails%3E)
