# BatteryManager

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBatteryManager&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `BatteryManager` interface of the [Battery Status API](/en-US/docs/Web/API/Battery_Status_API) provides information about the system's battery charge level. The [navigator.getBattery()](/en-US/docs/Web/API/Navigator/getBattery) method returns a promise that resolves with a `BatteryManager` interface.

Since Chrome 103, the `BatteryManager` interface of [Battery Status API](/en-US/docs/Web/API/Battery_Status_API) only expose to secure context.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[BatteryManager.charging](/en-US/docs/Web/API/BatteryManager/charging)Read only

A Boolean value indicating whether the battery is currently being charged.

[BatteryManager.chargingTime](/en-US/docs/Web/API/BatteryManager/chargingTime)Read only

A number representing the remaining time in seconds until the battery is fully charged, or 0 if the battery is already fully charged.

[BatteryManager.dischargingTime](/en-US/docs/Web/API/BatteryManager/dischargingTime)Read only

A number representing the remaining time in seconds until the battery is completely discharged and the system suspends.

[BatteryManager.level](/en-US/docs/Web/API/BatteryManager/level)Read only

A number representing the system's battery charge level scaled to a value between 0.0 and 1.0.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Events](#events)

Also inherits events from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[chargingchange](/en-US/docs/Web/API/BatteryManager/chargingchange_event)

Fired when the battery charging state (the [charging](/en-US/docs/Web/API/BatteryManager/charging) property) is updated.

[chargingtimechange](/en-US/docs/Web/API/BatteryManager/chargingtimechange_event)

Fired when the battery charging time (the [chargingTime](/en-US/docs/Web/API/BatteryManager/chargingTime) property) is updated.

[dischargingtimechange](/en-US/docs/Web/API/BatteryManager/dischargingtimechange_event)

Fired when the battery discharging time (the [dischargingTime](/en-US/docs/Web/API/BatteryManager/dischargingTime) property) is updated.

[levelchange](/en-US/docs/Web/API/BatteryManager/levelchange_event)

Fired when the battery level (the [level](/en-US/docs/Web/API/BatteryManager/level) property) is updated.

## [Specifications](#specifications)

Specification
[Battery Status API# the-batterymanager-interface](https://w3c.github.io/battery/#the-batterymanager-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [Battery Status API](/en-US/docs/Web/API/Battery_Status_API)
- [Navigator.getBattery()](/en-US/docs/Web/API/Navigator/getBattery)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/BatteryManager/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/batterymanager/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBatteryManager&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbatterymanager%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBatteryManager%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbatterymanager%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8d54a21ae2677dba11569e7b7d918eac828af0b3%0A*+Document+last+modified%3A+2024-03-24T22%3A15%3A52.000Z%0A%0A%3C%2Fdetails%3E)
