# WakeLock

 Baseline  2025 Newly available

 Since ⁨March 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWakeLock&level=low)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `WakeLock` interface of the [Screen Wake Lock API](/en-US/docs/Web/API/Screen_Wake_Lock_API) can be used to request a lock that prevents device screens from dimming or locking when an application needs to keep running.

This interface, and hence the system wake lock, is exposed through the [Navigator.wakeLock](/en-US/docs/Web/API/Navigator/wakeLock) property.

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[request()](/en-US/docs/Web/API/WakeLock/request)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [WakeLockSentinel](/en-US/docs/Web/API/WakeLockSentinel) object if the screen wake lock is granted.

## [Examples](#examples)

The following code `awaits` the request for a [WakeLockSentinel](/en-US/docs/Web/API/WakeLockSentinel) object, and continues if the request is granted.

The [WakeLock.request()](/en-US/docs/Web/API/WakeLock/request) method is wrapped in a `try...catch` statement to catch [cases when the promise might be rejected](/en-US/docs/Web/API/WakeLock/request#exceptions), such as due to low device power.

js

```
try {
  const wakeLock = await navigator.wakeLock.request("screen");
} catch (err) {
  // the wake lock request fails - usually system related, such being low on battery
  console.log(`${err.name}, ${err.message}`);
}
```

Note that the screen wake lock may be revoked by the device after it has been granted. The returned [WakeLockSentinel](/en-US/docs/Web/API/WakeLockSentinel) can be used to check the status of the lock, and/or to manually cancel a held screen wake lock.

## [Specifications](#specifications)

Specification
[Screen Wake Lock API# the-wakelock-interface](https://w3c.github.io/screen-wake-lock/#the-wakelock-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Stay awake with the Screen Wake Lock API](https://developer.chrome.com/docs/capabilities/web-apis/wake-lock/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WakeLock/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/wakelock/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWakeLock&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwakelock%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWakeLock%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwakelock%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdaa20da731748454675985dbcda02b2a0db3013a%0A*+Document+last+modified%3A+2025-12-15T22%3A57%3A50.000Z%0A%0A%3C%2Fdetails%3E)
