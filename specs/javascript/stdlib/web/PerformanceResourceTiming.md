# PerformanceResourceTiming

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2017⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceResourceTiming&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `PerformanceResourceTiming` interface enables retrieval and analysis of detailed network timing data regarding the loading of an application's resources. An application can use the timing metrics to determine, for example, the length of time it takes to fetch a specific resource, such as an [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest), [<SVG>](/en-US/docs/Web/SVG/Reference/Element/svg), image, or script.

## In this article

- [Description](#description)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Description](#description)

The interface's properties create a resource loading timeline with high-resolution timestamps for network events such as redirect start and end times, fetch start, DNS lookup start and end times, response start and end times, and more. Additionally, the interface extends [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) with other properties which provide data about the size of the fetched resource as well as the type of resource that initiated the fetch.

### [Typical resource timing metrics](#typical_resource_timing_metrics)

The properties of this interface allow you to calculate certain resource timing metrics. Common use cases include:

- Measuring TCP handshake time (`connectEnd` - `connectStart`)
- Measuring DNS lookup time (`domainLookupEnd` - `domainLookupStart`)
- Measuring redirection time (`redirectEnd` - `redirectStart`)
- Measuring interim request time (`firstInterimResponseStart` - `finalResponseHeadersStart`)
- Measuring request time (`responseStart` - `requestStart`)
- Measuring document request time (`finalResponseHeadersStart` - `requestStart`)
- Measuring TLS negotiation time (`requestStart` - `secureConnectionStart`)
- Measuring time to fetch (without redirects) (`responseEnd` - `fetchStart`)
- Measuring ServiceWorker processing time (`fetchStart` - `workerStart`)
- Checking if content was compressed (`decodedBodySize` should not be `encodedBodySize`)
- Checking if local caches were hit (`transferSize` should be `0`)
- Checking if modern and fast protocols are used (`nextHopProtocol` should be HTTP/2 or HTTP/3)
- Checking if the correct resources are render-blocking (`renderBlockingStatus`)

### [Managing resource buffer sizes](#managing_resource_buffer_sizes)

By default only 250 resource timing entries are buffered. For more information see the [resource buffer sizes](/en-US/docs/Web/API/Performance_API/Resource_timing#managing_resource_buffer_sizes) of the Resource Timing guide.

### [Cross-origin timing information](#cross-origin_timing_information)

Many of the resource timing properties are restricted to return `0` or an empty string when the resource is a cross-origin request. To expose cross-origin timing information, the [Timing-Allow-Origin](/en-US/docs/Web/HTTP/Reference/Headers/Timing-Allow-Origin) HTTP response header needs to be set.

The properties which are returned as `0` by default when loading a resource from an origin other than the one of the web page itself: `redirectStart`, `redirectEnd`, `domainLookupStart`, `domainLookupEnd`, `connectStart`, `connectEnd`, `secureConnectionStart`, `requestStart`, and `responseStart`.

For example, to allow `https://developer.mozilla.org` to see resource timing information, the cross-origin resource should send:

http

```
Timing-Allow-Origin: https://developer.mozilla.org
```

## [Instance properties](#instance_properties)

### [Inherited from PerformanceEntry](#inherited_from_performanceentry)

This interface extends the following [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) properties for resource performance entry types by qualifying and constraining them as follows:

[PerformanceEntry.duration](/en-US/docs/Web/API/PerformanceEntry/duration)Read only

Returns a [timestamp](/en-US/docs/Web/API/DOMHighResTimeStamp) that is the difference between the [responseEnd](/en-US/docs/Web/API/PerformanceResourceTiming/responseEnd) and the [startTime](/en-US/docs/Web/API/PerformanceEntry/startTime) properties.

[PerformanceEntry.entryType](/en-US/docs/Web/API/PerformanceEntry/entryType)Read only

Returns `"resource"`.

[PerformanceEntry.name](/en-US/docs/Web/API/PerformanceEntry/name)Read only

Returns the resource's URL.

[PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime)Read only

Returns the [timestamp](/en-US/docs/Web/API/DOMHighResTimeStamp) for the time a resource fetch started. This value is equivalent to [PerformanceResourceTiming.fetchStart](/en-US/docs/Web/API/PerformanceResourceTiming/fetchStart).

### [Timestamps](#timestamps)

The interface supports the following timestamp properties which you can see in the diagram and are listed in the order in which they are recorded for the fetching of a resource. An alphabetical listing is shown in the navigation, at left.

[PerformanceResourceTiming.redirectStart](/en-US/docs/Web/API/PerformanceResourceTiming/redirectStart)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) that represents the start time of the fetch which initiates the redirect.

[PerformanceResourceTiming.redirectEnd](/en-US/docs/Web/API/PerformanceResourceTiming/redirectEnd)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) immediately after receiving the last byte of the response of the last redirect.

[PerformanceResourceTiming.workerStart](/en-US/docs/Web/API/PerformanceResourceTiming/workerStart)Read only

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) immediately before dispatching the [FetchEvent](/en-US/docs/Web/API/FetchEvent) if a Service Worker thread is already running, or immediately before starting the Service Worker thread if it is not already running. If the resource is not intercepted by a Service Worker the property will always return 0.

[PerformanceResourceTiming.fetchStart](/en-US/docs/Web/API/PerformanceResourceTiming/fetchStart)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) immediately before the browser starts to fetch the resource.

[PerformanceResourceTiming.domainLookupStart](/en-US/docs/Web/API/PerformanceResourceTiming/domainLookupStart)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) immediately before the browser starts the domain name lookup for the resource.

[PerformanceResourceTiming.domainLookupEnd](/en-US/docs/Web/API/PerformanceResourceTiming/domainLookupEnd)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time immediately after the browser finishes the domain name lookup for the resource.

[PerformanceResourceTiming.connectStart](/en-US/docs/Web/API/PerformanceResourceTiming/connectStart)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) immediately before the browser starts to establish the connection to the server to retrieve the resource.

[PerformanceResourceTiming.secureConnectionStart](/en-US/docs/Web/API/PerformanceResourceTiming/secureConnectionStart)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) immediately before the browser starts the handshake process to secure the current connection.

[PerformanceResourceTiming.connectEnd](/en-US/docs/Web/API/PerformanceResourceTiming/connectEnd)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) immediately after the browser finishes establishing the connection to the server to retrieve the resource.

[PerformanceResourceTiming.requestStart](/en-US/docs/Web/API/PerformanceResourceTiming/requestStart)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) immediately before the browser starts requesting the resource from the server.

[PerformanceResourceTiming.firstInterimResponseStart](/en-US/docs/Web/API/PerformanceResourceTiming/firstInterimResponseStart)ExperimentalRead only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) that represents the interim response time (for example, 100 Continue or 103 Early Hints).

[PerformanceResourceTiming.responseStart](/en-US/docs/Web/API/PerformanceResourceTiming/responseStart)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) immediately after the browser receives the first byte of the response from the server (which may be an interim response).

[PerformanceResourceTiming.finalResponseHeadersStart](/en-US/docs/Web/API/PerformanceResourceTiming/finalResponseHeadersStart)ExperimentalRead only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) that represents the final headers response time (for example, 200 Success), after any interim response time.

[PerformanceResourceTiming.responseEnd](/en-US/docs/Web/API/PerformanceResourceTiming/responseEnd)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) immediately after the browser receives the last byte of the resource or immediately before the transport connection is closed, whichever comes first.

### [Additional resource information](#additional_resource_information)

Additionally, this interface exposes the following properties containing more information about a resource:

[PerformanceResourceTiming.contentType](/en-US/docs/Web/API/PerformanceResourceTiming/contentType)Read onlyExperimental

A string representing a minimized and standardized version of the MIME-type of the fetched resource.

[PerformanceResourceTiming.decodedBodySize](/en-US/docs/Web/API/PerformanceResourceTiming/decodedBodySize)Read only

A number that is the size (in octets) received from the fetch (HTTP or cache) of the message body, after removing any applied content encoding.

[PerformanceResourceTiming.deliveryType](/en-US/docs/Web/API/PerformanceResourceTiming/deliveryType)ExperimentalRead only

Indicates how the resource was delivered — for example from the cache or from a navigational prefetch.

[PerformanceResourceTiming.encodedBodySize](/en-US/docs/Web/API/PerformanceResourceTiming/encodedBodySize)Read only

A number representing the size (in octets) received from the fetch (HTTP or cache), of the payload body, before removing any applied content encodings.

[PerformanceResourceTiming.initiatorType](/en-US/docs/Web/API/PerformanceResourceTiming/initiatorType)Read only

A string representing the web platform feature that initiated the performance entry.

[PerformanceResourceTiming.nextHopProtocol](/en-US/docs/Web/API/PerformanceResourceTiming/nextHopProtocol)Read only

A string representing the network protocol used to fetch the resource, as identified by the [ALPN Protocol ID (RFC7301)](https://datatracker.ietf.org/doc/html/rfc7301).

[PerformanceResourceTiming.renderBlockingStatus](/en-US/docs/Web/API/PerformanceResourceTiming/renderBlockingStatus)Read only

A string representing the render-blocking status. Either `"blocking"` or `"non-blocking"`.

[PerformanceResourceTiming.responseStatus](/en-US/docs/Web/API/PerformanceResourceTiming/responseStatus)Read only

A number representing the HTTP response status code returned when fetching the resource.

[PerformanceResourceTiming.transferSize](/en-US/docs/Web/API/PerformanceResourceTiming/transferSize)Read only

A number representing the size (in octets) of the fetched resource. The size includes the response header fields plus the response payload body.

[PerformanceResourceTiming.serverTiming](/en-US/docs/Web/API/PerformanceResourceTiming/serverTiming)Read only

An array of [PerformanceServerTiming](/en-US/docs/Web/API/PerformanceServerTiming) entries containing server timing metrics.

## [Instance methods](#instance_methods)

[PerformanceResourceTiming.toJSON()](/en-US/docs/Web/API/PerformanceResourceTiming/toJSON)

Returns a JSON representation of the `PerformanceResourceTiming` object.

## [Examples](#examples)

### [Logging resource timing information](#logging_resource_timing_information)

Example using a [PerformanceObserver](/en-US/docs/Web/API/PerformanceObserver), which notifies of new `resource` performance entries as they are recorded in the browser's performance timeline. Use the `buffered` option to access entries from before the observer creation.

js

```
const observer = new PerformanceObserver((list) => {
  list.getEntries().forEach((entry) => {
    console.log(entry);
  });
});

observer.observe({ type: "resource", buffered: true });
```

Example using [Performance.getEntriesByType()](/en-US/docs/Web/API/Performance/getEntriesByType), which only shows `resource` performance entries present in the browser's performance timeline at the time you call this method:

js

```
const resources = performance.getEntriesByType("resource");
resources.forEach((entry) => {
  console.log(entry);
});
```

## [Specifications](#specifications)

Specification
[Resource Timing# resources-included-in-the-performanceresourcetiming-interface](https://w3c.github.io/resource-timing/#resources-included-in-the-performanceresourcetiming-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Resource timing (Overview)](/en-US/docs/Web/API/Performance_API/Resource_timing)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 12, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PerformanceResourceTiming/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performanceresourcetiming/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceResourceTiming&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformanceresourcetiming%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceResourceTiming%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformanceresourcetiming%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca730ef3d6e21e0cfbeac992b898539945cec3c7%0A*+Document+last+modified%3A+2025-11-12T09%3A11%3A30.000Z%0A%0A%3C%2Fdetails%3E)
