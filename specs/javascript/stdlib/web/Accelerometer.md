# Accelerometer

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAccelerometer&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `Accelerometer` interface of the [Sensor APIs](/en-US/docs/Web/API/Sensor_APIs) provides on each reading the acceleration applied to the device along all three axes.

To use this sensor, the user must grant permission to the `'accelerometer'`, device sensor through the [Permissions API](/en-US/docs/Web/API/Permissions_API).

This feature may be blocked by a [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) set on your server.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[Accelerometer()](/en-US/docs/Web/API/Accelerometer/Accelerometer)Experimental

Creates a new `Accelerometer` object.

## [Instance properties](#instance_properties)

In addition to the properties listed below, `Accelerometer` inherits properties from its parent interfaces, [Sensor](/en-US/docs/Web/API/Sensor) and [EventTarget](/en-US/docs/Web/API/EventTarget).

[Accelerometer.x](/en-US/docs/Web/API/Accelerometer/x)Read onlyExperimental

Returns a double containing the acceleration of the device along the device's x axis.

[Accelerometer.y](/en-US/docs/Web/API/Accelerometer/y)Read onlyExperimental

Returns a double containing the acceleration of the device along the device's y axis.

[Accelerometer.z](/en-US/docs/Web/API/Accelerometer/z)Read onlyExperimental

Returns a double containing the acceleration of the device along the device's z axis.

## [Instance methods](#instance_methods)

`Accelerometer` doesn't have its own methods. However, it inherits methods from its parent interfaces, [Sensor](/en-US/docs/Web/API/Sensor) and [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Events](#events)

`Accelerometer` doesn't have its own events. However, it inherits events from its parent interface, [Sensor](/en-US/docs/Web/API/Sensor).

## [Example](#example)

Acceleration is typically read in the [reading](/en-US/docs/Web/API/Sensor/reading_event) event callback. In the example below this occurs sixty times a second.

js

```
const acl = new Accelerometer({ frequency: 60 });
acl.addEventListener("reading", () => {
  console.log(`Acceleration along the X-axis ${acl.x}`);
  console.log(`Acceleration along the Y-axis ${acl.y}`);
  console.log(`Acceleration along the Z-axis ${acl.z}`);
});

acl.start();
```

## [Specifications](#specifications)

Specification
[Accelerometer# accelerometer-interface](https://w3c.github.io/accelerometer/#accelerometer-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 5, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Accelerometer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/accelerometer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAccelerometer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faccelerometer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAccelerometer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faccelerometer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F37a8f396715c6e2e6a0e3d3225e1481484a825b7%0A*+Document+last+modified%3A+2025-10-05T23%3A32%3A01.000Z%0A%0A%3C%2Fdetails%3E)
