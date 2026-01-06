# BackgroundFetchRecord

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchRecord&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `BackgroundFetchRecord` interface of the [Background Fetch API](/en-US/docs/Web/API/Background_Fetch_API) represents an individual request and response.

A `BackgroundFetchRecord` is created by the [BackgroundFetchRegistration.matchAll()](/en-US/docs/Web/API/BackgroundFetchRegistration/match) method, therefore there is no constructor for this interface.

There will be one `BackgroundFetchRecord` for each resource requested by `fetch()`.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[request](/en-US/docs/Web/API/BackgroundFetchRecord/request)Read onlyExperimental

Returns a [Request](/en-US/docs/Web/API/Request).

[responseReady](/en-US/docs/Web/API/BackgroundFetchRecord/responseReady)Read onlyExperimental

Returns a promise that resolves with a [Response](/en-US/docs/Web/API/Response).

## [Examples](#examples)

In this example an individual `BackgroundFetchRecord` is returned using [BackgroundFetchRegistration.matchAll()](/en-US/docs/Web/API/BackgroundFetchRegistration/match). The [BackgroundFetchRecord.request](/en-US/docs/Web/API/BackgroundFetchRecord/request) and [BackgroundFetchRecord.responseReady](/en-US/docs/Web/API/BackgroundFetchRecord/responseReady) are returned and logged to the console.

js

```
bgFetch.match("/ep-5.mp3").then(async (record) => {
  if (!record) {
    console.log("No record found");
    return;
  }

  console.log(`Here's the request`, record.request);
  const response = await record.responseReady;
  console.log(`And here's the response`, response);
});
```

## [Specifications](#specifications)

Specification
[Background Fetch# background-fetch-record-interface](https://wicg.github.io/background-fetch/#background-fetch-record-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 7, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/BackgroundFetchRecord/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/backgroundfetchrecord/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchRecord&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbackgroundfetchrecord%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchRecord%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbackgroundfetchrecord%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc77a11ee1509542c16b0348afc4fcb3ffe588e1c%0A*+Document+last+modified%3A+2024-05-07T14%3A59%3A11.000Z%0A%0A%3C%2Fdetails%3E)
