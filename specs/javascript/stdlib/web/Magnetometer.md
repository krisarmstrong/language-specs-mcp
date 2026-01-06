# Magnetometer

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMagnetometer&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `Magnetometer` interface of the [Sensor APIs](/en-US/docs/Web/API/Sensor_APIs) provides information about the magnetic field as detected by the device's primary magnetometer sensor.

To use this sensor, the user must grant permission to the `'magnetometer'` device sensor through the [Permissions API](/en-US/docs/Web/API/Permissions_API). In addition, this feature may be blocked by a [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) set on your server.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[Magnetometer()](/en-US/docs/Web/API/Magnetometer/Magnetometer)Experimental

Creates a new `Magnetometer` object.

## [Instance properties](#instance_properties)

[Magnetometer.x](/en-US/docs/Web/API/Magnetometer/x)Read onlyExperimental

Returns a double containing the magnetic field around the device's x axis.

[Magnetometer.y](/en-US/docs/Web/API/Magnetometer/y)Read onlyExperimental

Returns a double containing the magnetic field around the device's y axis.

[Magnetometer.z](/en-US/docs/Web/API/Magnetometer/z)Read onlyExperimental

Returns a double containing the magnetic field around the device's z axis.

## [Instance methods](#instance_methods)

`Magnetometer` doesn't have own methods. However, it inherits methods from its parent interfaces, [Sensor](/en-US/docs/Web/API/Sensor) and [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Events](#events)

`Magnetometer` doesn't have own events. However, it inherits events from its parent interface, [Sensor](/en-US/docs/Web/API/Sensor).

## [Example](#example)

The magnetometer is typically read in the [reading](/en-US/docs/Web/API/Sensor/reading_event) event callback. In the example below this occurs sixty times a second.

js

```
let magSensor = new Magnetometer({ frequency: 60 });

magSensor.addEventListener("reading", (e) => {
  console.log(`Magnetic field along the X-axis ${magSensor.x}`);
  console.log(`Magnetic field along the Y-axis ${magSensor.y}`);
  console.log(`Magnetic field along the Z-axis ${magSensor.z}`);
});
magSensor.start();
```

## [Specifications](#specifications)

Specification
[Magnetometer# magnetometer-interface](https://w3c.github.io/magnetometer/#magnetometer-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Magnetometer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/magnetometer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMagnetometer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmagnetometer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMagnetometer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmagnetometer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d929bb0a021c7130d5a71a4bf505bcb8070378d%0A*+Document+last+modified%3A+2025-03-13T12%3A48%3A23.000Z%0A%0A%3C%2Fdetails%3E)
