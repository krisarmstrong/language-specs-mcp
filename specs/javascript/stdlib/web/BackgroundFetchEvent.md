# BackgroundFetchEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `BackgroundFetchEvent` interface of the [Background Fetch API](/en-US/docs/Web/API/Background_Fetch_API) is the event type for background fetch events dispatched on the [service worker global scope](/en-US/docs/Web/API/ServiceWorkerGlobalScope).

It is the event type passed to [backgroundfetchclick](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchclick_event) event and [backgroundfetchabort](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchabort_event) event.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[BackgroundFetchEvent()](/en-US/docs/Web/API/BackgroundFetchEvent/BackgroundFetchEvent)Experimental

Creates a new `BackgroundFetchEvent` object. This constructor is not typically used, as the browser creates these objects itself and provides them to background fetch event callbacks.

## [Instance properties](#instance_properties)

Also inherits properties from its parent, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

[BackgroundFetchEvent.registration](/en-US/docs/Web/API/BackgroundFetchEvent/registration)Read onlyExperimental

Returns the [BackgroundFetchRegistration](/en-US/docs/Web/API/BackgroundFetchRegistration) that the event was initialized to.

## [Instance methods](#instance_methods)

Also inherits methods from its parent, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

None.

## [Examples](#examples)

In this example, if the user clicks on the user interface displaying the download progress, a new window will open. The current [BackgroundFetchRegistration](/en-US/docs/Web/API/BackgroundFetchRegistration) is returned by calling `event.registration`.

js

```
addEventListener("backgroundfetchclick", (event) => {
  const bgFetch = event.registration;

  if (bgFetch.result === "success") {
    clients.openWindow("/latest-podcasts");
  } else {
    clients.openWindow("/download-progress");
  }
});
```

## [Specifications](#specifications)

Specification
[Background Fetch# background-fetch-event](https://wicg.github.io/background-fetch/#background-fetch-event)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 7, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/BackgroundFetchEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/backgroundfetchevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbackgroundfetchevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbackgroundfetchevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc77a11ee1509542c16b0348afc4fcb3ffe588e1c%0A*+Document+last+modified%3A+2024-05-07T14%3A59%3A11.000Z%0A%0A%3C%2Fdetails%3E)
