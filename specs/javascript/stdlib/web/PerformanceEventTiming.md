# PerformanceEventTiming

 Baseline  2025 Newly available

 Since ⁨December 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceEventTiming&level=low)

The `PerformanceEventTiming` interface of the Event Timing API provides insights into the latency of certain event types triggered by user interaction.

## In this article

- [Description](#description)
- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Description](#description)

This API enables visibility into slow events by providing event timestamps and duration for certain event types ([see below](#events_exposed)). For example, you can monitor the time between a user action and the start of its event handler, or the time an event handler takes to run.

This API is particularly useful for measuring the [Interaction to Next Paint](/en-US/docs/Glossary/Interaction_to_next_paint) (INP): the longest time (minus some outliers) from the point when a user interacts with your app to the point until the browser was actually able to respond to that interaction.

You typically work with `PerformanceEventTiming` objects by creating a [PerformanceObserver](/en-US/docs/Web/API/PerformanceObserver) instance and then calling its [observe()](/en-US/docs/Web/API/PerformanceObserver/observe) method, passing in `"event"` or `"first-input"` as the value of the [type](/en-US/docs/Web/API/PerformanceEntry/entryType) option. The `PerformanceObserver` object's callback will then be called with a list of `PerformanceEventTiming` objects which you can analyze. See the [example below](#getting_event_timing_information) for more.

By default, `PerformanceEventTiming` entries are exposed when their `duration` is 104ms or greater. Research suggests that user input that is not handled within 100ms is considered slow and 104ms is the first multiple of 8 greater than 100ms (for security reasons, this API is rounded to the nearest multiple of 8ms). However, you can set the [PerformanceObserver](/en-US/docs/Web/API/PerformanceObserver) to a different threshold using the `durationThreshold` option in the [observe()](/en-US/docs/Web/API/PerformanceObserver/observe) method.

This interface inherits methods and properties from its parent, [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry):

### [Events exposed](#events_exposed)

The following event types are exposed by the Event Timing API:

Click events[auxclick](/en-US/docs/Web/API/Element/auxclick_event), [click](/en-US/docs/Web/API/Element/click_event), [contextmenu](/en-US/docs/Web/API/Element/contextmenu_event), [dblclick](/en-US/docs/Web/API/Element/dblclick_event)Composition events[compositionend](/en-US/docs/Web/API/Element/compositionend_event), [compositionstart](/en-US/docs/Web/API/Element/compositionstart_event), [compositionupdate](/en-US/docs/Web/API/Element/compositionupdate_event)Drag & drop events[dragend](/en-US/docs/Web/API/HTMLElement/dragend_event), [dragenter](/en-US/docs/Web/API/HTMLElement/dragenter_event), [dragleave](/en-US/docs/Web/API/HTMLElement/dragleave_event), [dragover](/en-US/docs/Web/API/HTMLElement/dragover_event), [dragstart](/en-US/docs/Web/API/HTMLElement/dragstart_event), [drop](/en-US/docs/Web/API/HTMLElement/drop_event)Input events[beforeinput](/en-US/docs/Web/API/Element/beforeinput_event), [input](/en-US/docs/Web/API/Element/input_event)Keyboard events[keydown](/en-US/docs/Web/API/Element/keydown_event), [keypress](/en-US/docs/Web/API/Element/keypress_event), [keyup](/en-US/docs/Web/API/Element/keyup_event)Mouse events[mousedown](/en-US/docs/Web/API/Element/mousedown_event), [mouseenter](/en-US/docs/Web/API/Element/mouseenter_event), [mouseleave](/en-US/docs/Web/API/Element/mouseleave_event), [mouseout](/en-US/docs/Web/API/Element/mouseout_event), [mouseover](/en-US/docs/Web/API/Element/mouseover_event), [mouseup](/en-US/docs/Web/API/Element/mouseup_event)Pointer events[pointerover](/en-US/docs/Web/API/Element/pointerover_event), [pointerenter](/en-US/docs/Web/API/Element/pointerenter_event), [pointerdown](/en-US/docs/Web/API/Element/pointerdown_event), [pointerup](/en-US/docs/Web/API/Element/pointerup_event), [pointercancel](/en-US/docs/Web/API/Element/pointercancel_event), [pointerout](/en-US/docs/Web/API/Element/pointerout_event), [pointerleave](/en-US/docs/Web/API/Element/pointerleave_event), [gotpointercapture](/en-US/docs/Web/API/Element/gotpointercapture_event), [lostpointercapture](/en-US/docs/Web/API/Element/lostpointercapture_event)Touch events[touchstart](/en-US/docs/Web/API/Element/touchstart_event), [touchend](/en-US/docs/Web/API/Element/touchend_event), [touchcancel](/en-US/docs/Web/API/Element/touchcancel_event)

Note that the following events are not included in the list because they are continuous events and no meaningful event counts or performance metrics can be obtained at this point: [mousemove](/en-US/docs/Web/API/Element/mousemove_event), [pointermove](/en-US/docs/Web/API/Element/pointermove_event), [pointerrawupdate](/en-US/docs/Web/API/Element/pointerrawupdate_event), [touchmove](/en-US/docs/Web/API/Element/touchmove_event), [wheel](/en-US/docs/Web/API/Element/wheel_event), [drag](/en-US/docs/Web/API/HTMLElement/drag_event).

To get a list of all exposed events, you can also look up keys in the [performance.eventCounts](/en-US/docs/Web/API/Performance/eventCounts) map:

js

```
const exposedEventsList = [...performance.eventCounts.keys()];
```

## [Constructor](#constructor)

This interface has no constructor on its own. See the [example below](#getting_event_timing_information) for how to typically get the information the `PerformanceEventTiming` interface holds.

## [Instance properties](#instance_properties)

This interface extends the following [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) properties for event timing performance entry types by qualifying them as follows:

[PerformanceEntry.duration](/en-US/docs/Web/API/PerformanceEntry/duration)Read only

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time from `startTime` to the next rendering paint (rounded to the nearest 8ms).

[PerformanceEntry.entryType](/en-US/docs/Web/API/PerformanceEntry/entryType)Read only

Returns `"event"` (for long events) or `"first-input"` (for the first user interaction).

[PerformanceEntry.name](/en-US/docs/Web/API/PerformanceEntry/name)Read only

Returns the associated event's type.

[PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime)Read only

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the associated event's [timestamp](/en-US/docs/Web/API/Event/timeStamp) property. This is the time the event was created and can be considered as a proxy for the time the user interaction occurred.

This interface also supports the following properties:

[PerformanceEventTiming.cancelable](/en-US/docs/Web/API/PerformanceEventTiming/cancelable)Read only

Returns the associated event's [cancelable](/en-US/docs/Web/API/Event/cancelable) property.

[PerformanceEventTiming.interactionId](/en-US/docs/Web/API/PerformanceEventTiming/interactionId)Read only

Returns the ID that uniquely identifies the user interaction which triggered the associated event.

[PerformanceEventTiming.processingStart](/en-US/docs/Web/API/PerformanceEventTiming/processingStart)Read only

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time at which event dispatch started. To measure the time between a user action and the time the event handler starts to run, calculate `processingStart-startTime`.

[PerformanceEventTiming.processingEnd](/en-US/docs/Web/API/PerformanceEventTiming/processingEnd)Read only

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time at which the event dispatch ended. To measure the time the event handler took to run, calculate `processingEnd-processingStart`.

[PerformanceEventTiming.target](/en-US/docs/Web/API/PerformanceEventTiming/target)Read only

Returns the associated event's last target, if it is not removed.

## [Instance methods](#instance_methods)

[PerformanceEventTiming.toJSON()](/en-US/docs/Web/API/PerformanceEventTiming/toJSON)

Returns a JSON representation of the `PerformanceEventTiming` object.

## [Examples](#examples)

### [Getting event timing information](#getting_event_timing_information)

To get event timing information, create a [PerformanceObserver](/en-US/docs/Web/API/PerformanceObserver) instance and then call its [observe()](/en-US/docs/Web/API/PerformanceObserver/observe) method, passing in `"event"` or `"first-input"` as the value of the [type](/en-US/docs/Web/API/PerformanceEntry/entryType) option. You also need to set `buffered` to `true` to get access to events the user agent buffered while constructing the document. The `PerformanceObserver` object's callback will then be called with a list of `PerformanceEventTiming` objects which you can analyze.

js

```
const observer = new PerformanceObserver((list) => {
  list.getEntries().forEach((entry) => {
    // Full duration
    const duration = entry.duration;

    // Input delay (before processing event)
    const delay = entry.processingStart - entry.startTime;

    // Synchronous event processing time
    // (between start and end dispatch)
    const eventHandlerTime = entry.processingEnd - entry.processingStart;
    console.log(`Total duration: ${duration}`);
    console.log(`Event delay: ${delay}`);
    console.log(`Event handler duration: ${eventHandlerTime}`);
  });
});

// Register the observer for events
observer.observe({ type: "event", buffered: true });
```

You can also set a different [durationThreshold](/en-US/docs/Web/API/PerformanceObserver/observe#durationthreshold). The default is 104ms and the minimum possible duration threshold is 16ms.

js

```
observer.observe({ type: "event", durationThreshold: 16, buffered: true });
```

## [Specifications](#specifications)

Specification
[Event Timing API# sec-performance-event-timing](https://w3c.github.io/event-timing/#sec-performance-event-timing)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Intersection Observer API](/en-US/docs/Web/API/Intersection_Observer_API)
- [Page Visibility API](/en-US/docs/Web/API/Page_Visibility_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 16, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PerformanceEventTiming/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performanceeventtiming/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceEventTiming&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformanceeventtiming%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceEventTiming%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformanceeventtiming%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcf16851e73da29823438198c4f0efcb7026b7d10%0A*+Document+last+modified%3A+2025-09-16T22%3A42%3A01.000Z%0A%0A%3C%2Fdetails%3E)
