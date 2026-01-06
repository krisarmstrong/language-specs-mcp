# BackgroundFetchUpdateUIEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchUpdateUIEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `BackgroundFetchUpdateUIEvent` interface of the [Background Fetch API](/en-US/docs/Web/API/Background_Fetch_API) is an event type for the [backgroundfetchsuccess](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchsuccess_event) and [backgroundfetchfail](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchfail_event) events, and provides a method for updating the title and icon of the app to inform a user of the success or failure of a background fetch.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[BackgroundFetchUpdateUIEvent()](/en-US/docs/Web/API/BackgroundFetchUpdateUIEvent/BackgroundFetchUpdateUIEvent)Experimental

Creates a new `BackgroundFetchUIEvent` object. This constructor is not typically used, as the browser creates these objects itself for the [backgroundfetchsuccess](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchsuccess_event) and [backgroundfetchfail](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchfail_event) events.

## [Instance properties](#instance_properties)

Also inherits properties from its parent, [BackgroundFetchEvent](/en-US/docs/Web/API/BackgroundFetchEvent).

## [Instance methods](#instance_methods)

Also inherits methods from its parent, [BackgroundFetchEvent](/en-US/docs/Web/API/BackgroundFetchEvent).

[BackgroundFetchUpdateUIEvent.updateUI()](/en-US/docs/Web/API/BackgroundFetchUpdateUIEvent/updateUI)Experimental

Updates the title and icon in the user interface to show the status of a background fetch. Resolves with a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

## [Examples](#examples)

In this example, the `backgroundfetchsuccess` event is listened for, indicating that a fetch has completed successfully. The [updateUI()](/en-US/docs/Web/API/BackgroundFetchUpdateUIEvent/updateUI) method is then called, with a message to let the user know the episode they downloaded is ready.

js

```
addEventListener("backgroundfetchsuccess", (event) => {
  const bgFetch = event.registration;

  event.waitUntil(
    (async () => {
      // Create/open a cache.
      const cache = await caches.open("downloads");
      // Get all the records.
      const records = await bgFetch.matchAll();
      // Copy each request/response across.
      const promises = records.map(async (record) => {
        const response = await record.responseReady;
        await cache.put(record.request, response);
      });

      // Wait for the copying to complete.
      await Promise.all(promises);

      // Update the progress notification.
      event.updateUI({ title: "Episode 5 ready to listen!" });
    })(),
  );
});
```

## [Specifications](#specifications)

Specification
[Background Fetch# background-fetch-update-ui-event](https://wicg.github.io/background-fetch/#background-fetch-update-ui-event)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 7, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/BackgroundFetchUpdateUIEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/backgroundfetchupdateuievent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchUpdateUIEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbackgroundfetchupdateuievent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchUpdateUIEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbackgroundfetchupdateuievent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc77a11ee1509542c16b0348afc4fcb3ffe588e1c%0A*+Document+last+modified%3A+2024-05-07T14%3A59%3A11.000Z%0A%0A%3C%2Fdetails%3E)
