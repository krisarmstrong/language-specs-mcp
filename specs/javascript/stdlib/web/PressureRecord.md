# PressureRecord

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPressureRecord&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API), except for [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `PressureRecord` interface is part of the [Compute Pressure API](/en-US/docs/Web/API/Compute_Pressure_API) and describes the pressure trend of a source at a specific moment of transition.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[PressureRecord.source](/en-US/docs/Web/API/PressureRecord/source)Read onlyExperimental

A string indicating the origin source from which the record is coming.

[PressureRecord.state](/en-US/docs/Web/API/PressureRecord/state)Read onlyExperimental

A string indicating the pressure state recorded.

[PressureRecord.time](/en-US/docs/Web/API/PressureRecord/time)Read onlyExperimental

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) indicating the timestamp of the record.

## [Instance methods](#instance_methods)

[PressureRecord.toJSON()](/en-US/docs/Web/API/PressureRecord/toJSON)Experimental

Returns a JSON representation of the `PressureRecord` object.

## [Examples](#examples)

### [Using the PressureRecord object](#using_the_pressurerecord_object)

In the following example we log the properties of the `PressureRecord` object in the pressure observer callback.

js

```
function callback(records) {
  const lastRecord = records[records.length - 1];
  console.log(`Current pressure is ${lastRecord.state}`);
  console.log(`Current pressure observed at ${lastRecord.time}`);
  console.log(`Current pressure source: ${lastRecord.source}`);
}

try {
  const observer = new PressureObserver(callback);
  await observer.observe("cpu", {
    sampleInterval: 1000, // 1000ms
  });
} catch (error) {
  // report error setting up the observer
}
```

## [Specifications](#specifications)

Specification
[Compute Pressure Level 1# the-pressurerecord-interface](https://w3c.github.io/compute-pressure/#the-pressurerecord-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 15, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PressureRecord/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/pressurerecord/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPressureRecord&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpressurerecord%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPressureRecord%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpressurerecord%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F55a1f6939679773b8f8178eb0dbee20bc8bfdeca%0A*+Document+last+modified%3A+2024-05-15T03%3A13%3A36.000Z%0A%0A%3C%2Fdetails%3E)
