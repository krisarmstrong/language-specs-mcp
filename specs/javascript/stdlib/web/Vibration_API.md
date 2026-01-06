# Vibration API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVibration_API&level=not)

Most modern mobile devices include vibration hardware, which lets software code provide physical feedback to the user by causing the device to shake. The Vibration API offers Web apps the ability to access this hardware, if it exists, and does nothing if the device doesn't support it.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Vibration is described as a pattern of on-off pulses, which may be of varying lengths. The pattern may consist of either a single integer, describing the number of milliseconds to vibrate, or an array of integers describing a pattern of vibrations and pauses. Vibration is controlled with a single method: [Navigator.vibrate()](/en-US/docs/Web/API/Navigator/vibrate).

### [A single vibration](#a_single_vibration)

You may pulse the vibration hardware one time by specifying either a single value or an array consisting of only one value:

js

```
navigator.vibrate(200);
navigator.vibrate([200]);
```

Both of these examples vibrate the device for 200 ms.

### [Vibration patterns](#vibration_patterns)

An array of values describes alternating periods in which the device is vibrating and not vibrating. Each value in the array is converted to an integer, then interpreted alternately as the number of milliseconds the device should vibrate and the number of milliseconds it should not be vibrating. For example:

js

```
navigator.vibrate([200, 100, 200]);
```

This vibrates the device for 200 ms, then pauses for 100 ms before vibrating the device again for another 200 ms.

You may specify as many vibration/pause pairs as you like, and you may provide either an even or odd number of entries; it's worth noting that you don't have to provide a pause as your last entry since the vibration automatically stops at the end of each vibration period.

### [Canceling existing vibrations](#canceling_existing_vibrations)

Calling [Navigator.vibrate()](/en-US/docs/Web/API/Navigator/vibrate) with a value of `0`, an empty array, or an array containing all zeros will cancel any currently ongoing vibration pattern.

### [Continued vibrations](#continued_vibrations)

Some basic `setInterval` and `clearInterval` action will allow you to create persistent vibration:

js

```
let vibrateInterval;

// Starts vibration at passed in level
function startVibrate(duration) {
  navigator.vibrate(duration);
}

// Stops vibration
function stopVibrate() {
  // Clear interval and stop persistent vibrating
  if (vibrateInterval) clearInterval(vibrateInterval);
  navigator.vibrate(0);
}

// Start persistent vibration at given duration and interval
// Assumes a number value is given
function startPersistentVibrate(duration, interval) {
  vibrateInterval = setInterval(() => {
    startVibrate(duration);
  }, interval);
}
```

Of course, the snippet above doesn't take into account the array method of vibration; persistent array-based vibration will require calculating the sum of the array items and creating an interval based on that number (with an additional delay, probably).

## [Interfaces](#interfaces)

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.vibrate()](/en-US/docs/Web/API/Navigator/vibrate)

Causes vibration on devices with support for it. Does nothing if vibration support isn't available.

## [Specifications](#specifications)

Specification[Vibration API](https://w3c.github.io/vibration/)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Navigator.vibrate()](/en-US/docs/Web/API/Navigator/vibrate)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 11, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Vibration_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/vibration_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVibration_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvibration_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVibration_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvibration_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F77915a2ad318fb78b1d02a35d6b1de61ea1b1f5f%0A*+Document+last+modified%3A+2024-04-11T21%3A51%3A09.000Z%0A%0A%3C%2Fdetails%3E)
