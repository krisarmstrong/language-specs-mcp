# Screen Wake Lock API

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The Screen Wake Lock API provides a way to prevent devices from dimming or locking the screen when an application needs to keep running.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Performance considerations](#performance_considerations)
- [Security considerations](#security_considerations)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Most devices by default turn off their screen after a specified amount of time to prolong the life of the hardware. Modern devices do this to save on battery power. Whilst this is a useful feature, some applications need the screen to stay awake to be their most useful.

The Screen Wake Lock API prevents the screen from turning off, dimming or locking. It allows for a simple platform-based solution for visible (active) documents to acquire the platform screen wake lock.

There are plenty of use cases for keeping a screen on, including reading an ebook, map navigation, following a recipe, presenting to an audience, scanning a QR/barcode or applications that use voice or gesture control, rather than tactile input (the default way to keep a screen awake).

You acquire a [WakeLockSentinel](/en-US/docs/Web/API/WakeLockSentinel) object by calling the [navigator.wakeLock.request()](/en-US/docs/Web/API/WakeLock/request)[Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)-based method that resolves if the platform allows it. A request may be rejected for a number of reasons, including system settings (such as power save mode or low battery level) or if the document is not active or visible. It is good practice to store a reference to the sentinel object to allow the application to later control release.

The sentinel is attached to the underlying system wake lock. It can be released by the system, again if the battery power is too low or the document is not active or visible. It can also be released manually via the [WakeLockSentinel.release()](/en-US/docs/Web/API/WakeLockSentinel/release) method. After being released a `WakeLockSentinel` can no longer be used. If a screen wake lock is required again/still, the application will need to request a new one.

The Screen Wake Lock API should be used to keep the screen on to benefit usability. It's a good idea to show some feedback on the interface to show if wake lock is active and a way for the user to disable it if they wish.

## [Interfaces](#interfaces)

[WakeLock](/en-US/docs/Web/API/WakeLock)

Prevents device screens from dimming or locking when an application needs to keep running.

[WakeLockSentinel](/en-US/docs/Web/API/WakeLockSentinel)

Provides a handle to the underlying platform wake lock and if referenced can be manually released and reacquired. Get an instance of the object by calling [WakeLock.request](/en-US/docs/Web/API/WakeLock/request).

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.wakeLock](/en-US/docs/Web/API/Navigator/wakeLock)Read only

Returns a [WakeLock](/en-US/docs/Web/API/WakeLock) object instance, from which all other functionality can be accessed.

[Permissions-Policy: screen-wake-lock](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/screen-wake-lock)

Access to the API is gated by the [Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy) directive `screen-wake-lock`. See [Security considerations](#security_considerations) below.

## [Examples](#examples)

### [Feature detection](#feature_detection)

This code checks for wake lock support and updates the UI accordingly.

js

```
if ("wakeLock" in navigator) {
  isSupported = true;
  statusElem.textContent = "Screen Wake Lock API supported!";
} else {
  wakeButton.disabled = true;
  statusElem.textContent = "Wake lock is not supported by this browser.";
}
```

### [Requesting a wake lock](#requesting_a_wake_lock)

The following example demonstrates how to request a [WakeLockSentinel](/en-US/docs/Web/API/WakeLockSentinel) object. The [WakeLock.request](/en-US/docs/Web/API/WakeLock/request) method is [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)-based and so we can create an asynchronous function, which in turn updates the UI to reflect the wake lock is active.

js

```
// Create a reference for the Wake Lock.
let wakeLock = null;

// create an async function to request a wake lock
try {
  wakeLock = await navigator.wakeLock.request("screen");
  statusElem.textContent = "Wake Lock is active!";
} catch (err) {
  // The Wake Lock request has failed - usually system related, such as battery.
  statusElem.textContent = `${err.name}, ${err.message}`;
}
```

### [Releasing wake lock](#releasing_wake_lock)

The following example shows how to release the previously acquired wake lock.

js

```
wakeLock.release().then(() => {
  wakeLock = null;
});
```

### [Listening for wake lock release](#listening_for_wake_lock_release)

This example updates the UI if the wake lock has been released for any reason (such as navigating away from the active window/tab).

js

```
wakeLock.addEventListener("release", () => {
  // the wake lock has been released
  statusElem.textContent = "Wake Lock has been released";
});
```

### [Reacquiring a wake lock](#reacquiring_a_wake_lock)

The following code reacquires the wake lock should the visibility of the document change and the wake lock is released.

js

```
document.addEventListener("visibilitychange", async () => {
  if (wakeLock !== null && document.visibilityState === "visible") {
    wakeLock = await navigator.wakeLock.request("screen");
  }
});
```

### [Putting it all together](#putting_it_all_together)

You can find the [complete code on GitHub here](https://github.com/mdn/dom-examples/tree/main/screen-wake-lock-api). The [demo](https://mdn.github.io/dom-examples/screen-wake-lock-api/) uses a button to acquire a wake lock and also release it, which in turn updates the UI. The UI also updates if the wake lock is released automatically for any reason. There's a checkbox which when checked, will automatically reacquire the wake lock if the document's visibility state changes and becomes visible again.

## [Performance considerations](#performance_considerations)

- Release the screen wake lock when user ends activity that required always-on screen. For example, a ticketing app which uses QR codes to transmit ticket information, might acquire screen wake lock when the QR code is displayed (so that code is successfully scanned) but release afterwards. A presentation app might hold the lock only while a presentation is active, but not when presentation is being edited.
- If your app is performing long-running downloads, consider using background fetch.
- If your app is synchronizing data from a remote server, consider using background sync.
- Only active documents can acquire screen wake locks and previously acquired locks are automatically released when document becomes inactive. Therefore make sure to re-acquire screen wake lock if necessary when document becomes active (listen for [visibilitychange](/en-US/docs/Web/API/Document/visibilitychange_event) event).

## [Security considerations](#security_considerations)

Access to the Screen Wake Lock API is controlled by the [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) directive [screen-wake-lock](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/screen-wake-lock).

When using the [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy), the default allowlist for `screen-wake-lock` is `self`. This allows lock wake usage in same-origin nested frames but prevents third-party content from using locks. Third party usage can be enabled by the server first setting the `Permissions-Policy` header to grant permission a particular third party origin.

http

```
Permissions-Policy: screen-wake-lock=(self b.example.com)
```

Then the `allow="screen-wake-lock"` attribute must be added the frame container element for sources from that origin:

html

```
<iframe src="https://b.example.com" allow="screen-wake-lock"></iframe>
```

Browsers may also block the screen lock in a particular document for an implementation specific reason, such as a user or platform setting. They are expected to provide some unobtrusive mechanism to inform the user when wake lock is active, and to provide users the ability to remove the application's screen lock.

The [Permissions API](/en-US/docs/Web/API/Permissions_API)`screen-wake-lock` permission can be used to test whether access to use the screen lock is `granted`, `denied` or `prompt` (requires user acknowledgement of a prompt).

## [Specifications](#specifications)

Specification[Screen Wake Lock API](https://w3c.github.io/screen-wake-lock/)

## [Browser compatibility](#browser_compatibility)

### [api.WakeLock](#api.WakeLock)

### [api.WakeLockSentinel](#api.WakeLockSentinel)

## [See also](#see_also)

- [Stay awake with the Screen Wake Lock API](https://developer.chrome.com/docs/capabilities/web-apis/wake-lock/) on developer.chrome.com

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Screen_Wake_Lock_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/screen_wake_lock_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreen_Wake_Lock_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fscreen_wake_lock_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScreen_Wake_Lock_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fscreen_wake_lock_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F50f826047f483a04d29c553da53aed365b138bee%0A*+Document+last+modified%3A+2025-07-03T11%3A03%3A33.000Z%0A%0A%3C%2Fdetails%3E)
