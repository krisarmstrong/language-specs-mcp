# IdleDetector

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdleDetector&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `IdleDetector` interface of the [Idle Detection API](/en-US/docs/Web/API/Idle_Detection_API) provides methods and events for detecting user activity on a device or screen.

This interface requires a secure context.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Events](#events)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[IdleDetector()](/en-US/docs/Web/API/IdleDetector/IdleDetector)Experimental

Creates a new `IdleDetector` object.

## [Instance properties](#instance_properties)

[IdleDetector.userState](/en-US/docs/Web/API/IdleDetector/userState)Read onlyExperimental

Returns a string indicating whether the users has interacted with either the screen or the device within the threshold provided to `start()`, one of `"active"` or `"idle"`. This attribute returns `null` before `start()` is called.

[IdleDetector.screenState](/en-US/docs/Web/API/IdleDetector/screenState)Read onlyExperimental

Returns a string indicating whether the screen is locked, one of `"locked"` or `"unlocked"`. This attribute returns `null` before `start()` is called.

## [Events](#events)

[change](/en-US/docs/Web/API/IdleDetector/change_event)Experimental

Called when the value of `userState` or `screenState` has changed.

## [Static methods](#static_methods)

[IdleDetector.requestPermission()](/en-US/docs/Web/API/IdleDetector/requestPermission_static)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the user has chosen whether to grant the origin access to their idle state. Resolves with `"granted"` on acceptance and `"denied"` on refusal.

## [Instance methods](#instance_methods)

[IdleDetector.start()](/en-US/docs/Web/API/IdleDetector/start)Experimental

Returns a `Promise` that resolves when the detector starts listening for changes in the user's idle state. `userState` and `screenState` are given initial values. This method takes an optional `options` object with the `threshold` in milliseconds where inactivity should be reported and `signal` for an `AbortSignal` to abort the idle detector.

## [Examples](#examples)

The following example shows creating a detector and logging changes to the user's idle state. A button is used to get the necessary user activation before requesting permission.

js

```
const controller = new AbortController();
const signal = controller.signal;

startButton.addEventListener("click", async () => {
  if ((await IdleDetector.requestPermission()) !== "granted") {
    console.error("Idle detection permission denied.");
    return;
  }

  try {
    const idleDetector = new IdleDetector();
    idleDetector.addEventListener("change", () => {
      const userState = idleDetector.userState;
      const screenState = idleDetector.screenState;
      console.log(`Idle change: ${userState}, ${screenState}.`);
    });

    await idleDetector.start({
      threshold: 60_000,
      signal,
    });
    console.log("IdleDetector is active.");
  } catch (err) {
    // Deal with initialization errors like permission denied,
    // running outside of top-level frame, etc.
    console.error(err.name, err.message);
  }
});

stopButton.addEventListener("click", () => {
  controller.abort();
  console.log("IdleDetector is stopped.");
});
```

## [Specifications](#specifications)

Specification
[Idle Detection API# api-idledetector](https://wicg.github.io/idle-detection/#api-idledetector)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/IdleDetector/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/idledetector/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdleDetector&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fidledetector%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIdleDetector%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fidledetector%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa28ce291736be0291feb822083b92c6f4385d57c%0A*+Document+last+modified%3A+2024-10-08T19%3A36%3A11.000Z%0A%0A%3C%2Fdetails%3E)
