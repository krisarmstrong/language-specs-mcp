# Profiler

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FProfiler&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `Profiler` interface of the [JS Self-Profiling API](/en-US/docs/Web/API/JS_Self-Profiling_API) enables you to create a [profile](/en-US/docs/Web/API/JS_Self-Profiling_API/Profile_content_and_format) of some part of your web application's execution.

## In this article

- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[Profiler()](/en-US/docs/Web/API/Profiler/Profiler)Experimental

Creates a new `Profiler` object, and starts collecting samples.

## [Instance methods](#instance_methods)

[Profiler.stop()](/en-US/docs/Web/API/Profiler/stop)Experimental

Stops the profiler, returning a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to the [profile](/en-US/docs/Web/API/JS_Self-Profiling_API/Profile_content_and_format).

## [Events](#events)

[samplebufferfull](/en-US/docs/Web/API/Profiler/samplebufferfull_event)

Fired when the profile has recorded enough samples to fill its internal buffer.

## [Examples](#examples)

### [Recording a profile](#recording_a_profile)

The following code profiles the `doWork()` operation, and logs the result.

js

```
const profiler = new Profiler({ sampleInterval: 10, maxBufferSize: 10000 });

doWork();

const profile = await profiler.stop();
console.log(JSON.stringify(profile));
```

### [Profiling page load](#profiling_page_load)

The following code profiles the time between the script first running and the window's [load](/en-US/docs/Web/API/Window/load_event) event firing.

js

```
const profiler = new Profiler({ sampleInterval: 10, maxBufferSize: 10000 });

window.addEventListener("load", async () => {
  const profile = await profiler.stop();
  console.log(JSON.stringify(profile));
});
```

## [Specifications](#specifications)

Specification
[JS Self-Profiling API# the-profiler-interface](https://wicg.github.io/js-self-profiling/#the-profiler-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Profiler/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/profiler/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FProfiler&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fprofiler%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FProfiler%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fprofiler%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff06910b17bbf44908adc559a9b7b95bd70ae88cf%0A*+Document+last+modified%3A+2025-03-24T00%3A13%3A46.000Z%0A%0A%3C%2Fdetails%3E)
