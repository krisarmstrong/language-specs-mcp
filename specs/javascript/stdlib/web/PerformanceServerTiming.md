# PerformanceServerTiming

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceServerTiming&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `PerformanceServerTiming` interface surfaces server metrics that are sent with the response in the [Server-Timing](/en-US/docs/Web/HTTP/Reference/Headers/Server-Timing) HTTP header.

This interface is restricted to the same origin, but you can use the [Timing-Allow-Origin](/en-US/docs/Web/HTTP/Reference/Headers/Timing-Allow-Origin) header to specify the domains that are allowed to access the server metrics. Note that this interface is only available in secure contexts (HTTPS) in some browsers.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[PerformanceServerTiming.description](/en-US/docs/Web/API/PerformanceServerTiming/description)Read only

A string value of the server-specified metric description, or an empty string.

[PerformanceServerTiming.duration](/en-US/docs/Web/API/PerformanceServerTiming/duration)Read only

A double that contains the server-specified metric duration, or value `0.0`.

[PerformanceServerTiming.name](/en-US/docs/Web/API/PerformanceServerTiming/name)Read only

A string value of the server-specified metric name.

## [Instance methods](#instance_methods)

[PerformanceServerTiming.toJSON()](/en-US/docs/Web/API/PerformanceServerTiming/toJSON)

Returns a JSON representation of the `PerformanceServerTiming` object.

## [Example](#example)

Given a server that sends the [Server-Timing](/en-US/docs/Web/HTTP/Reference/Headers/Server-Timing) header, for example a Node.js server like this:

js

```
const http = require("http");

function requestHandler(request, response) {
  const headers = {
    "Server-Timing": `
      cache;desc="Cache Read";dur=23.2,
      db;dur=53,
      app;dur=47.2
    `.replace(/\n/g, ""),
  };
  response.writeHead(200, headers);
  response.write("");
  return setTimeout(() => {
    response.end();
  }, 1000);
}

http.createServer(requestHandler).listen(3000).on("error", console.error);
```

The `PerformanceServerTiming` entries are now observable from JavaScript via the [PerformanceResourceTiming.serverTiming](/en-US/docs/Web/API/PerformanceResourceTiming/serverTiming) property and live on `navigation` and `resource` entries.

Example using a [PerformanceObserver](/en-US/docs/Web/API/PerformanceObserver), which notifies of new `navigation` and `resource` performance entries as they are recorded in the browser's performance timeline. Use the `buffered` option to access entries from before the observer creation.

js

```
const observer = new PerformanceObserver((list) => {
  list.getEntries().forEach((entry) => {
    entry.serverTiming.forEach((serverEntry) => {
      console.log(
        `${serverEntry.name} (${serverEntry.description}) duration: ${serverEntry.duration}`,
      );
      // Logs "cache (Cache Read) duration: 23.2"
      // Logs "db () duration: 53"
      // Logs "app () duration: 47.2"
    });
  });
});

["navigation", "resource"].forEach((type) =>
  observer.observe({ type, buffered: true }),
);
```

Example using [Performance.getEntriesByType()](/en-US/docs/Web/API/Performance/getEntriesByType), which only shows `navigation` and `resource` performance entries present in the browser's performance timeline at the time you call this method:

js

```
for (const entryType of ["navigation", "resource"]) {
  for (const { name: url, serverTiming } of performance.getEntriesByType(
    entryType,
  )) {
    if (serverTiming) {
      for (const { name, description, duration } of serverTiming) {
        console.log(`${name} (${description}) duration: ${duration}`);
        // Logs "cache (Cache Read) duration: 23.2"
        // Logs "db () duration: 53"
        // Logs "app () duration: 47.2"
      }
    }
  }
}
```

## [Specifications](#specifications)

Specification
[Server Timing# the-performanceservertiming-interface](https://w3c.github.io/server-timing/#the-performanceservertiming-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Server-Timing](/en-US/docs/Web/HTTP/Reference/Headers/Server-Timing)
- [PerformanceResourceTiming.serverTiming](/en-US/docs/Web/API/PerformanceResourceTiming/serverTiming)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 12, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PerformanceServerTiming/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performanceservertiming/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceServerTiming&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformanceservertiming%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceServerTiming%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformanceservertiming%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8ab0f2fde2a9c1c7e547884abedf3848f8d7dda5%0A*+Document+last+modified%3A+2024-10-12T14%3A21%3A59.000Z%0A%0A%3C%2Fdetails%3E)
