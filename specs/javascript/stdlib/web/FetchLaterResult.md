# FetchLaterResult

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFetchLaterResult&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `FetchLaterResult` interface of the [fetchLater() API](/en-US/docs/Web/API/fetchLater_API) is returned by the [Window.fetchLater()](/en-US/docs/Web/API/Window/fetchLater) method after a deferred fetch has been created.

It contains a single `activated` property that indicates whether the deferred request has been sent out or not.

After a successful sending, the whole response is ignored — including body and headers — so the response of the deferred fetch is never returned to the `FetchLaterResult` interface.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[FetchLaterResult.activated](/en-US/docs/Web/API/FetchLaterResult/activated)Read onlyExperimental

A read-only boolean field that indicates whether the deferred request has been sent out. This is initially set to `false` and will then be updated by the browser once the deferred fetch has been sent.

## [Examples](#examples)

### [Defer a POST request for around one minute and create a function to check if sent](#defer_a_post_request_for_around_one_minute_and_create_a_function_to_check_if_sent)

js

```
const result = fetchLater("https://report.example.com", {
  method: "POST",
  body: JSON.stringify(myReport),
  activateAfter: 60000 /* 1 minute */,
});

function checkIfFetched() {
  return result.activated;
}
```

## [Specifications](#specifications)

Specification
[Fetch# fetchlaterresult](https://fetch.spec.whatwg.org/#fetchlaterresult)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [fetchLater() API](/en-US/docs/Web/API/fetchLater_API)
- [Fetch API](/en-US/docs/Web/API/Fetch_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/FetchLaterResult/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fetchlaterresult/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFetchLaterResult&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffetchlaterresult%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFetchLaterResult%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffetchlaterresult%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff336c5b6795a562c64fe859aa9ee2becf223ad8a%0A*+Document+last+modified%3A+2025-11-03T18%3A29%3A25.000Z%0A%0A%3C%2Fdetails%3E)
