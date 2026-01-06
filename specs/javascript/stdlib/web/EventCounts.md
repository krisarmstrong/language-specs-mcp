# EventCounts

 Baseline  2025 Newly available

 Since ⁨December 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEventCounts&level=low)

The `EventCounts` interface of the [Performance API](/en-US/docs/Web/API/Performance_API) provides the number of events that have been dispatched for each event type.

An `EventCounts` instance is a read-only [Map-like object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#map-like_browser_apis), in which each key is the name string for an event type, and the corresponding value is an integer indicating the number of events that have been dispatched for that event type.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

This interface has no constructor. You typically get an instance of this object using the [performance.eventCounts](/en-US/docs/Web/API/Performance/eventCounts) property.

## [Instance properties](#instance_properties)

[size](#size)

See [Map.prototype.size](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/size) for details.

## [Instance methods](#instance_methods)

[entries()](#entries)

See [Map.prototype.entries()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/entries) for details.

[forEach()](#foreach)

See [Map.prototype.forEach()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/forEach) for details.

[get()](#get)

See [Map.prototype.get()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/get) for details.

[has()](#has)

See [Map.prototype.has()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/has) for details.

[keys()](#keys)

See [Map.prototype.keys()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/keys) for details.

[values()](#values)

See [Map.prototype.values()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/values) for details.

## [Examples](#examples)

### [Working with EventCount maps](#working_with_eventcount_maps)

Below are a few examples to get information from an `EventCounts` map. Note that the map is read-only and the `clear()`, `delete()`, and `set()` methods aren't available.

js

```
for (entry of performance.eventCounts.entries()) {
  const type = entry[0];
  const count = entry[1];
}

const clickCount = performance.eventCounts.get("click");

const isExposed = performance.eventCounts.has("mousemove");
const exposedEventsCount = performance.eventCounts.size;
const exposedEventsList = [...performance.eventCounts.keys()];
```

## [Specifications](#specifications)

Specification
[Event Timing API# sec-event-counts](https://w3c.github.io/event-timing/#sec-event-counts)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [performance.eventCounts](/en-US/docs/Web/API/Performance/eventCounts)
- [PerformanceEventTiming](/en-US/docs/Web/API/PerformanceEventTiming)
- [Map](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 5, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/EventCounts/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/eventcounts/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEventCounts&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Feventcounts%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEventCounts%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Feventcounts%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe18aa8e600733ebc25443075c563fd56361dfe98%0A*+Document+last+modified%3A+2023-09-05T23%3A54%3A58.000Z%0A%0A%3C%2Fdetails%3E)
