# WakeLockSentinel

 Baseline  2025 Newly available

 Since ⁨March 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWakeLockSentinel&level=low)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `WakeLockSentinel` interface of the [Screen Wake Lock API](/en-US/docs/Web/API/Screen_Wake_Lock_API) can be used to monitor the status of the platform screen wake lock, and manually release the lock when needed.

The screen wake lock prevents device screens from dimming or locking when an application needs to keep running.

A screen wake lock is requested using the [navigator.wakeLock.request()](/en-US/docs/Web/API/WakeLock/request) method, which returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a `WakeLockSentinel` object if the lock is granted.

An acquired screen wake lock can be released manually via the [release()](/en-US/docs/Web/API/WakeLockSentinel/release) method, or automatically via the platform screen wake lock. The latter may occur if the document becomes inactive or loses visibility, if the device is low on power, or if the user turns on a power save mode. A released `WakeLockSentinel` cannot be re-used: a new sentinel must be requested using [navigator.wakeLock.request()](/en-US/docs/Web/API/WakeLock/request) if a new lock is needed. Releasing all `WakeLockSentinel` instances of a given wake lock type will cause the underlying platform wake lock to be released.

An event is fired at the `WakeLockSentinel` if the platform lock is released, allowing applications to configure their UI, and re-request the lock if needed.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[released](/en-US/docs/Web/API/WakeLockSentinel/released)Read only

Returns a boolean indicating whether the `WakeLockSentinel` has been released.

[type](/en-US/docs/Web/API/WakeLockSentinel/type)Read only

Returns a string representation of the currently acquired `WakeLockSentinel` type. Return values are:

- `screen`: A screen wake lock. Prevents devices from dimming or locking the screen.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[release()](/en-US/docs/Web/API/WakeLockSentinel/release)

Releases the `WakeLockSentinel`, returning a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that is resolved once the sentinel has been successfully released.

## [Events](#events)

[release](/en-US/docs/Web/API/WakeLockSentinel/release_event)

Fired when the [release()](/en-US/docs/Web/API/WakeLockSentinel/release) method is called or the wake lock is released by the user agent.

## [Examples](#examples)

In this example, we create an asynchronous function that requests a `WakeLockSentinel`. Once the screen wake lock is acquired we listen for the `release` event, which can be used to give appropriate UI feedback. The sentinel can be acquired or released via appropriate interactions.

js

```
// create a reference for the wake lock
let wakeLock = null;

// create an async function to request a wake lock
const requestWakeLock = async () => {
  try {
    wakeLock = await navigator.wakeLock.request("screen");

    // listen for our release event
    wakeLock.addEventListener("release", () => {
      // if wake lock is released alter the UI accordingly
    });
  } catch (err) {
    // if wake lock request fails - usually system related, such as battery
  }
};

wakeLockOnButton.addEventListener("click", () => {
  requestWakeLock();
});

wakeLockOffButton.addEventListener("click", () => {
  if (wakeLock !== null) {
    wakeLock.release().then(() => {
      wakeLock = null;
    });
  }
});
```

## [Specifications](#specifications)

Specification
[Screen Wake Lock API# the-wakelocksentinel-interface](https://w3c.github.io/screen-wake-lock/#the-wakelocksentinel-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Stay awake with the Screen Wake Lock API](https://developer.chrome.com/docs/capabilities/web-apis/wake-lock/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WakeLockSentinel/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/wakelocksentinel/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWakeLockSentinel&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwakelocksentinel%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWakeLockSentinel%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwakelocksentinel%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
