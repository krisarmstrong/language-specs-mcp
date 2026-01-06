# PerformanceObserverEntryList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceObserverEntryList&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `PerformanceObserverEntryList` interface is a list of [performance events](/en-US/docs/Web/API/PerformanceEntry) that were explicitly observed via the [observe()](/en-US/docs/Web/API/PerformanceObserver/observe) method.

## In this article

- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance methods](#instance_methods)

[PerformanceObserverEntryList.getEntries()](/en-US/docs/Web/API/PerformanceObserverEntryList/getEntries)

Returns a list of all explicitly observed [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) objects.

[PerformanceObserverEntryList.getEntriesByType()](/en-US/docs/Web/API/PerformanceObserverEntryList/getEntriesByType)

Returns a list of all explicitly observed [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) objects of the given entry type.

[PerformanceObserverEntryList.getEntriesByName()](/en-US/docs/Web/API/PerformanceObserverEntryList/getEntriesByName)

Returns a list of all explicitly observed [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) objects based on the given name and entry type.

## [Example](#example)

### [Using PerformanceObserverEntryList](#using_performanceobserverentrylist)

In the following example, `list` is the `PerformanceObserverEntryList` object. The [getEntries()](/en-US/docs/Web/API/PerformanceObserverEntryList/getEntries) method is called to get all explicitly observed [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) objects which are "measure" and "mark" in this case.

js

```
function perfObserver(list, observer) {
  list.getEntries().forEach((entry) => {
    if (entry.entryType === "mark") {
      console.log(`${entry.name}'s startTime: ${entry.startTime}`);
    }
    if (entry.entryType === "measure") {
      console.log(`${entry.name}'s duration: ${entry.duration}`);
    }
  });
}
const observer = new PerformanceObserver(perfObserver);
observer.observe({ entryTypes: ["measure", "mark"] });
```

## [Specifications](#specifications)

Specification
[Performance Timeline# performanceobserverentrylist-interface](https://w3c.github.io/performance-timeline/#performanceobserverentrylist-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 12, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PerformanceObserverEntryList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performanceobserverentrylist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceObserverEntryList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformanceobserverentrylist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceObserverEntryList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformanceobserverentrylist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8ab0f2fde2a9c1c7e547884abedf3848f8d7dda5%0A*+Document+last+modified%3A+2024-10-12T14%3A21%3A59.000Z%0A%0A%3C%2Fdetails%3E)
