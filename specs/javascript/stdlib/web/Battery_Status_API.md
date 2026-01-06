# Battery Status API

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The Battery Status API, more often referred to as the Battery API, provides information about the system's battery charge level and lets you be notified by events that are sent when the battery level or charging status change. This can be used to adjust your app's resource usage to reduce battery drain when the battery is low, or to save changes before the battery runs out in order to prevent data loss.

Note: This API is not available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API) (not exposed via [WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator)).

## In this article

- [Interfaces](#interfaces)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces](#interfaces)

[BatteryManager](/en-US/docs/Web/API/BatteryManager)

Provides information about the system's battery charge level.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.getBattery()](/en-US/docs/Web/API/Navigator/getBattery)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a [BatteryManager](/en-US/docs/Web/API/BatteryManager) object.

## [Example](#example)

In this example, we watch for changes both to the charging status (whether or not we're plugged in and charging) and for changes to the battery level and timing. This is done by listening for the [chargingchange](/en-US/docs/Web/API/BatteryManager/chargingchange_event), [levelchange](/en-US/docs/Web/API/BatteryManager/levelchange_event), [chargingtimechange](/en-US/docs/Web/API/BatteryManager/chargingtimechange_event), [dischargingtimechange](/en-US/docs/Web/API/BatteryManager/dischargingtimechange_event) events.

js

```
navigator.getBattery().then((battery) => {
  function updateAllBatteryInfo() {
    updateChargeInfo();
    updateLevelInfo();
    updateChargingInfo();
    updateDischargingInfo();
  }
  updateAllBatteryInfo();

  battery.addEventListener("chargingchange", () => {
    updateChargeInfo();
  });
  function updateChargeInfo() {
    console.log(`Battery charging? ${battery.charging ? "Yes" : "No"}`);
  }

  battery.addEventListener("levelchange", () => {
    updateLevelInfo();
  });
  function updateLevelInfo() {
    console.log(`Battery level: ${battery.level * 100}%`);
  }

  battery.addEventListener("chargingtimechange", () => {
    updateChargingInfo();
  });
  function updateChargingInfo() {
    console.log(`Battery charging time: ${battery.chargingTime} seconds`);
  }

  battery.addEventListener("dischargingtimechange", () => {
    updateDischargingInfo();
  });
  function updateDischargingInfo() {
    console.log(`Battery discharging time: ${battery.dischargingTime} seconds`);
  }
});
```

See also [the example in the specification](https://w3c.github.io/battery/#examples).

## [Specifications](#specifications)

Specification[Battery Status API](https://w3c.github.io/battery/)

## [Browser compatibility](#browser_compatibility)

### [api.BatteryManager](#api.BatteryManager)

### [api.Navigator.getBattery](#api.Navigator.getBattery)

## [See also](#see_also)

- [Hacks blog post - Using the Battery API](https://hacks.mozilla.org/2012/02/using-the-battery-api-part-of-webapi/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Battery_Status_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/battery_status_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBattery_Status_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbattery_status_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBattery_Status_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbattery_status_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F941ade970fd7ebad52af692b6ac27cfd96f94100%0A*+Document+last+modified%3A+2025-05-28T14%3A25%3A52.000Z%0A%0A%3C%2Fdetails%3E)
