# JS Self-Profiling API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FJS_Self-Profiling_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The JS Self-Profiling API enables a website to run a sampling profiler, to understand where it is spending JavaScript execution time.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Security requirements](#security_requirements)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Concepts and usage](#concepts_and_usage)

To start a profile, a website creates a [Profiler](/en-US/docs/Web/API/Profiler) instance. As soon as the instance is created, it starts sampling the JavaScript execution context.

To stop collecting samples and retrieve the profile, the website calls [Profiler.stop()](/en-US/docs/Web/API/Profiler/stop). This returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves to an object containing the profile data.

For example, the following function creates a profiler, then calls a function `genPrimes()`, then stops the profiler and retrieves the profile data:

js

```
async function profileGeneratePrimes() {
  const profiler = new Profiler({ sampleInterval: 10, maxBufferSize: 10000 });

  genPrimes();

  const trace = await profiler.stop();
  console.log(trace);
}
```

The profiler is a sampling profiler: this means that it periodically records (or samples) the current state of the JavaScript [call stack](/en-US/docs/Glossary/Call_stack). The profile consists of the collection of these samples. This enables you to understand where, statistically, the program is spending most of its time.

To understand exactly what a profile contains and how it is formatted, see [Profile anatomy and format](/en-US/docs/Web/API/JS_Self-Profiling_API/Profile_content_and_format).

### [Profiling best practices](#profiling_best_practices)

Collecting and processing profile data incurs a performance overhead of its own, and developers should be careful to manage this. Practices to minimize performance overhead include:

- Use the [maxBufferSize](/en-US/docs/Web/API/Profiler/Profiler#maxbuffersize) and [sampleInterval](/en-US/docs/Web/API/Profiler/Profiler#sampleinterval) options to control how many samples to take and how often to sample.
- Sample for short periods in a sampled manner: for example, trace for 5 seconds out of every 60 seconds.
- Process the samples in a web worker to avoid impacting performance on the main thread.
- Aggregate samples on the client before sending them to a telemetry endpoint.

If the JavaScript in your site is [minified](/en-US/docs/Glossary/Minification), you will need to transform the profile data based on a [source map](/en-US/docs/Glossary/Source_map), either on the client or on the server, before the data will be usable.

## [Interfaces](#interfaces)

[Profiler](/en-US/docs/Web/API/Profiler)Experimental

The `Profiler` interface is used to create profiles.

## [Security requirements](#security_requirements)

To use this API, the document must be served with a [document policy](https://wicg.github.io/document-policy/) that includes the `"js-profiling"` configuration point.

## [Specifications](#specifications)

Specification[JS Self-Profiling API](https://wicg.github.io/js-self-profiling/)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/JS_Self-Profiling_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/js_self-profiling_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FJS_Self-Profiling_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fjs_self-profiling_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FJS_Self-Profiling_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fjs_self-profiling_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
