# LinearAccelerationSensor

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLinearAccelerationSensor&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `LinearAccelerationSensor` interface of the [Sensor APIs](/en-US/docs/Web/API/Sensor_APIs) provides on each reading the acceleration applied to the device along all three axes, but without the contribution of gravity.

To use this sensor, the user must grant permission to the `'accelerometer'` device sensor through the [Permissions API](/en-US/docs/Web/API/Permissions_API). In addition, this feature may be blocked by a [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) set on your server.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[LinearAccelerationSensor()](/en-US/docs/Web/API/LinearAccelerationSensor/LinearAccelerationSensor)

Creates a new `LinearAccelerationSensor` object.

## [Instance properties](#instance_properties)

Inherits properties from its ancestors, [Accelerometer](/en-US/docs/Web/API/Accelerometer), [Sensor](/en-US/docs/Web/API/Sensor), and [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Instance methods](#instance_methods)

`LinearAccelerationSensor` doesn't have own methods. However, it inherits methods from its parent interfaces, [Sensor](/en-US/docs/Web/API/Sensor) and [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Events](#events)

`LinearAccelerationSensor` doesn't have own events. However, it inherits events from its parent interface, [Sensor](/en-US/docs/Web/API/Sensor).

## [Example](#example)

Linear acceleration is typically read in the [reading](/en-US/docs/Web/API/Sensor/reading_event) event callback. In the example below this occurs sixty times a second.

js

```
let laSensor = new LinearAccelerationSensor({ frequency: 60 });

laSensor.addEventListener("reading", (e) => {
  console.log(`Linear acceleration along the X-axis ${laSensor.x}`);
  console.log(`Linear acceleration along the Y-axis ${laSensor.y}`);
  console.log(`Linear acceleration along the Z-axis ${laSensor.z}`);
});
laSensor.start();
```

## [Specifications](#specifications)

Specification
[Accelerometer# linearaccelerationsensor-interface](https://w3c.github.io/accelerometer/#linearaccelerationsensor-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/LinearAccelerationSensor/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/linearaccelerationsensor/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLinearAccelerationSensor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Flinearaccelerationsensor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLinearAccelerationSensor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Flinearaccelerationsensor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d929bb0a021c7130d5a71a4bf505bcb8070378d%0A*+Document+last+modified%3A+2025-03-13T12%3A48%3A23.000Z%0A%0A%3C%2Fdetails%3E)
